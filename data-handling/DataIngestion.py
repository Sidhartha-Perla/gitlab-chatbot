import yaml
import gc
from pathlib import Path
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores.utils import filter_complex_metadata
from chromadb import HttpClient



def read_file(file_path):
    return file_path.read_text(encoding="utf-8")

def create_source_url(base_url, file_path):
    file_name = file_path.name

    if any(keyword in file_name for keyword in ("_index", "index", "template")):
        return (base_url + "/" + str(file_path.parent).lstrip("/"))
    else:
        return (base_url + "/" + str(file_path.parent).lstrip("/") + "/" + str(file_path.stem))

def extract_metadata_and_content(markdown_text):
    metadata = {}
    content = markdown_text
    if markdown_text.startswith("---"):
        try:
            _, front_matter, body = markdown_text.split('---', 2)
            metadata = yaml.safe_load(front_matter)
            metadata = {k: v for k, v in metadata.items() if k in ("title", "description")}
            content = body.strip()
        except Exception as e:
            print("\033[91mWarning\033[0m: Failed to parse metadata:", e)
    return metadata, content

def split_into_chunks(content, metadata, base_url, file_path, chunk_size=1000, chunk_overlap=100):
    headers_to_split_on = [
        ("#", "Header_1"),
        ("##", "Header_2"),
        ("###", "Header_3")
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on = headers_to_split_on)
    chunks = markdown_splitter.split_text(content)
    documents = []
    
    source_url = create_source_url(base_url, file_path)
    
    for index, chunk in enumerate(chunks):
        page_content = ""
        
        for header, value in chunk.metadata.items():
            page_content += (value + "\n\n")
        
        page_content += chunk.page_content

        chunk_document = Document(
            page_content=page_content,
            metadata={
                "source_url" : source_url,
                **metadata,
                **chunk.metadata,
                "chunk_index" : index,
            }
        )
        documents.append(chunk_document)
    return documents


def ingest_site_data(base_url, source_dir, vector_store, batch_size=15):
    source_dir = Path(source_dir)
    batch_documents = []
    processed_count = 0
    
    for file_path in source_dir.rglob("*.md"):
        if file_path.is_file():
            print("Processing: ", file_path)
            # Load file
            print("-Loading")
            file_content = read_file(file_path)
            # Extract Metadata and content
            print("-Extracting Metadata")
            metadata, content = extract_metadata_and_content(file_content)
            # Split the content
            print("-Chunking file content")
            chunked_documents = split_into_chunks(content, metadata, base_url, file_path)
            
            # Add to batch
            if chunked_documents:
                clean_documents = filter_complex_metadata(chunked_documents)
                batch_documents.extend(clean_documents)
                processed_count += 1
            else:
                print(f"Skipping file: no content chunks generated")
            
            # Process batch when it reaches the limit
            if processed_count == batch_size:
                print(f"Embedding and storing batch of {len(batch_documents)} chunks")
                vector_store.add_documents(documents=batch_documents)

                batch_documents = []
                processed_count = 0

                # Force garbage collection
                gc.collect()
    
    # Process any remaining documents
    if batch_documents:
        print(f"-Embedding and storing final batch of {len(batch_documents)} chunks")
        vector_store.add_documents(documents=batch_documents)
        print(f"Total processed: {processed_count} chunks")



print("\033[1mStarting data ingestion\033[0m")

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
print("\033[1mUsing model 'all-MiniLM-L6-v2' for embedding data\033[0m")

# Create HTTP client to connect to the Chroma server
chroma_client = HttpClient(
    host="localhost",
    port=8000
)

# Create vector store using the client
vector_store = Chroma(
    client=chroma_client,
    collection_name="gitlab_data",
    embedding_function=embedding_model
)
print("\033[1mCreated Vector store for storing data\033[0m")

# Process the files in batches
ingest_site_data("https://handbook.gitlab.com", "./handbook", vector_store, batch_size=50)
ingest_site_data("https://about.gitlab.com", "./direction", vector_store, batch_size=50)
# GitLab Handbook Chatbot

## Description
This project is a chatbot that allows users to interact with the GitLab Handbook and Direction pages through natural language queries. It uses document ingestion, vector search, and a conversational interface to make exploring GitLab's internal resources easier.

## Tech Stack
- **Backend**: Python (FastAPI)
- **Frontend**: React
- **Database**: ChromaDB (vector database)

## Setup Instructions

### Prerequisites
- Python 3.8+
- `bash` (for running scripts)

### **Environment Variables**
Create a `.env` file by copying from the `.env.template` provided in the repository. The required environment variables are:

```bash
LANGSMITH_TRACING=true   # Optional, can be set to false if not using Langsmith
LANGSMITH_API_KEY=       # Optional, only if LANGSMITH_TRACING is true
LANGSMITH_PROJECT=       # Optional, only if LANGSMITH_TRACING is true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"   # Optional, only if LANGSMITH_TRACING is true
GOOGLE_API_KEY=          # Required
```
### Installation Steps

1. **Clone the repository**:

    ```bash
    https://github.com/Sidhartha-Perla/gitlab-chatbot.git
    cd gitlab-chatbot
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Python dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Start ChromaDB** (in one terminal):

    ```bash
    ./run-chroma.sh
    ```

5. **Ingest documents** (in another terminal):

    ```bash
    ./run-ingestion.sh
    ```

6. **Start the FastAPI server** (after ingestion is complete):

    ```bash
    ./run.sh
    ```

7. **Access the Web UI**:
   - Open your browser and go to: [http://127.0.0.1:8001](http://127.0.0.1:8001)

## Usage
- Enter your queries related to the GitLab Handbook or Direction pages into the chatbot.
- The system retrieves and summarizes the most relevant information from the ingested documents.


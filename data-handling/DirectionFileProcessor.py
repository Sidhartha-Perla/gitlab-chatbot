"""
    This module transforms the Direction pages' .html.md.erb data files and .erb data 
    components into a single .md(Markdown) file for each section of the Direction website
"""


import re
from pathlib import Path
import markdownify

def read_file(file_path):
    return file_path.read_text(encoding="utf-8")

def write_file(file_path, content):
    file_path.write_text(content, encoding="utf-8")

def strip_ruby_code(content):
    """Remove Ruby code blocks."""
    content = re.sub(r"<%=?[\s\S]*?%>", "", content)
    return content

def replace_html_with_markdown(content):
    """Replace all blocks of HTML content with equivalent markdown"""
    
    pattern = r'<[^>]+>.*?</[^>]+>'
    
    # Convert HTML to Markdown
    def html_to_markdown(match):
        """Convert HTML content to Markdown."""
        html = match.group(0)
        return markdownify.markdownify(html, heading_style="ATX")
    
    return re.sub(pattern, html_to_markdown, content, flags=re.DOTALL)


def resolve_partials(content):
    """Replace embedded md files using 'partial' with the content of the referenced partials."""
    pattern = r'<%=\s*partial\(["\'](.+?)["\']\)\s*%>'

    return re.sub(pattern, replace_partials_with_content, content)

def replace_partials_with_content(match):
        partial_path = match.group(1)
        possible_paths = [
            add_underscore_to_filename(partial_path.lstrip("/")).with_suffix(".erb"),
            add_underscore_to_filename(partial_path.lstrip("/")).with_suffix(".html.md.erb")
        ]

        for path in possible_paths:
            if path.exists():
                print(f"Partial {path} found")
                partial_content = read_file(path)
                # Recursively resolve partials inside this partial
                partial_content = resolve_partials(partial_content)
                return partial_content
            else:
                print(f"Warning: Partial {path} not found.")

def add_underscore_to_filename(partial_path):
    new_path = Path(partial_path)
    if not new_path.name.startswith("_"):
        new_path = new_path.parent / ("_" + new_path.name)
    return new_path

def process_file(file_path):
    """Process each file based on extensions"""

    # Process only Markdown files
    file_name = file_path.name
    if not ".md" in file_name:
        return None
    
    content = read_file(file_path)
    
    # If erb file, replace all partials and strip erb code
    if ".erb" in file_name:
        # Only process index/template erb files
        if "index" in file_name or "template" in file_name:
            content = resolve_partials(content)
            content = strip_ruby_code(content)
        else:
            return None
    # Convert HTML content to markdown
    if ".html" in file_name:
        content = replace_html_with_markdown(content)

    return content

def process_direction_data(source_dir, output_dir):
    """Process all files in the directory and its subdirectories."""
    source_dir = Path(source_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for file_path in source_dir.rglob("*"):
        if file_path.is_file():
            result = process_file(file_path)
            if result is not None:
                relative_path = file_path.relative_to(source_dir)
                output_path = output_dir / Path(
                    re.sub(r"\.md|\.html|\.htm|\.erb", "", str(relative_path))
                ).with_suffix(".md")
                output_path.parent.mkdir(parents=True, exist_ok=True)
                write_file(output_path, result)
                print(f"Processed: {relative_path}")


process_direction_data('./direction-unprocessed', './direction')
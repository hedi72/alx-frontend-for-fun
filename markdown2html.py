import sys
import os

def convert_markdown_to_html(markdown_file, output_file):
    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Perform Markdown to HTML conversion here
    # For demonstration purposes, let's assume it's a simple copy operation
    with open(markdown_file, 'r') as f:
        markdown_content = f.read()

    # Convert Markdown to HTML here
    html_content = markdown_content  # Placeholder for actual conversion

    # Write HTML content to the output file
    with open(output_file, 'w') as f:
        f.write(html_content)

    sys.exit(0)

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <Markdown_file> <Output_file>", file=sys.stderr)
        sys.exit(1)

    # Extract arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML
    convert_markdown_to_html(markdown_file, output_file)

#!/usr/bin/python3
"""
markdown2html.py module

This script converts a Markdown file to HTML.
"""

import sys
import os

def main():
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file
    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()

    # Convert Markdown to HTML (Basic implementation)
    html_content = markdown_content  # For now, just copying the content

    # Write the HTML content to the output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

    # Exit with status 0 if successful
    sys.exit(0)

if __name__ == "__main__":
    main()


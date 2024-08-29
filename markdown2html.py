#!/usr/bin/python3
"""
markdown2html.py: Converts Markdown text to HTML.

Usage:
    ./markdown2html.py <input_file> <output_file>

This script reads a Markdown file, converts it to HTML, and writes the result
to an output file.
"""

import sys
import os
import re

def markdown_to_html(markdown_text):
    """
    Converts Markdown to HTML.
    Handles headers, lists, bold, italics, and special cases.
    """
    # Convert headers
    markdown_text = re.sub(r'###### (.*)', r'<h6>\1</h6>', markdown_text)
    markdown_text = re.sub(r'##### (.*)', r'<h5>\1</h5>', markdown_text)
    markdown_text = re.sub(r'#### (.*)', r'<h4>\1</h4>', markdown_text)
    markdown_text = re.sub(r'### (.*)', r'<h3>\1</h3>', markdown_text)
    markdown_text = re.sub(r'## (.*)', r'<h2>\1</h2>', markdown_text)
    markdown_text = re.sub(r'# (.*)', r'<h1>\1</h1>', markdown_text)

    # Convert lists
    markdown_text = re.sub(r'(?m)^\* (.*)', r'<ul>\n<li>\1</li>\n</ul>', markdown_text)
    markdown_text = re.sub(r'(?m)^- (.*)', r'<ul>\n<li>\1</li>\n</ul>', markdown_text)

    # Merge consecutive lists
    markdown_text = re.sub(r'</ul>\n<ul>', '', markdown_text)

    # Convert bold
    markdown_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', markdown_text)
    markdown_text = re.sub(r'__(.+?)__', r'<b>\1</b>', markdown_text)

    # Convert italics
    markdown_text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', markdown_text)
    markdown_text = re.sub(r'_(.+?)_', r'<i>\1</i>', markdown_text)

    # Handle special cases
    markdown_text = re.sub(r'\[\[(.+?)\]\]', r'<b>\1</b>', markdown_text)
    markdown_text = re.sub(r'\(\((.+?)\)\)', r'<i>\1</i>', markdown_text)

    return markdown_text

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if input file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}")
        sys.exit(1)

    try:
        # Read the input markdown file
        with open(input_file, 'r') as f:
            markdown_text = f.read()

        # Convert markdown to HTML
        html_text = markdown_to_html(markdown_text)

        # Write the HTML to the output file
        with open(output_file, 'w') as f:
            f.write(html_text)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


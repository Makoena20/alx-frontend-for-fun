#!/usr/bin/python3
"""
Markdown2HTML script that converts a markdown file to an HTML file.
"""
import sys
import os
import hashlib

def convert_md_to_html(markdown_content):
    """Converts markdown content to HTML."""
    html_content = []
    in_list = False
    for line in markdown_content:
        line = line.rstrip()

        if line.startswith('#'):
            level = len(line.split(' ')[0])
            html_content.append(f"<h{level}>{line[level+1:].strip()}</h{level}>")

        elif line.startswith('- '):
            if not in_list:
                html_content.append("<ul>")
                in_list = True
            html_content.append(f"    <li>{line[2:].strip()}</li>")

        elif line.startswith('* '):
            if not in_list:
                html_content.append("<ol>")
                in_list = True
            html_content.append(f"    <li>{line[2:].strip()}</li>")

        elif line == "":
            if in_list:
                if line.startswith('- '):
                    html_content.append("</ul>")
                elif line.startswith('* '):
                    html_content.append("</ol>")
                in_list = False
            html_content.append("</p><p>")

        else:
            line = line.replace('**', '<b>').replace('__', '<em>')
            line = line.replace('[[', '').replace(']]', lambda x: hashlib.md5(x.encode()).hexdigest())
            line = line.replace('((', '').replace('))', lambda x: x.replace('c', '').replace('C', ''))
            if not in_list:
                html_content.append(f"<p>{line}</p>")
            else:
                html_content.append(line)
    
    if in_list:
        if line.startswith('- '):
            html_content.append("</ul>")
        elif line.startswith('* '):
            html_content.append("</ol>")
            
    return "\n".join(html_content)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_filename = sys.argv[1]
    html_filename = sys.argv[2]

    if not os.path.exists(markdown_filename):
        print(f"Missing {markdown_filename}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_filename, 'r') as md_file:
        markdown_content = md_file.readlines()

    html_content = convert_md_to_html(markdown_content)

    with open(html_filename, 'w') as html_file:
        html_file.write(html_content)

    sys.exit(0)


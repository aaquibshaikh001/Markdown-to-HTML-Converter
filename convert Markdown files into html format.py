import argparse
import os
import markdown
from datetime import datetime

def convert_markdown_to_html(input_file, output_file=None):
    """
    Convert a Markdown file to HTML
    
    Args:
        input_file (str): Path to the input Markdown file
        output_file (str, optional): Path to the output HTML file. If None, uses input filename with .html extension
    
    Returns:
        str: Path to the generated HTML file
    """
    # Validate input file
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    if not input_file.endswith('.md'):
        raise ValueError("Input file must have a .md extension")
    
    # Set default output filename if not provided
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.html'
    
    # Read Markdown content
    with open(input_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    
    # Convert to HTML
    html_content = markdown.markdown(md_content)
    
    # Add basic HTML structure
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{os.path.basename(input_file)}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }}
    </style>
</head>
<body>
{html_content}
<footer>
    <p>Generated from {os.path.basename(input_file)} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
</footer>
</body>
</html>"""
    
    # Write HTML file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(full_html)
    
    return output_file

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown files to HTML')
    parser.add_argument('input', help='Input Markdown file (.md)')
    parser.add_argument('-o', '--output', help='Output HTML file (optional)')
    
    args = parser.parse_args()
    
    try:
        output_path = convert_markdown_to_html(args.input, args.output)
        print(f"Successfully converted {args.input} to {output_path}")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == '__main__':
    main()
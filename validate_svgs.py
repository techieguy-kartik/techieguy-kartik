import os
import glob
import xml.etree.ElementTree as ET

repo_dir = "/Users/apple/Downloads/Devanik21/techieguy-kartik"
svg_files = glob.glob(os.path.join(repo_dir, "**/*.svg"), recursive=True)

for svg_path in svg_files:
    rel_path = os.path.relpath(svg_path, repo_dir)
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()

    try:
        ET.fromstring(content)
        print(f"✅ {rel_path} is VALID XML!")
    except ET.ParseError as e:
        print(f"❌ {rel_path} XML ERROR: {e}")
        line_no = getattr(e, 'position', (0, 0))[0]
        col_no = getattr(e, 'position', (0, 0))[1]
        lines = content.splitlines()
        if 0 <= line_no - 1 < len(lines):
            print(f"   Line {line_no}, Col {col_no}: {lines[line_no - 1]}")

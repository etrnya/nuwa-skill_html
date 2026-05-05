import os
import json
import re

def parse_frontmatter(content):
    """
    簡單解析 markdown frontmatter
    """
    matter = {}
    pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n(.*)', re.DOTALL)
    match = pattern.match(content)
    
    if match:
        yaml_part = match.group(1)
        # 用簡單的正則擷取 name 和 description
        name_match = re.search(r'^name:\s*(.*?)$', yaml_part, re.MULTILINE)
        if name_match:
            matter['name'] = name_match.group(1).strip()
            
        desc_match = re.search(r'^description:\s*\|(.*?)(?:^\w|\Z)', yaml_part, re.MULTILINE | re.DOTALL)
        if desc_match:
            matter['description'] = desc_match.group(1).strip()
        else:
            # Maybe single line description
            desc_match_single = re.search(r'^description:\s*(.*?)$', yaml_part, re.MULTILINE)
            if desc_match_single:
                matter['description'] = desc_match_single.group(1).strip()
                
        tags_match = re.search(r'^tags:\s*\[(.*?)\]', yaml_part, re.MULTILINE)
        if tags_match:
            tags_str = tags_match.group(1).strip()
            matter['tags'] = [t.strip() for t in tags_str.split(',') if t.strip()]
        else:
            matter['tags'] = []
    return matter

def build_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    examples_dir = os.path.join(base_dir, 'examples')
    
    skills = []
    
    if not os.path.exists(examples_dir):
        print(f"Error: {examples_dir} does not exist.")
        return
        
    for root, dirs, files in os.walk(examples_dir):
        for file in files:
            if file == 'SKILL.md':
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    frontmatter = parse_frontmatter(content)
                    folder_name = os.path.basename(root)
                    
                    name = frontmatter.get('name', folder_name)
                    description = frontmatter.get('description', '無提供描述。')
                    tags = frontmatter.get('tags', [])
                    
                    skills.append({
                        "id": folder_name,
                        "name": name,
                        "description": description,
                        "tags": tags,
                        "system_prompt": content
                    })
                    print(f"Successfully loaded: {name.encode('cp950', 'replace').decode('cp950')}")
                except Exception as e:
                    print(f"Failed to read {file_path}: {e}")
                    
    # Generate JS file
    output_path = os.path.join(base_dir, 'skills_data.js')
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("window.NUWA_SKILLS = ")
            f.write(json.dumps(skills, ensure_ascii=False, indent=2))
            f.write(";\n")
        print(f"Generated {output_path} with {len(skills)} skills.")
    except Exception as e:
        print(f"Failed to write JS data file: {e}")

if __name__ == '__main__':
    build_data()

import os
from opencc import OpenCC

def convert_dir_to_tc(directory):
    cc = OpenCC('s2twp') # Simplified to Traditional (Taiwan standard with phrases)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Convert the content
                converted_content = cc.convert(content)
                
                # Write back
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(converted_content)
                print(f"Converted file successfully")

if __name__ == "__main__":
    examples_dir = os.path.join(os.path.dirname(__file__), "examples")
    convert_dir_to_tc(examples_dir)
    print("All markdown files have been converted to Traditional Chinese.")

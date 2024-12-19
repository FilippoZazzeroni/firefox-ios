import os
from lxml import etree

# Get the current directory
current_dir = os.getcwd()

# List all folders in the current directory
folders = [f for f in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, f))]

# Function to check if a folder name is a valid language code (basic validation)
def is_language_code(folder_name):
    return len(folder_name) in (2, 5) and folder_name.isalpha()

# Filter folders with valid language codes
language_folders = [folder for folder in folders if is_language_code(folder)]

# Process each folder
for folder in language_folders:
    folder_path = os.path.join(current_dir, folder)
    
    # Process each file in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Ensure we process only XML files
        if file_name.endswith(".xliff"):
            try:
                # Parse the XML file
                tree = etree.parse(file_path)
                root = tree.getroot()
                NS = {"x": "urn:oasis:names:tc:xliff:document:1.2"}
                # Find all <original> tags
                for file_node in root.xpath("//x:file", namespaces=NS):
                    file_node.set("original", file_node.get("original").replace("en.lproj", "en-US.lproj"))
                tree.write(file_path, pretty_print=True, xml_declaration=True, encoding="UTF-8")                
                print(f"Updated file: {file_path}")

            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
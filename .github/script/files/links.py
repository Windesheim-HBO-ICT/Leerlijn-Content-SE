# Imports
import re, os
from pathlib import Path

# Variables
from config import VALID_DYNAMIC_LINK_PREFIXES, ERROR_INVALID_DYNAMIC_LINK, VERBOSE

"""
Update dynamic links in the content of a markdown file.

Args:
    filePath (str): Path to the markdown file.
    content (str): Content of the markdown file.
"""
def updateDynamicLinks(filePath, content, skipValidateDynamicLinks):
    # Find all dynamic links in the content
    dynamic_links = re.findall(r'\[\[[^"\[][^]]*?\]\]', content)

    errors = []
    
    for link in dynamic_links:
        # Skip links that start with any of the valid prefixes
        cleaned_link = link.strip('[[]]')
        
        if any(cleaned_link.startswith(prefix) for prefix in VALID_DYNAMIC_LINK_PREFIXES):
            return content, errors
        
        # Strip 'content/' prefix if present
        new_link = link.replace('content/', '')
        
        # Replace the old link with the new link in the content
        content = content.replace(link, new_link)
        
        # Skip dynamic link check if flag is set
        # This is used in the PR validation check when only updated the content is being checked
        if(skipValidateDynamicLinks):
            continue

        # Check if the dynamic link is valid
        if not validateDynamicLink(filePath, new_link):
            if VERBOSE: print(ERROR_INVALID_DYNAMIC_LINK + new_link)
            errors.append(ERROR_INVALID_DYNAMIC_LINK + ' `' + new_link + '` ')

    return content, errors

"""
Checks if the dynamic link is valid and the file exists.

Args:
    source_filePath (str): Path to the source file.
    link (str): Dynamic link to validate.
"""
def validateDynamicLink(source_filePath, link):
    # Define the root content directory (assuming it is one level up from the current script)
    content_path = source_filePath
    while Path(content_path).name != 'content' and Path(content_path).name != 'test_cases':
        content_path = content_path.parent
    
    # Verify that content_path exists
    if not content_path.exists():
        print(f"Error: Content path '{content_path}' does not exist.")
        return False

    # Clean up the link by removing the surrounding [[ and ]]
    cleaned_link = link.strip('[[]]')

    # If the link contains a section (anchor), split the link at '#'
    if '#' in cleaned_link:
        cleaned_link = cleaned_link.split('#')[0]  # Use only the part before '#'

    # Parse the base name from the cleaned link
    link_parts = cleaned_link.split('|')
    file_name = link_parts[0].strip().split('/')[-1]

    # Search for the file in all subdirectories within 'content' using os.walk
    found_file = None
    for root, dirs, files in os.walk(content_path):
        for file in files:
            if file.startswith(file_name):  # Check if the file name matches
                found_file = os.path.join(root, file)
                return True

    # If no valid file is found, report error with details
    if not found_file:
        if VERBOSE: print(f"Error: source file: {source_filePath}, target file '{file_name}' not found in content.")

    return False

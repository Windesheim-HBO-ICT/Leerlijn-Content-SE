# Imports
import re
from pathlib import Path

# Variables
from config import failedFiles, dataset, Report_2, WIPFiles

# Constants
from config import PROCES_COL, PROCESSTAP_COL, TC3_COL, TC2_COL, TAXONOMIE_PATTERN, TODO_PATTERN, FOLDERS_FOR_4CID, VERBOSE, ERROR_INVALID_TAXCO
from config import ERROR_MISSING_TAXCO, NOT_NECESSARY, ERROR_TAXCO_NOT_NEEDED, ERROR_TAXCO_NOT_FOUND, ERROR_TAXCO_IN_WRONG_4CID_COMPONENT

# Functions
from report.table import generateMarkdownTable
from report.update import updateProcessReportData, updateSubjectReportData


# Create a new row in the file report based on the status, file path, taxonomie, and tags.
def createFileReportRow(status, filePath, src_dir, taxonomie, tags, errors):
    return {
        "status": status,
        "file": filePath.stem,
        "path": str(filePath.relative_to(src_dir)),
        "taxonomie": '<br>'.join(taxonomie) if taxonomie else "N/A",
        "tags": '<br>'.join(tags) if tags else "N/A",
        "errors": '<br>'.join(errors) if errors else "N/A"
    }

# Format the success or failed report table based on a list.
def formatFileReportTable(file_report):
    headers = ["Status", "File", "Path", "Taxonomie", "Tags", "Errors"]

    if file_report == failedFiles or file_report == WIPFiles : headers.append("Errors")
    rows = [[
        file['status'], 
        file['file'], 
        file['path'], 
        file['taxonomie'], 
        file['tags'],
        file['errors']
     ] for file in file_report]

    table = generateMarkdownTable(headers, rows)
    return table

"""
Generate tags based on the taxonomie values
Args:
    taxonomies (list): List of taxonomie values.
    filePath (str): Path to the file.
"""
def generateTags(taxonomies, filePath, existingTags):
    tags = []
    errors = []
    combined_tags = []
    taxonomie_tags = []

    if taxonomies is not None and taxonomies != ['None'] and taxonomies != [''] and taxonomies != []:
        for taxonomie in taxonomies:
            if VERBOSE : print(f"Generating tags for taxonomie: {taxonomie}")
            # Check if the taxonomie is in the correct format
            if not re.match(TAXONOMIE_PATTERN, taxonomie):
                errors.append(ERROR_INVALID_TAXCO + ' `' + taxonomie + '` ')
                print(ERROR_INVALID_TAXCO + taxonomie)
                continue

            # split the taxonomie in it's different parts
            tc_1, tc_2, tc_3, tc_4 = split_taxonomie(taxonomie)
            # if the parts are all valid
            if tc_1 and tc_2 and tc_3 and tc_4:
                # Loop trough every row in the dataset
                for row in dataset[1:]:
                    # Check if the first part of the taxonomie is equal to the second column (TC1) in the dataset
                    if row[1] == tc_1:
                        # Check if the second part of the taxonomie is equal to the third column (TC2) in the dataset
                        if row[5] in Report_2 and row[5] == tc_3:
                            # Adds the taxonomie
                            new_tag = "HBO-i/niveau-" + tc_2
                            if new_tag not in tags:
                                tags.append(new_tag)
    
                            # Adds the proces
                            if row[PROCES_COL] not in tags:
                                tags.append(row[PROCES_COL])

                            # Adds the processtap
                            if row[PROCESSTAP_COL] not in tags:
                                tags.append(row[PROCESSTAP_COL])

                            # Check if the third part of the taxonomie is in the lookup table
                            if row[TC3_COL] not in tags:
                                tags.append(row[TC3_COL])

                            # Check if the taxonomie is not needed
                            splitted_row2 =  row[TC2_COL].split(',')
                            if splitted_row2[int(tc_2)-1] == "X": 
                               tags.append(NOT_NECESSARY)
                            
                            # Checks if the fourth path has the matching 4C/ID component (looking at the folder and taxonomie code)
                            containsCorrectTaxcos = checkIfFileContainsWrong4cid(taxonomies, filePath)
                            if containsCorrectTaxcos:
                                updateProcessReportData(tc_1, tc_2)
                                updateSubjectReportData(getFileType(filePath), tc_1, tc_2, tc_3)   
                            else:   
                                errors.append(ERROR_TAXCO_IN_WRONG_4CID_COMPONENT + ' `' + taxonomie + '` ')                        

                            taxonomie_tags = sorted(list(set(taxonomies)))

        # If no tags were found, add an error
            if NOT_NECESSARY in tags: 
                tags.remove(NOT_NECESSARY)
                errors.append(ERROR_TAXCO_NOT_NEEDED + ' `' + taxonomie + '` ')   
            if tags == [] and not errors:
                errors.append(ERROR_TAXCO_NOT_FOUND + ' `' + taxonomie + '` ')   
                if VERBOSE: print(ERROR_TAXCO_NOT_FOUND + taxonomie)
    else:
        errors.append(ERROR_MISSING_TAXCO)
        if VERBOSE: print(ERROR_MISSING_TAXCO)  

    # Combine the existing tags with the new tags
    if existingTags: combined_tags += existingTags 
    if tags : combined_tags += tags 
    if taxonomie_tags : combined_tags += taxonomie_tags
    
    # Sort combined_tags so that "HBO-i/niveau-" tags are moved to the start
    combined_tags = sorted(combined_tags, key=lambda tag: (not tag.startswith("HBO-i/niveau-"), tag))

    return list(dict.fromkeys(combined_tags)), errors

# Returns the folder name after the 'content' directory in the path.
def getFileType(filePath):
    # Convert to Path object if not already
    filePath = Path(filePath)
    # Find the 'content' directory in the path
    folder_path = filePath

    while folder_path.parent.name != 'content' and folder_path.parent.name != 'test_cases':
        folder_path = folder_path.parent
    if not folder_path.name.endswith('.md') :
        cleaned_folder_name = re.sub(r'^\d+\.\s*', '', folder_path.name)
        return cleaned_folder_name
    return None

def split_taxonomie(taxonomie):
    return taxonomie.split('.')

# Helper function to extract specific values from the content of a markdown file.
def extractHeaderValues(content, field_name):
    lines = content.splitlines()
    values = []

    for i, line in enumerate(lines):
        if line.startswith(f'{field_name}:'):
            # Handle case where the field has a single value
            if ':' in line and len(line.split(':', 1)[1].strip()) > 0:
                values.append(line.split(':', 1)[1].strip())
            else:
                # Handle case where the field is a list
                for j in range(i + 1, len(lines)):
                    sub_line = lines[j].strip()
                    if sub_line.startswith('- '):
                        values.append(sub_line.lstrip('- ').strip())
                    else:
                        break
            break

    return values if values else None

# Helper function to find all the To-Do items in the content of a markdown file.	
def findWIPItems(content):
    # Find all the todo items in the content
    todo_items = re.findall(TODO_PATTERN, content)
    return todo_items

# Checks if a file contains at least one wrong taxonomie code (based on incorrect placement of 4C/ID)
def checkIfFileContainsWrong4cid(taxonomies, filePath):
    containsOnlyCorrectTaxonomie = True
    for taxonomie in taxonomies:
        if not re.match(TAXONOMIE_PATTERN, taxonomie):
            continue
        tc_1, tc_2, tc_3, tc_4 = split_taxonomie(taxonomie)  
        if tc_1 and tc_2 and tc_3:
            if tc_4 in FOLDERS_FOR_4CID:
                expected_folder = FOLDERS_FOR_4CID[tc_4]
                if expected_folder not in str(filePath):
                    containsOnlyCorrectTaxonomie = False
    return containsOnlyCorrectTaxonomie            

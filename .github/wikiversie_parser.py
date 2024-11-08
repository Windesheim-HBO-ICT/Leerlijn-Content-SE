import os
import re
import csv
import time
import shutil
import argparse
import sys
import json
from pathlib import Path
import pandas as pd

# Global variables
Dataset = list()  # Dataset list
Successful_files = [] # Track the status of each file
Failed_files = [] # Track the status of each file
Successful_test_files = [] # Track which files where successful in testing
Failed_test_files = [] # Track which files failed in testing
Verbose = False # Verbose output flag
Testing = False # Testing output flag
Taxonomie_pattern = r'^[a-z]{2}-\d{1,3}\.[123]\.[^\s\.]+(\.[^\s\.]+)*\.[A-Z]{2}$' # Taxonomie pattern

Rapport_1 = {} # Rapport 1 data
Rapport_2 = {} # Rapport 2 data

# Dataset columns
TC1_COL = 1
TC2_COL = 2
TC3_COL = 5
PROCES_COL = 3
PROCESSTAP_COL = 4
LT_COL = 7
OI_COL = 8
PI_COL = 9
DT_COL = 10

# 4CID
LT = "Leertaken"
OI = "Ondersteunende-informatie" 
PI = "Procedurele-informatie"
DT = "Deeltaken"

#Error message for not including any taxonomy code
ERROR_MISSING_TAXCO = "No taxonomie found in file."

# Icons
SUCCESS = "✅"
FAIL_CIRCLE = "⛔️"
FAIL_CROSS = "❌"
NOT_NECESSARY = "🏳️"
WRONG_TAXONOMY_CODE = "⚠️"
NOT_NEEDED = "🟠"

## Structure of Rapport_1
#
# Rapport_1 = {
#     'rv-8' : {
#         'Proces' : "Requirementanalyseproces"
#         'Processtap' : "Verzamelen requirements",
#         'TC2' : ['x', '~', 'x']
#     },
#     'pu-13' : {
#         'Proces' : "Pakketselectieproces"
#         'Processtap' : "Uitvoeren analyse",
#         'TC2' : ['x', 'x', 'x']
#     }
# }

## Structure of Rapport_2
#
# Rapport_2 = {
#     'functioneel-ontwerp' : {
#         'oo-15' : {
#             'TC2' : ['x', 'x', 'x'],
#             LT : ['x', 'x', 'x'],
#             OI : ['x', 'x', 'x'], 
#             PI : ['x', 'x', 'x'], 
#             DT : ['x', 'x', 'x']
#         },
#         'rs-10' : {
#             'TC2' : ['x', 'x', 'x'],
#             LT : ['x', 'x', 'x'],
#             OI : ['x', 'x', 'x'], 
#             PI : ['x', 'x', 'x'], 
#             DT : ['x', 'x', 'x']
#         },
#         'ra-9' : {
#             'TC2' : ['x', 'x', 'x'],
#             LT : ['x', 'x', 'x'],
#             OI : ['x', 'x', 'x'], 
#             PI : ['x', 'x', 'x'], 
#             DT : ['x', 'x', 'x']
#         }
#     },
#     "Technisch ontwerp": {
#         'oo-15' : {
#           'TC2' : ['x', 'x', 'x'],
#           LT : ['x', 'x', 'x'],
#           OI : ['x', 'x', 'x'], 
#           PI : ['x', 'x', 'x'], 
#           DT : ['x', 'x', 'x']
#       }
#    }
# }

"""
Parse the dataset file from a XLSX file to a list.

Args:
    dataset_file (str): Path to the dataset XLSX file.
"""
def parse_dataset_file(dataset_file):
    global Dataset

    try:
        df = pd.read_excel(dataset_file)
        csv_data = df.to_csv(index=False, sep=';')
        reader = csv.reader(csv_data.splitlines(), delimiter=';', quotechar='|')
        Dataset = list(reader)
    except FileNotFoundError:
        print(f"File {dataset_file} not found.")
        exit()
    except Exception as e:
        print(f"An error occurred while reading the dataset file: {e}")
        exit()

"""
Fills the rapport 1 data with the data from the dataset
Every TC1 code is the unique identifier
"""
def populate_rapport1():
    global Rapport_1
    for row in Dataset[1:]:
        tc_1 = row[TC1_COL]
        tc_2 = row[TC2_COL]
        proces = row[PROCES_COL]
        processtap = row[PROCESSTAP_COL]

        if tc_1 not in Rapport_1: 
            splitted_tc2 = tc_2.split(',')

            Rapport_1[tc_1] = {
                "Proces" : proces,
                "Processtap" : processtap,
                'TC2': [NOT_NECESSARY if splitted_tc2[0] == 'X' else 'x', NOT_NECESSARY if splitted_tc2[1] == 'X' else 'x', NOT_NECESSARY if splitted_tc2[2] == 'X' else 'x']        
            }

"""
Fills the Rapport 2 data with the data from the dataset.
Every unique TC3 and TC1 combination will be added to the Rapport 2 data.
"""
def populate_rapport2():
    global Rapport_2

    for row in Dataset[1:]:
        tc_1 = row[TC1_COL]
        tc_2 = row[TC2_COL]
        tc_3 = row[TC3_COL]
        lt = row[LT_COL]
        oi = row[OI_COL]
        pi = row[PI_COL]
        dt = row[DT_COL]

        if tc_3 not in Rapport_2:
            Rapport_2[tc_3] = {}

        if tc_1 not in Rapport_2[tc_3]:
            splitted_tc2 = tc_2.split(',')
            splitted_lt = lt.split(',')
            splitted_oi = oi.split(',')
            splitted_pi = pi.split(',')
            splitted_dt = dt.split(',')
            
            Rapport_2[tc_3][tc_1] = {
                'TC2': [NOT_NECESSARY if splitted_tc2[0] == 'X' else 'x', NOT_NECESSARY if splitted_tc2[1] == 'X' else 'x', NOT_NECESSARY if splitted_tc2[2] == 'X' else 'x'],
                LT: [NOT_NECESSARY if splitted_lt[0] == 'X' else 'x', NOT_NECESSARY if splitted_lt[1] == 'X' else 'x', NOT_NECESSARY if splitted_lt[2] == 'X' else 'x'],
                OI: [NOT_NECESSARY if splitted_oi[0] == 'X' else 'x', NOT_NECESSARY if splitted_oi[1] == 'X' else 'x', NOT_NECESSARY if splitted_oi[2] == 'X' else 'x'],
                PI: [NOT_NECESSARY if splitted_pi[0] == 'X' else 'x', NOT_NECESSARY if splitted_pi[1] == 'X' else 'x', NOT_NECESSARY if splitted_pi[2] == 'X' else 'x'],
                DT: [NOT_NECESSARY if splitted_dt[0] == 'X' else 'x', NOT_NECESSARY if splitted_dt[1] == 'X' else 'x', NOT_NECESSARY if splitted_dt[2] == 'X' else 'x'],
            }

"""
Helper function to extract values from the content of a markdown file.
Args:
    content (str): Content of the markdown file.
    field_name (str): Field name to extract values for.
Returns:
    values (list): List of values extracted from the content.
"""
def extract_values(content, field_name):
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

"""
Split the taxonomie value into a list of individual taxonomie parts.
Args:
    taxonomie (str): Taxonomie value to split.
Returns:
    parts (list): List of taxonomie parts.
"""
def split_taxonomie(taxonomie):
    return taxonomie.split('.')

"""
Returns the folder name after the 'content' directory in the path.
Args:
    file_path (str): Path to the file.
Returns:
    folder_name (str): Folder name after the 'content' directory.
"""
def get_file_type(file_path):
    # Convert to Path object if not already
    file_path = Path(file_path)
    
    # Find the 'content' directory in the path
    parts = file_path.parts
    if 'content' in parts:
        content_index = parts.index('content')
        # Return the first folder after 'content' without leading number and space
        if content_index + 1 < len(parts):
            folder_name = parts[content_index + 1]
            # Remove leading number and space
            cleaned_folder_name = re.sub(r'^\d+\.\s*', '', folder_name)
            return cleaned_folder_name
    
    return None

"""
Generate a markdown table string from a list of rows and headers.
Args:
    headers (list): List of header values.
    rows (list): List of lists containing row values.
Returns:
    table (str): Markdown table string.
"""
def generate_markdown_table(headers, rows):
    table = "| " + " | ".join(headers) + " |\n"
    table += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    for row in rows:
        table += "| " + " | ".join(row) + " |\n"
    return table

"""
Generate tags based on the taxonomie values
Args:
    taxonomies (list): List of taxonomie values.
    file_path (str): Path to the file.
Returns:
    tags (list): List of tags generated from the taxonomie values.
"""
def generate_tags(taxonomies, file_path):
    global Rapport_2

    tags = []
    errors = []
    if taxonomies is not None:
        for taxonomie in taxonomies:
            # Check if the taxonomie is in the correct format
            if not re.match(Taxonomie_pattern, taxonomie):
                errors.append(f"Invalid taxonomie: {taxonomie}")
                if Verbose: print(f"Invalid taxonomie: {taxonomie}")
                continue

            # split the taxonomie in it's different parts
            tc_1, tc_2, tc_3, tc_4 = split_taxonomie(taxonomie)

            # if the parts are all valid
            if tc_1 and tc_2 and tc_3:
                # Loop trough every row in the dataset
                for row in Dataset[1:]:
                    # Check if the first part of the taxonomie is equal to the second column (TC1) in the dataset
                    if row[1] == tc_1:
                        # Check if the second part of the taxonomie is equal to the third column (TC2) in the dataset
                        if row[5] in Rapport_2 and row[5] == tc_3:
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

                            # Sort the tags so that the HBO-i tags are first
                            tags.sort(key=lambda x: x.startswith('HBO-i'), reverse=True)
                            
                            update_rapport1_data(tc_1, tc_2)
                            update_rapport2_data(get_file_type(file_path), tc_1, tc_2, tc_3)

        # If no tags were found, add an error
        if NOT_NECESSARY in tags: 
            tags.remove(NOT_NECESSARY)
            errors.append(f"Taxonomie used where it is not needed: {taxonomie}")
        if tags == [] and not errors:
            errors.append(f"Taxonomie not found in dataset: {taxonomie}")
            if Verbose: print(f"Taxonomie not found in dataset: {taxonomie}")
    else:
        errors.append(ERROR_MISSING_TAXCO)
        if Verbose: print(ERROR_MISSING_TAXCO)

    return tags, errors

"""
Update the Rapport 1 data with the new values.
Args:
    tc_1 (str): TC1 code.
    tc_2 (str): TC2 code.
"""
def update_rapport1_data(tc_1, tc_2):
    Rapport_1[tc_1]['TC2'] = ['v' if tc_2 == '1' and Rapport_1[tc_1]['TC2'][0] != NOT_NECESSARY else Rapport_1[tc_1]['TC2'][0], 'v' if tc_2 == '2' and Rapport_1[tc_1]['TC2'][1] != NOT_NECESSARY else Rapport_1[tc_1]['TC2'][1], 'v' if tc_2 == '3' and Rapport_1[tc_1]['TC2'][2] != NOT_NECESSARY else Rapport_1[tc_1]['TC2'][2]]

"""
Update the Rapport 2 data with the new values.
Args:
    file_type (str): File type.
    tc_1 (str): TC1 code.
    tc_2 (str): TC2 code.
    tc_3 (str): TC3 code.
"""
def update_rapport2_data(file_type, tc_1, tc_2, tc_3):
    # Update the record with the new values
    def update_rapport2_row(tc_3, tc_1, tc_2, file_type, searchType):
        Rapport_2[tc_3][tc_1][searchType] = [
            'v' if file_type == searchType and tc_2 == '1' and Rapport_2[tc_3][tc_1][searchType][0] != NOT_NECESSARY else Rapport_2[tc_3][tc_1][searchType][0], 
            'v' if file_type == searchType and tc_2 == '2' and Rapport_2[tc_3][tc_1][searchType][1] != NOT_NECESSARY else Rapport_2[tc_3][tc_1][searchType][1], 
            'v' if file_type == searchType and tc_2 == '3' and Rapport_2[tc_3][tc_1][searchType][2] != NOT_NECESSARY else Rapport_2[tc_3][tc_1][searchType][2]
        ]

    Rapport_2[tc_3][tc_1]['TC2'] = ['v' if tc_2 == '1' and Rapport_2[tc_3][tc_1]['TC2'][0] != NOT_NECESSARY else Rapport_2[tc_3][tc_1]['TC2'][0], 'v' if tc_2 == '2' and Rapport_2[tc_3][tc_1]['TC2'][1] != NOT_NECESSARY else Rapport_2[tc_3][tc_1]['TC2'][1], 'v' if tc_2 == '3' and Rapport_2[tc_3][tc_1]['TC2'][2] != NOT_NECESSARY else Rapport_2[tc_3][tc_1]['TC2'][2]]
    update_rapport2_row(tc_3, tc_1, tc_2, file_type, LT)
    update_rapport2_row(tc_3, tc_1, tc_2, file_type, OI)
    update_rapport2_row(tc_3, tc_1, tc_2, file_type, PI)
    update_rapport2_row(tc_3, tc_1, tc_2, file_type, DT)

"""
Format the report table for table 1
Returns:
    table (str): Markdown table string.
"""
def generate_rapport_1():
    if Verbose: print("Generating Rapport 1 table...")

    headers = ["TC1", "Proces", "Processtap", "Niveau 1", "Niveau 2", "Niveau 3"]
    rows = []
    for tc, details in Rapport_1.items():
        proces = details.get('Proces', '')
        processtap = details.get('Processtap', '')
        tc2_levels = details.get('TC2', {})
        niveau_1 = FAIL_CIRCLE if tc2_levels[0] == 'x' else SUCCESS if tc2_levels[0] == 'v' or tc2_levels[0] == 'g' else NOT_NECESSARY
        niveau_2 = FAIL_CIRCLE if tc2_levels[1] == 'x' else SUCCESS if tc2_levels[1] == 'v' or tc2_levels[1] == 'g' else NOT_NECESSARY        
        niveau_3 = FAIL_CIRCLE if tc2_levels[2] == 'x' else SUCCESS if tc2_levels[2] == 'v' or tc2_levels[2] == 'g' else NOT_NECESSARY

        rows.append([tc, proces, processtap, niveau_1, niveau_2, niveau_3])

    table = generate_markdown_table(headers, rows)

    if Verbose: print("Rapport 1 table generated.")

    return table

"""
Format the report for table 2
Returns:
    table (str): Markdown table string.
"""
def generate_rapport_2():
    if Verbose: print("Generating Rapport 2 table...")

    headers = ["TC3", "TC1", "TC2", LT, OI, PI, DT]
    rows = []

    def get_status(value):
        if value == 'v' or value == 'g':
            return SUCCESS
        elif value != NOT_NECESSARY:
            return FAIL_CIRCLE
        else:
            return NOT_NECESSARY

    for tc3, details in Rapport_2.items():
        for tc1, other in details.items():
            tc2_levels = other.get('TC2', [''] * 3)
            tc2 = ' '.join([get_status(level) for level in tc2_levels])

            leertaak_levels = other.get(LT, [''] * 3)
            leertaak = ' '.join([get_status(level) for level in leertaak_levels])
            
            ondersteunende_informatie_levels = other.get(OI, [''] * 3)
            ondersteunende_informatie = ' '.join([get_status(level) for level in ondersteunende_informatie_levels])
            
            procedurele_informatie_levels = other.get(PI, [''] * 3)
            procedurele_informatie = ' '.join([get_status(level) for level in procedurele_informatie_levels])
            
            deeltaak_levels = other.get(DT, [''] * 3)
            deeltaak = ' '.join([get_status(level) for level in deeltaak_levels])

            rows.append([tc3, tc1, tc2, leertaak, ondersteunende_informatie, procedurele_informatie, deeltaak])

    table = generate_markdown_table(headers, rows)

    if Verbose: print("Rapport 2 table generated.")

    return table

"""
Format the success or failed report table.
Args:
    file_report (list): List of file reports.
Returns:
    table (str): Markdown table string.
"""
def format_file_report_table(file_report):
    headers = ["Status", "File", "Path", "Taxonomie", "Tags"]

    if file_report == Failed_files: headers.append("Errors")
    rows = [[
        file['status'], 
        file['file'], 
        file['path'], 
        file['taxonomie'], 
        file['tags'],
        file['errors']
    ] for file in file_report]

    table = generate_markdown_table(headers, rows)
    return table

"""
Create a file report based on the status, file path, taxonomie, and tags.
Args:
    status (str): Status of the file processing.
    file_path (str): Path to the file.
    taxonomie (list): List of taxonomie values.
    tags (list): List of tags.
Returns:
    file_report (dict): File report dictionary.
"""
def create_file_report(status, file_path, src_dir, taxonomie, tags, errors):
    return {
        "status": status,
        "file": file_path.stem,
        "path": str(file_path.relative_to(src_dir)),
        "taxonomie": '<br>'.join(taxonomie) if taxonomie else "N/A",
        "tags": '<br>'.join(tags) if tags else "N/A",
        "errors": '<br>'.join(errors) if errors else "N/A"
    }

"""
Create a list of a file for test cases
"""
def create_test_file_result(file_path, taxonomie, tags, errors):
    return {
        "file": file_path.stem,
        "taxonomie": '<br>'.join(taxonomie) if taxonomie else "N/A",
        "tags": '<br>'.join(tags) if tags else "N/A",
        "errors": '<br>'.join(errors) if errors else "N/A"
    }

"""
Generate the report based on the taxonomie report, success, and failed reports.
"""
def generate_report():
    if Verbose: print("Generating report...")

    report_path = "report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write('---\ndraft: true\n---\n')
        
        # Rapport 1 Section
        f.write('## Rapport 1 - Processtappen\n')
        f.write('*Doel: achterhalen welke processtappen nog helemaal niet zijn geïmplementeerd*\n\n')
        f.write('✅ Er bestaat een bestand met deze taxonomiecode op dit niveau\n')
        f.write('⛔️ Er is geen enkel bestand met deze taxonomiecode op dit niveau\n')
        f.write('🏳️ De taxonomiecode wordt niet aangeboden op dit niveau (X in de Dataset)\n')
        f.write('\n')
        f.write(generate_rapport_1())

        f.write('\n\n')

        # Rapport 2 Section
        f.write('## Rapport 2 - Onderwerpen Catalogus\n')
        f.write('*Doel: Lijst met onderwerpen + gekoppelde taxonomie code voor inzicht in aangeboden onderwerpen.*\n')
        f.write('Bij kolom *TC2*, *Leertaken*, *Ondersteunende informatie*, *Procedurele informatie* en *Deeltaken* zijn drie tekens aanwezig om de drie HBO-i niveaus weer te geven\n\n')
        f.write('✅ Het onderwerp met taxonomie code wordt aangeboden op het aangegeven niveau\n')
        f.write('⛔️ Het onderwerp met taxonomie code wordt **niet** aangeboden op het aangegeven niveau\n')
        f.write('🏳️ Het onderwerp hoeft met deze taxonomie code niet aangeboden te worden op het aangegeven niveau\n')
        f.write('\n')
        f.write(generate_rapport_2())

        f.write('\n\n')

        # Passed Files Section
        f.write("## Geslaagde bestanden\n")
        f.write("De onderstaande bestanden zijn succesvol verwerkt.\n")
        f.write('\n')
        f.write(format_file_report_table(Successful_files))

        f.write('\n\n')

        # Failed Files Section
        f.write("## Gefaalde bestanden\n")
        f.write("*Doel: De onderstaande bestanden zijn niet succesvol verwerkt.*\n\n")
        f.write('❌ Dit bestand bevat nog geen taxonomie code\n')
        f.write('⚠️ Dit bestand bevat een foute taxonomie code. Zie de *Errors* kolom om te weten wat er mis is\n')
        f.write('🟠 Dit bestand bevat een taxonomie code die niet toegevoegd hoeft te zijn\n')
        f.write('\n')
        f.write(format_file_report_table(Failed_files))

    # Print reports for quick feedback
    if Verbose:
        print("Rapport 1:")
        print(generate_rapport_1())
        print("Rapport 2:")
        print(generate_rapport_2())
        print("Geslaagde bestanden:")
        print(format_file_report_table(Successful_files))
        print("Gefaalde bestanden:")
        print(format_file_report_table(Failed_files))

        print("Report generated.")

"""
Update markdown files in the source directory with taxonomie tags and generate reports.
Args:
    src_dir (str): Source directory containing markdown files.
    dest_dir (str): Destination directory to save updated markdown files and reports.
"""
def parse_markdown_files(src_dir, dest_dir):
    if Verbose: print("Parsing markdown files...")

    dest_dir.mkdir(parents=True, exist_ok=True)

    # Loop through all markdown files in the source directory
    for file_path in Path(src_dir).rglob('*.md'):
        relative_path = file_path.relative_to(src_dir)
        dest_path = dest_dir / relative_path

        if Verbose: print(f"Parsing file: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract existing tags and taxonomie
        existing_tags = extract_values(content, 'tags')
        taxonomie = extract_values(content, 'taxonomie')
        new_tags, errors = generate_tags(taxonomie, file_path)
        difficulty = extract_values(content, 'difficulty')

        # If any errors occurred, add the file to the failed files list
        if errors:
            if(ERROR_MISSING_TAXCO in errors): 
                Failed_files.append(create_file_report(FAIL_CROSS, file_path, src_dir, taxonomie, new_tags, errors))
            elif any("Taxonomie use where it is not need" in error for error in errors):
                Failed_files.append(create_file_report(NOT_NEEDED, file_path, src_dir, taxonomie, new_tags, errors))
            else: 
                Failed_files.append(create_file_report(WRONG_TAXONOMY_CODE, file_path, src_dir, taxonomie, new_tags, errors))
            if Verbose: print(f"Failed to parse file: {file_path}")
        else:
            Successful_files.append(create_file_report(SUCCESS, file_path, src_dir, taxonomie, new_tags, errors))

        # Combine existing and new tags
        if existing_tags:
            combined_tags = existing_tags + new_tags + taxonomie if taxonomie and new_tags else existing_tags
        else:
            combined_tags = new_tags + taxonomie if taxonomie and new_tags else new_tags

        # Create the new content with updated tags
        new_content = (
            f"---\ntitle: {file_path.stem}\ntaxonomie: {taxonomie}\ntags:\n" +
            '\n'.join([f"- {tag}" for tag in combined_tags]) +
            "\n"
        )

        if difficulty:
            new_content += "difficulty: " + ''.join([f"{level}" for level in difficulty]) + "\n"

        new_content += "---" + content.split('---', 2)[-1]

        # Create the destination directory if it doesn't exist
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the new content to the destination file
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

    generate_report()


def check_test_cases(test_dir):
    for file_path in Path(test_dir).rglob('*.md'):
        if Verbose: print(f"Testing file: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract existing tags and taxonomie
        taxonomie = extract_values(content, 'taxonomie')
        tags, errors = generate_tags(taxonomie, file_path)

        if errors:
            if(ERROR_MISSING_TAXCO in errors): 
                Failed_test_files.append(create_test_file_result(file_path, taxonomie, tags, errors))
            elif any("Taxonomie use where it is not need" in error for error in errors):
                Failed_test_files.append(create_test_file_result(file_path, taxonomie, tags, errors))
            else: 
                Failed_test_files.append(create_test_file_result(file_path, taxonomie, tags, errors))
            if Verbose: print(f"Failed to parse file: {file_path}")
        else:
            Successful_test_files.append(create_test_file_result(file_path, taxonomie, tags, errors))
    return validate_test();    

def validate_test():
    Expected_successful_test_files = [{'file': '7. Dezelfde taxonomie code 2 keer', 'taxonomie': 'rv-8.1.interviewen-met-stakeholder.OI<br>rv-8.1.interviewen-met-stakeholder.OI', 'tags': 'HBO-i/niveau-1<br>Requirementsanalyseproces<br>Verzamelen requirements<br>interviewen-met-stakeholder', 'errors': 'N/A'}, 
                                      {'file': '1. Succesvolle taxonomie codes', 'taxonomie': 'rv-8.1.interviewen-met-stakeholder.OI<br>rv-8.2.interviewen-met-stakeholder.OI<br>rv-8.3.interviewen-met-stakeholder.OI<br>ra-9.2.toestandsdiagrammen.OI', 'tags': 'HBO-i/niveau-1<br>HBO-i/niveau-2<br>HBO-i/niveau-3<br>Requirementsanalyseproces<br>Verzamelen requirements<br>interviewen-met-stakeholder<br>Analyseren requirements<br>toestandsdiagrammen', 'errors': 'N/A'}]
    Expected_failed_test_files = [{'file': '3. Taxonomie code die niet moet bestaan ( combo die een 🏳️ toont)', 'taxonomie': 'ib-21.1.object-oriëntatie-applicatielagen.OI', 'tags': 'HBO-i/niveau-1<br>Implementatieproces<br>Beredeneren bouwkeuzes<br>object-oriëntatie-applicatielagen', 'errors': 'Taxonomie used where it is not needed: ib-21.1.object-oriëntatie-applicatielagen.OI'}, 
                                  {'file': '9. 0 als niveau meegeven', 'taxonomie': 'rv-8.0.interviewen-met-stakeholder.OI', 'tags': 'N/A', 'errors': 'Invalid taxonomie: rv-8.0.interviewen-met-stakeholder.OI'}, 
                                  {'file': '12. Spaties in de taxonomie code', 'taxonomie': 'rv-8.1.interviewen met stakeholder.OI', 'tags': 'N/A', 'errors': 'Invalid taxonomie: rv-8.1.interviewen met stakeholder.OI'}, 
                                  {'file': '4. Mismatch met tc-1 en tc-3', 'taxonomie': 'ra-9.1.interviewen-met-stakeholder.OI', 'tags': 'N/A', 'errors': 'Taxonomie not found in dataset: ra-9.1.interviewen-met-stakeholder.OI'}, 
                                  {'file': '11. 0 als tc-1 meegeven', 'taxonomie': 'rv-0.1.inteviewen-met-stakeholder.OI', 'tags': 'N/A', 'errors': 'Taxonomie not found in dataset: rv-0.1.inteviewen-met-stakeholder.OI'}, 
                                  {'file': '2. Taxonomie code op niveau 4', 'taxonomie': 'rv-8.1.interviewen-met-stakeholder.OI<br>rv-8.2.interviewen-met-stakeholder.OI<br>rv-8.3.interviewen-met-stakeholder.OI<br>rv-8.4.interviewen-met-stakeholder.OI', 'tags': 'HBO-i/niveau-1<br>HBO-i/niveau-2<br>HBO-i/niveau-3<br>Requirementsanalyseproces<br>Verzamelen requirements<br>interviewen-met-stakeholder', 'errors': 'Invalid taxonomie: rv-8.4.interviewen-met-stakeholder.OI'}, 
                                  {'file': '8. Negatieve getallen in tc-2', 'taxonomie': 'rv-8.-1.interviewen-met-stakeholder.OI', 'tags': 'N/A', 'errors': 'Invalid taxonomie: rv-8.-1.interviewen-met-stakeholder.OI'}, 
                                  {'file': '6. Niet bestaande tc-3 (onderwerp)', 'taxonomie': 'rv-8.1.niet-bestaand-onderwerp.OI', 'tags': 'N/A', 'errors': 'Taxonomie not found in dataset: rv-8.1.niet-bestaand-onderwerp.OI'}, 
                                  {'file': '5. Niet bestaande tc-1 (processtap)', 'taxonomie': 'rv-9.1.interviewen-met-stakeholder.OI', 'tags': 'N/A', 'errors': 'Taxonomie not found in dataset: rv-9.1.interviewen-met-stakeholder.OI'}, 
                                  {'file': '10. Negatieve getallen in tc-1', 'taxonomie': 'rv--8.1.interviewen-met-stakeholder.OI', 'tags': 'N/A', 'errors': 'Invalid taxonomie: rv--8.1.interviewen-met-stakeholder.OI'}]
    return check_files_set_equal(Successful_test_files, Expected_successful_test_files) and check_files_set_equal(Failed_test_files, Expected_failed_test_files)

def check_files_set_equal(unsorted_list, expected_unsorted):
    sorted_1 = sorted([json.dumps(d, sort_keys=True) for d in unsorted_list])
    sorted_2 = sorted([json.dumps(d, sort_keys=True) for d in expected_unsorted])
    return sorted_1 == sorted_2


"""
Main entry point of the script.
"""
def main():
    global Verbose
    global Testing

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Update markdown files with taxonomie tags and generate reports.")
    parser.add_argument("--src", required=True, help="Source directory containing markdown files.")
    parser.add_argument("--dest", required=True, help="Destination directory to save updated markdown files and reports.")
    parser.add_argument("--dataset", required=True, help="Path to the dataset file (XLSX file).")
    parser.add_argument("--verbose", action="store_true", help="Print verbose output.")
    parser.add_argument("--testing", action="store_true", help="Determines if it should only check testcases")
    parser.add_argument("--testdir", required=False, help="The directory where the tests are located")

    args = parser.parse_args()
    src_dir = Path(args.src).resolve()
    dest_dir = Path(args.dest).resolve()
    Verbose = args.verbose
    Testing = args.testing
    test_dir = Path(args.testdir).resolve()
    

    # Fill the reports with the dataset information
    parse_dataset_file(args.dataset)

    populate_rapport1()
    populate_rapport2()

    if Testing :
        if check_test_cases(test_dir): sys.exit(0) # 0 means it was successful and pipeline will succeed
        else: sys.exit(1)  # 1 means it was unsuccessful and pipeline will fail
    else :
        # Delete everything in the destination folder
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir)
            os.mkdir(dest_dir)

        # Copy the folder content/sources to the destination directory
        shutil.copytree(src_dir / "sources", dest_dir / "sources")

        # Parse the markdown files in the source directory
        parse_markdown_files(src_dir, dest_dir)

if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")
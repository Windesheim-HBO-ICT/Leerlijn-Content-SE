# Imports
import re
from pathlib import Path
import shutil
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#variables
from config import failedFiles

# Functions
from files.images import fillFailedImages
from report.generateTaxcoReport import generateTaxcoReport
from report.generateContentReport import generateContentReport
from files.parse import parseMarkdownFiles, parseDatasetFile
from tests.evaluate import evaluate_tests
from report.populate import populateReport1, populateReport2

def validate_test_report(expected, actual):

    expected_test_report_path =  Path(__file__).resolve().parents[1] / expected
    actual_test_report_path = Path(__file__).resolve().parents[1] / actual
    with open(expected_test_report_path, 'r') as f1, open(actual_test_report_path, 'r') as f2:
        expected_test_report_content = f1.read()
        actual_test_report_content = f2.read()

    if expected_test_report_content == actual_test_report_content:
        return True
    else:
        return False
    
def validate_draft():
    expectedAmountOfDraftFiles = len(failedFiles)
    actualAmountOfDraftFiles = 0
    for file in failedFiles:
        fullPath = "./.github/script/tests/test_cases_build/" + file['path']
        try:
            with open(fullPath, 'r', encoding='utf-8') as file:
                for line in file:
                    if line.strip().startswith('draft:'):
                        draft_value = line.strip().split(':', 1)[1].strip().lower()
                        if draft_value == 'true':
                            actualAmountOfDraftFiles += 1
        except FileNotFoundError:
            print(f"Error: The file at '{fullPath}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
    return expectedAmountOfDraftFiles == actualAmountOfDraftFiles

"""
Runs the tests for the pipeline
"""
def test():
    global SRC_DIR, DEST_DIR, REPORT_PATH, DATASET

    SRC_DIR = Path(__file__).resolve().parents[0] / 'test_cases'
    DEST_DIR = Path(__file__).resolve().parents[0] / 'test_cases_build'
    DATASET = Path(__file__).resolve().parents[2] / 'datasets/test_dataset.xlsx'
    REPORT_PATH = "./.github/script/report/actual_test_report.md"
    TAXCO_REPORT_PATH = "./.github/script/tests/reports/actual_taxco_test_report.md"
    CONTENT_REPORT_PATH = "./.github/script/tests/reports/actual_content_test_report.md"

    if not os.path.exists(DATASET):
        print(f"Dataset file {DATASET} not found.")
        exit(404) 

    if not os.path.exists(SRC_DIR):
        print(f"Source directory {SRC_DIR} not found.")
        exit(404)
    

    if os.path.exists(DEST_DIR):
        shutil.rmtree(DEST_DIR)
        os.mkdir(DEST_DIR)

    parseDatasetFile(DATASET)
    populateReport1()
    populateReport2()

    parseMarkdownFiles(SRC_DIR, DEST_DIR, False) 
    
    fillFailedImages(SRC_DIR, DEST_DIR) 

    generateTaxcoReport(TAXCO_REPORT_PATH)
    generateContentReport(CONTENT_REPORT_PATH) 

    if validate_test_report('tests/reports/expected_taxco_test_report.md', 'tests/reports/actual_taxco_test_report.md'): 
        print("Taxco test report validation successful")
        if validate_test_report('tests/reports/expected_content_test_report.md', 'tests/reports/actual_content_test_report.md'):
            print("Content Test report validation successful")
            if evaluate_tests():
                print("Test evaluation successful")
                if(validate_draft()):
                    print("Draft test successful")
                    sys.exit(0)
                else:
                    print("Draft test failed")
                    sys.exit(14)
            else : 
                print("Test evaluation failed")
                sys.exit(13)  
        else:
            print("Content Test report validation failed")
            sys.exit(12)
    else : 
        print("Taxco Test report validation failed")
        sys.exit(11)

if __name__ == "__main__":
    test()
    

#Global variables
dataset = list()  # Dataset list 
parsedFiles = [] # Track the status of each parsed file
failedFiles = [] # Track the status of each failed file
failedImages = [] # Track which images don't start with a 4C/ID component
WIPFiles = [] # Track the files that contain Work-in-progress items
Report_1 = {} # Report 1 data
Report_2 = {} # Report 2 data

# Constants
SRC_DIR = "./content" # Source directory where the markdown files are located
DEST_DIR = "./build" # Destination directory where the updated markdown files will be saved
TAXCO_REPORT_PATH = "./taxco_report.md" # Taxco report path where the taxco report will be saved
CONTENT_REPORT_PATH = "./content_report.md" # Content report path where the content report will be saved
DATASET = "./.github/datasets/dataset.xlsx" # Dataset containing the taxonomie information
TODO_PATTERN = r'-=[A-Z]+=-' # To-Do pattern
TAXONOMIE_PATTERN = r'^[a-z]{2}-\d{1,3}\.[123]\.[^\s\.]+(-[^\s\.]+)*\.(?:OI|DT|PI|LT)$' # Taxonomie pattern
VALID_DYNAMIC_LINK_PREFIXES = ['https://', 'http://', 'tags/'] # List of valid dynamic links
IGNORE_FOLDERS = ["schrijfwijze"] # Folders to ignore
FOLDERS_FOR_4CID = { # List of 4C/ID components
    "LT": "1. Leertaken",
    "OI": "2. Ondersteunende-informatie",
    "PI": "3. Procedurele-informatie",
    "DT": "4. Deeltaken",
}

VERBOSE = False # VERBOSE output flag

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

# Error message for not including any taxonomy code
ERROR_INVALID_TAXCO = "Ongeldige taxonomiecode: "
ERROR_MISSING_TAXCO = "Geen taxonomiecode gevonden."
ERROR_TAXCO_NOT_NEEDED = "Taxonomiecode gebruikt wanneer niet nodig: "
ERROR_TAXCO_NOT_FOUND = "Taxonomie niet gevonden in dataset: "
ERROR_TAXCO_IN_WRONG_4CID_COMPONENT = "4C/ID-component van taxonomie komt niet overeen met 4C/ID-map: "

# Error message for images
ERROR_IMAGE_NOT_FOUND = "Afbeelding niet gevonden: "
ERROR_IMAGE_NOT_USED = "Afbeelding wordt in geen enkel bestand gebruikt"
ERROR_NO_4CID_COMPONENT = "Afbeelding bevat geen 4C/ID-component."

# Error message for dynamic links
ERROR_INVALID_DYNAMIC_LINK = "Ongeldige dynamische link: "

# WIP errors
ERROR_WIP_FOUND = "Work-in-progress items gevonden: "

# Icons
SUCCESS = "✅"
FAIL_CIRCLE = "⛔️"
FAIL_CROSS = "❌"
NOT_NECESSARY = "🏳️"
WARNING = "⚠️"
NOT_NEEDED = "🟠"
TODO_ITEMS = "🔨"

# Variables
from config import VERBOSE, WIPFiles, failedFiles, failedImages, parsedFiles

# Functions
from files.markdown_utils import formatFileReportTable
from files.images import formatImageReportTable
from report.table import generateMarkdownTable

"""
Generate the report based on the taxonomie report, success, and failed reports.
"""
def generateContentReport(REPORT_PATH):
    if VERBOSE: print("Generating report...")
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write('---\ndraft: true\n---\n')
        
        f.write("## Work-in-progress bestanden\n")
        f.write('Doel: De onderstaande bestanden hebben nog todo items in de markdown staan.\n')
        f.write('Deze todo items moeten nog worden afgehandeld.\n')
        f.write('\n')
        f.write(formatFileReportTable(sorted(WIPFiles, key=lambda x: x['file'])))

        f.write('\n\n')

        f.write("## Gefaalde bestanden\n")
        f.write("*Doel: De onderstaande bestanden zijn niet succesvol verwerkt.*\n\n")
        f.write('❌ Dit bestand bevat nog geen taxonomie code\n')
        f.write('⚠️ Dit bestand bevat fouten. Zie de *Errors* kolom om te weten wat er mis is\n')
        f.write('🟠 Dit bestand bevat een taxonomie code die niet toegevoegd hoeft te zijn\n')
        f.write('\n')
        f.write(formatFileReportTable(sorted(failedFiles, key=lambda x: x['file'])))

        f.write('\n\n')

        f.write("## Gefaalde images\n")
        f.write("*Doel: De onderstaande images missen een 4C/ID component.*\n\n")
        f.write('Als een image de error heeft over het niet gebruikt worden, betekent dit dat de image niet in build staat, maar nog wel in content.\n\n')
        f.write(formatImageReportTable(sorted(failedImages, key=lambda x: x['image'])))

        f.write('\n\n')

        f.write("## Geslaagde bestanden\n")
        f.write("De onderstaande bestanden zijn succesvol verwerkt.\n")
        f.write('\n')
        f.write(formatFileReportTable(sorted(parsedFiles, key=lambda x: x['file'])))

    if VERBOSE:
        print("Geslaagde bestanden:")
        print(formatFileReportTable(sorted(parsedFiles, key=lambda x: x['file'])))
        print("Gefaalde bestanden:")
        print(formatFileReportTable(sorted(failedFiles, key=lambda x: x['file'])))
        print("Gefaalde images:")
        print(formatImageReportTable(sorted(failedImages, key=lambda x: x['image'])))
        print("Report generated.")

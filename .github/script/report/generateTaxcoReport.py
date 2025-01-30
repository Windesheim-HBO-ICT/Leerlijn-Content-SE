# Variables
from config import VERBOSE, Report_1, Report_2

# Constants
from config import LT, DT, OI, PI, FAIL_CIRCLE, SUCCESS, NOT_NECESSARY

# Functions
from files.images import formatImageReportTable
from report.table import generateMarkdownTable

"""
Generate the report based on the taxonomie report, success, and failed reports.
"""
def generateTaxcoReport(REPORT_PATH):
    if VERBOSE: print("Generating report...")
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write('---\ndraft: true\n---\n')
        
        f.write('## Rapport 1 - Processtappen\n')
        f.write('*Doel: achterhalen welke processtappen nog helemaal niet zijn geïmplementeerd*\n\n')
        f.write('- ✅ Er bestaat een bestand met deze taxonomiecode op dit niveau \n')
        f.write('- ⛔️ Er is geen enkel bestand met deze taxonomiecode op dit niveau \n')
        f.write('- 🏳️ De taxonomiecode wordt niet aangeboden op dit niveau (X in de Dataset) \n')
        f.write('\n')
        f.write(generateProcess())

        f.write('\n\n')

        f.write('## Rapport 2 - Onderwerpen Catalogus\n')
        f.write('*Doel: Lijst met onderwerpen + gekoppelde taxonomie code voor inzicht in aangeboden onderwerpen.*\n')
        f.write('Bij kolom *TC2*, *Leertaken*, *Ondersteunende informatie*, *Procedurele informatie* en *Deeltaken* zijn drie tekens aanwezig om de drie HBO-i niveaus weer te geven\n\n')
        f.write('- ✅ Het onderwerp met taxonomie code wordt aangeboden op het aangegeven niveau \n')
        f.write('- ⛔️ Het onderwerp met taxonomie code wordt **niet** aangeboden op het aangegeven niveau \n')
        f.write('- 🏳️ Het onderwerp hoeft met deze taxonomie code niet aangeboden te worden op het aangegeven niveau \n')
        f.write('\n')
        f.write(generateSubject())

    if VERBOSE:
        print("Rapport 1:")
        print(generateProcess())
        print("Rapport 2:")
        print(generateSubject())
        print("Report generated.")


"""
Format the report table for table 1
Returns:
    table (str): Markdown table string.
"""
def generateProcess():
    if VERBOSE: print("Generating Report 1 table...")

    headers = ["TC1", "Proces", "Processtap", "Niveau 1", "Niveau 2", "Niveau 3"]
    rows = []
    for tc, details in Report_1.items():
        proces = details.get('Proces', '')
        processtap = details.get('Processtap', '')
        tc2_levels = details.get('TC2', {})
        niveau_1 = FAIL_CIRCLE if tc2_levels[0] == 'x' else SUCCESS if tc2_levels[0] == 'v' or tc2_levels[0] == 'g' else NOT_NECESSARY
        niveau_2 = FAIL_CIRCLE if tc2_levels[1] == 'x' else SUCCESS if tc2_levels[1] == 'v' or tc2_levels[1] == 'g' else NOT_NECESSARY        
        niveau_3 = FAIL_CIRCLE if tc2_levels[2] == 'x' else SUCCESS if tc2_levels[2] == 'v' or tc2_levels[2] == 'g' else NOT_NECESSARY
        rows.append([tc, proces, processtap, niveau_1, niveau_2, niveau_3])

    table = generateMarkdownTable(headers, rows)
    if VERBOSE: print("Report 1 table generated.")
    return table

"""
Format the report for table 2
Returns:
    table (str): Markdown table string.
"""
def generateSubject():
    if VERBOSE: print("Generating Report 2 table...")

    headers = ["TC3", "TC1", "TC2", LT, OI, PI, DT]
    rows = []

    def getStatus(value):
        if value == 'v' or value == 'g':
            return SUCCESS
        elif value != NOT_NECESSARY:
            return FAIL_CIRCLE
        else:
            return NOT_NECESSARY

    for tc3, details in Report_2.items():
        for tc1, other in details.items():
            tc2_levels = other.get('TC2', [''] * 3)
            tc2 = ' '.join([getStatus(level) for level in tc2_levels])

            leertaak_levels = other.get(LT, [''] * 3)
            leertaak = ' '.join([getStatus(level) for level in leertaak_levels])

            ondersteunende_informatie_levels = other.get(OI, [''] * 3)
            ondersteunende_informatie = ' '.join([getStatus(level) for level in ondersteunende_informatie_levels])
            
            procedurele_informatie_levels = other.get(PI, [''] * 3)
            procedurele_informatie = ' '.join([getStatus(level) for level in procedurele_informatie_levels])
            
            deeltaak_levels = other.get(DT, [''] * 3)
            deeltaak = ' '.join([getStatus(level) for level in deeltaak_levels])

            rows.append([tc3, tc1, tc2, leertaak, ondersteunende_informatie, procedurele_informatie, deeltaak])

    table = generateMarkdownTable(headers, rows)
    if VERBOSE: print("Report 2 table generated.")
    return table
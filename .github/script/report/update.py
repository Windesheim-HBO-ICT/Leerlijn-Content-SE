# Variables
from config import Report_1, Report_2

# Constants
from config import NOT_NECESSARY, LT, DT, OI, PI

"""
Update the Report 1 data with the new values.
Args:
    tc_1 (str): TC1 code.
    tc_2 (str): TC2 code.
"""
def updateProcessReportData(tc_1, tc_2):
    Report_1[tc_1]['TC2'] = ['v' if tc_2 == '1' and Report_1[tc_1]['TC2'][0] != NOT_NECESSARY else Report_1[tc_1]['TC2'][0], 'v' if tc_2 == '2' and Report_1[tc_1]['TC2'][1] != NOT_NECESSARY else Report_1[tc_1]['TC2'][1], 'v' if tc_2 == '3' and Report_1[tc_1]['TC2'][2] != NOT_NECESSARY else Report_1[tc_1]['TC2'][2]]

"""
Update the Report 2 data with the new values.
Args:
    file_type (str): File type.
    tc_1 (str): TC1 code.
    tc_2 (str): TC2 code.
    tc_3 (str): TC3 code.
"""
def updateSubjectReportData(file_type, tc_1, tc_2, tc_3):
    # Update the record with the new values
    def updateReport2Row(tc_3, tc_1, tc_2, file_type, searchType):
        Report_2[tc_3][tc_1][searchType] = [
            'v' if file_type == searchType and tc_2 == '1' and Report_2[tc_3][tc_1][searchType][0] != NOT_NECESSARY else Report_2[tc_3][tc_1][searchType][0], 
            'v' if file_type == searchType and tc_2 == '2' and Report_2[tc_3][tc_1][searchType][1] != NOT_NECESSARY else Report_2[tc_3][tc_1][searchType][1], 
            'v' if file_type == searchType and tc_2 == '3' and Report_2[tc_3][tc_1][searchType][2] != NOT_NECESSARY else Report_2[tc_3][tc_1][searchType][2]
        ]

    Report_2[tc_3][tc_1]['TC2'] = ['v' if tc_2 == '1' and Report_2[tc_3][tc_1]['TC2'][0] != NOT_NECESSARY else Report_2[tc_3][tc_1]['TC2'][0], 'v' if tc_2 == '2' and Report_2[tc_3][tc_1]['TC2'][1] != NOT_NECESSARY else Report_2[tc_3][tc_1]['TC2'][1], 'v' if tc_2 == '3' and Report_2[tc_3][tc_1]['TC2'][2] != NOT_NECESSARY else Report_2[tc_3][tc_1]['TC2'][2]]
    updateReport2Row(tc_3, tc_1, tc_2, file_type, LT)
    updateReport2Row(tc_3, tc_1, tc_2, file_type, OI)
    updateReport2Row(tc_3, tc_1, tc_2, file_type, PI)
    updateReport2Row(tc_3, tc_1, tc_2, file_type, DT)


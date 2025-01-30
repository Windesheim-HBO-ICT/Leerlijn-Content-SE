# Imports
from pathlib import Path

# Variables
from config import dataset, Report_1, Report_2

# Constants
from config import TC1_COL, TC2_COL, TC3_COL, PROCES_COL, PROCESSTAP_COL, NOT_NECESSARY, LT_COL, DT_COL, OI_COL, PI_COL, LT, DT, OI, PI


## Structure of Report_1
#
# Report_1 = {
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

## Structure of Report_2
#
# Report_2 = {
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
Fills the report 1 data with the data from the dataset
Every TC1 code is the unique identifier
"""
def populateReport1():
    global Report_1

    for row in dataset[1:]:
        tc_1 = row[TC1_COL]
        tc_2 = row[TC2_COL]
        proces = row[PROCES_COL]
        processtap = row[PROCESSTAP_COL]

        if tc_1 in Report_1:
            if Report_1[tc_1]['TC2'][1] == '🏳️' or Report_1[tc_1]['TC2'][2] == '🏳️':
                splitted_tc2 = tc_2.split(',')
                for index in range(1, 3):
                    if Report_1[tc_1]['TC2'][index] == '🏳️' and splitted_tc2[index] != '🏳️':
                        Report_1[tc_1]['TC2'][index] = splitted_tc2[index]

        if tc_1 not in Report_1: 
            splitted_tc2 = tc_2.split(',')

            Report_1[tc_1] = {
                "Proces" : proces,
                "Processtap" : processtap,
                'TC2': [NOT_NECESSARY if splitted_tc2[0] == 'X' else 'x', NOT_NECESSARY if splitted_tc2[1] == 'X' else 'x', NOT_NECESSARY if splitted_tc2[2] == 'X' else 'x']        
            }

"""
Fills the Report 2 data with the data from the dataset.
Every unique TC3 and TC1 combination will be added to the Report 2 data.
"""
def populateReport2():
    global Report_2

    for row in dataset[1:]:
        tc_1 = row[TC1_COL]
        tc_2 = row[TC2_COL]
        tc_3 = row[TC3_COL]
        lt = row[LT_COL]
        oi = row[OI_COL]
        pi = row[PI_COL]
        dt = row[DT_COL]

        if tc_3 not in Report_2:
            Report_2[tc_3] = {}

        if tc_1 not in Report_2[tc_3]:
            splitted_tc2 = tc_2.split(',')
            splitted_lt = lt.split(',')
            splitted_oi = oi.split(',')
            splitted_pi = pi.split(',')
            splitted_dt = dt.split(',')
            
            Report_2[tc_3][tc_1] = {
                'TC2': [NOT_NECESSARY if splitted_tc2[0] == 'X' else 'x', NOT_NECESSARY if splitted_tc2[1] == 'X' else 'x', NOT_NECESSARY if splitted_tc2[2] == 'X' else 'x'],
                LT: [NOT_NECESSARY if splitted_lt[0] == 'X' else 'x', NOT_NECESSARY if splitted_lt[1] == 'X' else 'x', NOT_NECESSARY if splitted_lt[2] == 'X' else 'x'],
                OI: [NOT_NECESSARY if splitted_oi[0] == 'X' else 'x', NOT_NECESSARY if splitted_oi[1] == 'X' else 'x', NOT_NECESSARY if splitted_oi[2] == 'X' else 'x'],
                PI: [NOT_NECESSARY if splitted_pi[0] == 'X' else 'x', NOT_NECESSARY if splitted_pi[1] == 'X' else 'x', NOT_NECESSARY if splitted_pi[2] == 'X' else 'x'],
                DT: [NOT_NECESSARY if splitted_dt[0] == 'X' else 'x', NOT_NECESSARY if splitted_dt[1] == 'X' else 'x', NOT_NECESSARY if splitted_dt[2] == 'X' else 'x'],
            }  
 
"""
Generate a markdown table string from a list of rows and headers.
Args:
    headers (list): List of header values.
    rows (list): List of lists containing row values.
Returns:
    table (str): Markdown table string.
"""
def generateMarkdownTable(headers, rows):
    table = "| " + " | ".join(headers) + " |\n"
    table += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    for row in rows:
        table += "| " + " | ".join(row) + " |\n"
    return table


# python3 -m pip install pycurl 
# python3 -m pip install bs4 

import pycurl
from bs4 import BeautifulSoup
from io import BytesIO

# url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

def is_number(string):
    """
    is_number checks if the provided string input is a number

    :param string: string to check if is a number
    :return: true if string is a number and false if it is not
    """ 

    try:
        float(string)
        return True
    except ValueError:
        return False

def fetch_html(url):
    """
    fetch_html scrapes url and returns test result

    :param url: string of url to scrape
    :return: string of scraped text content
    """ 

    # Use cURL to scrape URL content
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    return buffer.getvalue().decode('utf-8')

def scrape_table(html):
    """
    scrape_table extracts a table from provided html

    :param html: html to extract table from
    :return: string of extracted table
    """ 

    # Use BeautifulSoup to extract the table from the HTML string
    html = BeautifulSoup(html, 'html.parser')
    table = html.find("table")

    return table
    
def decode_message(url):
    """
    decode scrapes the provided url and outputs the decoded message

    :param url: url to scrape table data from
    :return: void
    """ 

    # Fetch the URL HTML
    html = fetch_html(url)

    # Extract the table from the HTML
    table = scrape_table(html)

    # Define a list to store message charaters
    data = []

    # Define variables to store the number of rows and columns the message will require
    rows = 0
    cols = 0

    # Loop through hHTML table and extract data into the data list
    for row in table.find_all('tr'):
        row_data = []
        for cell in row.find_all('td'):
            value = cell.text.strip()

            if is_number(value):
                value = int(value)

            row_data.append(value)

        data.append(row_data)

        if is_number(row_data[0]):
            if row_data[0] > cols:
                cols = row_data[0]
            if row_data[2] > rows:
                rows = row_data[2]

    # Remove the headers from the list
    del data[0]

    # Define an empty grid using the rows and cols variable
    grid = [[" " for x in range(0, cols + 1, 1)] for y in range(0, rows + 1, 1)]

    # Place extracted data into the grid
    for row in data:
        grid[row[2]][row[0]] = row[1]

    # Output the message using the grid data
    for i in range(rows, -1, -1):
        output = ""
        for j in range(cols + 1):
            output = output + grid[i][j]
        print(output)

decode_message(url)

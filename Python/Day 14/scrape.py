import os
import sys
import datetime
import requests
import pandas as pd  # conevrt dict to data
from requests_html import HTML

BASE_DIR = os.path.dirname(__file__)
# scrapes and stores data
# def url_to_file(url, filename="world.html"):


# 1> save data...and pass it later
def url_to_txt(url, filename="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:    #open(f"..)
            with open("world-{year}.html", 'w') as f:
                f.write(html_text)
        return html_text
    return None


# parse and extract ,,,html and css ... pass coreect tool
def parse_and_extract(url, name='2020'):
    html_text = url_to_txt(url)
    if html_text == None:
        return False
    r_html = HTML(html=html_text)
    table_class = ".imdb-scroll-table"
    # table_class = "#table"
    r_table = r_html.find(table_class)

    # print(r_table)
    table_data = []
    # table_data_dicts = []
    header_names = []
    if len(r_table) == 0:
        return False
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_row = rows[0]
    header_cols = header_row.find('th')
    header_names = [x.text for x in header_cols]
    for row in rows[1:]:
        # print(row.text)
        cols = row.find("td")
        row_data = []
        row_dict_data = {}
        for i, col in enumerate(cols):
            # print(i, col.text, '\n\n')
            header_name = header_names[i]
            # row_dict_data[header_name] = col.text
            row_data.append(col.text)
        #table_data_dicts.append(row_dict_data)  this was there original
        table_data.append(row_data)
    df = pd.DataFrame(table_data, columns=header_names)
    # df = pd.DataFrame(table_data_dicts)
    path = os.path.join(BASE_DIR, 'data')
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join('data', f'{name}.csv')
    df.to_csv(filepath, index=False)
    return True

# scrape multple things not just once


def run(start_year=None, years_ago=0):  # take years ago...change to one
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year
    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(f"{start_year}") == 4  # 4 digits year
    for i in range(0, years_ago+1):  # with this loop
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        finished = parse_and_extract(url, name=start_year)
        if finished:
            print(f"Finished {start_year}")  # turn it into string
        else:
            print(f"{start_year} not finished")
        start_year -= 1  # starts with initial start year n substracts one




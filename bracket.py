import pandas
import requests

urls = {}
imgs = {}

def create_url_brackets():
    df = pandas.read_csv("stats.csv")
    for index, row in df.iterrows():
        player = row['Player'].split('\\')
        urls[player[0]] = player[1]

create_url_brackets()

for key, value in urls.items():
    search_url = "http://www.basketball-reference.com/players/" + value[0] + "/" + value

import pandas
from bokeh.charts import Scatter, output_file, show
from bokeh.models import HoverTool

urls = {}

def create_chart(df, attr1, attr2):
    values = {'PTS': 15, 'TRB': 10, 'AST': 7, 'BLK': 1, 'STL': 1}
    full_names = {'PTS': 'Points', 'TRB': 'Rebounds', 'AST': 'Assists', 'BLK': 'Blocks', 'STL': 'Steals'}
    query_string1 = attr1 + " > " + str(values[attr1])
    query_string2 = attr2 + " > " + str(values[attr2])
    df = df.query(query_string1)
    df = df.query(query_string2)
    label1 = full_names[attr1] + ' PER 36'
    label2 = full_names[attr2] + ' PER 36'
    tooltips = [('Player', '@Player'), (attr1, '@' + attr1), (attr2, '@' + attr2), ('Team', '@Tm')]
    p = Scatter(df, x=attr1, y=attr2, xlabel=label1, ylabel=label2, tooltips=tooltips)
    output_file('stats.html')
    show(p)

def create_url_brackets():
    df = pandas.read_csv("stats.csv")
    for index, row in df.iterrows():
        player = row['Player'].split('\\')
        urls[player[0]] = player[1]

df = pandas.read_csv("stats.csv")

fuckin_backslash = '\\'

for index, row in df.iterrows():
    row['Player'] = row['Player'].split(fuckin_backslash)[0]
    df.loc[index, 'Player'] = row['Player']

tot = df.query("Tm == 'TOT'")
tot_list = tot['Player'].tolist()

df = df[~df['Player'].isin(tot_list)]
df = df.append(tot)

df = df.query("MP > 500")

category1 = input("Category 1: ")
category2 = input("Category 2: ")
create_url_brackets()
create_chart(df, category1, category2)

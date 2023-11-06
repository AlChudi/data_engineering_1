import json
from bs4 import BeautifulSoup

str_json = ''
with open('text_6_var_32', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        str_json += line

data = json.loads(str_json)
data = data['cases_time_series']

soup = BeautifulSoup("""<table>
            <tr>
                <th>dailyconfirmed</th>
                <th>dailydeceased</th>
                <th>dailyrecovered</th>
                <th>date</th>
                <th>dateymd</th>
                <th>totalconfirmed</th>
                <th>totaldeceased</th>
                <th>totalrecovered</th>
            <tr>
        </table>""", "html.parser")

table = soup.contents[0]

for tick in data:
    tr = soup.new_tag("tr")
    for key, val in tick.items():
        td = soup.new_tag("td")
        td.string = val
        tr.append(td)
    table.append(tr)

#print(soup.prettify())

with open('r_text_6_var_32.html', 'w') as result:
    result.write(soup.prettify())
    result.write("\n")
#https://documenter.getpostman.com/view/10724784/SzYXWz3x
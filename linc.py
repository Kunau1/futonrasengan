import csv
import requests
from bs4 import BeautifulSoup 
import re

url = 'https://www.link.kg/catalog/1/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
box = soup.find_all('tr',class_='r2')
data = []

for x in box:
    td = x.find_all('td')

    if len(td) >= 5:
        title = td[1].text.strip().replace(u'\xa0','')
        price_c = td[2].text.strip().replace(u'\xa0','').strip('*')
        price_d = td[3].text.strip().replace(u'\xa0','').strip('*')

        data.append([title, price_c, price_d])
print(data)
with open('mew.csv','w') as f:
    csv.writer(f).writerows(data)
# for i in pre_title:
#     info = i.text
#     print(info)
# print("Prices in Soms:", prices)
# print("Prices in Dollars:", prices2)

# notebook_elements = soup.find_all('div', class_='product-name')

# notebook_names = [element.text.strip() for element in notebook_elements]

# for name in notebook_names:
#     print(name)




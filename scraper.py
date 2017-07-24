import urllib.request
from bs4 import BeautifulSoup
import datetime as dt
import pandas as pd
from tabulate import tabulate

today = dt.datetime.today().strftime(" %m/%d/%Y")
loopNet = input("URL >> ")
page = urllib.request.urlopen(loopNet)

soup = BeautifulSoup(page, "lxml")

# print(soup.prettify())


date_table = soup.find('table', class_ = 'property-timestamp')
data_table = soup.find('table', class_ = 'property-data')
broker_name = soup.find('div', class_ = 'center-wrap')
#broker_phone = 

check = 1
while check == 1:
	for row in date_table.findAll('td'):
		if today in row:
			print('New or updated property. Collecting relevant information.')
			check = 2
			getData = 1
			break
		else:
			check = 2
			getData = 1

A=[]
B=[]
C=[]
D=[]
# E=[]


if getData == 1:
	for row in data_table.findAll("tr"):
		cells = row.findAll("td")
		A.append(cells[0].find(text=True))
		B.append(cells[1].find(text=True))
		C.append(cells[2].find(text=True))
		D.append(cells[3].find(text=True))




df = pd.DataFrame(A, columns = ['column1'])
df['column2'] = B
df['column3'] = C
df['column4'] = D
# df['column5'] = E
print(tabulate(df))
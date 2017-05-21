import requests
from bs4 import BeautifulSoup
import csv

def table_to_csv():
	html = requests.get('http://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500.html', headers={'User-Agent': 'Mozilla/5.0'})
	#print (html.status_code)
	bsobj = BeautifulSoup(html.content)
	table=bsobj.find("table",{"id":"quotesFuturesProductTable1"})
	

	csvFile = open("sp_h.csv", 'wt')
	writer = csv.writer(csvFile)

	rows = table.findAll("tr")

	for row in rows:
		print(row)
		csvRow = []
		for cell in row.findAll(['td','th']):
			#print (Cell)
			csvRow.append(cell.get_text())
		print(csvRow)

	writer.writerow(csvRow)

table_to_csv()
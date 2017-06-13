"""
Scrapping with Requests + BeautifulSoup4
"""
import requests
import bs4

url = 'http://jadwalsholat.pkpu.or.id/monthly.php?id=308'
r = requests.get(url)

if r.status_code == 200 :
	#print(r.text)
	data = bs4.BeautifulSoup(r.content,'lxml')
	#print(data)
	#find table_highlight class
	row = data.find_all('tr','table_highlight')
	#print(row)
	cols = row[0].find_all('td')
	maghrib  = ''
	for idx, val in enumerate(cols) :
		#print(idx)
		#print(val)
		if(idx == 6) :
			maghrib = val
	print(maghrib.get_text())
else :
	print('Unable to get data from website')

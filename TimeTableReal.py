from bs4 import BeautifulSoup as bs
import urllib2
page = 'Timetable.html'
source = open(page, 'r')
soup = bs(source, 'lxml')

#table = soup.find('table')
table_rows = soup.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    row_m = [x.encode('utf-8') for x in row]
    print row_m

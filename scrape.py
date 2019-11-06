import sys
import requests
import json
from bs4 import BeautifulSoup as bs4

# Future:
# 1. Robust command line options for printing. (format(id's vs links), to std out or to file, help option)
# 2. Option to give list id insread of url
# 3. Other types of list?


def main():
	try:
		link = sys.argv[1]
	except:
		print("Usage: ./scrape.py List_Url")
		return
	try:
		scrape_link(link)
	except NameError:
		print("Url not valid")

def scrape_link(link):
	bs = requests.get(link)
	if (bs.status_code == 404):
		raise NameError("URL not valid")
	bs1 = bs4(bs.content, 'html.parser')
	jsonified = json.loads(bs1.findAll('script')[11].string)
	title_data = jsonified['about']['itemListElement']
	imdb_id_list = [i['url'].split("/")[2] for i in title_data]
	for i in imdb_id_list:
		print(i)
		print('https://www.imdb.com/title/' + i + "/")


if __name__ == '__main__':
	main()

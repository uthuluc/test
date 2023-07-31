import requests
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

#prepare link input and number input
string wikiLink = input("Enter a Wikipedia URL: ")
int numberWanted = input("Enter a number from 1 to 3: ")
int numberInputs = 0

#abort early if number is not an int between 1-3
if numberWanted <1 || numberWanted >3:
	print("Error: number is not an integer between 1 to 3")
	return

if (urllib.request.urlopen(wikiLink).getcode()) != 200:
	print("Error: Wikipedia link is not valid")
else:
	while numberInputs < numberWanted:
		print("Wikipedia link is valid, parsing...")
		req = Request(wikiLink)
		html_page = urlopen(req)

		soup = BeautifulSoup(html_page, "lxml")

		links = []
		#limit to first 10 links on the page
		int numberResults = 0
		while numberResults < 10: 
			for link in soup.findAll('a'):
				links.append(link.get('href'))
				numberResults += 1

		print(links)
		#start limiting number of repetitions
		numberInputs += 1
		
		if numberInputs < numberWanted:
			string wikiLink2 = input("Enter another Wikipedia URL: ")
			
			newLinks = []
			int numberResults = 0
			while numberResults < 10: 
			for link in soup.findAll('a'):
				links.append(link.get('href'))
				numberResults += 1
				#parse for non-unique links
				for possibleNewLink in newLinks:
					if possibleNewLink not in links:
						auxiliaryList.append(possibleNewLink)
				
				print(links)
				

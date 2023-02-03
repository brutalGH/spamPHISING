import requests,json,random,rich,bs4,sys,time,os
from bs4 import BeautifulSoup
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich import print as cetak
from rich.console import Console as sol
x = '\33[m'
h = '\x1b[1;92m'
m = '\x1b[1;91m'

url1 = 'https://codashop-freefire-gratis5048.indox.sbs/id/final.php'
ses = requests.Session()
id = []
tulis = []
jalan = []
def brut(u):
        for e in u :sys.stdout.write(e);sys.stdout.flush();time.sleep(0.02)

def banner():
	brut(f'{x}.....')
	if "linux" in sys.platform.lower():
		try:os.system('clear')
		except:pass
	elif "win" in sys.platform.lower():
	    try:os.system('cls')
	    except:pass
	else:
	    try:os.sytem('clear')
	    except:pass

	wel = '# SPAMMER TOOLS'
	wel2 = mark(wel, style='red')
	sol().print(wel2)
	au="""[white]
╔═╗╔╗╔╦╗╦   ╦╔╦╗
╚═╗╠╩╗║ ║   ║ ║║
╚═╝╚═╝╩ ╩═╝o╩═╩╝
[white][green]\n Copyright 2023 By Brutal.ID[white] """
    
	pengembang1=nel(au,style="cyan")
	cetak(nel(pengembang1, title='v 3.144'))
	if 'menu' in jalan:
		brut(f'{x} ╗\n ╠ [ {h}• {x}] Processing....\n')
	elif 'pilih' in jalan:
		brut(f'{x} ╗\n ╠ [ {h}• {x}] Waitting....\n')
	else:
		brut(f'{x} ╗\n ╠ [ {h}• {x}] Processing....\n')

def check(idf,pw):
	ua = 'Mozilla/5.0 (Linux; Android 9; ASUS_Z01QD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36'
	header = {
		"authority": "codashop-freefire-gratis5048.indox.sbs",
		"sec-ch-ua": 'Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108',
		"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
		"sec-ch-ua-mobile": "?0",
		"content-type": "application/x-www-form-urlencoded",
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"user-agent": ua,
		"sec-ch-ua-platform": "Android",
		"origin": "https://codashop-freefire-gratis5048.indox.sbs",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://codashop-freefire-gratis5048.indox.sbs/id/verification.php",
		"accept-encoding": "gzip, deflate, br"
	    }

	data = {
		'user': idf,
		'pass': pw,
		'login': 'Facebook',
		'nickname': 'tolol',
		'playid': '11111111',
		'level': 'level 200',
		'elitepass': 'gacor',
		'tier': 'epic',
		'phone': '+1234567890'
	}
	
	ok = ses.post(url1,headers=header,data=data)
	if ok.status_code == 200:
		jum = str(len(id))
		if 'tidak' in tulis:
			print(f'\r{x} ╠{x} [ {h}• {x}]{x} Succes Post{h} '+str(len(id))+f'{x} Result',end=" ")
		elif 'ya' in tulis:
			print(f'{x} ╠{x} [ {m}• {x}] Send ke {m} '+jum+f' {h}Succes ')
			print(f'{x} ╠{x} [ {h}• {x}] Email :{h} '+idf)
			print(f'{x} ╠{x} [ {h}• {x}] Pw    :{h} '+pw)
		else:
			print(f'\r{x} ╠{x} [ {h}• {x}]{x} Succes Post{h} '+str(len(id))+f'{x} Result',end=" ")
	else:
		print('	=>> Failed Send email : '+idf+'pw : '+pw)

def mulai():
	jalan.append('menu')
	banner()		
	file = open('data.txt','r').readlines()		
	for i in file:
	    seq = i.strip()
	    id.append(seq)
	    acc = seq.split(':')
	    check(acc[0],acc[1])

def pilih():
	jalan.append('pilih')
	banner()
	print(f'\r{x} ╠{x} [ {h}• {x}] Print Email & Pw Y / T ')
	pil = input(f'\r{x} ╠{x} [ {h}• {x}] Pilih :{h} ')
	if pil in ['Y','y']:
		tulis.append('ya')
	elif pil in ['T','t']:
		tulis.append('tidak')
	else:
		tulis.append('ya')

if __name__=='__main__':
	pilih()
	mulai()
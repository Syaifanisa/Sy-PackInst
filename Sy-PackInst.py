#IMPORT AND COLOR ——

import os
import time
import sys
os.system("clear")
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'    # ^_^ Hi!
C = '\033[96m'
P = '\033[95m'    #Overline for copy -> ‾
r = '\033[0m'

#LIST/VAR ——

packages = ["All Packages","python","nodejs","php","clang","proot-distro","sl","nsnake","nudoku","bastet","burpsuite","nmap","ffmpeg","cava","peaclock","cmatrix","wireshark","pulseaudio","mpv","fastfetch","vim","lolcat","figlet","git","neovim","nano","pip","yarn","make","cmake","gdb","ruby","go","rust","javac","gradle","maven","netcat","tcpdump","whois","dnsutils","hydra","sqlmap","nikto","aircrack-ng","ettercap","openssl","cowsay","fortune","toilet","boxes","bb","oneko","moon-buggy","greed","ninvaders","htop","btop","neofetch","tmux","screen","fish","zsh","unzip","tar","tree","sox","imagemagick","feh","sxiv","yt-dlp","termux-api"]

packman = ["pkg install ", "apt install ", "pacman -S ", "dnf install ", "yum install "]

pmp = ""

ProgrammerPack = ["python", "nodejs", "php", "clang", "git", "neovim" ,"vim", "nano", "pip", "yarn", "make", "cmake", "gdb" "ruby", "go", "rust", "javac", "gradle", "maven"]

MediaPack = ["mpv", "ffmpeg", "pulseaudio", "cava", "peaclock", "sox", "imagemagick", "feh", "sxiv" ,"yt-dlp", "termux-api"]

CyberPack = ["netcat", "burpsuite", "nmap", "wireshark" ,"tcpdump", "whois", "dnsutils", "hydra", "sqlmap", "nikto", "aircrack-ng", "ettercap", "openssl"]
GamePack = ["cowsay", "fortune", "toilet", "boxes" ,"bb", "oneko", "moon-buggy", "greed", "ninvaders"]

SystemUPack = ["htop", "btop", "fastfetch", "neofetch", "tmux", "screen", "fish", "zsh", "unzip", "tar", "tree", "proot-distro"]

packs = [ProgrammerPack,MediaPack,CyberPack,GamePack,SystemUPack]

HoGUI = f"""{G}_____________
|{Y}Sy-PackInst{G}|______________________________________________________
|{Y}     ____              ____            _    ___           _      {G}|
|{Y}    / ___| _   _      |  _ \\ __ _  ___| | _|_ _|_ __  ___| |_    {G}|
|{Y}    \\___ \\| | | |_____| |_) / _` |/ __| |/ /| || '_ \\/ __| __|   {G}|
|{Y}     ___) | |_| |_____|  __/ (_| | (__|   < | || | | \\__ \\ |_    {G}|
|{Y}    |____/ \\__, |     |_|   \\__,_|\\___|_|\\_\\___|_| |_|___/\\__|   {G}|
|{Y}           |___/                                                 {G}|
|____________________________________________________{C}v1.0{G}_________|\n{G}|{Y}[1] Package{G}|{Y}[2] Pkg pack{G}|{Y}[3] More info{G}{Y}|[4] Exit{G}|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾{r}"""

#FUNCTION ——

def HGW():
	for char in HoGUI:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.001)

def tywr(text):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.001)
		

def home():
	#package/pkgpack/moreinfo
	os.system("clear")
	HGW()
	print(f"\n{Y}[?] {G}Where do you wanna go?{r}")
	
def package():
	#home
	pl = 1
	os.system("clear")
	print(HoGUI)
	
	
	for i in packages:
		print(f"{G}[{Y}P{G}] — {pl}.{Y}{i}")
		pl += 1
		time.sleep(0.01)
	print("type /e to exit")
	In4 = input(f"\n{G}[{Y}Pick the package here!{G}]{r} ")
	os.system("clear")
	if "/e" in In4.lower():
		home()
		return
	for i in In4.split():
			try:
				os.system(packman[pmp]+packages[int(i)-1])
			except:
				print(f"{P}[{R}!{P}]Install Failed [{R} Reason: Invalid Input{P}].")
		
	os.system("clear")
	HGW()			
	print(f"\n{Y}[{G}+{Y}] Task Completed{r}")
		
		
def pkgpack():
	#home
	os.system("clear")
	print(HoGUI)
	tywr(f"""{Y}
1.Programmer Pack:
		{G}1.Python | 16.rust
		2.Nodejs | 17.javac
		3.php    | 18.gradle
		4.clang  | 19.maven
		5.git    |
		6.neovim |
		7.vim    |
		8.nano   |
		9.pip    |
		10.yarn  |
		11.make  |
		12.cmake |
		13.gdb   |
		14.ruby  |
		15.go    |
	
{Y}2.Media Pack:
		{G}1.mpv        | 11.termux-api
		2.ffmpeg     |
		3.pulseaudio |
		4.cava       |
		5.peaclock   |
		6.sox        |
		7.imagemagick|
		8.feh        |
		9.sxiv       |
		10.yt-dlp    |
	
{Y}3.CyberSecurity Pack:
		{G}1.netcat    | 11.aircrack-ng
		2.burpsuite | 12.ettercap
		3.nmap      | 13.openssl
		4.wireshark |
		5.tcpdump   |
		6.whois     |
		7.dnsutils  |
		8.hydra     |
		9.sqlmap    |
		10.nikto    |
	
{Y}4.Game Pack:
		{G}1.cowsay     |
		2.fortune    |
		3.toilet     |
		4.boxes      |
		5.bb         |
		6.oneko      |
		7.moon-buggy |
		8.greed      |
		9.ninvaders  |
		
{Y}5.System Utility Pack:
		{G}1.htop     | 11.tree
		2.btop     | 12.proot-distro
		3.fastfetch| 
		4.neofetch |
		5.tmux     |
		6.screen   |
		7.fish     |
		8.zsh      |
		9.unzip    | 
		10.tar     |{r}""")
	print(f"{Y}\ntype /e to exit")
	In2 = input(f"\n{G}[{Y}Pick the pack here!{G}]{r} ")
	os.system("clear")
	if "/e" in In2.lower():
		home()
		return
	for i in In2.split():
			try:
				for e in packs[int(i)-1]:
					os.system(packman[pmp]+e)
			except:
				print(f"{P}[{R}!{P}]Install Failed [{R} Reason: Invalid Input{P}].")
		
	os.system("clear")
	HGW()						
	print(f"\n{Y}[{G}+{Y}] Task Completed{r}")
	
	
def moreinfo():
	#home
	os.system("clear")
	print(HoGUI)
	tywr(f"""
{Y}Why do some packages error during installation?: it's because the package is based on your repository, so that's why :)
—— -
{Y}What is this tool for?: {G}This tool makes installing packages easier and faster with less typing!
—— -
{Y}How to use this tool?: {G}Just go to Package or Pkg Pack and pick the package/pack that you want (make sure to follow the instructions!)
—— -
{Y}What programming language does this tool use?: {G}it's python, so, don't remove the python package in your terminal or this tool won't work :0
—— -
{Y}How did you make that ASCII text?:{G} I use package figlet to make that because i dont know how to make a ascii text :)
—— -
{Y}Who's the developer of this tool?:{G} it's Syaifani S.A, a 13 years old boy from indonesia, he likes potatoes lol

————[!]— -
{Y}Note:{G} This is the first version of this tools, so, there's may still be some bug! ¯\\_(ツ)_/¯
{r}""")

#LOOP/BREAK ——
print("[(1)Pkg|(2)Apt|(3)Pacman|(4)dnf|(5)yum]\nWhat package manager do you use?")
while True:
	In3 = input(">>> ")
	if In3 == "1":
		pmp = 0
		break
	elif In3 == "2":
		pmp = 1
		break
	elif In3 == "3":
		pmp = 2
		break
	elif In3 == "4":
		pmp = 3
		break
	elif In3 == "5":
		pmp = 4
		break
	else:
		print("Invalid Input.")
home()
while True:
	In1 = input(f"\n{G}[{Y}Input Here!{G}]:{r} ")
	if In1 == "1":
		package()
	elif In1 == "2":
		pkgpack()
	elif In1 == "3":
		moreinfo()
	elif In1 == "4":
		os.system("clear")
		print(f"{R}Exit...{r}")
		break

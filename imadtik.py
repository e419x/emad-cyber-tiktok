
import requests,os,pycountry
from datetime import datetime

os.system('clear')

# ================= LOGO =================
title = r"""
███████╗███╗   ███╗ █████╗ ██████╗      ██████╗██╗   ██╗██████╗ ███████╗██████╗
██╔════╝████╗ ████║██╔══██╗██╔══██╗    ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║  ██║    ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║  ██║    ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██████╔╝    ╚██████╗    ██║   ██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝      ╚═════╝    ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

print("\033[1;36m" + title + "\033[0m")
print("\033[1;33m" + " " * 30 + "by @e4_19" + "\033[0m")
print("\033[1;34m" + "═" * 72 + "\033[0m\n")

def get_info(username):
     patre={
    "Host": "www.tiktok.com",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-language": "en-US,en;q=0.9",}

     patrek=requests.get(f'https://www.tiktok.com/@{username}',headers=patre).text

     try:
        getting = str(patrek.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]

        try:id = str(getting.split('id":"')[1]).split('",')[0]
        except:id=""
        try:name = str(getting.split('nickname":"')[1]).split('",')[0]
        except:name=""
        try:bio = str(getting.split('signature":"')[1]).split('",')[0]
        except:bio=""
        try:country = str(getting.split('region":"')[1]).split('",')[0]
        except:country=""
        try:private = str(getting.split('privateAccount":')[1]).split(',"')[0]
        except:private=""
        try:followers = str(getting.split('followerCount":')[1]).split(',"')[0]
        except:followers=""
        try:following = str(getting.split('followingCount":')[1]).split(',"')[0]
        except:following=""
        try:like = str(getting.split('heart":')[1]).split(',"')[0]
        except:like=""
        try:video = str(getting.split('videoCount":')[1]).split(',"')[0]
        except:video=""
        try:secid = str(getting.split('secUid":"')[1]).split('"')[0]
        except:secid=""

        countryn=str(pycountry.countries.get(alpha_2=country)).split("name='")[1].split("'")[0]
        countryf=str(pycountry.countries.get(alpha_2=country)).split("flag='")[1].split("'")[0]

        binary = "{0:b}".format(int(id))
        bits = binary[:31]
        timestamp = int(bits, 2)
        cdt = datetime.fromtimestamp(timestamp)

        print("\033[1;32m[+] ACCOUNT INFORMATION\033[0m")
        print("─" * 55)
        print(f"\033[1;37mUsername     :\033[0m {username}")
        print(f"\033[1;37mSecUID       :\033[0m {secid}")
        print(f"\033[1;37mName         :\033[0m {name}")
        print(f"\033[1;37mFollowers    :\033[0m {followers}")
        print(f"\033[1;37mFollowing    :\033[0m {following}")
        print(f"\033[1;37mLikes        :\033[0m {like}")
        print(f"\033[1;37mVideos       :\033[0m {video}")
        print(f"\033[1;37mPrivate      :\033[0m {private}")
        print(f"\033[1;37mCountry      :\033[0m {countryn} {countryf}")
        print(f"\033[1;37mCreated Date :\033[0m {cdt}")
        print(f"\033[1;37mUser ID      :\033[0m {id}")
        print("─" * 55)
        print(f"\033[1;36mBio:\033[0m {bio}")
        print("\n\033[1;34m" + "═" * 72 + "\033[0m")
        print("\033[1;33mEMAD CYBER | by @e4_19\033[0m")

     except:
        print(f'\033[1;31m[!] Username incorrect or parsing error: {username}\033[0m')

print("\n")
get_info(username=input('\033[92mEnter TikTok Username: \033[0m '))

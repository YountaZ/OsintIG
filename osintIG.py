#!/usr/bin/python
# MAU RECODE GPP ASAL KASIH NAMA AKUN MIMIN BIAR BERKAH...
import os
import time
import sys
from sys import stderr
import instaloader

Bl='\033[30m' # VARIABLE BUAT WARNA CUYY
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

# AUTO CUY!!
def autoketik(x):
    for y in x + "\n":
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(0.200)

os.system('clear')
def banner(): #BANNER GW
    stderr.writelines(f"""{Gr}   
  ___   _____ ____  ____   ______        ____   ____ 
 /   \ / ___/|    ||    \ |      |      |    | /    |
|     (   \_  |  | |  _  ||      | _____ |  | |   __|
|  O  |\__  | |  | |  |  ||_|  |_||     ||  | |  |  |
|     |/  \ | |  | |  |  |  |  |  |_____||  | |  |_ |
|     |\    | |  | |  |  |  |  |         |  | |     |
 \___/  \___||____||__|__|  |__|        |____||___,_|

    {Wh}<< << << {Ye}TOOLS OSINT INSTAGRAM BY HUNX {Wh}>> >> >>
""")
banner()

try:
    def target_user():
        insta = instaloader.Instaloader()
        user = input(f"\n{Wh}[{Ye}+{Wh}]{Wh} Input username target : {Ye}")
        print(f"{Wh}[{Ye}!{Wh}]{Wh} Checking target account ")
        autoketik(f"{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-{Gr}-{Wh}-")
        profile = instaloader.Profile.from_username(insta.context, user)
        print()
        print(f"{Wh}Username   :{Gr}", profile.username)
        print(f"{Wh}User       :{Gr}", profile.full_name)
        print(f"{Wh}ID         :{Gr}", profile.userid)
        print(f"{Wh}Bio        :{Gr}", profile.biography)
        print(f"{Wh}Followers  :{Gr}", profile.followers)
        print(f"{Wh}Following  :{Gr}", profile.followees)
        print(f"{Wh}Total post :{Gr}", profile.mediacount)
        print()
        print(f"{Wh}[{Ye}+{Wh}]{Wh} Download target post :")
        time.sleep(0.3)
        for post in profile.get_posts():
            insta.download_post(post, target=profile.username)
except KeyboardInterrupt:
    print(f"{White} stopped Program...")

if __name__ ==  "__main__":
    target_user()






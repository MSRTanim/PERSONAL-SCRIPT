print("""
\033[1;32m
▄▄▄█████▓ ▒█████  ▒██   ██▒ ██▓ ▄████▄  
▓  ██▒ ▓▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▒██▀ ▀█  
▒ ▓██░ ▒░▒██░  ██▒░░  █   ░▒██▒▒▓█    ▄ 
░ ▓██▓ ░ ▒██   ██░ ░ █ █ ▒ ░██░▒▓▓▄ ▄██▒
  ▒██▒ ░ ░ ████▓▒░▒██▒ ▒██▒░██░▒ ▓███▀ ░
  ▒ ░░   ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░ ░▒ ▒  ░
    ░      ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░  ░  ▒   
  ░      ░ ░ ░ ▒   ░    ░   ▒ ░░        
             ░ ░   ░    ░   ░  ░ ░      
                               ░        

\033[0;31m════════════════════════════════════════════
\033[0;34mTOOLS UPDATE COMPLETED
\033[0;31m════════════════════════════════════════════
\033[32;1m┌──────────────────────────────────────────┐
\033[32;1m│ [✓] AUTHOR   : 𝐌𝐃 𝐒𝐀𝐌𝐈𝐔𝐑 𝐑𝐀𝐇𝐌𝐀𝐍 𝐓𝐀𝐍𝐈𝐌    │
\033[33;1m│ [✓] GITHUB   : 𝐌𝐒𝐑𝐓𝐚𝐧𝐢𝐦                  │
\033[34;1m│ [✓] WHATSAPP : +𝟖𝟖𝟎𝟏𝟓𝟕𝟓𝟏𝟐𝟎𝟔𝟖𝟐            │
\033[35;1m│ [✓] VERSION  : 3.0                       │
\033[36;1m│ [✓] POWER BY : \033[1;32m𝐓𝐎𝐗𝐈𝐂 𝐂𝐘𝐁𝐄𝐑 SECURITY \033[1;37m     │
\033[37;1m└──────────────────────────────────────────┘        
\033[0;31m════════════════════════════════════════════""")


def menu():
  print("\033[32;1m[1] Termux Setup")
  print("[2] URL Shortner")
  print("[3] Follow Owner")
  print("[0] Exit the program.")


menu()
option = int(input("Enter your option: "))

while option != 0:
  if option == 1:
    print(""" 
      \033[1;36m
      ┳      ┓┓•       
      ┃┏┓┏╋┏┓┃┃┓┏┓┏┓   
      ┻┛┗┛┗┗┻┗┗┗┛┗┗┫•••
                   ┛                
      """)

    import os

    os.system('clear')
    #Install apt
    print(""" 
      \033[1;36m
      ┏┓  ┓   ┳┳   ┓   •       
      ┣┫┏┓┃┏  ┃┃┏┓┏┫┏┓╋┓┏┓┏┓   
      ┛┗┣┛┛┗  ┗┛┣┛┗┻┗┻┗┗┛┗┗┫•••
        ┛       ┛          ┛   
      """)

    # print("""
    # \033[1;36m

    # """)

    os.system('apt update && apt upgrade')
    os.system('clear')
    #Install all command
    print(""" 
      \033[1;36m
      ┏┓             ┏┓          
      ┗┓╋┏┓┏┓┏┓┏┓┏┓  ┗┓┏┓╋┓┏┏┓   
      ┗┛┗┗┛┛ ┗┻┗┫┗   ┗┛┗ ┗┗┻┣┛•••
                ┛           ┛    
      """)
    os.system('termux-setup-storage')
    os.system('clear')
    print(""" 
      \033[1;36m
      ┏┓   ┓         ┳┳   ┓   •       
      ┃┃┏┓┏┃┏┏┓┏┓┏┓  ┃┃┏┓┏┫┏┓╋┓┏┓┏┓   
      ┣┛┗┻┗┛┗┗┻┗┫┗   ┗┛┣┛┗┻┗┻┗┗┛┗┗┫•••
                ┛      ┛          ┛   
      """)
    os.system('pkg update')
    os.system('pkg upgrade')
    os.system('clear')
    print(""" 
      \033[1;36m
      ┏┓   ┓       ┳      ┓┓•       
      ┃┃┓┏╋┣┓┏┓┏┓  ┃┏┓┏╋┏┓┃┃┓┏┓┏┓   
      ┣┛┗┫┗┛┗┗┛┛┗  ┻┛┗┛┗┗┻┗┗┗┛┗┗┫•••
         ┛                      ┛   
      """)
    os.system('pkg install python2')
    os.system('pkg install python3')
    os.system('clear')
    print(""" 
      \033[1;36m
      ┏┓•    ┳      ┓┓•       
      ┃┃┓┏┓  ┃┏┓┏╋┏┓┃┃┓┏┓┏┓   
      ┣┛┗┣┛  ┻┛┗┛┗┗┻┗┗┗┛┗┗┫•••
         ┛                ┛   
      """)
    os.system('pip install requests')
    os.system('pip2 install requests')
    os.system('pip install mechanize')
    os.system('pip2 install mechanize')
    os.system('pip install bs4')
    os.system('pip2 install bs4')
    os.system('clear')

    print(""" 
      \033[1;36m
      •  ┏┓    ┳      ┓┓•       
      ┓┏┓┏┛┏┓  ┃┏┓┏╋┏┓┃┃┓┏┓┏┓   
      ┃┣┛┗━┗┻  ┻┛┗┛┗┗┻┗┗┗┛┗┗┫•••
      ┛┛                    ┛   
      """)
    os.system('apt install jp2a')
    os.system('clear')

    print(""" 
      \033[1;36m
          ┓     ┳      ┓┓•       
      ┏┓┓┏┣┓┓┏  ┃┏┓┏╋┏┓┃┃┓┏┓┏┓   
      ┛ ┗┻┗┛┗┫  ┻┛┗┛┗┗┻┗┗┗┛┗┗┫•••
             ┛               ┛   
      """)
    os.system('pkg install ruby')
    os.system('clear')

    print(""" 
      \033[1;36m
      ┓         ┳      ┓┓•       
      ┣┓╋╋┏┓┓┏  ┃┏┓┏╋┏┓┃┃┓┏┓┏┓   
      ┛┗┗┗┣┛┛┗  ┻┛┗┛┗┗┻┗┗┗┛┗┗┫•••
          ┛                  ┛   
      """)
    os.system('pip install httpx')
    os.system('clear')

    print(""" 
      \033[1;36m
      ┓        •┏  ┓         ┳      ┓┓•       
      ┣┓┏┓┏┓┓┏╋┓╋┓┏┃┏┏┓┓┏┏┓  ┃┏┓┏╋┏┓┃┃┓┏┓┏┓   
      ┗┛┗ ┗┻┗┻┗┗┛┗┻┗┛┗┛┗┻┣┛  ┻┛┗┛┗┗┻┗┗┗┛┗┗┫•••
                         ┛                ┛   
      """)
    os.system('pip install beautifulsoup')
    os.system('clear')

    print(""" 
      \033[1;36m
      ┓  ┓      ┳      ┓┓•       
      ┃┏┓┃┏┏┓╋  ┃┏┓┏╋┏┓┃┃┓┏┓┏┓   
      ┗┗┛┗┗┗┻┗  ┻┛┗┛┗┗┻┗┗┗┛┗┗┫•••
                             ┛   
      """)
    os.system('pip install lolcat')
    os.system('gem install lolcat')
    os.system('clear')

    print(""" 
      \033[1;36m
                ┳      ┓┓•       
      ┓┏┏┏┓┏┓╋  ┃┏┓┏╋┏┓┃┃┓┏┓┏┓   
      ┗┻┛┗┫┗ ┗  ┻┛┗┛┗┗┻┗┗┗┛┗┗┫•••
          ┛                  ┛   
      """)
    os.system('pkg install wget')
    os.system('clear')

    print(""" 
      \033[1;36m
        ┓     ┳      ┓┓•       
      ┏┓┣┓┏┓  ┃┏┓┏╋┏┓┃┃┓┏┓┏┓   
      ┣┛┛┗┣┛  ┻┛┗┛┗┗┻┗┗┗┛┗┗┫•••
      ┛   ┛                ┛   
      """)
    os.system('pkg install php')
    os.system('clear')

    print(""" 
      \033[1;36m
      ┓    ┓   ┳      ┓┓•       
      ┣┓┏┓┏┣┓  ┃┏┓┏╋┏┓┃┃┓┏┓┏┓   
      ┗┛┗┻┛┛┗  ┻┛┗┛┗┗┻┗┗┗┛┗┗┫•••
                            ┛   
      """)
    os.system('pkg install bash')
    os.system('clear')

    print(""" 
      \033[1;36m
           ┓  ┳      ┓┓•       
      ┏┓┏┏┓┃  ┃┏┓┏╋┏┓┃┃┓┏┓┏┓   
      ┗┗┻┛ ┗  ┻┛┗┛┗┗┻┗┗┗┛┗┗┫•••
                           ┛   
      """)
    os.system('pkg install curl')
    os.system('clear')

    print(""" 
      \033[1;36m
            ┓  ┳      ┓┓•       
      ┏┓┏┓┏┓┃  ┃┏┓┏╋┏┓┃┃┓┏┓┏┓   
      ┣┛┗ ┛ ┗  ┻┛┗┛┗┗┻┗┗┗┛┗┗┫•••
      ┛                     ┛   
      """)
    os.system('pkg install perl')
    os.system('clear')

    print("""
      ┳      ┓┓  ┏┓       ┓   •       
      ┃┏┓┏╋┏┓┃┃  ┃ ┏┓┏┳┓┏┓┃┏┓╋┓┏┓┏┓   
      ┻┛┗┛┗┗┻┗┗  ┗┛┗┛┛┗┗┣┛┗┗ ┗┗┛┗┗┫•••
                        ┛         ┛   
      """)
    os.system('clear')

    print("""
      \033[1;32m
      ▄▄▄█████▓ ▒█████  ▒██   ██▒ ██▓ ▄████▄  
      ▓  ██▒ ▓▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▒██▀ ▀█  
      ▒ ▓██░ ▒░▒██░  ██▒░░  █   ░▒██▒▒▓█    ▄ 
      ░ ▓██▓ ░ ▒██   ██░ ░ █ █ ▒ ░██░▒▓▓▄ ▄██▒
        ▒██▒ ░ ░ ████▓▒░▒██▒ ▒██▒░██░▒ ▓███▀ ░
        ▒ ░░   ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░ ░▒ ▒  ░
          ░      ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░  ░  ▒   
        ░      ░ ░ ░ ▒   ░    ░   ▒ ░░        
                   ░ ░   ░    ░   ░  ░ ░      
                                     ░        


      \033[0;31m════════════════════════════════════════════
      \033[32;1m┌──────────────────────────────────────────┐
      \033[32;1m│ [✓] AUTHOR   : 𝐌𝐃 𝐒𝐀𝐌𝐈𝐔𝐑 𝐑𝐀𝐇𝐌𝐀𝐍 𝐓𝐀𝐍𝐈𝐌    │
      \033[33;1m│ [✓] GITHUB   : 𝐌𝐒𝐑𝐓𝐚𝐧𝐢𝐦                  │
      \033[34;1m│ [✓] WHATSAPP : +𝟖𝟖𝟎𝟏𝟓𝟕𝟓𝟏𝟐𝟎𝟔𝟖𝟐            │
      \033[35;1m│ [✓] VERSION  : 3.0                       │
      \033[36;1m│ [✓] POWER BY : \033[1;32m𝐓𝐎𝐗𝐈𝐂 𝐂𝐘𝐁𝐄𝐑 SECURITY \033[1;37m     │
      \033[37;1m└──────────────────────────────────────────┘        
      \033[0;31m════════════════════════════════════════════

      \033[1;36m
      ┏┓         ┏┓       ┓      ┓
      ┗┓┏┓╋┓┏┏┓  ┃ ┏┓┏┳┓┏┓┃┏┓╋┏┓┏┫
      ┗┛┗ ┗┗┻┣┛  ┗┛┗┛┛┗┗┣┛┗┗ ┗┗ ┗┻•••
             ┛          ┛         

      \033[5m Setup has been Completed
      \033[0;34m RUN "exit" command for Complete the process

      """)

  elif option == 2:
    os.system('pip install pyshorteners')
    os.system('pip install pyperclip')
    # pip install pyshorteners
    # pip install pyperclip
    url = input('Enter the url: ')
    def shortenurl(url):
        s = pyshorteners.Shortener()
        print(s.tinyurl.short(url))

    shortenurl(url)

  elif option == 3:
    os.system("xdg-open https://www.facebook.com/msrtanim.py")
  else:
    print("Invalid Option Selected")

  menu()
  option = int(input("Enter your option: "))
print("Thanks for using this Program. Have a Great time!")

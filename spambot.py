from requests.sessions import Session
from requests import get
from random import choice
from multiprocessing import Process
from colorama import init,Style,Fore

BANNER = """
                                     ..o$***R$"#N..
                                .e@F")dC.  .Jh*"""N.
                              oPh 'E""" ^$""*c. u**R.
                           .dEh@$P"$mm**$hmJ""C$"   R
                          :P$$hu.$x$.. 8Lum@8"C$u.uP
                  .       $b?LR4Bx"?E"$7L.om*""  '$
              .e*""#hu   JF'"$N.$*$b5JP"" .   ..  M
      ...    JF      '#ud#*N@".@")(7d"  u@"  4f""N$
    .@"""Nu. $         '#o Mo$#he@5P  m"CdR> 4Ld$E$
   .$     '"@B           '#$ JE*$.$    "***\ '$"""$
   4>        Mr            '#b.$sJF           R   '#c
    R        'B.             'RL.$            #c    ?L
    "Nu.     :P"#h..           '"B         ....$     R
      d"     M    "#Ru.          '?k    d\       d- :P
     @       *r       ""*n         $  '""#$@**"3P  .@
     M       4>                   JF       """""  d"
     M       'Ro                 uP        .   .d*"
     ^*o.      ^N@***hmmmr      @"      d"""**#"
        "$*    4P              JF     u$.
         B     4>              $       ^"#b.
         *r    'B      ....   'b          '#u
         '#h.   ^"@*"""""      ?L           *r
            #Nm  @"        .    R.          4>
             $   $      x@R"    '           4>
             '#bedR**N@""                   4>
                'N. JF    J>       $        4>
                  ""#Nou@"   J    'E        4>
                       $*hxo*      $        4>
                     .dPNmmr       '"\      'L
                   .dP"               \      B
                  #"                   \     *r
                /                       \    'B
               /'                        N.   ?>
               d                         '#c  'R
               M                           $  .R
               M                           *ruP
               ?>        $                 4F"
               'L        @.                4>
                ?L       'B                4>
                 "h.     .JNu.             4k
                   "#*@@*"  '"$**Nm        d>
                      4F     J>           .$
                      4>     M           .$"
                      4>     $          .R
                      4L    .R         xP
                       R    J>        .R
                       R    M        xP
                     .@"   uR       .R
                    JF    d"       d"
                   .$    @"       4F
                   M     $        J>
                   M     R        M
                   "L    $        $
                    N.   ^N.      "b
                    'R     Rr      '*s.
                    uP    :$          ^*mumc
                    $     'B   ...       ..R
                    $$$$$$$^$$$$$$$$$$$$$$$'

                        Le Slob's Angel
                                                
"""

USER_AGENTS = ["Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0",
"Mozilla/5.0 (Android 4.4; Tablet; rv:41.0) Gecko/41.0 Firefox/41.0",
"Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0",
"Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0",
"Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0"]

USER_AGENT = choice(USER_AGENTS)

class Client:
    def __init__(self,username,password,proxy):
        self.ses = Session()
        self.loggedIn = False
        self.username = username
        self.password = password
        self.proxy = proxy
    
    def Login(self):
        if self.loggedIn == True:
            return None
        
        loginData = {
            "password":self.password,
            "username":self.username,
            "queryParams":"{}"
        }
        homePageResponse = self.ses.get("https://www.instagram.com/accounts/login/")
        loginHeaders = {
            "Accept":"*/*",
            "Accept-Encoding":"gzip,deflate,br",
            "Accept-Language":"en-US,en;q=0.5",
            "Connection":"keep-alive",
            "Content-Type":"application/x-www-form-urlencoded",
            "Host":"www.instagram.com",
            "Referer":"https://www.instagram.com/accounts/login/",
            "X-Requested-With":"XMLHttpRequest",
            "X-Instagram-AJAX":"1",
            "User-Agent":USER_AGENT,
            "X-CSRFToken":homePageResponse.cookies.get_dict()["csrftoken"],
        }
        loginCookies = {
            "rur":"PRN",
            "csrftoken":homePageResponse.cookies.get_dict()["csrftoken"],
            "mcd":homePageResponse.cookies.get_dict()["mcd"],
            "mid":homePageResponse.cookies.get_dict()["mid"]
        }
        self.ses.headers.update(loginHeaders)
        self.ses.cookies.update(loginCookies)

        loginPostResponse = self.ses.post("https://www.instagram.com/accounts/login/ajax/",data=loginData)
    
        if loginPostResponse.status_code == 200 and loginPostResponse.json()["authenticated"] == True:
            self.loggedIn = True
            mainPageResponse = self.ses.get("https://www.instagram.com/")
            self.ses.cookies.update(mainPageResponse.cookies)
    
    def Spam(self,username,userid):
        if self.loggedIn == False:
            return None   

        link = "https://www.instagram.com/" + username + "/"
        profileGetResponse = self.ses.get(link)
        self.ses.cookies.update(profileGetResponse.cookies)
        spamHeaders = {
            "Accept":"*/*",
            "Accept-Encoding":"gzip,deflate,br",
            "Accept-Language":"en-US,en;q=0.5",
            "Connection":"keep-alive",
            "Content-Type":"application/x-www-form-urlencoded",
            "DNT":"1",
            "Host":"www.instagram.com",
            "X-Instagram-AJAX":"2",
            "X-Requested-With":"XMLHttpRequest",
            "Referer":link,
            "User-Agent":USER_AGENT,
            "X-CSRFToken":profileGetResponse.cookies.get_dict()["csrftoken"],
        }
        spamData = {
            "reason_id":"1",
            "source_name":"profile"
        }

        self.ses.headers.update(spamHeaders)

        spamPostResponse = self.ses.post("https://www.instagram.com/users/"+ userid +"/report/",data=spamData)
        if spamPostResponse.status_code == 200 and spamPostResponse.json()["description"] == "Your reports help keep our community free of spam.":
            self.ses.close()
            return True
        else:
            return False

def Success(username,shit):
    print(Fore.GREEN +"[" + username +"]" + Style.RESET_ALL
    + " " + shit)

def Fail(username,shit):
    print(Fore.RED +"[" + username +"]" + Style.RESET_ALL
    + " " + shit)

def Status(shit):
    print(Fore.YELLOW +"[ İnsta Spam ]" + Style.RESET_ALL
    + " " + shit)

def DoitAnakin(reportedGuy,reportedGuyID,username,password,proxy):
    try:
        insta = None
        if proxy != None:
            insta = Client(username,password,None)
        else:
            insta = Client(username,password,None)
        insta.Login()
        result = insta.Spam(reportedGuy,reportedGuyID)
        if insta.loggedIn == True and result == True:
            Success(username,"Başarıyla SPAM atıldı!")
        elif insta.loggedIn == True and result == False:
            Fail(username,"Giriş başarılı ama SPAM atılması başarısız!")
        elif insta.loggedIn == False:
            Fail(username,"Giriş başarısız!")
    except:
        Fail(username,"Giriş yapılırken hata oluştu!")

if __name__ == "__main__":
    init()
    userFile = open("userlist.txt","r")

    USERS = []
    for user in userFile.readlines():
        if user.replace("\n","").replace("\r","\n") != "":
            USERS.append(user.replace("\n","").replace("\r","\n"))


    print(Fore.RED + BANNER + Style.RESET_ALL)
    Status(str(len(USERS)) + " Adet Kullanıcı Yüklendi!\n")
    reportedGuy = input(Fore.GREEN + "SPAM'lanacak Kişinin Kullanıcı Adı: " + Style.RESET_ALL)
    reportedGuyID = input(Fore.GREEN + "SPAM'lanacak Kişinin User ID'si: " + Style.RESET_ALL)
    print("")
    Status("Saldırı başlatılıyor!\n")

    for user in USERS:
        p = Process(target=DoitAnakin,args=(reportedGuy,reportedGuyID,user.split(" ")[0],user.split(" ")[1],None))
        p.start()

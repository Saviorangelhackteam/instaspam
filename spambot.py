dan requests.sessions ithalat Oturumu
dan istekleri içe olsun
dan rastgele ithalat seçimi
dan çoklu işlem ithalat Süreci
dan Colorama ithalat init, Stil, Fore

BANNER  =  "" "
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

                      Savior Angel Hack Team Mr.Bomba

   
"""

USER_AGENTS  = [ " Mozilla / 5.0 (Android 4.4; Mobil; rv: 41.0) Gecko / 41.0 Firefox / 41.0 " ,
" Mozilla / 5.0 (Android 4.4; Tablet; rv: 41.0) Gecko / 41.0 Firefox / 41.0 " ,
" Mozilla / 5.0 (Windows NT xy; rv: 10.0) Gecko / 20100101 Firefox / 10.0 " ,
" Mozilla / 5.0 (X11; Linux i686; rv: 10.0) Gecko / 20100101 Firefox / 10.0 " ,
" Mozilla / 5.0 (X11; Linux x86_64; rv: 10.0) Gecko / 20100101 Firefox / 10.0 " ,
" Mozilla / 5.0 (Android 4.4; Mobil; rv: 41.0) Gecko / 41.0 Firefox / 41.0 " ]

USER_AGENT  = seçim ( USER_AGENTS )

sınıf  müşteri :
    def  __init__ ( kişisel , kullanıcı adı , şifre , vekil ):
        kendi kendine .ses = Oturum ()
        self .loggedIn =  Yanlış
        self .username = kullanıcı adı
        kendi kendine .password = şifre
        öz .proxy = vekil
    
    def  Giriş ( kişisel ):
        eğer  kendini .loggedIn ==  Doğru :
            geri dönüş  Yok
        
        loginData = {
            " Parola " : kendini .password,
            " username " : kişisel kullanıcı adı ,
            " queryParams " : " {} "
        }
        homePageResponse =  self .ses.get ( " https://www.instagram.com/accounts/login/ " )
        loginHeaders = {
            " Kabul et " : " * / * " ,
            " Kabul Kodlama " : " gzip, deflate, br " ,
            " Kabul Dili " : " en-US, en; q = 0.5 " ,
            " Bağlantı " : " canlı tutma " ,
            " İçerik Türü " : " uygulama / x-www-form-urlencoded " ,
            " Ana Bilgisayar " : " www.instagram.com " ,
            " Yönlendiren " : " https://www.instagram.com/accounts/login/ " ,
            " X-İstenen-İle " : " XMLHttpRequest " ,
            " X-Instagram-AJAX " : " 1 " ,
            " Kullanıcı Aracısı " : USER_AGENT ,
            " X-CSRFToken " : homePageResponse.cookies.get_dict () [ " csrftoken " ],
        }
        loginCookies = {
            " rur " : " PRN " ,
            " csrftoken " : homePageResponse.cookies.get_dict () [ " csrftoken " ],
            " mcd " : homePageResponse.cookies.get_dict () [ " mcd " ],
            " mid " : homePageResponse.cookies.get_dict () [ " mid " ]
        }
        kendini .ses.headers.update (loginHeaders)
        self .ses.cookies.update (loginCookies)

        loginPostResponse =  self .ses.post ( " https://www.instagram.com/accounts/login/ajax/ " , data = loginData)
    
        eğer loginPostResponse.status_code ==  200  ve loginPostResponse.json () [ " doğrulanmış " ] ==  Doğru :
            self .loggedIn =  Doğru
            mainPageResponse =  self .ses.get ( " https://www.instagram.com/ " )
            self .ses.cookies.update (mainPageResponse.cookies)
    
    def  Spam ( öz , kullanıcı adı , kullanıcı kimliği ):
        eğer  öz. KupasıIn ==  Yanlış :
            geri dönüş  Yok   

        link =  " https://www.instagram.com/ "  + kullanıcı adı +  " / "
        profileGetResponse =  self .ses.get (bağlantı)
        self .ses.cookies.update (profileGetResponse.cookies)
        spamHeaders = {
            " Kabul et " : " * / * " ,
            " Kabul Kodlama " : " gzip, deflate, br " ,
            " Kabul Dili " : " en-US, en; q = 0.5 " ,
            " Bağlantı " : " canlı tutma " ,
            " İçerik Türü " : " uygulama / x-www-form-urlencoded " ,
            " DNT " : " 1 " ,
            " Ana Bilgisayar " : " www.instagram.com " ,
            " X-Instagram-AJAX " : " 2 " ,
            " X-İstenen-İle " : " XMLHttpRequest " ,
            " Yönlendirici " : link,
            " Kullanıcı Aracısı " : USER_AGENT ,
            " X-CSRFToken " : profileGetResponse.cookies.get_dict () [ " csrftoken " ],
        }
        spamData = {
            " reason_id " : " 1 " ,
            " kaynak_adı " : " profil "
        }

        kendini .ses.headers.update (spamHeaders)

        spamPostResponse =  self .ses.post ( " https://www.instagram.com/users/ " + userid + " / report / " , data = spamData)
        eğer spamPostResponse.status_code ==  200  ve spamPostResponse.json () [ " açıklama " ] ==  " Raporlarınız, topluluğumuzun spam'lerden korunmasına yardımcı olur. " :
            kendini. ses.close ()
            return  True
        başka :
             Yanlış döndürmek

def  Başarı ( kullanıcı adı , bok ):
    print (Fore. YEŞİL  + " [ "  + kullanıcı adı + " ] "  + Stil. RESET_ALL
    +  "  "  + bok

def  Fail ( kullanıcı adı , bok ):
    print (Fore. RED  + " [ "  + kullanıcı adı + " ] "  + Stil. RESET_ALL
    +  "  "  + bok

def  Durum ( bok ):
    print (Fore. SARI  + " [İstenmeyen Posta Kodu] "  + Stil. RESET_ALL
    +  "  "  + bok

def  DoitAnakin ( reportedGuy , reportedGuyID , kullanıcı adı , şifre , vekil ):
    dene :
        insta =  Yok
        eğer proxy ! =  Yok :
            insta = Müşteri (kullanıcı adı, şifre, Yok )
        başka :
            insta = Müşteri (kullanıcı adı, şifre, Yok )
        insta.Login ()
        sonuç = insta.Spam (reportGuy, reportGuyID)
        eğer insta.loggedIn ==  Doğru  ve sonuç ==  Doğru :
            Success (kullanıcı adı, " Başarıyla SPAM atıldı! " )
        elif insta.loggedIn ==  Doğru  ve sonuç ==  Yanlış :
            Başarısız (kullanıcı adı, " Giriş başarılı ama SPAM atılması başarısız! " )
        elif insta.loggedIn ==  Yanlış :
            Başarısız (kullanıcı adı, " Giriş başarısız! " )
    hariç :
        Başarısız (kullanıcı adı, " Giriş yapıldıken hata oluştu! " )

eğer  __name__  ==  " __main__ " :
    içinde()
    userFile =  open ( " userlist.txt " , " r " )

    KULLANICILAR  = []
    userFile.readlines () içindeki kullanıcı için :
        eğer user.replace ( " \ n " , " " ) .replace ( " \ r " , " \ n " ) ! =  " " :
            USERS .append (user.replace ( " \ n " , " " )) .replace ( " \ r " , " \ n " ))


    print (Fore. RED  +  BANNER  + Stil. RESET_ALL )
    Durum ( str ( len ( USERS )) +  " Adet Kullanıcı Yüklendi! \ N " )
    reportedGuy =  girişi (. Ön YEŞİL  +  " SPAM'lanacak Kişinin Kullanıcı Adı: "  + . Stil RESET_ALL )
    reportedGuyID =  input (Fore. YEŞİL  +  " SPAM'lanacak Kişinin Kullanıcı ID'si: "  + . Stil RESET_ALL )
    Yazdır ( " " )
    Durum ( " Saldırı başlatılıyor! \ N " )

    için kullanıcı içinde  KULLANICILAR :
        p = Süreç ( target = DoitAnakin, args = ( işlem gördüGuy, reportGuyID, user.split ( "  " ) [ 0 ], user.split ( "  " ) [ 1 ], Yok ))
        p.start ()

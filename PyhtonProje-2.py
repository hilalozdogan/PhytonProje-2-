
import random


def menu_goruntule():
    print("\n------MENÜ-------")
    print("1.Fal Bakma Oyunu")
    print("2.Blackjack (21) Oyunu")
    print("3.Çıkış")

def sayi_al(alt_sinir,ust_sinir):
    sayi=int(input())
    while sayi<alt_sinir or sayi>ust_sinir: # sayi dogru girilinceye kadar bekleniyor
        sayi=int(input("hatali veri girisi, lutfen tekrar giriniz:"))
    return sayi

def desteyi_karıştır():
    kart_isimleri = [["As", 1], ["İkili", 2], ["Üçlü", 3], ["Dörtlü", 4], ["Beşli", 5], ["Altılı", 6], ["Yedili", 7],
                     ["Sekizli", 8], ["Dokuzlu", 9], ["Onlu", 10], ["Vale", 11], ["Kız", 12], ["Papaz", 13]]

    kart_türü = ["Kupa", "Karo", "Maça", "Sinek"]
    deste = 52 * []

    for x in kart_türü:
        for y in kart_isimleri:
            deste.append([x, y])

    random.shuffle(deste) #shuffle fonksiyonu ile deste karıştırılıyor

    return deste

def toplam_bul(a):
    x=y=z=0
    for i in range(len(a)):
        if 1 < a[i][1][1] <= 10: #kart_isimleri listesindeki elemanların değeri 1-10 arası ise olduğu gibi alınıp toplanmalı
            x+=a[i][1][1]
        elif a[i][1][1] > 10: #Yukarıdaki koşul sağlanmıyorsa kart değerleri 10 alıp toplanmalı.(Vale-Kız-Papaz için)
            x+= 10

    for i in range(len(a)):
        if 'As' in a[i][1][0]  and  x+11<=21: #Eğer elde As varsa ve elin toplamı 21'i geçmiyorsa As 11 değerini alıyor
            y=x+11
        elif 'As' in a[i][1][0]: #Yukarıdaki koşul sağlanmıyorsa As 1 değerini alır
            z=x+1

    if(y!=0):
        return y-10,y
    elif(z!=0):
        return z,z+10
    else:
        return x,0 #return 'un ikinci döndürdüğü 0 ise elde as yoktur


def toplam_yazdır(a):
    deger1,deger2=toplam_bul(a)
    if(deger2==0): #return'un ikinci değeri 0'sa yani elde as yoksa tek bir toplam değeri oluyor
        print("Toplam:",deger1)
    else:
        print("Toplam:{} ya da {}".format(deger1,deger2)) #Eğer As varsa As'ın 1 ve 11 değerine göre 2 toplam değeri yazdırılıyor

def kart_cek(a,deste):
    a.append(deste[0])
    deste.pop(0)
    for i in range(len(a)):
        print(a[i][0], a[i][1][0])

def menu():
    cikis = 'h'
    while cikis == 'H' or cikis == 'h':
        menu_goruntule()
        print("Seciminizi giriniz [0-3]:", end='')
        secim = sayi_al(1, 3)

        if secim == 1:
            print("\nFal Bakma Oyununa Hoşgeldiniz!")
            tekrar='e'
            while tekrar=='e' or tekrar=='E':
                devam=input("\nNiyetinizi tuttunuz mu(E/e/H/h)?:")
                while devam not in ['E', 'e', 'H','h']: #(E/e/H/h) harflerinden birinin girilmesini sağlar
                    devam = input("Lütfen (E/e/H/h) harflerinden birini giriniz:")
                yeni_deste = desteyi_karıştır()
                puan_kartları = []
                acılan_kartlar = []

                while (devam == 'e' or devam == 'E') and len(acılan_kartlar)==0:

                    for i in range(len(yeni_deste)):
                        acılan_kartlar.append(yeni_deste[0])
                        print(i + 1,".",acılan_kartlar[i][0],acılan_kartlar[i][1][0],end=' ')
                        input()
                        yeni_deste.pop(0)

                        if (i + 1 == acılan_kartlar[i][1][1]):
                            print("(Eşleşti, saymaya yeniden başlanıyor...)\n")
                            puan_kartları.append(acılan_kartlar[i])
                            acılan_kartlar.pop()
                            yeni_deste.extend(acılan_kartlar) #Eşleşen kart diğer açılan kartlar destenin sonuna ekleniyor
                            acılan_kartlar.clear()
                            break

                        elif (i + 1 == 13 and not (i + 1 == acılan_kartlar[i][1][1])):
                            print("(Hiç eşleşmedi, saymaya yeniden başlanıyor...)\n")
                            acılan_kartlar.clear() #Hiç eşleşmediği için açılan kartlar siliniyor ve desteye eklenmiyor
                            break

                    else:
                        toplam=0
                        for x in range(len(puan_kartları)):
                            if puan_kartları[x][1][0]=="Vale" or puan_kartları[x][1][0]=="Kız" or puan_kartları[x][1][0]=="Papaz":
                               puan_kartları[x][1][1]=10

                        for y in range(len(puan_kartları)):
                            toplam+=puan_kartları[y][1][1]
                        print("\nBitti,Toplam puanınız:",toplam)
                        print("Niyetiniz %{} ihtimalle gerçekleşecek!\n".format(toplam))

                        tekrar = input("Tekrar oynamak ister misiniz(e/E/h/H)?")
                        while tekrar not in ['e', 'E', 'h', 'H']:
                            tekrar = input("Tekrar oynamak ister misiniz(e/E/h/H)?")

                        if(tekrar=='h' or tekrar=="H"):
                            break


        elif secim == 2:

            print("\nBlackjack(21) Oyununa Hoşgeldiniz!")

            tekrar = 'e'
            while tekrar == 'e' or tekrar == 'E':
                yeni_deste=desteyi_karıştır()
                dagıtıcı_kart=[]
                oyuncu_kart=[]
                kapalı_kart=[]


                dagıtıcı_kart.append(yeni_deste[0])
                yeni_deste.pop(0)
                print("\nDağıtıcının Açık Kağıdı:",dagıtıcı_kart[0][0],dagıtıcı_kart[0][1][0])
                kapalı_kart.append(yeni_deste[0])
                yeni_deste.pop(0)

                oyuncu_kart.append(yeni_deste[0])
                yeni_deste.pop(0)
                oyuncu_kart.append(yeni_deste[0])
                yeni_deste.pop(0)
                print("Oyuncunun Kağıtları:", oyuncu_kart[0][0], oyuncu_kart[0][1][0], "-", oyuncu_kart[1][0],oyuncu_kart[1][1][0])

                toplam_yazdır(oyuncu_kart)
                top1,top2=toplam_bul(oyuncu_kart) #toplam_bul fonksiyonu 2 değer döndürüyor.Bu yüzden bu değerleri top1 ve top2'ye atadım
                if (top2==21): #top2'de As 11 değerini alır bu yüzden iki kart açıkken ancak top2=21 olabilir
                    print("BLACKJACK!","Oyuncu blackjack yaptı,sıra dağıtıcıda\n","Dağıtıcının kartları:",sep="\n")
                    kart_cek(dagıtıcı_kart,yeni_deste)
                    toplam_yazdır(dagıtıcı_kart)
                    dtop1,dtop2=toplam_bul(dagıtıcı_kart) #dtop1 ve dtop2 ,toplam_bul fonksiyonun dağıtıcı için döndürdüğü toplamlardır
                    if(dtop2==21):
                        print("BLACKJACK!","Dağıtıcı da Blackjack yaptı","\nOyun Berabere",sep="\n")
                        break
                    else:
                        print("\nDağıtıcı battı", "Oyunu oyuncu kazandı", sep="\n")
                        break

                else:
                    devam = input("\n(K)ağıt mı, (P)as mı?:")
                    while devam not in ['K', 'k', 'P','p']:
                        devam = input("Lütfen (K/k/P/p) harflerinden birini giriniz?:")
                    while (devam == 'K' or devam == 'k'):
                        print("\nOyuncunun kağıtları:")
                        print("----------------------")
                        kart_cek(oyuncu_kart,yeni_deste)
                        toplam_yazdır(oyuncu_kart)
                        top1,top2=toplam_bul(oyuncu_kart)
                        if(top1>21):
                            print("\nOyuncu battı", "Oyunu dağıtıcı kazandı", sep="\n")
                            break
                        elif(top1==21 or top2==21):
                            devam='P'
                        else:
                            devam = input("\n(K)ağıt mı, (P)as mı?:")

                    else:
                        print("\nSıra dağıtıcıda","Dağıtıcının kartları:",sep="\n")
                        print("----------------------")
                        dagıtıcı_kart.extend(kapalı_kart)
                        print(dagıtıcı_kart[0][0], dagıtıcı_kart[0][1][0])
                        print(dagıtıcı_kart[1][0],dagıtıcı_kart[1][1][0])
                        toplam_yazdır(dagıtıcı_kart)
                        dtop1,dtop2=toplam_bul(dagıtıcı_kart)
                        if(dtop2==21):
                            print("BLACKJACK","\nOyuncu battı","Oyunu dağıtıcı kazandı",sep="\n")
                            break

                        while ((dtop2==0 and dtop1<17)  or (1<dtop2<17)) : #Dağıtıcının elinin toplamı 17 den küçük olduğu sürece kart çekebilir
                            print("\nDağıtıcının kartları:")
                            print("----------------------")
                            kart_cek(dagıtıcı_kart,yeni_deste)
                            toplam_yazdır(dagıtıcı_kart)
                            dtop1, dtop2 = toplam_bul(dagıtıcı_kart)
                        else:
                            if dtop1==21 or dtop2==21 or ((dtop2==0 and dtop1<21 and dtop2<21) and dtop1>top1) or (dtop2<21 and ((dtop2>top1) and (dtop2>top2)) ):
                                print("\nOyuncu battı", "Oyunu dağıtıcı kazandı", sep="\n")

                            elif ((dtop2!=0 and (top1==dtop2 or top2==dtop2))) or (top2==0 and top1==dtop1):
                                print("\nOyun berabere")

                            else:
                                print("\nDağıtıcı battı","Oyunu oyuncu kazandı",sep="\n")

                tekrar = input("\nTekrar oynamak ister misiniz(e/E/h/H)?")
                while tekrar not in ['e', 'E', 'h','H']:
                    tekrar = input("Tekrar oynamak ister misiniz(e/E/h/H)?")

                if (tekrar == 'h' or tekrar == "H"):
                    break

        else:
            cikis = input("Cikmak istediginize emin misiniz(e/E/h/H)?:")
            while cikis not in ['e', 'E', 'h', 'H']:  # cevap dogru girilinceye kadar bekleniyor
                cikis = input("hatali veri girisi, lutfen tekrar giriniz:")

menu()


































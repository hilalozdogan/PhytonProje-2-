# PyhtonProje-2

### GENEL BİLGİLER

#### İskambil destesi:
Bir iskambil destesinde 4 grup (kupa-♥, karo-♦, maça-♠ ve sinek-♣) ve her grupta sırasıyla As, İkili, Üçlü, Dörtlü, Beşli, Altılı, Yedili, Sekizli, Dokuzlu, Onlu, Vale, Kız, Papaz isimli 13 adet olmak üzere toplam 52 adet kağıt bulunur.
Fal Bakma Oyunu: Bir oyuncu ve bir iskambil destesi ile oynanır. Oyuncunun amacı, tuttuğu niyetin gerçekleşme ihtimalini 100 üzerinden bulmaktır. Bunun için oyuncu bir niyet tutar, iskambil destesini karıştırır ve kağıtlar kapalı olarak bir elinde tutar. Sonra As’tan Papaz’a kadar sırayla sayarak kağıtları açmaya başlar ve açılan kağıtları üst üste dizer. Bu arada açılan bir kağıdın ismi ile sıra numarası eşleşirse, o kağıdı puan kağıdı olarak ayırır ve o ana kadar açılan diğer kağıtları ters çevirerek elindeki destenin altına koyar ve saymaya tekrar As’tan başlayarak kağıtları açmaya devam eder. Eğer arka arkaya 13 kağıttan hiçbirisinin ismi sıra numarasıyla eşleşmezse, açılmış 13 kağıdı elenmiş kağıtlar olarak ayırır (elindeki desteye eklemez) ve saymaya tekrar As’tan başlayarak kağıtları açmaya devam eder. Oyuncu elindeki tüm kağıtlar bittiğinde, puan kağıdı olarak ayırdığı kağıtların puanlarını (As 1 puan, İkili’den Onlu’ya kadar olan kağıtlar sırasıyla 2-10 puan, Vale, Kız ve Papaz ise 10 puan değerindedir.) toplayarak kendi puanını hesaplar. Bu puan, oyuncunun niyetinin 100 üzerinden gerçekleşme ihtimalidir. Örnek bir oyun için bakınız: https://youtu.be/GwY_BAq9SDo?t=660

#### Blackjack (21) Oyunu: 
Bir oyuncu, bir dağıtıcı ve bir iskambil destesi ile oynanır. Oyunda As 1 veya 11 puan, İkili’den Onlu’ya kadar olan kağıtlar sırasıyla 2-10 puan, Vale, Kız ve Papaz ise 10 puan değerindedir. Alınan ilk iki kağıdın toplamı 21 ise Blackjack yapılmış olur. Blackjack her zaman toplamı 21 yapan bir elden üstündür. Oyuncunun amacı, toplamı 21 eden bir ele sahip olmak ya da 21’e en yakın toplamla, ama 21 sayısının üzerine çıkmadan dağıtıcının elini yenmektir. Bunun için dağıtıcı başlangıçta, oyuncuya açık olarak iki kağıt ve kendisine de biri açık biri kapalı olarak iki kağıt dağıtır. Aynı kağıt ikinci bir kez çekilemez. Oyuncu ilk iki kağıdı aldıktan sonra, eğer elinde Blackjack yoksa, yeni bir kağıt isteyebilir ya da pas diyerek sırayı dağıtıcıya verebilir. Oyuncunun kağıtlarının toplamı 21’i geçmediği sürece yeni kağıt isteyebilir, 21’i geçerse oyuncu batmış olur ve oyunu direkt olarak kaybeder. As’ın değeri oyuncu için en avantajlı olacak şekilde alınır. Oyuncu Blackjack ya da 21 yaptıysa, battıysa ya da pas dediyse, sıra dağıtıcıya geçer. Sonra dağıtıcı kapalı olan kağıdını açar. Oyuncu batmışsa, oyunu direkt olarak dağıtıcı kazanır; oyuncu Blackjack yapmışsa ve dağıtıcı Blackjack yapmamışsa, dağıtıcı oyunu direkt olarak kaybeder. Diğer durumlarda dağıtıcı elindeki kağıtların toplamı 16 veya altındaki sayılarda yeni kağıt almak, 17 veya üzerindeki sayılarda da durmak zorundadır. Dağıtıcı için As her zaman 11 değerindedir, ancak kağıtlarının toplamı 21’i geçiyorsa As’ın değeri 1 olarak alınır. Örnek oyunlar için bakınız: https://youtu.be/6LG5f0x1Ikc , https://youtu.be/S8Lov_3KeiU

### PROBLEM TANIMI
Yukarıda tarif edilen iskambil oyunlarının simüle edilmesini sağlayacak bir program istenmektedir. Program ilk çalıştırıldığında ekranda aşağıdaki gibi bir menü görüntülenmelidir:

- MENÜ
1. Fal Bakma Oyunu
2. Blackjack (21) Oyunu 
3. Çıkış
- Seçiminizi giriniz:

Kullanıcı, [1-3] aralığı dışında bir değer girerse seçimi tekrar sorulmalıdır. 1 ya da 2 değerini girerse, kullanıcının isteği yerine getirilmelidir. Oyun bitince aynı oyunu tekrar oynamak isteyip istemediği sorulmalı [e/E/h/H], istiyorsa iskambil destesi karıştırılarak aynı oyun tekrar oynanmalı, istemiyorsa menüye geri dönülmelidir. Kullanıcı 3 değerini girerse, programdan çıkmak istediğinden emin olup olmadığı sorulmalı [e/E/h/H], emin değilse tekrar menüye dönülmeli, eminse programdan çıkılmalıdır.

#### 1) Fal Bakma Oyunu Simülasyonu
Kullanıcıya niyetini tutup tutmadığı sorulmalı, kullanıcı niyetini tuttuktan sonra simülasyon başlamalıdır. Açılan her kağıdın sıra numarası ile grubu ve ismi (Kupa Papaz, Sinek Yedili v.b.) ekranda görüntülenmelidir. Ayrıca oyunla ilgili yukarıda bahsedilen bir özel durum oluştuysa, bu durumla ilgili bilgi mesajı görüntülenmelidir. Her kağıttan sonra kullanıcının bir tuşa basması beklenmelidir. Oyun sonunda oyuncunun puanı, yani niyetinin gerçekleşme ihtimali olan yüzde değeri, görüntülenmelidir.

**Örnek Çıktı:**
Aşağıda belirli bir durum için örnek bir çıktı formatı verilmiştir. Farklı durumlarda başka çıktı formatları söz konusu olabilecektir. Ayrıca, herkes kendi çıktı formatını da oluşturabilir. Burada amaçlanan, oyunun durumunu açık ve anlaşılır bir şekilde ekranda göstermek olmalıdır.
- Niyetinizi tuttunuz mu(e/h)? e
1. Karo As (Eşleşti, saymaya yeniden başlanıyor...)
1. Maça Dört
2. Maça Kız
3. Kupa Üçlü (Eşleşti, saymaya yeniden başlanıyor...)
1. Karo Vale
2. Karo Dokuzlu
3. Kupa As
4. Sinek As
5. Maça Altılı
6. Sinek Sekizli
7. Kupa Papaz
8. Kupa İkili
9. Kupa Kız
10. Sinek Vale
11. Sinek Onlu
12. Maça Beşli
13. Sinek Yedili (Hiç eşleşmedi, saymaya yeniden başlanıyor...)
1. Sinek Kız
...
- Bitti, toplam puanınız: 67
- Niyetiniz %67 ihtimalle gerçekleşecek
- Tekrar oynamak istiyor musunuz(E/H)? h

#### 2) Blackjack (21) Oyunu Simülasyonu
Bilgisayar dağıtıcı, kullanıcı ise oyuncu rolünü oynamalıdır. Önce dağıtıcının açık olan kağıdının grubu ve ismi ile oyuncunun ilk 2 kağıdının grubu ve ismi ile toplam puanı ekranda görüntülenmelidir. İlk olarak sıra oyuncudadır. Oyuncu Blackjack yapmışsa sıra dağıtıcıya geçmelidir, yapmamışsa kağıt isteyip istemediği sorulmalıdır. Oyuncu batarsa ya da pas derse, sıra dağıtıcıya geçmelidir. Oyuncu batmışsa dağıtıcı oyunu kazanmalı, batmamışsa yukarıda bahsedilen kurallara göre dağıtıcı yeni kağıt almalı ya da durmalıdır. Her adımda oyuncunun/dağıtıcının elindeki kağıtların grubu ile ismi, toplam puanı ve yukarıda bahsedilen bir özel durum oluştuysa bu durumla ilgili bilgi mesajı görüntülenmelidir. Oyun sonunda sonuç (“oyuncu kazandı”, “dağıtıcı kazandı”, “berabere”) görüntülenmelidir.

**Örnek Çıktı:** Aşağıda belirli bir durum için örnek bir çıktı formatı verilmiştir. Farklı durumlarda başka çıktı formatları söz konusu olabilecektir. Ayrıca, herkes kendi çıktı formatını da oluşturabilir. Burada amaçlanan, oyunun durumunu açık ve anlaşılır bir şekilde ekranda göstermek olmalıdır.

- Dağıtıcının Açık Kağıdı: Maça Kız
- Oyuncunun Kağıtları: Karo As, Maça Dört (Toplam 5 ya da 15)
- (K)ağıt mı, (P)as mı?: K
- Oyuncunun Kağıtları: Karo As, Maça Dört, Sinek Üç (Toplam 8 ya da 18)
- (K)ağıt mı, (P)as mı?: P
- Oyuncunun puanı:18, sıra dağıtıcıda
- Dağıtıcının Kağıtları: Kupa İki, Maça Kız (Toplam 12)
- Dağıtıcının Kağıtları: Kupa İki, Maça Kız, Sinek Dört (Toplam 16)
- Dağıtıcının Kağıtları: Kupa İki, Maça Kız, Sinek Dört, Kupa On (Toplam 26)
- Dağıtıcı battı
- Oyunu oyuncu kazandı
- Tekrar oynamak istiyor musunuz(E/H)? E
- Dağıtıcının Açık Kağıdı: Maça Kız
- Oyuncunun Kağıtları: Karo As, Kupa Vale (Blackjack)
- Oyuncu Blackjack yaptı, sıra dağıtıcıda
- Dağıtıcının Kağıtları: Maça Kız, Maça As (Blackjack)
- Dağıtıcı Blackjack yaptı
- Oyun berabere
- Tekrar oynamak istiyor musunuz(E/H)? h



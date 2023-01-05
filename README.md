# Form_Web_App_With_Django
I developed this web form page. I saved some parameters from users in the user feedback form to mariaDB. I coded the backend with Django. For the frontend, I used html css and javascript.

## Projede Kullanılan Yazılım/Donanım Araçları
+ Django
+ MariaDB
+ Html
+ JavaScript
+ Bootstrap

### Django Kurulumu
Django kurulumu için bilgisayarınızda python ve pip kurulu olması gerekmektedir. Django kurulumu için öncelikle komut ekranını açıp bir klasör oluşturalım.

Pip freeze komutu ile mevcut olarak eklenmiş paketleri görelim. Komut çalıştırıldığında görüldüğü gibi birde fazla paket bulunmakta bu paketler bizim projemizi etkileyebilir veya projemiz için güncelleyeceğimiz bir paket daha önce oluşturduğumuz projeleri etkileyebilir. Projeyi dış ortamdaki paket, sürüm değişiklikleri gibi problemlerden korumak için sanal ortam oluştururuz.
Sanal ortamı pip install virtualenv komutu ile kurabiliriz.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/Sanal%20ortam%20kurulumu.png)

Virtualenv sanalortamadı komutu ile yeni bir sanal ortam oluşturalım. Scripts klasörüne girelim ve sanal ortamımızı aktifleştirelim. Aktifleştirildiğinde başında sanal ortam ismi gelmektedir.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2010.%20Aktifle%C5%9Ftirmek%20i%C3%A7in%20gerekli%20komutlar.png)

pip install Django komutu ile Django kurulumunu yapalım. Eski bir versiyon için versiyon numarası ile de kurulum yapabiliriz.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2011.%20Django%20kurulumu.png)

Pip freeze komutu ile kurulu paketleri kontrol edelim.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2012.%20Kurulu%20paketleri%20listelemek.png)

Django paketi sanal ortamımıza kuruldu. python -m django --version yazarak Django versiyonunu kontrol edebiliriz.

### Bir Django projesi oluşturmak

Kurulumlarımızı yaptık, hemen ardından boş bir klasörü Visual Studio Code’de açalım, new terminal diyelim ve django-admin komutunu girelim.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2013.%20Komut%20listesi.png)

Bu komutu kullanarak Django projesi geliştirirken kullanabileceğimiz komutlar ekranımıza geliyor. Bunlardan startproject diyerek yeni bir proje oluşturalım.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2014.%20Olu%C5%9Fturulan%20dosyan%C4%B1n%20i%C3%A7eri%C4%9Fi.png)

### Projede uygulama oluşturmak

Django-admin startproject “projeismi” diyerek projemizi oluşturduk. Bulunduğu konumu açarak içindeki manage.py dosyasını görmüş olduk.

Python manage.py startapp “uygulamaismi” komutlarıyla projemizde uygulamalar oluşturuyoruz ve uygulamalarımızı bu komutlarla beraber gelen dosyalar içinde geliştireceğiz.

Oluşturduğumuz bu uygulamaları asıl proje klasöründeki settings.py dosyasında tanıtmamız gerekir

### URL oluşturmak
Projeye gelen istekleri karşılamak için ana klasör içindeki urls.py dosyası içinde url’lerimizi tanımlıyoruz.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2018.%20URL%20tan%C4%B1mlamalar%C4%B1.png)

Örnek olarak görseldeki gibi tek tek karşılanması gereken istekler için url ekliyoruz. Kaydettiğimiz url’leri ilgili projelere ekliyoruz. Usercomment uygulamasına gelerek urls.py dosyası ekliyoruz. Ardından urls pattern diyerek görseldeki gibi düzenliyoruz. URL’yi kullanıcı talep edecek biz ise istenilen url’yi eşleşen view’e göndereceğiz. Ekstradan views.py dosyasına yeni metot oluşturacağız.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2019.%20View%20dosyas%C4%B1nda%20metot%20olu%C5%9Fturmak.png)

Views.py dosyasında home metodunu oluşturduktan sonra ilgili projeye template dosyası ekliyoruz. Template’nin içine de index.html diyerek ilgili url’nin front end’ine dokuyoruz. Örneğin biz aşağıdaki gibi diyelim.

Projede bunları yaptıktan sonra tekrardan asıl dosyaya gelip(formweb) oluşturduğumuz bu request’i urls.py dosyasına görseldeki gibi ekliyoruz.

### Form uygulaması yapmak

Yeni bir proje oluşturalım. Sırasıyla gerekli komutları yazalım. Virtualenv venv (sanal ortamımızı oluşturduk) ardından scripti active edelim ve projeye templates klasörünü oluşturalım. django-admin startproject core .  komutu ile projeyi başlatalım. django-admin startapp form diyelim. python manage.py migrate, python manage.py createproject, python manage.py createsuperuser (username=deneme, password=. diyerek oluşturdum.), python manage.py runserver, komutuyla serveri ayağı kaldıralım. Templates klasörüne index.html diyerek gerekli formları yazacağımız dosyayı oluşturalım. Body taglerinin içerisine bootstrapleri yazalım.

CSS ve JS komutlarını da index.html’ye ekledikten sonra projemizin settings.py dosyasından INSTALLED_APPS bölümüne ‘form’ uygulamamızı ekleyelim. Templates bölümünde ise ‘DIRS’ı görseldeki gibi yazalım ve os’u import edelim.

Bir form oluşturabilmek için önce onun modelini oluşturmamız gerekiyor. Models.py içine classımızı oluşturuyoruz.

Oluşturduğumuz modeli makemigration ediyoruz. Fakat burada oluşturduğumuz modeli algılamadı ve ‘No changes detected’ output’unu aldık.

Python manage.py migrate diyerek modelimizi migrate ediyoruz. Ardından tekrar runserver diyerek çalıştıralım. Form klasörünün içine forms.py adlı bir dosya oluşturalım. ModelForm’u import edelim Daha sonra yazdığımız modeli import edelim. Ardından models’deki gibi bir sınıf tanımlıyoruz.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2026.%20Form%20olu%C5%9Fturma.png)

Admin dosyasına contactFormModel’i import edelim ve görünmesini istediğimiz alanlar için bir sınıf tanımlayalım.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2027.%20Admin%20dosyas%C4%B1n%C4%B1n%20i%C3%A7eri%C4%9Fi.png)

Hemen ardından views.py’dan formu göndermemiz gerekiyor.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2028.%20Formun%20g%C3%B6nderimi.png)

Bunun ardından yeni bir sayfa dönmeyecek ve yine aynı sayfayı dönmesini sağlayacak.

Ardından index.html’de formu tanımlamamız gerekiyor. Django’da güvenliği sağlamak amacıyla ‘{% csrf_token %}’ kullanmadığımız sürece bir veri gönderemiyoruz.

Vscode kullanırken oluşturduğumuz sanal ortam gerekli komutları yazmamıza rağmen çalışmıyordu. Windows komut isteminden manuel olarak proje klasörümüzü açıp oradan “venv\Scripts\activate” diyerek sanal ortamımızı aktif ettik.
![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2029.%20Sanal%20ortam%C4%B1%20manuel%20olarak%20aktif%20etmek.png)

Formları widget oluşturarak ekledik.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2030.%20Widgetlerin%20eklenmesi.png)

Ardından test ettiğimizde form url’miz post isteğini başarılı şekilde algıladı. Fakat admin panelinde GET isteğimizde http 500 internal server hatası aldık.

Hatayı araştırırken yeniden migrate işlemlerini yapınca isimlendirmeden kaynaklı bir hata yaptığımı fark ettim.

Bu hatayı ele alıp çözdükten sonra local host’da attığımız post isteklerinin veri tabanına kaydedilmediğini gördüm. POST url’miz çalışıyor fakat admin panelinde verileri ekleyemiyorduk. Bunun sebebinin ise django’nun case sensitive olmasından kaynaklı olduğunu fark ettim.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2033.%20Versiyona%20ba%C4%9Fl%C4%B1%20olarak%20post%20iste%C4%9Finin%20fark%C4%B1.png)

Görseldeki bölümlerde “POST” yerine “post” yazdığımızdan ötürü hata almıştık. Hemen ardından test ettik ve başarılı şekilde admin panelinde attığımız post isteklerini görebildik.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2034.%20Veri%20taban%C4%B1%20%C3%A7%C4%B1kt%C4%B1s%C4%B1.png)

Ardından ara yüzümüze 2 tane derecelendirme butonu eklememiz gerekti. Sorgu yapıp bunu 5 puan üzerinden puanlamak için gerekli komutları kodumuza ekledik. Front-end’e aşağıdaki görsel gibi oldu.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2035.%20Html%20g%C3%B6r%C3%BCn%C3%BCm%C3%BC.png)

CSS ile birlikte button’larımızı aşağıdaki hale getirdik.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2036.%20CSS%20kullanarak%20derecelendirmenin%20g%C3%B6r%C3%BCn%C3%BCm%C3%BC.png)

localhost’da front-end bu hale geldikten sonra girilen verileri submit ederek şu anlık django tarafından gelen admin panelindeki veri tabanına kaydetmeyi denedik. Fakat burada hem POST isteğimizde hem de admin panelinden erişilen GET isteğinde hatalar aldık. Bu hataların sebebini araştırınca, contactFormModel class’ındaki puanlama sistemi için oluşturduğumuz değerlere eksik parametre girdiğimizi fark ettik. Bunu da araştırmalar sonucu ve benzer hataları yaşayanların çözümlerine bakarak aşağıdaki görsel şeklinde değiştirdik(unique=True, null=True ekledik). Ardından yeniden makemigrations ve migrate işlemlerini yaptık.

## MariaDB
MariaDB, verileri ve bunlara erişim yolunu yöneten açık kaynaklı bir veri tabanı yönetim sistemidir. Oracle’nin Sun Microsystems'i satın almasından sonra oluşturulan MySQL'in bir çatalıdır ve bu yazılımın ana hedeflerinden biri mysql ile uyumlu olmaktır ama performansa odaklanan yeni özellikler de aynı zamanda eklenmektir. MariaDB, tamamen ücretsiz ve açık kaynak olması ve MySQL ile uyumlu olması nedeniyle pazar payını hızla artırmaktadır.

### MariaDB Kurulumu
MariaDB’nin kendi sitesi üzerinden MariaDB Server 10.11.0 Alpha sürümünü indirdik. Root password’u ‘yusuf’ şeklinde girdim. Daha önceden bilgisayarımda ‘3306’ portunu MySQL üzerinde kullandığımdan ötürü default şeklinde ayarlı gelen 3306 portunu 3307 şeklinde değiştirdim. Ardından MariaDB için DBeaver editörünü kurduk.

### Verileri MariaDB’ye Kaydetmek
MariaDB bağlantısı için mariadb python kütüphanesini kullanacağız. Bağlantıyı verilen komutu kullanarak kuralım: pip install mariadb veya pip3.9 install mariadb

Daha önceden settings dosyamızdaki Database ayarlarını sqlite3’den MySQL’e aşağıdaki şekilde değiştirdik.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2040.%20MariaDB%20entegrasyonu.png)

Bu değişimlerin ardından yeniden migrate işlemlerini yapıyoruz. Bunu yaparken derleyiciden bir hata aldık mysqlclient kurulu olmasına rağmen derleyici tarafından algılanmadı. ‘pip install mysqlclient’ kodu ile VSCode’a kuralım.

Password’u ‘yusuf’ olacak şekilde admin adında bir superuser oluşturdum.

MariaDB kullanırken önceden contactFormModel class’ımızdan oluşturduğumuz Model sınıfımız django’nun kendi veri tabanı için sorunsuz çalışmaktaydı. Fakat manuel olarak oluşturduğumuz kendi veri tabanımızda bazı sorunlar yaşadık ve model sınıfımızı aşağıdaki görseldeki şekline getirerek oluşan sorunları çözdük.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2042.%20Uygun%20database%20ayarlar%C4%B1n%C4%B1n%20yap%C4%B1lmas%C4%B1.png)

Veri tabanı bağlantımızı tekrardan kontrol ettikten sonra herhangi bir sorun olmayınca aşağıdaki görüntüyü elde ettik. Bağlantıyı başarılı şekilde gerçekleştirdik.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2043.%20Veri%20taban%C4%B1%20g%C3%B6r%C3%BCn%C3%BCm%C3%BC.png)

Runserver deyip form üzerinden submit ettik. Herhangi bir bug olmasına karşın birkaç veri daha ekledikten sonra veri tabanımız görseldeki gibi oldu ve test aşamalarını sorunsuz geçti.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2044.%20Olu%C5%9Fturulan%20veritaban%C4%B1.png)

Formlarımızı oluşturduğumuz tarihleri de belirli formatlar ile yine veri tabanına ekledik.
Web arayüzündeki ‘Ad Soyad’ ve ‘e-mail’ bölmelerini zorunlu hale required diyerek getirdik.
Web Sayfamıza girilen geri bildirimlerin gönder butonunun altında listelemek istedik bu durumda ilk önce ön yüzümüze aşağıdaki gibi ekledik.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2047.%20Tablolar%C4%B1%20olu%C5%9Fturmak%20ve%20JavaScript%20ile%20verileri%20%C3%A7ekmek.png)

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2048.%20Veri%20tablosunun%20olu%C5%9Fmas%C4%B1.png)

Backend tarafından veri tabanındaki verileri çekme işlemini yapalım.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2049.%20Verileri%20html%E2%80%99ye%20d%C3%B6nd%C3%BCrmek.png)

Farklı bir url üzerinden veriyi sorunsuz çekip çekemeyeceğimizi test ettim.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2050.%20Test%20a%C5%9Famalar%C4%B1.png)

Veri tabanımız web sayfamıza gelmekte fakat aynı url üzerinden hem form gönderme işlemi hem de veri tabanını listeleme işlemini şu anlık yapamadık.
Jquery ve bootstrap CDN’lerini upload etmiştik. Şimdi ise sort işlemleri için datatable cdn kullanacağız.
Konfigürasyon ayarlarını da yaptıktan sonra web sayfamız aşağıdaki şekilde gözükmeye başladı.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2052.%20Uygun%20de%C4%9Fi%C5%9Fikliklerin%20ard%C4%B1ndan%20web%20sayfas%C4%B1%20g%C3%B6r%C3%BCn%C3%BCm%C3%BC.png)

Sort işlemleri ve search işlemi sorunsuz çalışmakta. Form üzerinden isim ve email’i zorunlu tutmuştuk ‘required’ ile şu an ise geri bildirim için en az bir belirteç bulunmasını istiyoruz. Aksi halde formun veri tabanına ulaşmasını istemiyoruz. Yani en az bir mesaj veya 2 puanlama girmeli veya hem mesaj hem de puanlamaları girebilmeli ama sadece isim ad soyad ve email ile girilen formları kabul etmemeli. Bunu da clean metodu ile yapıyoruz.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2053.%20Clean%20metodu%20olu%C5%9Fturmak.png)

Girilen eksik post isteği sonucunda aşağıdaki hata ekranını alabiliyoruz.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2054.%20Hata%20ekran%C4%B1.png)

Ardından daha önceden test ettiğimiz veri tabanı listeleme fonksiyonunu index metodumuzda gerekli kısmı değiştirerek return ediyoruz.

Bunun ardından web sayfamız hem form işlemi isteği atabiliyor hem de aşağıda veri tabanını listeleyip duruma göre sort işlemi yapıyor.
Datatable ile oluşturduğumuz tablomuz İngilizceydi ve kendi formumuz ile uyuşmayan bir dil farklılığına sahipti. Dokümanları araştırmamız sonucunda uygun değişiklikleri javascript ile yaptık ve tablomuzda kullandığımız dil yapısını Türkçe kelimeler ile değiştirdik.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2056.%20Yap%C4%B1y%C4%B1%20uygun%20hale%20getirmek.png)

Veri tabanımıza localhost tarafından 11 form gönderdik ve onları ilk önce Ad soyad şeklinde sıraladık.

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/%C5%9Eekil%2057.%20Veri%20taban%C4%B1%20g%C3%B6r%C3%BCn%C3%BCm%C3%BC.png)

![alt text](https://github.com/yusufseyitoglu/Form_Web_App_With_Django/blob/main/png%20for%20md/Form%20sayfas%C4%B1n%C4%B1n%20Datatable%20b%C3%B6l%C3%BCm%C3%BC.png)


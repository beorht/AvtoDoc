#### Mavzusi № 3: Tahdid turlari: maxfiylikka, yaxlitlikka, mavjudlikka hujumlar. Tarmoqlardagi zaifliklarni aniqlash. Taklif qilingan axborot tizimi uchun tahdid va hujumchi modelini yaratish.

Ta’limiy materialning asosiy bo‘limlari:
1.  Maxfiylik, Yaxlitlik va Mavjudlik (CIA triada) tushunchasi va ularga qilingan hujum turlari
2.  Tarmoqlardagi zaifliklarni aniqlash metodologiyasi
3.  Tahdid modelini yaratish tamoyillari
4.  Hujumchi modelini yaratish tamoyillari
5.  Taklif qilingan axborot tizimi uchun tahdid va hujumchi modellarini shakllantirish bo‘yicha amaliy yondashuv

---

Ta’limiy material matni:

Axborot xavfsizligi har qanday tashkilotning muvaffaqiyatli faoliyatini ta'minlashda hal qiluvchi ahamiyatga ega. Uning asosiy ustunlari bo'lmish Maxfiylik (Confidentiality), Yaxlitlik (Integrity) va Mavjudlik (Availability) tushunchalarini tushunish va ularga qilingan hujum turlarini bilish tizimlarni himoya qilish uchun muhimdir.

### 1. Maxfiylik, Yaxlitlik va Mavjudlik (CIA triada) tushunchasi va ularga qilingan hujum turlari

Axborot xavfsizligining asosini CIA triada tashkil etadi:

*   **Maxfiylik (Confidentiality):** Bu axborotga faqatgina unga kirishga ruxsat berilgan shaxslar, jarayonlar yoki tizimlar kira olishini ta'minlashdir. Boshqacha aytganda, ruxsat etilmagan tomonlarning maxfiy ma'lumotlarga kirishining oldini olish.
    *   **Maxfiylikka qilingan hujum turlari:**
        *   **Ruxsatsiz kirish (Unauthorized Access):** Parollarni buzish, fishing (firibgarlik), kalitlarni taxmin qilish orqali tizimga kirish.
        *   **Tinglash (Eavesdropping):** Tarmoqdagi ma'lumotlar oqimini ushlab olish va tahlil qilish (sniffing).
        *   **Kriptoanaliz (Cryptanalysis):** Shifrlangan ma'lumotlarni shifrini ochishga urinish.
        *   **Yelkalash (Shoulder Surfing):** Kompyuter ekraniga yashirincha qarab, maxfiy ma'lumotlarni o'g'irlash.
        *   **Ma'lumotlar sizishi (Data Leakage):** Ma'lumotlarning tasodifan yoki qasddan tashqi muhitga chiqib ketishi (masalan, noto'g'ri konfiguratsiya qilingan bulut xizmatlari orqali).
    *   **Misol:** Xodimlarning shaxsiy ma'lumotlari saqlangan serverga ruxsatsiz kirish va bu ma'lumotlarni o'g'irlash.

*   **Yaxlitlik (Integrity):** Bu axborotning to'g'riligi, aniqligi va butunligini saqlashni anglatadi. Ya'ni, ma'lumotlar ruxsatsiz o'zgartirilmagan, o'chirilmagan yoki buzilmagan bo'lishi kerak.
    *   **Yaxlitlikka qilingan hujum turlari:**
        *   **Ma'lumotlarni o'zgartirish (Data Tampering):** Bazadagi yozuvlarni qasddan o'zgartirish.
        *   **Ruxsatsiz o'zgartirish (Unauthorized Modification):** Tizim fayllarini yoki dastur kodini buzish.
        *   **Manba soxtalashtirilishi (Source Spoofing):** Ma'lumotlarning kelib chiqish manbasini soxtalashtirish.
        *   **Viruslar va troyanlar (Viruses and Trojans):** Tizimga kirib, fayllarni buzish yoki o'zgartirish.
        *   **Ma'lumotlarni jo'natish (Repudiation):** Tranzaksiyaning qatnashchisi o'z harakatini inkor etishi, chunki uning yaxlitligi buzilgan.
    *   **Misol:** Bank hisobvaraqlaridagi pul miqdorini ruxsatsiz o'zgartirish yoki veb-sayt tarkibini buzish (deface).

*   **Mavjudlik (Availability):** Bu axborot tizimlari va ma'lumotlarning foydalanuvchilar tomonidan kerakli paytda foydalanish uchun doimiy ravishda mavjud bo'lishini ta'minlash.
    *   **Mavjudlikka qilingan hujum turlari:**
        *   **Xizmatdan voz kechish (DoS/DDoS - Denial of Service/Distributed Denial of Service) hujumlari:** Server yoki tarmoq resurslarini haddan tashqari yuklab, ularni ishdan chiqarish.
        *   **Resurslarni tugatish (Resource Exhaustion):** Tizim resurslarini (CPU, xotira, disk maydoni) haddan tashqari ishlatish.
        *   **Apparat nosozliklari (Hardware Failures):** Jismoniy shikastlanishlar yoki komponentlarning ishdan chiqishi.
        *   **Tizim xatolari (System Crashes):** Dasturiy ta'minotdagi xatolar tufayli tizimning ishdan chiqishi.
        *   **Tabiiy ofatlar (Natural Disasters):** Elektr uzilishlari, yong'inlar, suv toshqinlari.
    *   **Misol:** Onlayn-do'kon veb-saytiga DDoS hujum uyushtirilib, xaridorlar mahsulot sotib ololmay qolishi.

### 2. Tarmoqlardagi zaifliklarni aniqlash metodologiyasi

**Zaiflik (Vulnerability)** – bu tizim, tarmoq, dasturiy ta'minot yoki jarayondagi kamchilik bo'lib, undan tahdid agenti (hujumchi) axborot xavfsizligini buzish uchun foydalanishi mumkin.

**Tarmoqlardagi keng tarqalgan zaifliklar:**
*   **Dasturiy ta'minotdagi xatolar (Software Bugs):** Xavfsizlik bo'shliqlari, buffer overflow, SQL injection, XSS.
*   **Noto'g'ri konfiguratsiyalar (Misconfigurations):** Standart parollar, ochiq portlar, noto'g'ri o'rnatilgan ruxsatnomalar, keraksiz xizmatlar.
*   **Yangilanmagan tizimlar (Unpatched Systems):** Dasturiy ta'minot va operatsion tizimlardagi ma'lum xavfsizlik bo'shliqlarini tuzatuvchi yamalarning o'rnatilmaganligi.
*   **Kuchsiz avtorizatsiya va autentifikatsiya (Weak Authentication/Authorization):** Oson topiladigan parollar, ikki faktorli autentifikatsiyaning yo'qligi.
*   **Jismoniy xavfsizlik kamchiliklari (Physical Security Weaknesses):** Server xonalariga ruxsatsiz kirish imkoniyati.
*   **Ijtimoiy muhandislik (Social Engineering):** Xodimlarni aldab ma'lumot olish.

**Zaifliklarni aniqlash metodologiyasi:**
1.  **Vulnerability Scanning (Zaifliklarni skanerlash):** Maxsus dasturiy vositalar (Nessus, OpenVAS, Qualys) yordamida tarmoq, serverlar va ilovalardagi ma'lum zaifliklarni avtomatik ravishda aniqlash.
2.  **Penetration Testing (Kirib borish testi):** Ruxsat berilgan "hujumchilar" (penetration testerlar) tomonidan tizimga real hujumlarni simulyatsiya qilish orqali zaifliklarni topish va ulardan foydalanishga urinish. Bu chuqurroq tahlilni ta'minlaydi.
3.  **Xavfsizlik auditlari (Security Audits):** Tashkilotning xavfsizlik siyosatlari, konfiguratsiyalari va jarayonlarini belgilangan standartlarga muvofiqligini tekshirish.
4.  **Kod tahlili (Code Review):** Dasturiy ta'minot kodini xavfsizlik bo'shliqlari nuqtai nazaridan qo'lda yoki avtomatik tahlil qilish.
5.  **Risk tahlili (Risk Analysis):** Aniqlangan zaifliklarning axborot tizimiga ta'sirini baholash va ularning yuzaga kelish ehtimolini hisoblash.
6.  **Xavfsizlik siyosatlarini ko'rib chiqish (Policy Review):** Tashkilotning xavfsizlik siyosatlari va protseduralarining samaradorligini baholash.

### 3. Tahdid modelini yaratish tamoyillari

**Tahdid modeli (Threat Model)** – bu axborot tizimining xavfsizlik zaifliklarini aniqlash, ularni potensial tahdidlar va hujumchilar bilan bog'lash hamda xavflarni minimallashtirish uchun chora-tadbirlarni ishlab chiqish jarayoni. U tizimning qaysi qismlari xavf ostida ekanligini, qanday tahdidlar mavjudligini va ularni qanday kamaytirish mumkinligini tushunishga yordam beradi.

**Tahdid modelini yaratish bosqichlari (STRIDE yondashuvi):**
1.  **Tizimni tasvirlash (Identify Assets/System Description):** Himaoya qilinadigan asosiy aktivlar (ma'lumotlar, dasturlar, uskunalar, xizmatlar) va ularning o'zaro aloqalari, ma'lumotlar oqimini aniqlash. Tizimning arxitekturasi, komponentlari, foydalanuvchilar va ma'lumotlar saqlanadigan joylarni chizma yoki diagramma ko'rinishida tasvirlash.
2.  **Tahdidlarni aniqlash (Identify Threats):** Har bir aktiv yoki jarayon uchun potensial tahdidlarni aniqlash. Buning uchun STRIDE modelidan foydalanish mumkin:
    *   **S**poofing (soxtalashtirish): Hujumchi boshqa shaxs yoki tizim sifatida o'zini ko'rsatadi. (Maxfiylik, Yaxlitlik)
    *   **T**ampering (o'zgartirish): Ma'lumotlarning ruxsatsiz o'zgartirilishi. (Yaxlitlik)
    *   **R**epudiation (inkor qilish): Hujumchi o'z harakatlarini inkor etadi. (Yaxlitlik)
    *   **I**nformation Disclosure (ma'lumotlarni oshkor qilish): Maxfiy ma'lumotlarning ruxsatsiz ochilishi. (Maxfiylik)
    *   **D**enial of Service (xizmatdan voz kechish): Tizimning mavjud emasligi. (Mavjudlik)
    *   **E**levation of Privilege (imtiyozlarni oshirish): Ruxsatsiz foydalanuvchi yuqori darajadagi imtiyozlarni oladi. (Maxfiylik, Yaxlitlik, Mavjudlik)
3.  **Zaifliklarni aniqlash (Identify Vulnerabilities):** Aniqlangan tahdidlarga olib kelishi mumkin bo'lgan tizimdagi zaifliklar va kamchiliklarni topish.
4.  **Risklarni baholash (Assess Risks):** Har bir tahdidning yuzaga kelish ehtimoli va uning tizimga ta'sirini (xarajat, obro'-e'tiborga zarar, huquqiy oqibatlar) baholash.
5.  **Kamaytirish choralarini ko'rish (Mitigate Threats):** Aniqlangan tahdidlar va xavflarni bartaraf etish yoki kamaytirish bo'yicha chora-tadbirlarni ishlab chiqish va amalga oshirish. Bu texnik (shifrlash, xavfsizlik devorlari), tashkiliy (siyosatlar, treninglar) yoki jismoniy (kirish nazorati) choralar bo'lishi mumkin.

### 4. Hujumchi modelini yaratish tamoyillari

**Hujumchi modeli (Attacker Model)** – bu axborot tizimiga potentsial tahdid soluvchi shaxslar yoki guruhlarning motivatsiyalari, imkoniyatlari, resurslari va potentsial hujum usullarini tasvirlashdir. Bu model tahdid modelini to'ldiradi va himoya strategiyalarini ishlab chiqishda yordam beradi.

**Hujumchi modelini yaratishda quyidagilar hisobga olinadi:**
1.  **Hujumchi turlari (Types of Attackers):**
    *   **Ichki hujumchilar (Insider Threats):** Noto'g'ri ishlarni qiladigan xodimlar, sobiq xodimlar, ishonchsiz pudratchilar.
    *   **Tashqi hujumchilar (External Threats):**
        *   **Hakerlar (Hackers):** Qasddan buzuvchilar (black-hat), etika qoidalari asosida ishlaydiganlar (white-hat), ikkalasi aralash (grey-hat).
        *   **Xaker guruhlari (Organized Crime/State-sponsored Groups):** Katta resurslarga ega, yuqori malakali guruhlar.
        *   **Haktivistlar (Hacktivists):** Ijtimoiy yoki siyosiy sabablarga ko'ra hujum qiluvchilar.
        *   **Raqubatchilar (Competitors):** Raqobatbardosh ma'lumotlarni olishga intiluvchilar.
        *   **Tasodifiy hujumchilar (Script Kiddies):** Tayyor vositalardan foydalanuvchi, ko'pincha jiddiy maqsadsiz shaxslar.
2.  **Motivatsiyalar (Motivations):** Hujumchi nima uchun hujum qilmoqchi?
    *   Moliyaviy foyda (pul, kriptovalyuta)
    *   Ma'lumot o'g'irlash (intellektual mulk, shaxsiy ma'lumotlar)
    *   Obro'sizlantirish (veb-sayt deface)
    *   Siyosiy/ijtimoiy sabablar (haktivizm)
    *   O'zini namoyon etish/kuchini sinab ko'rish
    *   Sabotaj
    *   Jazodan qochish
3.  **Imkoniyatlar (Capabilities):** Hujumchining texnik bilimlari, tajribasi va mahorati.
    *   Past (faqat tayyor skriptlardan foydalanish)
    *   O'rta (ma'lum vositalarni tushunish va moslashtirish)
    *   Yuqori (murakkab hujum mexanizmlarini ishlab chiqish, nol kunlik zaifliklardan foydalanish)
4.  **Resurslar (Resources):** Hujumchi ega bo'lgan va hujum uchun ishlatishi mumkin bo'lgan vositalar.
    *   Moliyaviy resurslar (hujum uchun uskunalar, dasturiy ta'minot sotib olish)
    *   Vaqt (hujumga tayyorgarlik va amalga oshirishga ketadigan vaqt)
    *   Inson resurslari (guruh a'zolari soni va malakasi)
    *   Texnik vositalar (kompyuter quvvati, tarmoq ulanishi, nol kunlik zaifliklar)
5.  **Hujum vektorlari (Attack Vectors):** Hujumchi tizimga qanday yo'llar orqali kirishi mumkinligi.
    *   Tarmoq orqali (portlar, protokollar)
    *   Veb-ilovalar orqali (SQLi, XSS, SSRF)
    *   Foydalanuvchilar orqali (fishing, ijtimoiy muhandislik)
    *   Jismoniy kirish orqali (USB, server xonasiga kirish)
    *   Bulut xizmatlari orqali

### 5. Taklif qilingan axborot tizimi uchun tahdid va hujumchi modellarini shakllantirish bo‘yicha amaliy yondashuv

Faraz qilaylik, biz "Onlayn Talabalar Ma'lumotlar Bazasini Boshqarish Tizimi" (OTMBBT) uchun tahdid va hujumchi modelini yaratishimiz kerak.

**1. Tizimni tasvirlash (OTMBBT):**
*   **Asosiy Aktivlar:** Talabalarning shaxsiy ma'lumotlari (ism, familiya, tug'ilgan sana, ID), o'quv natijalari (baholar, kurslar), ota-ona ma'lumotlari, to'lov ma'lumotlari.
*   **Foydalanuvchilar:** Talabalar, o'qituvchilar, dekanat xodimlari, administratorlar.
*   **Komponentlar:** Veb-interfeys, ilova serveri, ma'lumotlar bazasi serveri, autentifikatsiya xizmati, fayl saqlash (rasmlar, hujjatlar).
*   **Ma'lumotlar oqimi:** Foydalanuvchi -> Veb-interfeys -> Ilova serveri -> Ma'lumotlar bazasi.

**2. Tahdid modelini yaratish (OTMBBT uchun STRIDE):**

*   **S (Spoofing - soxtalashtirish):**
    *   *Tahdid:* Talaba boshqa talaba sifatida tizimga kirishi; O'qituvchi boshqa o'qituvchi sifatida baholarni o'zgartirishi; Fishing hujumlari orqali foydalanuvchi ma'lumotlarini o'g'irlash.
    *   *Zaifliklar:* Kuchsiz parollar, ikki faktorli autentifikatsiyaning yo'qligi, sessiya boshqaruvi zaifliklari.
    *   *Choralar:* Kuchli parol siyosati, 2FA, sessiya tokenlarini himoyalash, fishing haqida foydalanuvchilarni o'rgatish.

*   **T (Tampering - o'zgartirish):**
    *   *Tahdid:* Talaba o'z baholarini o'zgartirishi; O'qituvchi boshqa talabaning ma'lumotlarini noto'g'ri o'zgartirishi; Administrator tizim konfiguratsiyasini buzishi.
    *   *Zaifliklar:* Noto'g'ri ruxsatnomalar (ACL), SQL Injection, ma'lumotlar bazasiga ruxsatsiz kirish.
    *   *Choralar:* Foydalanuvchi rollari va huquqlarini to'g'ri boshqarish, barcha kirish nuqtalarida ma'lumotlarni validatsiya qilish, SQL Injection'dan himoyalanish (parametrized queries), ma'lumotlar bazasining zaxira nusxalari.

*   **R (Repudiation - inkor qilish):**
    *   *Tahdid:* O'qituvchi bergan bahoni o'zi bermaganligini da'vo qilishi; Talaba to'lovni amalga oshirmaganligini da'vo qilishi.
    *   *Zaifliklar:* Harakatlarni qayd etish (logging) tizimining yo'qligi yoki yetarli emasligi.
    *   *Choralar:* Har bir muhim harakatni (login, baho qo'yish, ma'lumot o'zgartirish) vaqt tamg'asi bilan jurnalga yozib borish, jurnal fayllarini himoyalash.

*   **I (Information Disclosure - ma'lumotlarni oshkor qilish):**
    *   *Tahdid:* Ruxsatsiz shaxslar talabalarning shaxsiy ma'lumotlariga kirishi; Ma'lumotlar bazasidan umumiy ma'lumotlarni ommaga oshkor qilish.
    *   *Zaifliklar:* Shifrlanmagan aloqa (HTTP o'rniga HTTPS), ma'lumotlar bazasining himoyalanmaganligi, noto'g'ri konfiguratsiya qilingan serverlar.
    *   *Choralar:* Barcha aloqa kanallarini (SSL/TLS) shifrlash, ma'lumotlar bazasini shifrlash (at rest and in transit), server konfiguratsiyasini mustahkamlash, ma'lumotlarga kirish nazoratini kuchaytirish.

*   **D (Denial of Service - xizmatdan voz kechish):**
    *   *Tahdid:* Talabalar imtihon paytida tizimga kira olmasligi; Xizmat serveriga DDoS hujumi.
    *   *Zaifliklar:* Tarmoq resurslarining cheklanganligi, DoS hujumlariga qarshi himoyaning yo'qligi.
    *   *Choralar:* Tarmoq monitoringi, DDoS himoya vositalari (WAF, CDN), resurslarni masshtablash imkoniyati, yuklamani balanslash.

*   **E (Elevation of Privilege - imtiyozlarni oshirish):**
    *   *Tahdid:* Oddiy talaba administratsiya huquqlarini olishga urinishi; Veb-ilova zaifligi orqali tizimga root huquqlarini olish.
    *   *Zaifliklar:* Dasturiy ta'minotdagi bo'shliqlar, noto'g'ri konfiguratsiya qilingan operatsion tizim, zaif kirish nuqtalari.
    *   *Choralar:* Dasturiy ta'minotni muntazam yangilash, serverlarni mustahkamlash (hardening), eng kam imtiyoz prinsipi, kirish nuqtalarini cheklash.

**3. Hujumchi modelini yaratish (OTMBBT uchun):**

*   **Hujumchi turlari:**
    *   **Ichki:** Norozi talaba/xodim (baholarini o'zgartirish, ma'lumot o'g'irlash), administrator (ma'lumotlarni sotish).
    *   **Tashqi:** Haktivistlar (universitet obro'sini tushirish), raqobatchi universitet (talaba ma'lumotlarini o'g'irlash), yovuz hakerlar (moliyaviy foyda, ma'lumotlarni sotish).

*   **Motivatsiyalar:**
    *   Baholarini o'zgartirish, akademik firibgarlik (talabalar).
    *   Shaxsiy ma'lumotlarni o'g'irlash va sotish.
    *   Universitet obro'sini tushirish, siyosiy norozilik.
    *   Moliyaviy foyda olish (to'lov ma'lumotlari).

*   **Imkoniyatlar:**
    *   **Past:** Skript kiddies (tayyor DoS skriptlar, fishing email templates).
    *   **O'rta:** Web ilova zaifliklarini biladigan, SQL Injection yoki XSS hujumlarini amalga oshira oladigan shaxslar.
    *   **Yuqori:** Nol kunlik zaifliklarni topa oladigan yoki murakkab ijtimoiy muhandislik sxemalarini ishlab chiqa oladigan professionallar.

*   **Resurslar:**
    *   **Past:** Shaxsiy kompyuter, bepul VPN, ochiq manbali vositalar.
    *   **O'rta:** Bir nechta kompyuter, oddiy bulut xizmatlari, premium vositalar.
    *   **Yuqori:** Botnetlar, maxsus dasturiy ta'minot, jamoaviy ish, katta moliyaviy resurslar.

*   **Hujum vektorlari:**
    *   Veb-ilova zaifliklari (SQLi, XSS, RCE, Broken Auth).
    *   Tarmoq zaifliklari (ochiq portlar, noto'g'ri firewall qoidalari).
    *   Ijtimoiy muhandislik (fishing email, spear phishing).
    *   Kuchsiz parollar, lug'at hujumlari.
    *   Jismoniy kirish (server xonasiga ruxsatsiz kirish).

**Xulosa:**

Tahdid va hujumchi modellarini yaratish axborot tizimining zaif tomonlarini strategik ravishda tushunish va ularga qarshi samarali himoya choralarini ishlab chiqish uchun muhim vositadir. Bu jarayon tizimni loyihalashning dastlabki bosqichlaridanoq amalga oshirilishi va tizim rivojlanishi bilan muntazam ravishda yangilanib turishi lozim. Shundagina, maxfiylik, yaxlitlik va mavjudlik tamoyillari asosida qurilgan mustahkam axborot xavfsizligi tizimiga erishish mumkin.
#### Mavzusi № 2: OSI modeli. IEEE Project 802 modeli, OSI modelining kengaytmasi. Drayverlar va tarmoq dasturiy taʼminoti, tarmoq adapteri drayveri. Paket tuzilishi, asosiy komponentlar. Protokollar. Kommutatsiya.

Ta’limiy materialning asosiy bo‘limlari:
1.  OSI modeli.
2.  IEEE Project 802 modeli va uning OSI modeliga kengaytmasi.
3.  Drayverlar va tarmoq dasturiy taʼminoti, tarmoq adapteri drayveri.
4.  Paket tuzilishi va asosiy komponentlari.
5.  Protokollar va Kommutatsiya.

---

Ta’limiy material matni:

### 1. OSI modeli

**OSI (Open Systems Interconnection – Ochiq tizimlarni o‘zaro bog‘lash)** modeli – bu turli xil kompyuter tizimlari orasida aloqa o‘rnatish jarayonini standartlashtirish uchun ishlab chiqilgan nazariy modeldir. U 1980-yillarda Xalqaro Standartlashtirish Tashkiloti (ISO) tomonidan yaratilgan bo‘lib, tarmoq funksiyalarini etti mustaqil qatlamga ajratadi. Har bir qatlam o‘ziga xos vazifaga ega va faqat o‘zining pastki qatlamidan xizmat oladi hamda yuqori qatlamiga xizmat ko‘rsatadi.

OSI modelining asosiy maqsadi:
*   Turli ishlab chiqaruvchilarning apparat va dasturiy ta’minotlari o‘rtasida o‘zaro ishlash qobiliyatini ta’minlash.
*   Tarmoq aloqasining murakkab jarayonini soddalashtirish va tushunishni osonlashtirish.
*   Tarmoq muammolarini aniqlash va bartaraf etishni osonlashtirish.

**OSI modelining etti qatlami:**

1.  **Fizik qatlam (Physical Layer – 1-qatlam):** Bu qatlam ma’lumotlarni uzatishning jismoniy vositalari (kabel, optik tolali kabel, simsiz aloqa) va ularni uzatish usullari (elektr signallari, yorug‘lik impulslari, radio to‘lqinlar) bilan shug‘ullanadi. U ma’lumotlarni bitlar (0 va 1) ko‘rinishida uzatadi.
    *   *Qurilmalar:* Hub, repeater, kabel.
    *   *Vazifalar:* Bitlarni uzatish, voltaj darajalari, kabellar turlari va ulagichlari.

2.  **Kanalli qatlam (Data Link Layer – 2-qatlam):** Bu qatlam jismoniy aloqa kanali orqali xatolarsiz ma’lumot uzatishni ta’minlaydi. U ma’lumotlarni kadrlar (frames)ga bo‘ladi, manzil (MAC-manzil) qo‘shadi va xatolarni aniqlash/tuzatish mexanizmlariga ega. U ikki kichik qatlamga bo‘linadi:
    *   **Mantiqiy aloqani boshqarish (Logical Link Control – LLC):** Tarmoq qatlamidan ma’lumot olib, uni freymga joylaydi va xatolarni boshqarishni ta’minlaydi.
    *   **Mediaga kirishni boshqarish (Media Access Control – MAC):** Jismoniy muhitga kirishni boshqaradi, manzilni aniqlaydi (MAC-manzil) va freymlarni uzatishni amalga oshiradi.
    *   *Qurilmalar:* Switch, bridge.
    *   *Vazifalar:* Freymlarni shakllantirish, MAC-manzillash, xatolarni aniqlash, oqimni boshqarish.

3.  **Tarmoq qatlami (Network Layer – 3-qatlam):** Bu qatlam turli xil tarmoqlar o‘rtasida (inter-network) ma’lumotlarni marshrutlash (routing) va logik manzillash (IP-manzil) bilan shug‘ullanadi. U ma’lumotlarni paketlarga bo‘ladi va ularni manbadan manzilga yetkazib berish uchun eng yaxshi yo‘lni aniqlaydi.
    *   *Qurilmalar:* Router, Layer 3 switch.
    *   *Vazifalar:* IP-manzillash, marshrutlash, paketlarni parchalash va yig‘ish.

4.  **Transport qatlami (Transport Layer – 4-qatlam):** Bu qatlam butun ulanish bo‘ylab ma’lumotlarning ishonchli va to‘g‘ri yetkazilishini ta’minlaydi. U segmentatsiyani (ma’lumotni segmentlarga bo‘lish), oqimni boshqarishni, xatolarni tuzatishni va port manzillashni (TCP/UDP portlari) amalga oshiradi.
    *   *Protokollar:* TCP (Transmission Control Protocol – ishonchli, ulanishga asoslangan), UDP (User Datagram Protocol – tezkor, ulanishsiz).
    *   *Vazifalar:* Segmentatsiyalash, xatolarni tuzatish, oqimni boshqarish, port manzillash.

5.  **Sessiya qatlami (Session Layer – 5-qatlam):** Bu qatlam turli qurilmalar orasida aloqa sessiyasini o‘rnatish, boshqarish va yakunlash uchun javobgardir. U dialoglarni boshqarish (bir vaqtda yoki navbatma-navbat aloqa), sinxronizatsiya va ma’lumotlar almashinuvi tartibini belgilaydi.
    *   *Vazifalar:* Sessiya o‘rnatish/yakunlash, dialoglarni boshqarish, sinxronizatsiya.

6.  **Taqdimot qatlami (Presentation Layer – 6-qatlam):** Bu qatlam ma’lumotlarning taqdimot formatini boshqaradi. U ma’lumotlarni kodlash (ASCII, EBCDIC), dekodlash, siqish va shifrlash/deshifrlash kabi vazifalarni bajaradi, shunda turli tizimlar ularni tushunishi mumkin.
    *   *Vazifalar:* Ma’lumotlarni formatlash (kodlash/dekodlash), shifrlash/deshifrlash, siqish.

7.  **Amaliy dastur qatlami (Application Layer – 7-qatlam):** Bu qatlam foydalanuvchi ilovalariga tarmoq xizmatlaridan foydalanish imkoniyatini beradi. U bevosita foydalanuvchi dasturlari (brauzerlar, elektron pochta mijozlari) bilan o‘zaro aloqa qiladi va ularga tarmoq orqali ma’lumot almashish imkoniyatini yaratadi.
    *   *Protokollar:* HTTP, FTP, SMTP, DNS, SSH, Telnet.
    *   *Vazifalar:* Tarmoq xizmatlariga kirish, ma’lumotlar uzatish.

### 2. IEEE Project 802 modeli va uning OSI modeliga kengaytmasi

**IEEE (Institute of Electrical and Electronics Engineers – Elektrotexnika va Elektronika Muhandislari Instituti) Project 802** – bu lokal tarmoqlar (LAN) va shahar tarmoqlari (MAN) uchun standartlarni ishlab chiquvchi texnik standartlar seriyasidir. U OSI modelining erta versiyalari yetishmovchiliklarini bartaraf etish va jismoniy hamda kanalli qatlamlarning batafsil standartizatsiyasini ta’minlash maqsadida yaratilgan.

**IEEE 802 modelining OSI modeliga kengaytmasi:**

IEEE 802 standartlari asosan OSI modelining **Fizik qatlami (Layer 1)** va **Kanalli qatlami (Layer 2)** bilan bog‘liqdir. Eng muhim jihati shundaki, IEEE 802 kanalli qatlamni ikki kichik qatlamga ajratadi:

1.  **Mantiqiy aloqani boshqarish (Logical Link Control – LLC) – IEEE 802.2:**
    *   Bu kichik qatlam yuqori, ya’ni Tarmoq qatlamidan ma’lumotlarni qabul qiladi va pastki, ya’ni MAC qatlamiga uzatadi.
    *   U tarmoq qatlamiga qanday tarmoq protokoli (masalan, IP, IPX) ishlatilayotganini aniqlash imkonini beradi.
    *   U xatolarni tekshirish va oqimni boshqarish funksiyalarini ta’minlaydi. OSI ning Kanalli qatlamidagi LLC ga mos keladi.

2.  **Mediaga kirishni boshqarish (Media Access Control – MAC):**
    *   Bu kichik qatlam jismoniy aloqa muhitiga kirishni boshqaradi.
    *   U har bir tarmoq adapteriga noyob bo‘lgan MAC-manzilni (fizik manzil) ishlatadi.
    *   U ma’lumotlarni kadrlar (frames) ga soladi va ularni jismoniy muhit orqali uzatishni boshqaradi.

**IEEE 802 standarti misollari:**

*   **IEEE 802.3:** Ethernet standartini belgilaydi. Bu bugungi kunda eng keng tarqalgan simli LAN texnologiyasidir. U MAC qatlamida CSMA/CD (Carrier Sense Multiple Access with Collision Detection) protokolidan foydalangan.
*   **IEEE 802.11:** Wi-Fi (simsiz) tarmoqlar standartini belgilaydi. U MAC qatlamida CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance) protokolidan foydalanadi.
*   **IEEE 802.1Q:** VLAN (Virtual Local Area Network) standartini belgilaydi, bu switchlarda tarmoqlarni mantiqiy segmentlarga bo‘lish imkonini beradi.

IEEE 802 standartlari lokal tarmoq texnologiyalarining rivojlanishiga katta hissa qo‘shgan va hozirgi zamonaviy tarmoqlarning asosini tashkil etadi.

### 3. Drayverlar va tarmoq dasturiy taʼminoti, tarmoq adapteri drayveri

**Drayver (Driver)** – bu apparat qurilmasi va operatsion tizim (OS) o‘rtasidagi interfeysni ta’minlaydigan maxsus dasturiy ta’minot. Drayverlar operatsion tizimga apparat qurilmalarini boshqarish va ular bilan o‘zaro aloqa qilish imkonini beradi. Har bir apparat turi (printer, video karta, tarmoq adapteri) uchun o‘ziga xos drayver talab qilinadi.

**Tarmoq dasturiy taʼminoti** – bu tarmoq resurslaridan foydalanish, tarmoq orqali ma’lumot uzatish va qabul qilish, tarmoq xizmatlarini boshqarish uchun mo‘ljallangan barcha dasturlar majmuasi. Bu dasturiy ta’minot operatsion tizimning ichki tarmoq stekidan tortib, foydalanuvchi ilovalarigacha bo‘lishi mumkin (masalan, brauzerlar, FTP mijozlari, elektron pochta dasturlari).

**Tarmoq adapteri drayveri (Network Adapter Driver)** – bu kompyuterning tarmoq adapterini (NIC – Network Interface Card) boshqaradigan va operatsion tizimga uning funksiyalaridan foydalanish imkoniyatini beradigan drayver.
*   **Vazifasi:** Tarmoq adapteri drayveri operatsion tizimning tarmoq stekidan kelayotgan raqamli ma’lumotlarni tarmoq adapteri tushunadigan formatga o‘giradi va aksincha, tarmoq adapteridan kelayotgan elektr/yorug‘lik signallarini OS tushunadigan raqamli ma’lumotlarga aylantiradi.
*   **Mexanizmi:** U ma’lumotlarni MAC qatlamida freymlarga aylantirish, ularga MAC-manzilni qo‘shish, xatolarni tekshirish va jismoniy muhitga uzatish uchun apparatni dasturlashtirish kabi vazifalarni bajaradi. U shuningdek, tarmoqdan kelayotgan freymlarni qabul qiladi, ularning to‘g‘riligini tekshiradi va yuqori qatlamlarga (masalan, IP protokoli) uzatadi.

Drayverisiz tarmoq adapteri ishlata olmaydi va kompyuter tarmoqqa ulanolmaydi.

### 4. Paket tuzilishi va asosiy komponentlari

Tarmoqlarda ma’lumotlar **paketlar (packets)** yoki **freymlar (frames)** shaklida uzatiladi. Paket – bu uzatish uchun ajratilgan ma’lumotlarning kichik, o‘z-o‘zini saqlovchi birligidir. OSI modelining har bir qatlamida ma’lumotlarning o‘ziga xos nomi bor:
*   **Segment:** Transport qatlamida (Layer 4).
*   **Paket (Datagram):** Tarmoq qatlamida (Layer 3).
*   **Freym (Frame):** Kanalli qatlamda (Layer 2).
*   **Bit:** Fizik qatlamda (Layer 1).

Umumiy qilib aytganda, "paket" atamasi ko‘pincha har qanday tarmoq ma’lumot birligi uchun ishlatiladi.

**Paketning asosiy komponentlari (umumiy tuzilishi):**

1.  **Sarlavha (Header):** Bu paketing eng boshida joylashgan bo‘lib, paketni boshqarish va marshrutlash uchun zarur bo‘lgan barcha ma’lumotlarni o‘z ichiga oladi. Sarlavha ma’lumotlari protokoldan protokolga farq qiladi, lekin odatda quyidagilarni o‘z ichiga oladi:
    *   **Manba manzili (Source Address):** Paketni yuborgan qurilmaning manzili (masalan, MAC-manzil, IP-manzil).
    *   **Manzil manzili (Destination Address):** Paketni qabul qilishi kerak bo‘lgan qurilmaning manzili.
    *   **Protokol turi (Protocol Type):** Paketda qanday turdagi ma’lumotlar yoki keyingi qatlam protokoli borligini ko‘rsatadi (masalan, IP paket ichida TCP yoki UDP borligini ko‘rsatadi).
    *   **Paket uzunligi (Length):** Paketning umumiy uzunligi.
    *   **Identifikatorlar (Identifiers):** Paketni boshqalardan ajratib turish yoki parchalangan paket bo‘laklarini birlashtirish uchun.
    *   **Boshqarish bayroqlari (Control Flags):** Paketni qayta uzatish, sinxronizatsiya va boshqa boshqaruv funksiyalari uchun.
    *   **Xatolarni tekshirish summasi (Checksum):** Sarlavhaning o‘zi buzilmaganligini tekshirish uchun.

2.  **Ma’lumotlar (Payload / Data):** Bu paketning asosiy qismi bo‘lib, foydalanuvchi ma’lumotlari yoki yuqori qatlamlardan kelgan ma’lumotlarni o‘z ichiga oladi. Masalan, veb-sahifa matni, elektron pochta mazmuni, video fragmenti.

3.  **Treyler (Trailer / Footer):** Bu paketing oxirida joylashgan bo‘lib, asosan ma’lumotlarni xatolardan himoya qilish uchun ishlatiladi.
    *   **Xatolarni tekshirish kodi (Error Checking Code):** Ma’lumotlar uzatish jarayonida buzilmaganligini tekshirish uchun (masalan, CRC – Cyclic Redundancy Check).

**Misol (IP paketi tuzilishi):**

*   **IP Header:** Manba IP-manzili, manzil IP-manzili, IP-versiyasi, paket uzunligi, TTL (Time To Live), protokol turi (masalan, TCP, UDP).
*   **Data:** Transport qatlamidan kelgan segment (masalan, TCP segmenti yoki UDP datagrami).
*   **Ethernet Frame (2-qatlam):** MAC-manzillar, freym turi, ma’lumotlar (IP paketi), FCS (Frame Check Sequence – xatolarni tekshirish).

Paket tuzilishi har bir qatlamda ma’lumotlar qo‘shilishi (inkapsulyatsiya) orqali shakllanadi va ma’lumotlar qabul qilinganda har bir qatlamda sarlavhalar olib tashlanadi (dekapsulyatsiya).

### 5. Protokollar

**Protokol** – bu tarmoqqa ulangan qurilmalar o‘rtasida ma’lumot almashish uchun belgilangan qoidalar va tartiblar to‘plami. Protokollar yordamida turli ishlab chiqaruvchilarning apparat va dasturiy ta’minotlari bir-biri bilan o‘zaro aloqa qila oladi. Har bir protokol o‘ziga xos vazifaga ega va ma’lum bir tarmoq qatlami bilan bog‘liq.

**Protokollarning ahamiyati:**
*   **Standartizatsiya:** Turli qurilmalar bir xil qoidalar bo‘yicha aloqa qilishini ta’minlaydi.
*   **Tartiblilik:** Ma’lumotlar almashish jarayonini tartibga soladi.
*   **Ishonchlilik:** Ma’lumotlarning to‘g‘ri va butun yetib borishini ta’minlaydi.
*   **O‘zaro ishlash:** Turli tizimlar o‘rtasida aloqani mumkin qiladi.

**Ba’zi muhim protokollar misollari (OSI qatlamlari bo‘yicha):**

*   **1-qatalam (Fizik):** Kabel va ulagichlar standartlari.
*   **2-qatalam (Kanalli):**
    *   **Ethernet:** LANlarda kadrlar uzatish uchun eng keng tarqalgan protokol.
    *   **ARP (Address Resolution Protocol):** IP-manzilga mos keladigan MAC-manzilni aniqlash.
    *   **RARP (Reverse ARP):** MAC-manzilga mos keladigan IP-manzilni aniqlash (kam ishlatiladi).
*   **3-qatalam (Tarmoq):**
    *   **IP (Internet Protocol):** Paketlarni manbadan manzilga marshrutlash. Internetning asosiy protokoli.
    *   **ICMP (Internet Control Message Protocol):** Tarmoq qurilmalari o‘rtasida xatolarni va boshqaruv xabarlarini almashish (masalan, ping buyrug‘i).
    *   **IGMP (Internet Group Management Protocol):** Ko‘p nuqtali (multicast) aloqani boshqarish.
*   **4-qatalam (Transport):**
    *   **TCP (Transmission Control Protocol):** Ishonchli, ulanishga asoslangan ma’lumot uzatish. Xatolarni tuzatish va qayta uzatishni ta’minlaydi. (Masalan, veb-brauzerlar, elektron pochta).
    *   **UDP (User Datagram Protocol):** Tezkor, ulanishsiz ma’lumot uzatish. Ishonchliligi kamroq, lekin tezligi yuqori. (Masalan, real vaqt rejimida video/audio uzatish, DNS so‘rovlari).
*   **5, 6, 7-qatlamlar (Sessiya, Taqdimot, Amaliy dastur):**
    *   **HTTP (Hypertext Transfer Protocol):** Veb-sahifalarni uzatish.
    *   **HTTPS (HTTP Secure):** Shifrlangan HTTP.
    *   **FTP (File Transfer Protocol):** Fayllarni uzatish.
    *   **SMTP (Simple Mail Transfer Protocol):** Elektron pochta yuborish.
    *   **POP3 (Post Office Protocol version 3) / IMAP (Internet Message Access Protocol):** Elektron pochta qabul qilish.
    *   **DNS (Domain Name System):** Domen nomlarini IP-manzillarga aylantirish.
    *   **SSH (Secure Shell):** Tarmoq orqali xavfsiz masofaviy kirish.
    *   **DHCP (Dynamic Host Configuration Protocol):** Qurilmalarga avtomatik ravishda IP-manzillar berish.

### 6. Kommutatsiya

**Kommutatsiya (Switching)** – bu tarmoqda ma’lumotlarni bir nuqtadan boshqa nuqtaga yo‘naltirish jarayoni. U tarmoq qurilmalariga (masalan, switchlar, routerlar) kelgan ma’lumotlarni to‘g‘ri manzilga yetkazib berish imkonini beradi. Kommutatsiya tarmoqlar samaradorligini oshirish va resurslardan oqilona foydalanish uchun juda muhimdir.

**Kommutatsiya turlari:**

1.  **Kanalli kommutatsiya (Circuit Switching):**
    *   Uzatish boshlanishidan oldin manba va manzil o‘rtasida doimiy, ajratilgan aloqa kanali o‘rnatiladi.
    *   Ushbu kanal butun aloqa davomida faqat shu aloqa uchun band bo‘ladi va boshqa foydalanuvchilar undan foydalana olmaydi.
    *   *Misol:* An’anaviy telefon tarmoqlari. Bir qo‘ng‘iroq paytida ikki abonent o‘rtasida butun bir liniya band bo‘ladi.
    *   *Afzalliklari:* Uzatish kechikishsiz, doimiy sifat.
    *   *Kamchiliklari:* Resurslardan samarasiz foydalanish (kanal bo‘sh tursa ham band), kanal o‘rnatish uchun boshlang‘ich kechikish.

2.  **Paketli kommutatsiya (Packet Switching):**
    *   Ma’lumotlar kichik paketlarga bo‘linadi va har bir paket mustaqil ravishda tarmoq orqali o‘z yo‘lini topadi.
    *   Paketlar har xil marshrutlar orqali yetib borishi va manzilga yetib borgach qayta yig‘ilishi mumkin.
    *   Har bir paketning sarlavhasida manba va manzil manzillari mavjud bo‘ladi.
    *   *Misol:* Internet.
    *   *Afzalliklari:* Tarmoq resurslaridan yuqori samaradorlik bilan foydalanish (bir kanal orqali bir vaqtda ko‘plab paketlar uzatilishi mumkin), tarmoqning nosozliklarga chidamliligi (bir marshrut ishlamasa, boshqa yo‘l topiladi).
    *   *Kamchiliklari:* Paketlarning kechikishlari va tartibsiz yetib kelishi mumkin, ularni qayta yig‘ish zarurati.

3.  **Xabar kommutatsiyasi (Message Switching):**
    *   Butun xabar bitta blok sifatida uzatiladi. Har bir tugun xabarni to‘liq qabul qiladi, saqlaydi va keyingi tugunga uzatadi (store-and-forward).
    *   U hozirgi zamonaviy tarmoqlarda kamdan-kam qo‘llaniladi, lekin elektron pochta kabi ba’zi ilovalarda uning elementlari mavjud.

**Tarmoq qurilmalarida kommutatsiya:**

*   **2-qatlami kommutatsiya (Layer 2 Switching):**
    *   Bu **switchlar** tomonidan amalga oshiriladi.
    *   Switchlar MAC-manzillar jadvali (CAM table yoki MAC address table) asosida ishlaydi. Ular kelgan kadrning manzil MAC-manzilini o‘qiydi va jadvalda unga mos keladigan portni topib, kadrni faqat o‘sha portga yuboradi.
    *   *Maqsad:* Lokal tarmoq ichida (bir segmentda) trafikni optimallashtirish va to‘qnashuv domenlarini (collision domains) kamaytirish.

*   **3-qatlami kommutatsiya (Layer 3 Switching / Routing):**
    *   Bu **routerlar** (marshrutizatorlar) tomonidan amalga oshiriladi. Ba’zi yuqori unumdor switchlar ham 3-qatlamda ishlashi mumkin (Layer 3 switchlar).
    *   Routerlar IP-manzillar va marshrutlash jadvallari (routing tables) asosida ishlaydi. Ular kelgan paketning manzil IP-manzilini o‘qiydi, eng yaxshi yo‘lni aniqlaydi va paketni boshqa tarmoqqa (subnets) yo‘naltiradi.
    *   *Maqsad:* Turli xil tarmoqlar (subnets) o‘rtasida aloqa o‘rnatish va tarmoqlararo trafikni boshqarish.

Kommutatsiya zamonaviy tarmoqlarning asosini tashkil etadi, u ma’lumotlarni samarali va ishonchli tarzda uzatishga imkon beradi.
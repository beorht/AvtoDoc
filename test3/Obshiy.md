
#### Mavzusi № 0: Asosiy tushunchalar: maxfiylik, yaxlitlik, mavjudlik.
Axborot xavfsizligi sohasidagi qonunchilik va standartlarning asoslari. Mavjud xavfsizlik standartlarini tahlil qilish (ISO 27001, NIST). Axborot xavfsizligi tushunchasi. Axborotni himoya qilish standartlari.

---

1.  Axborot xavfsizligi tushunchasi va uning asosiy prinsiplari (CIA Triad).
2.  Axborot xavfsizligi sohasidagi qonunchilik va normativ hujjatlarning ahamiyati.
3.  Xalqaro axborot xavfsizligi standartlari: ISO 27001.
4.  AQSHning Milliy Standartlar va Texnologiyalar Instituti (NIST) freymvorklari.
5.  Axborotni himoya qilish standartlarini tatbiq etish va ularning ahamiyati.

---

Ta’limiy material matni:

### 1. Axborot xavfsizligi tushunchasi va uning asosiy prinsiplari (CIA Triad).

Axborot xavfsizligi (Information Security) – bu axborotni ruxsatsiz kirish, foydalanish, oshkor qilish, buzish, o‘zgartirish, yo‘q qilish yoki tarqatishdan himoya qilish bilan bog‘liq choralar majmuidir. U shuningdek, axborot tizimlarini barqaror va ishonchli ishlashini taʼminlashni ham o‘z ichiga oladi. Axborot xavfsizligining asosini uchta tamoyil tashkil etadi, bu tamoyillar ko‘pincha inglizcha qisqartma “CIA Triad” (Confidentiality, Integrity, Availability) deb nomlanadi:

*   **Maxfiylik (Confidentiality):** Axborotga faqat vakolatli shaxslar, tashkilotlar yoki tizimlar kirishi mumkinligini taʼminlash. Bu axborotning ruxsatsiz shaxslar qo‘liga tushib qolmasligi va ularga oshkor etilmasligini anglatadi.
    *   **Misol:** Bank mijozining shaxsiy ma’lumotlari (hisob raqami, paroli) faqat shu mijoz va vakolatli bank xodimlari uchun mavjud bo‘lishi kerak. Boshqa shaxslar ularga kira olmasligi lozim.
    *   **Himoya choralari:** Shifrlash, parollash, kirishni boshqarish (Access Control), foydalanuvchilarni autentifikatsiya qilish.

*   **Yaxlitlik (Integrity):** Axborotning to‘g‘ri, aniq va ishonchli bo‘lishini, uning ruxsatsiz yoki tasodifiy o‘zgartirishlardan himoyalanganligini taʼminlash. Bu axborotning manbadan maqsadga o‘zgarmasdan yetib borishini va uni faqat vakolatli shaxslar o‘zgartira olishini anglatadi.
    *   **Misol:** Universitet talabasining baholarini aks ettiruvchi hujjatni hech kim ruxsatsiz o‘zgartira olmasligi kerak. Agar o‘zgarish sodir bo‘lsa, bu aniqlanishi shart.
    *   **Himoya choralari:** Raqamli imzolar, hash funksiyalari, versiyalarni boshqarish, tranzaksiya jurnallari.

*   **Mavjudlik (Availability):** Vakolatli foydalanuvchilar axborot va axborot tizimlariga ular talab qilgan vaqtda kirishi mumkinligini taʼminlash. Bu xizmatlarning uzluksiz ishlashi va resurslarga erishish imkoniyatini anglatadi.
    *   **Misol:** Elektron tijorat veb-sayti mijozlar uchun doimiy ravishda ochiq bo‘lishi va mahsulotlarga buyurtma berish imkoniyatini taqdim etishi kerak. Saytga hujumlar (masalan, DDoS) uning mavjudligini buzmasligi lozim.
    *   **Himoya choralari:** Zaxira nusxalash (Backup), tiklash rejalari (Disaster Recovery), yuklamani muvozanatlash (Load Balancing), ortiqcha tizimlar (Redundancy), DDoS hujumlaridan himoya.

**Xulosa:** CIA Triad axborot xavfsizligining poydevori bo‘lib, har qanday axborotni himoya qilish strategiyasining asosiy maqsadlarini belgilab beradi. Ushbu uchta tamoyil muvozanatda bo‘lishi zarur, chunki ulardan biriga haddan tashqari e’tibor berish boshqalarini zaiflashtirishi mumkin.

### 2. Axborot xavfsizligi sohasidagi qonunchilik va normativ hujjatlarning ahamiyati.

Zamonaviy raqamli dunyoda axborotni himoya qilish nafaqat texnik masala, balki huquqiy va me’yoriy masaladir. Davlatlar va xalqaro tashkilotlar axborot xavfsizligini ta’minlash, jismoniy shaxslarning shaxsiy ma’lumotlarini himoya qilish, kiberjinoyatlarga qarshi kurashish va tashkilotlarning mas’uliyatini belgilash maqsadida qonunchilik va standartlarni ishlab chiqadi.

**Qonunchilikning ahamiyati:**

*   **Huquqiy asos:** Axborot xavfsizligi siyosatlari va choralarini qo‘llash uchun huquqiy asos yaratadi.
*   **Majburiyatlar:** Tashkilotlar va shaxslarga axborotni himoya qilish bo‘yicha aniq majburiyatlarni yuklaydi.
*   **Javobgarlik:** Qonun buzilishi holatlarida yuridik va ma’muriy javobgarlikni belgilaydi, bu esa axborotni himoya qilishga jiddiy yondashishni rag‘batlantiradi.
*   **Ishonch:** Fuqarolar va biznes subyektlarining raqamli muhitga bo‘lgan ishonchini oshiradi.
*   **Kiberjinoyatlarga qarshi kurash:** Kiberjinoyatlarni aniqlash, tergov qilish va jazolash uchun asos yaratadi.

**Misollar:**
*   **GDPR (General Data Protection Regulation):** Yevropa Ittifoqida shaxsiy ma’lumotlarni himoya qilish bo‘yicha qat’iy qoida. U tashkilotlarga ma’lumotlarni qanday yig‘ish, saqlash va qayta ishlash bo‘yicha aniq talablarni qo‘yadi va ma’lumot subyektlariga keng huquqlar beradi.
*   **HIPAA (Health Insurance Portability and Accountability Act):** AQShda sog‘liqni saqlash sohasidagi shaxsiy ma’lumotlarning maxfiyligi va xavfsizligini tartibga soluvchi qonun.
*   **O‘zbekiston Respublikasining "Shaxsiy ma’lumotlar to‘g‘risida"gi Qonuni:** Fuqarolarning shaxsiy ma’lumotlarini yig‘ish, qayta ishlash va himoya qilish tartiblarini belgilaydi.
*   **"Axborotlashtirish to‘g‘risida"gi Qonun:** Axborotlashtirish sohasidagi munosabatlarni tartibga soladi.

**Normativ hujjatlar va standartlarning ahamiyati:**

*   **Eng yaxshi amaliyotlar:** Tashkilotlarga axborot xavfsizligini samarali boshqarish uchun eng yaxshi amaliyotlar va yo‘l-yo‘riqlarni taqdim etadi.
*   **Muvozanat:** Turli tashkilotlar va mamlakatlar o‘rtasida axborot xavfsizligi darajasini muvozanatlashga yordam beradi.
*   **Sertifikatlash:** Tashkilotlarga o‘zlarining xavfsizlik amaliyotlari standartlarga muvofiq ekanligini tasdiqlovchi sertifikatlarni olish imkonini beradi.
*   **Xatarlarni kamaytirish:** Tashkilotlarga xavflarni aniqlash, baholash va ularni boshqarishda yordam beradi.

**Xulosa:** Axborot xavfsizligi bo‘yicha qonunchilik va standartlar nafaqat majburiy talablarni belgilaydi, balki tashkilotlarga xavflarni samarali boshqarish, xavfsizlik darajasini oshirish va raqamli muhitda ishonchni mustahkamlash uchun yo‘l xaritasi vazifasini ham bajaradi.

### 3. Xalqaro axborot xavfsizligi standartlari: ISO 27001.

**ISO/IEC 27001** – bu Axborot xavfsizligini boshqarish tizimi (Information Security Management System – ISMS) uchun xalqaro standart bo‘lib, axborotni samarali himoya qilish uchun talablarni belgilaydi. Bu standart tashkilotlarga o‘z axborot aktivlarini (ma’lumotlar, tizimlar, jarayonlar) xavf-xatarlardan himoya qilishga yordam beradi.

**Asosiy maqsadi:**
Tashkilotlarga axborot xavfsizligi risklarini tizimli, samarali va doimiy asosda boshqarish uchun asos yaratish. U faqat texnik choralar haqida emas, balki butun tashkilotni qamrab oluvchi boshqaruv tizimi haqida bo‘lib, xavfsizlikni biznes jarayonlariga integratsiyalashni talab qiladi.

**ISO 27001 ning asosiy komponentlari:**

1.  **Axborot xavfsizligi siyosati:** Yuqori rahbariyat tomonidan tasdiqlangan, tashkilotning axborot xavfsizligi maqsadlari va majburiyatlarini belgilovchi hujjat.
2.  **Xavflarni baholash va ishlov berish:** Axborot xavfsizligi xatarlarini aniqlash, ularning ehtimolini va ta’sirini baholash, so‘ngra ularga qarshi tegishli boshqaruv choralarini (kontrollarni) tanlash.
3.  **Xavfsizlik nazoratlari (Controls):** ISO 27002 standartida ko‘rsatilgan va ISO 27001 ilovasining A qismida keltirilgan turli xil nazorat choralari. Bularga quyidagilar kiradi:
    *   Tashkiliy xavfsizlik (siyosatlar, rollar, mas’uliyatlar).
    *   Inson resurslari xavfsizligi (ishga qabul qilish, o‘qitish, ishdan bo‘shatish).
    *   Aktivlarni boshqarish (inventarizatsiya, tasniflash).
    *   Kirishni boshqarish (foydalanuvchilarni autentifikatsiya qilish, ruxsatlar).
    *   Kriptografiya.
    *   Fizikaviy va ekologik xavfsizlik.
    *   Operatsion xavfsizlik (zaxira nusxalash, loglash).
    *   Aloqa xavfsizligi.
    *   Tizimlarni sotib olish, ishlab chiqish va texnik xizmat ko‘rsatish.
    *   Yetkazib beruvchi munosabatlari.
    *   Axborot xavfsizligi hodisalarini boshqarish.
    *   Axborot xavfsizligining uzluksizligi.
    *   Muvofiqlik.
4.  **Boshqaruv tizimi (Management System):** ISMSni rejalashtirish, amalga oshirish, monitoring qilish, ko‘rib chiqish va doimiy takomillashtirish (Plan-Do-Check-Act – PDCA sikli).

**Afzalliklari:**

*   **Tizimli yondashuv:** Xavfsizlikni boshqarishga tizimli va takrorlanadigan yondashuvni ta’minlaydi.
*   **Xalqaro tan olinish:** Butun dunyoda tan olingan bo‘lib, tashkilotlarga xalqaro savdoda va hamkorlikda ishonchni oshirishga yordam beradi.
*   **Komplayens:** Axborot xavfsizligi bo‘yicha qonunchilik va me’yoriy talablarga rioya qilishni osonlashtiradi.
*   **Xatarlarni kamaytirish:** Xavflarni samarali boshqarish orqali ma’lumotlarning yo‘qolishi, buzilishi yoki oshkor bo‘lish xavfini kamaytiradi.
*   **Biznes uzluksizligi:** Xavfsizlik hodisalari natijasida yuzaga kelishi mumkin bo‘lgan ta’sirni minimallashtirib, biznesning uzluksizligini ta’minlaydi.

**Xulosa:** ISO 27001 – bu tashkilotlarga axborot xavfsizligini nafaqat texnik jihatdan, balki butun boshqaruv tizimi darajasida samarali tashkil etishga imkon beruvchi muhim standartdir. U sertifikatlash imkoniyatini berib, tashkilotning axborot xavfsizligiga jiddiy yondashuvini isbotlaydi.

### 4. AQSHning Milliy Standartlar va Texnologiyalar Instituti (NIST) freymvorklari.

**NIST (National Institute of Standards and Technology)** – AQShning Federal hukumati agentligi bo‘lib, turli sohalarda standartlar va ko‘rsatmalar ishlab chiqadi. Axborot xavfsizligi sohasida NIST bir qator muhim freymvorklar va nashrlarni (Special Publications – SP) taqdim etadi, ular butun dunyo bo‘ylab keng qo‘llaniladi, ayniqsa federal agentliklar va ularning hamkorlari orasida.

**NIST ning asosiy xavfsizlik freymvorklari va ko‘rsatmalari:**

1.  **NIST Cybersecurity Framework (CSF):** Bu freymvork tashkilotlarga kiberxavflarni boshqarish va kamaytirishga yordam berish uchun ishlab chiqilgan bo‘lib, ayniqsa tanqidiy infratuzilma operatorlari uchun mo‘ljallangan. U uchta asosiy komponentga ega:
    *   **Freymvork yadrosi (Framework Core):** Kiberxavfsizlik amaliyotlarini tavsiflaydigan beshta funktsiya (Identifikasiyalash, Himoya qilish, Aniqlash, Javob berish, Tiklash) va ularning ostidagi toifalar, quyi toifalar va ma’lumot beruvchi referensiyalar.
    *   **Freymvork tatbiq qilish bosqichlari (Framework Tiers):** Tashkilotning kiberxavflarni boshqarishga bo‘lgan yondashuvining yetuklik darajasini baholaydi (Qisman, Xavf ostida, Takrorlanuvchi, Adaptiv).
    *   **Freymvork profillari (Framework Profiles):** Tashkilotning hozirgi va maqsadli kiberxavfsizlik holatini tasvirlaydi, bu esa yaxshilash sohalarini aniqlashga yordam beradi.
    *   **Maqsadi:** Tashkilotlarga kiberxavfsizlik risklarini samarali boshqarish, ichki va tashqi aloqani yaxshilash, xavfsizlikka investitsiyalarni ustuvorlashtirish.

2.  **NIST Special Publication 800 Series:** Bu nashrlar turkumi axborot xavfsizligining turli jihatlari bo‘yicha batafsil ko‘rsatmalar va standartlarni o‘z ichiga oladi. Eng mashhurlari:
    *   **NIST SP 800-53: "Security and Privacy Controls for Federal Information Systems and Organizations":** Bu hujjat federal axborot tizimlari va tashkilotlari uchun tavsiya etilgan xavfsizlik va maxfiylik nazoratlari katalogini taqdim etadi. U axborot tizimlarini himoya qilish uchun keng qamrovli nazorat choralarini belgilaydi va ularni xavf-xatarlar darajasi bo‘yicha guruhlaydi.
    *   **NIST SP 800-30: "Guide for Conducting Risk Assessments":** Xavflarni baholash bo‘yicha batafsil ko‘rsatmalar beradi.
    *   **NIST SP 800-61: "Computer Security Incident Handling Guide":** Xavfsizlik hodisalarini boshqarish bo‘yicha yo‘l-yo‘riq.
    *   **NIST SP 800-171: "Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations":** Federal bo‘lmagan tizimlardagi nazorat ostidagi maxfiy bo‘lmagan ma’lumotlarni himoya qilish bo‘yicha talablar.

**ISO 27001 va NIST o‘rtasidagi farqlar va o‘xshashliklar:**

*   **Asosiy farq:** ISO 27001 – bu sertifikatlanadigan boshqaruv tizimi standarti bo‘lib, u “nimani qilish kerak” degan savolga javob beradi (ya’ni, ISMSni joriy etish talablari). NIST freymvorklari va nashrlari esa ko‘pincha “qanday qilish kerak” degan savolga javob beradi (ya’ni, batafsil texnik ko‘rsatmalar va eng yaxshi amaliyotlar).
*   **Foydalanish doirasi:** ISO 27001 global miqyosda qo‘llaniladi, NIST esa AQSh federal hukumati va uning hamkorlari tomonidan keng qo‘llaniladi, ammo uning amaliyotlari global miqyosda tan olingan va boshqa tashkilotlar tomonidan ham o‘zlashtiriladi.
*   **Boshqaruv vs. Texnik tafsilot:** ISO 27001 ko‘proq yuqori darajadagi boshqaruv tizimiga e’tibor qaratadi, NIST SP 800 seriyasi esa juda batafsil texnik va operatsion ko‘rsatmalarni beradi.

**Xulosa:** NIST freymvorklari va nashrlari tashkilotlarga kiberxavfsizlikni boshqarish bo‘yicha juda qimmatli va batafsil yo‘l-yo‘riqlar beradi. Ular axborot xavfsizligi sohasida chuqur bilim va amaliyotlarni taqdim etib, tashkilotlarning o‘z xavfsizlik pozitsiyalarini kuchaytirishiga yordam beradi. ISO 27001 bilan birgalikda, ular axborot xavfsizligini ta’minlash uchun mustahkam asos yaratadi.

### 5. Axborotni himoya qilish standartlarini tatbiq etish va ularning ahamiyati.

Axborot xavfsizligi standartlarini tatbiq etish – bu tashkilotlarning axborot aktivlarini samarali himoya qilish uchun strategik zaruratdir. Bu standartlar, masalan, ISO 27001 va NIST kabi freymvorklar, axborot xavfsizligi bo‘yicha eng yaxshi amaliyotlarni to‘plagan va ularni tizimli ravishda joriy etish uchun yo‘l-yo‘riq beradi.

**Standartlarni tatbiq etish jarayoni odatda quyidagi bosqichlarni o‘z ichiga oladi:**

1.  **Rejalashtirish va doirasi (Scope definition):** Axborot xavfsizligi boshqaruv tizimining doirasini aniqlash – qaysi axborot aktivlari, tizimlar va jarayonlar himoyalanishi kerakligini belgilash.
2.  **Rahbariyatning majburiyati:** Yuqori rahbariyatning axborot xavfsizligi siyosatini qo‘llab-quvvatlashini ta’minlash.
3.  **Xavflarni baholash (Risk Assessment):** Mavjud va potentsial xavflarni, zaifliklarni aniqlash va ularning tashkilotga ta’sirini baholash.
4.  **Xavflarni boshqarish (Risk Treatment):** Aniqlangan xavflarni kamaytirish, yo‘q qilish, qabul qilish yoki boshqa tomonlarga o‘tkazish bo‘yicha tegishli nazorat choralarini (controls) tanlash va joriy etish.
5.  **Nazorat choralarini amalga oshirish:** Tanlangan texnik, tashkiliy va fizikaviy xavfsizlik choralarini (masalan, shifrlash, kirishni cheklash, xodimlarni o‘qitish) amaliyotga tatbiq etish.
6.  **Monitoring va ko‘rib chiqish:** Axborot xavfsizligi tizimining samaradorligini doimiy ravishda monitoring qilish, ichki auditlar o‘tkazish va rahbariyat tomonidan ko‘rib chiqish.
7.  **Doimiy takomillashtirish:** Aniqlovlar va audit natijalari asosida tizimni muntazam ravishda yangilab borish va takomillashtirish.

**Standartlarni tatbiq etishning ahamiyati:**

*   **Tizimli himoya:** Axborot xavfsizligiga tarqoq emas, balki tizimli va kompleks yondashuvni ta’minlaydi.
*   **Xatarlarni kamaytirish:** Axborot xavfsizligi hodisalari va ularning salbiy oqibatlarini minimallashtiradi.
*   **Qonuniy va me’yoriy muvofiqlik (Compliance):** Turli milliy va xalqaro qonunchilik talablariga rioya qilishni osonlashtiradi, jarimalar va huquqiy muammolardan himoya qiladi.
*   **Ishonchni oshirish:** Mijozlar, hamkorlar va investorlar uchun tashkilotning axborotni ishonchli himoya qilishga qodirligini ko‘rsatadi.
*   **Raqobatbardoshlik:** Bozorda ustunlik beradi, chunki xavfsizlik sertifikatiga ega bo‘lgan tashkilotlar ko‘pincha afzal ko‘riladi.
*   **Biznes uzluksizligi:** Favqulodda vaziyatlarda biznes jarayonlarining uzluksizligini ta’minlashga yordam beradi.
*   **Resurslarni optimallashtirish:** Xavfsizlik choralariga investitsiyalarni oqilona yo‘naltirishga yordam beradi, ortiqcha xarajatlarni oldini oladi.

**Xulosa:** Axborotni himoya qilish standartlari – bu zamonaviy tashkilotlar uchun shunchaki bir talab emas, balki ularning raqamli aktivlarini, obro‘sini va biznes uzluksizligini ta’minlash uchun muhim vositadir. Ularni tatbiq etish murakkab jarayon bo‘lsada, u uzoq muddatli istiqbolda katta foyda keltiradi va tashkilotni kiberxavflar dunyosida barqaror qiladi.
#### Mavzusi № 1: Mahalliy hisoblash tarmoqlari, kompyuter tarmoqlarini kengaytirish. Kompyuter tarmog'ining maqsadi. Teng huquqli tarmoqlar, tarmoq hajmi, tarmoq qiymati, operatsion tizimlar, amalga oshirish, qo'llashning maqsadga muvofiqligi. Serverga asoslangan tarmoqlar, ixtisoslashtirilgan serverlar.

Ta’limiy materialning asosiy bo‘limlariga bo'lib boshida yozib ket:
1. Mahalliy hisoblash tarmoqlari (LAN) va ularni kengaytirish
2. Kompyuter tarmoqlarining maqsadi va teng huquqli (Peer-to-peer) tarmoqlar
3. Tarmoq parametrlari, operatsion tizimlar va ularni amalga oshirish
4. Serverga asoslangan tarmoqlar va ixtisoslashtirilgan serverlar
5. Tarmoq texnologiyalarini qo'llashning maqsadga muvofiqligi

---

#### Ta’limiy material matni:

**1. Mahalliy hisoblash tarmoqlari (LAN) va ularni kengaytirish**

Mahalliy hisoblash tarmog'i (LAN – Local Area Network) nisbatan kichik geografik hududda, masalan, bitta bino, ofis yoki maktab ichida joylashgan kompyuterlar va boshqa tarmoq qurilmalarini o'zaro bog'laydigan tarmoq turidir. LANlar foydalanuvchilarga ma'lumotlar, dasturlar va apparat resurslarini (masalan, printerlar, fayl serverlari) o'zaro almashish imkonini beradi. Ular yuqori tezlikda ma'lumot uzatishni ta'minlaydi va odatda o'rta darajadagi xarajat bilan o'rnatiladi.

**LANlarning asosiy xususiyatlari:**
*   **Geografik qamrov:** Kichik hudud bilan chegaralangan.
*   **Ma'lumot uzatish tezligi:** Yuqori (odatda 100 Mbps dan 100 Gbps gacha).
*   **Xarajat:** O'rta darajada, katta masofali tarmoqlarga nisbatan arzon.
*   **Egalik:** Odatda bitta tashkilot yoki shaxs tomonidan boshqariladi.

**Kompyuter tarmoqlarini kengaytirish:**
Tarmoqlar doimo bir joyda qolib ketmaydi. Tashkilotlarning ehtiyojlari ortib borishi bilan, mavjud LANlarni kengaytirish yoki ularni bir-biriga bog'lash zarurati tug'iladi. Kengaytirish quyidagicha bo'lishi mumkin:
*   **Taqsimlangan LANlar:** Bir nechta kichik LANlarni switch (kalit) yoki router (yo'naltiruvchi) yordamida bir-biriga bog'lash.
*   **Metropolitan Area Network (MAN):** Katta shahar yoki kampus kabi bir necha o'nlab kilometr masofani qamrab oluvchi tarmoq. MANlar odatda bir nechta LANlarni birlashtiradi.
*   **Wide Area Network (WAN):** Eng keng tarmoq turi bo'lib, turli shaharlar, mamlakatlar yoki qit'alar orasidagi LANlarni bir-biriga bog'laydi. Internet — global WANning yorqin misolidir.
*   **Simsiz kengaytirish:** Wi-Fi kabi simsiz texnologiyalar orqali tarmoq qamrovini oshirish, simli ulanish imkoni bo'lmagan joylarga kirishni ta'minlash.

**Misol:** Kichik ofisda 5 ta kompyuterni bir-biriga bog'lash LAN hisoblanadi. Agar kompaniya boshqa shaharda filial ochsa va har ikki ofisdagi kompyuterlar bir-biri bilan ma'lumot almashishi kerak bo'lsa, bu ikki LANni WAN orqali bog'lash tarmoqni kengaytirishga misol bo'ladi.

---

**2. Kompyuter tarmoqlarining maqsadi va teng huquqli (Peer-to-peer) tarmoqlar**

**Kompyuter tarmog'ining maqsadi:**
Kompyuter tarmoqlarining asosiy maqsadi quyidagilarni ta'minlashdan iborat:
*   **Resurslarni almashish:** Dasturiy ta'minot, apparat resurslari (printerlar, skanerlar, qattiq disklar) va ma'lumotlarni tarmoqqa ulangan barcha foydalanuvchilar o'rtasida samarali almashish imkoniyatini yaratish. Bu xarajatlarni kamaytiradi va samaradorlikni oshiradi.
*   **Ma'lumotlar almashinuvi va kommunikatsiya:** Foydalanuvchilar o'rtasida tezkor ma'lumot almashish (elektron pochta, chat, fayl almashinuvi) va hamkorlik qilish uchun platforma yaratish.
*   **Markazlashtirilgan ma'lumotlar saqlash va boshqarish:** Ma'lumotlarni serverlarda markazlashtirilgan holda saqlash, ularning zaxira nusxalarini yaratish va xavfsizligini ta'minlash.
*   **Uzoqdan kirish:** Tarmoqqa ulangan resurslarga dunyoning istalgan nuqtasidan (tegishli ruxsatnomalar bilan) kirish imkoniyatini berish.
*   **Ma'lumotlar xavfsizligi:** Kirish nazorati, shifrlash va boshqa xavfsizlik mexanizmlari orqali ma'lumotlarni ruxsatsiz kirishdan himoya qilish.

**Teng huquqli (Peer-to-peer - P2P) tarmoqlar:**
Teng huquqli tarmoqda har bir kompyuter (peer) ham server, ham mijoz vazifasini bajarishi mumkin. Ya'ni, hech bir kompyuter markaziy boshqaruvchi rolini o'ynamaydi. Barcha ulangan kompyuterlar bir xil huquqlarga ega va bevosita bir-biri bilan resurslarni almasha oladi.

**P2P tarmoqlarning afzalliklari:**
*   **O'rnatish osonligi:** Maxsus server talab etilmaydi, shuning uchun kichik tarmoqlar uchun tez va oson o'rnatiladi.
*   **Kam xarajat:** Server sotib olish va uni boshqarish xarajatlari yo'q.
*   **Ishonchlilik:** Bir kompyuter ishdan chiqsa ham, butun tarmoq faoliyatini davom ettiradi (chunki markaziy nuqta yo'q).

**P2P tarmoqlarning kamchiliklari:**
*   **Xavfsizlik:** Ma'lumotlar xavfsizligini ta'minlash qiyinroq, chunki markaziy boshqaruv mavjud emas. Har bir kompyuter o'z xavfsizligi uchun javobgar.
*   **Boshqaruv:** Tarmoq kattalashgan sari uni boshqarish murakkablashadi.
*   **Ma'lumotlarning tarqoqligi:** Fayllar va resurslar turli kompyuterlarda saqlanib, ularni topish va boshqarishni qiyinlashtirishi mumkin.
*   **Kichik tarmoqlar uchun mos:** Odatda 10-15 tadan ortiq kompyuter uchun samarali emas.

**Misol:** Uy tarmog'ida oila a'zolarining kompyuterlari bir-biri bilan fayl almashish uchun P2P tarmoqdan foydalanishi mumkin. Shuningdek, ba'zi fayl almashish dasturlari (masalan, BitTorrent) ham P2P prinsipiga asoslanadi.

---

**3. Tarmoq parametrlari, operatsion tizimlar va ularni amalga oshirish**

Tarmoqni loyihalash va amalga oshirishda bir qator muhim parametrlarni hisobga olish kerak.

**Tarmoq hajmi:**
Tarmoq hajmi tarmoqqa ulanadigan qurilmalar (kompyuterlar, serverlar, printerlar va boshqalar) soni va tarmoq qamrab oladigan geografik maydonni anglatadi.
*   **Kichik tarmoqlar (1-10 qurilma):** P2P yoki oddiy server-mijoz tarmoqlar mos keladi. Kam resurs talab qiladi.
*   **O'rta tarmoqlar (10-100 qurilma):** Odatda serverga asoslangan tarmoqlar afzalroq. Maxsus serverlar va tarmoq infratuzilmasini talab qiladi.
*   **Katta tarmoqlar (100+ qurilma):** Murakkab server arxitekturasi, bir nechta ixtisoslashtirilgan serverlar, yuqori darajadagi xavfsizlik va boshqaruv tizimlarini talab qiladi.

Tarmoq hajmi o'sishi bilan tarmoqning murakkabligi, xavfsizlik talablari va boshqaruv xarajatlari ham ortadi.

**Tarmoq qiymati:**
Tarmoqni o'rnatish va uni saqlash bilan bog'liq xarajatlar quyidagilarni o'z ichiga oladi:
*   **Apparat ta'minoti:** Kompyuterlar, serverlar, switchlar, routerlar, kabellar, simsiz ulanish nuqtalari.
*   **Dasturiy ta'minot:** Tarmoq operatsion tizimlari, xavfsizlik dasturlari, boshqaruv vositalari.
*   **O'rnatish xarajatlari:** Kabel tortish, uskunalarni o'rnatish va sozlash uchun ish haqi.
*   **Ta'mirlash va texnik xizmat ko'rsatish:** Tarmoqni ish holatida ushlab turish, muammolarni bartaraf etish.
*   **Xodimlar:** Tarmoq administratorlarining ish haqi.
*   **O'qitish:** Foydalanuvchilarni tarmoqdan foydalanishga o'rgatish.

**Operatsion tizimlar (OS) tarmoq kontekstida:**
Har bir tarmoqqa ulangan kompyuter o'z operatsion tizimiga ega. Tarmoq operatsion tizimlari (NOS – Network Operating System) esa tarmoq resurslarini boshqarish, foydalanuvchilarga kirishni nazorat qilish va tarmoq xavfsizligini ta'minlash uchun mo'ljallangan.

**Misollar:**
*   **Mijoz OS:** Windows (Client versiyalari), macOS, Linux (desktop distributivlari) — foydalanuvchilarning shaxsiy kompyuterlarida ishlaydi va tarmoqqa ulangan resurslarga kirishni ta'minlaydi.
*   **Server OS:** Windows Server, Linux (server distributivlari kabi Ubuntu Server, CentOS), Novell NetWare (kam qo'llaniladi) — serverlarda ishlaydi va tarmoq resurslarini boshqaradi, xizmatlarni ta'minlaydi.

**Tarmoqni amalga oshirish (Implementation):**
Tarmoqni amalga oshirish tarmoqni loyihalashdan tortib uni ishga tushirishgacha bo'lgan barcha jarayonlarni o'z ichiga oladi. Bu quyidagi bosqichlarni qamrab oladi:
1.  **Talablarni aniqlash:** Foydalanuvchi ehtiyojlari, tarmoqning maqsadi, byudjet va kelajakdagi kengaytirish imkoniyatlari.
2.  **Loyihalash:** Tarmoq topologiyasi, apparat va dasturiy ta'minotni tanlash, IP-adreslash sxemasi, xavfsizlik siyosati.
3.  **Apparat sotib olish va o'rnatish:** Kabellash, kommutatorlar (switchlar), yo'naltiruvchilar (routerlar), serverlar va boshqa uskunalarni o'rnatish.
4.  **Dasturiy ta'minotni sozlash:** Server OS, tarmoq xizmatlari (DHCP, DNS), foydalanuvchi hisoblari, xavfsizlik devorlari (firewalls) konfiguratsiyasi.
5.  **Testlash:** Tarmoqning to'g'ri ishlashini ta'minlash, samaradorlikni baholash.
6.  **Hujjatlashtirish:** Tarmoq konfiguratsiyasi, qurilmalar ro'yxati, parollar va boshqa muhim ma'lumotlarni yozib borish.
7.  **Texnik xizmat ko'rsatish va monitoring:** Tarmoq faoliyatini kuzatish, muammolarni bartaraf etish, yangilanishlarni o'rnatish.

---

**4. Serverga asoslangan tarmoqlar va ixtisoslashtirilgan serverlar**

**Serverga asoslangan tarmoqlar (Client-Server networks):**
Bu turdagi tarmoqda bitta yoki bir nechta markaziy kompyuterlar (serverlar) resurslar va xizmatlarni taqdim etadi, qolgan kompyuterlar (mijozlar) esa ushbu resurslarga kiradi. Serverlar odatda kuchli protsessorlarga, katta operativ xotiraga va keng hajmli saqlash qurilmalariga ega bo'ladi. Ushbu arxitektura P2P tarmoqlarga nisbatan kattaroq va murakkabroq tarmoqlar uchun juda mos keladi.

**Afzalliklari:**
*   **Markazlashtirilgan boshqaruv:** Foydalanuvchilar, xavfsizlik, resurslar bir joydan boshqariladi.
*   **Kengaytiriluvchanlik:** Tarmoqni o'sishi bilan serverlarni yangilash yoki qo'shimcha serverlar qo'shish orqali osongina kengaytirish mumkin.
*   **Xavfsizlik:** Ma'lumotlar xavfsizligi markazlashtirilgan tarzda ta'minlanadi, kirish nazorati va audit tizimlari osonroq amalga oshiriladi.
*   **Zaxiralash:** Ma'lumotlarning zaxira nusxalarini yaratish va tiklash serverda markazlashtirilgan holda amalga oshiriladi.
*   **Samaradorlik:** Serverlar yuqori unumdorlikka ega bo'lib, bir vaqtning o'zida ko'plab mijozlarga xizmat ko'rsata oladi.

**Kamchiliklari:**
*   **Qimmatligi:** Server apparat va dasturiy ta'minoti P2P tarmoqlarga nisbatan qimmatroq.
*   **Murakkablik:** O'rnatish va boshqarish malakali mutaxassislarni talab qiladi.
*   **Bitta nuqtaning nosozligi:** Agar server ishdan chiqsa, butun tarmoq yoki uning muhim qismlari ishlashdan to'xtashi mumkin (bu muammoni bartaraf etish uchun ortiqchalik (redundancy) tizimlari qo'llaniladi).

**Ixtisoslashtirilgan serverlar:**
Katta tarmoqlarda bitta server barcha vazifalarni bajarishi qiyin bo'ladi. Shu sababli, ma'lum vazifalarni bajarish uchun maxsus serverlar qo'llaniladi:

*   **Fayl serveri:** Tarmoqdagi foydalanuvchilar uchun fayllarni saqlash, boshqarish va ularga kirishni ta'minlash uchun ishlatiladi.
*   **Chop etish serveri (Print server):** Tarmoqdagi printerlarga kirishni boshqaradi, chop etish navbatlarini tashkil qiladi va mijozlar uchun chop etish xizmatlarini taqdim etadi.
*   **Veb-server (Web server):** Veb-sahifalarni (HTML, CSS, JavaScript) saqlaydi va mijozlarga (brauzerlar) ularni yetkazib beradi (masalan, Apache, Nginx, IIS).
*   **Ma'lumotlar bazasi serveri (Database server):** Ma'lumotlar bazasini saqlaydi va mijoz dasturlardan kelgan so'rovlarga javob beradi (masalan, MySQL, PostgreSQL, SQL Server, Oracle).
*   **Pochta serveri (Mail server):** Elektron pochtani jo'natish, qabul qilish va saqlash uchun mo'ljallangan (masalan, Microsoft Exchange, Postfix).
*   **DNS serveri (Domain Name System server):** Domen nomlarini (masalan, example.com) IP manzillarga tarjima qiladi, bu foydalanuvchilarga saytlarga osonlik bilan kirish imkonini beradi.
*   **DHCP serveri (Dynamic Host Configuration Protocol server):** Tarmoqdagi qurilmalarga avtomatik ravishda IP manzillar va boshqa tarmoq sozlamalarini tayinlaydi.
*   **Proksi serveri (Proxy server):** Mijozlar va boshqa serverlar o'rtasida vositachi vazifasini bajaradi, xavfsizlikni oshirishi va tarmoq trafigini optimallashtirishi mumkin.
*   **Virtualizatsiya serveri:** Bir jismoniy serverda bir nechta virtual serverlarni (virtual mashinalar) ishga tushirish imkonini beradi, resurslardan samarali foydalanishni ta'minlaydi.

**Misol:** Katta korporatsiyada, e-mail uchun alohida server, veb-sayt uchun boshqa server, foydalanuvchi fayllari uchun uchinchi server, ma'lumotlar bazasi uchun to'rtinchi server mavjud bo'lishi mumkin. Bu serverlarning har biri o'z vazifasini bajaradi va butun tarmoqning samaradorligini oshiradi.

---

**5. Tarmoq texnologiyalarini qo'llashning maqsadga muvofiqligi**

Har qanday tarmoqni loyihalash va amalga oshirishda uning maqsadga muvofiqligini baholash juda muhimdir. Bu nafaqat texnik jihatlarni, balki iqtisodiy, operatsion va strategik omillarni ham o'z ichiga oladi.

**Qo'llashning maqsadga muvofiqligini baholash omillari:**

1.  **Talablarga muvofiqlik:**
    *   Tarmoq tashkilotning hozirgi va kelajakdagi ehtiyojlarini qondira oladimi?
    *   Qancha foydalanuvchi va qurilma ulanishi kutilmoqda?
    *   Qanday dasturlar va xizmatlar qo'llaniladi? (Masalan, real vaqt rejimidagi videokonferensiyalar uchun yuqori o'tkazuvchanlik kerak).

2.  **Iqtisodiy samaradorlik (Cost-effectiveness):**
    *   Tarmoqni o'rnatish va saqlash xarajatlari byudjetga mos keladimi?
    *   Investitsiya qaytish davri (ROI) qanday? Tarmoq investitsiyasidan kutilayotgan foyda (samaradorlikni oshirish, xarajatlarni kamaytirish) xarajatlarni qoplaydimi?
    *   Umumiy egalik xarajati (TCO – Total Cost of Ownership) nimalardan iborat bo'ladi? (Apparat, dasturiy ta'minot, o'rnatish, texnik xizmat, o'qitish).

3.  **Texnik imkoniyatlar va kengaytiriluvchanlik (Scalability):**
    *   Tanlangan texnologiyalar kelajakdagi o'sish va kengaytirish uchun mosmi?
    *   Tarmoq yuklamasining ortishiga chidamliligini qanday ta'minlash mumkin?
    *   Yangi texnologiyalar va standartlarga moslasha oladimi?

4.  **Xavfsizlik (Security):**
    *   Ma'lumotlar va resurslarning xavfsizligi qanday ta'minlanadi?
    *   Kiberxavfsizlik tahdidlariga qarshi qanday choralar ko'riladi? (Xavfsizlik devorlari, shifrlash, kirishni nazorat qilish).
    *   Ma'lumotlarning maxfiyligi, yaxlitligi va mavjudligi kafolatlanadimi?

5.  **Ishonchlilik va uzluksiz ishlash (Reliability & Uptime):**
    *   Tarmoq qanchalik ishonchli ishlaydi? Nosozliklar ehtimoli qanday?
    *   Uzluksiz ishlashni ta'minlash uchun qanday mexanizmlar (masalan, ortiqchalik – redundancy) ko'zda tutilgan?
    *   Favqulodda vaziyatlarda ma'lumotlarni tiklash rejalari (Disaster Recovery Plan) mavjudmi?

6.  **Boshqaruv va texnik xizmat ko'rsatish (Management & Maintenance):**
    *   Tarmoqni boshqarish va unga texnik xizmat ko'rsatish qanchalik murakkab?
    *   Bunga malakali xodimlar yetarlimi?
    *   Monitoring va muammolarni bartaraf etish uchun qanday vositalar mavjud?

**Xulosa:**
Tarmoq texnologiyalarini qo'llashning maqsadga muvofiqligi turli tarmoq turlarining (P2P, mijoz-server) afzallik va kamchiliklarini, tarmoq hajmi, qiymati va operatsion tizimlarni hisobga olgan holda atroflicha tahlil qilishni talab qiladi. Kichik va oddiy ehtiyojlar uchun P2P tarmoqlar arzon va oson yechim bo'lsa, katta, murakkab va yuqori xavfsizlik talablariga ega tashkilotlar uchun serverga asoslangan, ixtisoslashtirilgan serverlardan foydalangan holda arxitektura afzalroqdir. Har bir holatda, tanlov byudjet, mavjud resurslar, kelajakdagi o'sish rejalari va xavfsizlik talablariga asoslanishi kerak. Optimal yechimni tanlash tarmoqning samaradorligi, ishonchliligi va uzoq muddatli muvaffaqiyatini ta'minlaydi.
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
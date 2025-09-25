
Albatta, talab qilingan mavzu bo‘yicha ta’limiy lektsiya materialini quyidagi shablon asosida tuzib chiqdim:

---

### Lektsiya
#### Lektsiya mavzusi: Axborot xavfsizligining asosiy tushunchalari, tamoyillari, qonunchilik va standartlari (ISO 27001, NIST tahlili)

Ta’limiy materialning asosiy bo‘limlariga bo'lib boshida yozib ket:

1.  Axborot xavfsizligi tushunchasi va ahamiyati.
2.  Axborot xavfsizligining asosiy tamoyillari: Maxfiylik, Yaxlitlik, Mavjudlik (CIA Triad).
3.  Axborot xavfsizligi sohasidagi qonunchilik va me'yoriy hujjatlarning asoslari.
4.  Axborotni himoya qilish standartlarining umumiy tavsifi.
5.  Asosiy xavfsizlik standartlarini tahlil qilish: ISO/IEC 27001 va NIST Framework.
6.  Xulosa.

Ta’limiy material matni:

---

Bugungi raqamli davrda axborot har qanday tashkilot va shaxs uchun eng qimmatli aktivlardan biriga aylandi. Shu sababli, uni himoya qilish, ya’ni axborot xavfsizligini ta’minlash dolzarb vazifadir. Ushbu lektsiyada biz axborot xavfsizligining fundamental tushunchalari, uning asosiy tamoyillari, bu sohadagi qonunchilik bazasi hamda xalqaro standartlar bilan yaqindan tanishamiz.

### 1. Axborot xavfsizligi tushunchasi va ahamiyati

**Axborot xavfsizligi** – axborot va axborot tizimlarini ruxsatsiz kirish, foydalanish, oshkor qilish, buzish, o‘zgartirish yoki yo‘q qilishdan himoya qilishga qaratilgan chora-tadbirlar, jarayonlar va amaliyotlar majmuidir. Uning asosiy maqsadi axborotni uning hayotiy siklining barcha bosqichlarida ishonchli va himoyalangan holda saqlashdir.

**Ahamiyati:**

*   **Ma’lumotlar yo‘qotilishining oldini olish:** Maxfiy ma’lumotlarning oqib chiqishi yoki yo‘q qilinishi moliyaviy, obro‘-e’tibor va huquqiy oqibatlarga olib kelishi mumkin.
*   **Biznes uzluksizligini ta’minlash:** Kiberhujumlar yoki texnik nosozliklar kompaniyalarning ishini to‘xtatib qo‘yishi mumkin. Xavfsizlik choralari biznes jarayonlarining uzluksizligini kafolatlaydi.
*   **Qonuniy talablarga rioya qilish:** Ko‘pgina mamlakatlarda, jumladan O‘zbekistonda ham, ma’lumotlarni himoya qilish bo‘yicha qonuniy talablar mavjud. Ularga rioya qilish yuridik javobgarlikdan saqlaydi.
*   **Mijozlar ishonchini qozonish:** Mijozlar o‘z ma’lumotlarining xavfsizligini ta’minlaydigan tashkilotlarga ko‘proq ishonadilar.

### 2. Axborot xavfsizligining asosiy tamoyillari: Maxfiylik, Yaxlitlik, Mavjudlik (CIA Triad)

Axborot xavfsizligining asosi uchta o‘zaro bog‘liq tamoyilga tayanadi, ular "CIA Triad" (Confidentiality, Integrity, Availability) nomi bilan mashhur:

*   **Maxfiylik (Confidentiality):** Bu tamoyil axborotga faqat ruxsat etilgan shaxslar, jarayonlar yoki tizimlar kirishini ta’minlaydi. Boshqacha qilib aytganda, maxfiy ma'lumotlar ruxsatsiz shaxslar qo'liga tushmasligi kerak.
    *   **Misollar:** Parollar, biometrik autentifikatsiya, ma’lumotlarni shifrlash, kirishni boshqarish (Access Control List - ACL).
    *   **Buzilishi oqibatlari:** Maxfiy biznes rejalarning raqobatchilarga oqib chiqishi, mijozlarning shaxsiy ma’lumotlarining tarqalishi.

*   **Yaxlitlik (Integrity):** Bu tamoyil axborotning aniqligi, to‘liqligi va o‘zgaruvchanligini ta’minlaydi. Ya’ni, ma’lumotlar ruxsatsiz yoki aniqlanmagan tarzda o‘zgartirilmasligi, o‘chirilmasligi yoki buzilmasligi kerak.
    *   **Misollar:** Hashing funksiyalari (ma’lumotlarning o‘zgarmaganligini tekshirish), raqamli imzolar, ma’lumotlar bazasini tranzaksiyalarni boshqarish, fayl versiyalarini boshqarish tizimlari.
    *   **Buzilishi oqibatlari:** Moliyaviy hisobotlardagi xatolar, mijozlarning hisobraqamlaridagi noto‘g‘ri ma’lumotlar, tibbiy yozuvlardagi noto‘g‘ri ma'lumotlar tufayli noto'g'ri davolash.

*   **Mavjudlik (Availability):** Bu tamoyil ruxsat etilgan foydalanuvchilar axborotga va axborot tizimlariga ular kerak bo‘lganda kirishi mumkinligini ta’minlaydi. Tizimlar va ma’lumotlar doimiy ravishda ish holatida bo‘lishi kerak.
    *   **Misollar:** Zaxira nusxalash va tiklash rejalari (Backup & Recovery), klasterlash va yukni taqsimlash (load balancing), DoS/DDoS hujumlaridan himoya qilish, quvvat manbalarining uzluksizligi (UPS).
    *   **Buzilishi oqibatlari:** Veb-saytlarning ishlamay qolishi, onlayn bank xizmatlarining buzilishi, favqulodda xizmatlarning mavjud emasligi.

Bu uch tamoyil bir-birini to‘ldiradi va ulardan birining buzilishi boshqalariga ham salbiy ta’sir ko‘rsatishi mumkin.

### 3. Axborot xavfsizligi sohasidagi qonunchilik va me'yoriy hujjatlarning asoslari

Axborot xavfsizligi, shunchaki texnik chora-tadbirlar majmuasi emas, balki qonuniy va me'yoriy asoslarga ega bo‘lgan tizimdir. Qonunchilik va standartlar tashkilotlarga axborotni samarali himoya qilish bo‘yicha yo‘l-yo‘riq beradi, javobgarlikni belgilaydi va jazo choralarini nazarda tutadi.

*   **Qonunchilikning roli:**
    *   Axborotni himoya qilish bo‘yicha majburiy talablarni belgilaydi.
    *   Shaxsiy ma’lumotlarni qayta ishlash va saqlash qoidalarini o‘rnatadi.
    *   Kiberjinoyatlar uchun javobgarlikni belgilaydi.
    *   Davlat va maxfiy ma’lumotlarning himoyasini kafolatlaydi.
    *   *Misol:* "Shaxsiy ma’lumotlar to‘g‘risida"gi O‘zbekiston Respublikasi Qonuni.

*   **Me'yoriy hujjatlar va standartlarning roli:**
    *   Axborot xavfsizligini boshqarish bo‘yicha eng yaxshi amaliyotlarni (best practices) taqdim etadi.
    *   Tashkilotlarga risklarni baholash va ularni boshqarishda yordam beradi.
    *   Xalqaro miqyosda tan olingan yondashuvlarni joriy etishga ko‘maklashadi, bu esa hamkorlik va ishonchni oshiradi.
    *   Sertifikatlashtirish imkoniyatini beradi, bu esa tashkilotning xavfsizlikka jiddiy e’tibor berishini ko‘rsatadi.

Xalqaro miqyosda GDPR (General Data Protection Regulation) kabi qonunlar shaxsiy ma’lumotlarni himoya qilish bo‘yicha global standartlarni belgilab bergan.

### 4. Axborotni himoya qilish standartlarining umumiy tavsifi

Axborotni himoya qilish standartlari – bu axborot xavfsizligi siyosatlari, jarayonlari, texnikalari va chora-tadbirlarini ishlab chiqish, amalga oshirish va saqlash uchun tashkilotlarga yo‘l-yo‘riq beruvchi rasmiy hujjatlar to‘plami. Ular quyidagi maqsadlarga xizmat qiladi:

*   **Izchillikni ta’minlash:** Barcha bo‘limlarda va tizimlarda bir xil xavfsizlik darajasini ta’minlash.
*   **Risklarni boshqarish:** Xavfsizlikka tahdidlarni aniqlash, baholash va ularni kamaytirish bo‘yicha tizimli yondashuvni taqdim etish.
*   **Muvofiqlik (Compliance):** Tegishli qonunlar va qoidalarga rioya qilishni osonlashtirish.
*   **Ishonchni oshirish:** Hamkorlar, mijozlar va regulyatorlar oldida tashkilotning ishonchliligini namoyish etish.
*   **Uzluksiz takomillashtirish:** Xavfsizlikni boshqarish jarayonlarini muntazam ravishda ko‘rib chiqish va takomillashtirish mexanizmlarini yaratish.

Axborot xavfsizligi standartlari ko‘pincha Axborot Xavfsizligini Boshqarish Tizimini (Information Security Management System - ISMS) yaratish va joriy etish uchun asos bo‘lib xizmat qiladi.

### 5. Asosiy xavfsizlik standartlarini tahlil qilish: ISO/IEC 27001 va NIST Framework

Hozirgi kunda axborot xavfsizligi sohasida eng ko‘p qo‘llaniladigan va tan olingan standartlardan ikkitasi – bu ISO/IEC 27001 va NIST Framework.

#### 5.1. ISO/IEC 27001

**ISO/IEC 27001** – bu Axborot Xavfsizligini Boshqarish Tizimi (ISMS) uchun xalqaro standartdir. U tashkilotlarga axborot xavfsizligi risklarini boshqarish uchun tizimli yondashuvni ishlab chiqish, joriy etish, saqlash va doimiy takomillashtirishda yordam beradi.

*   **Asosiy jihatlari:**
    *   **Riskka asoslangan yondashuv:** Tashkilotlar o‘zlarining xavfsizlik risklarini aniqlashi, baholashi va ularni kamaytirish uchun tegishli choralarni ko‘rishi shart.
    *   **PDCA sikli (Plan-Do-Check-Act):** Standart ushbu doimiy takomillashtirish sikliga asoslangan:
        *   **Plan (Rejalashtirish):** ISMSni o‘rnatish, uning doirasini aniqlash va risklarni baholash.
        *   **Do (Amalga oshirish):** ISMSni joriy etish va boshqarish.
        *   **Check (Tekshirish):** ISMS faoliyatini monitoring qilish va ko‘rib chiqish.
        *   **Act (Harakat qilish):** ISMSni takomillashtirish.
    *   **Annex A (Nazorat choralari ro‘yxati):** Standartning bu qismida 14 ta domen bo‘yicha 114 ta tavsiya etilgan nazorat choralarining to‘liq ro‘yxati keltirilgan (masalan, kirishni boshqarish, kriptografiya, jismoniy va ekologik xavfsizlik, xodimlar xavfsizligi).
*   **Afzalliklari:**
    *   Xalqaro miqyosda tan olingan sertifikatni olish imkoniyati.
    *   Axborot xavfsizligini boshqarishga tizimli va samarali yondashuvni ta’minlaydi.
    *   Huquqiy talablarga rioya qilishni osonlashtiradi.
    *   Mijozlar, hamkorlar va regulyatorlar oldida ishonchni oshiradi.
*   **Kim uchun?** Barcha turdagi va hajmdagi tashkilotlar, ayniqsa maxfiy ma’lumotlar bilan ishlovchilar (banklar, sog‘liqni saqlash, IT kompaniyalar).

#### 5.2. NIST Cybersecurity Framework (CSF)

**NIST (National Institute of Standards and Technology)** – bu AQShning texnologiya sohasida standartlar ishlab chiquvchi milliy instituti. Ular tomonidan ishlab chiqilgan **Kiberxavfsizlik Doiraviy Hujjati (Cybersecurity Framework - CSF)** ixtiyoriy bo‘lib, asosan muhim infratuzilmalarni himoya qilish uchun mo‘ljallangan, ammo hozirda keng qo‘llanilmoqda.

*   **Asosiy jihatlari:**
    *   **5 ta funksiya:** Framework kiberxavfsizlikni boshqarish jarayonini 5 ta asosiy funksiyaga ajratadi:
        *   **Identify (Aniqlash):** Tizimlar, aktivlar, ma’lumotlar va imkoniyatlarni boshqarish uchun risklarni tushunish.
        *   **Protect (Himoya qilish):** Muhim infratuzilma xizmatlarining yetkazib berilishini ta’minlash uchun tegishli himoya choralarini amalga oshirish.
        *   **Detect (Aniqlash):** Kiberxavfsizlik hodisalarini o‘z vaqtida aniqlash.
        *   **Respond (Javob berish):** Aniqlangan kiberxavfsizlik hodisalariga javob berish.
        *   **Recover (Tiklash):** Kiberxavfsizlik hodisasidan keyin ish faoliyatini tiklash va chidamlilikni saqlash.
    *   **Moslashuvchanlik:** Tashkilotlarga o‘z ehtiyojlari va risk tolerantligiga qarab moslashish imkonini beradi.
    *   **Riskni boshqarishga e’tibor:** Tashkilotlarga kiberxavfsizlik risklarini tizimli ravishda tushunish, boshqarish va kamaytirishga yordam beradi.
*   **Afzalliklari:**
    *   Moslashuvchan va har qanday tashkilotga, sanoatga yoki sektorga mos keladi.
    *   Riskga asoslangan yondashuvni ta’kidlaydi.
    *   Kiberxavfsizlik to‘g‘risidagi aloqani yaxshilaydi.
    *   Mavjud standartlar va eng yaxshi amaliyotlar bilan integratsiyalashgan.
*   **Kim uchun?** Kiberxavfsizlik holatini yaxshilashni istagan barcha tashkilotlar, ayniqsa AQShda va muhim infratuzilma sektorlarida.

#### ISO 27001 va NIST CSF o‘rtasidagi farqlar va o‘xshashliklar:

*   **ISO 27001** – bu sertifikatlashtiriladigan standart bo‘lib, ISMSni joriy etishga qaratilgan tizimli va rasmiy yondashuvni taqdim etadi. U asosan nima qilish kerakligini belgilaydi (riskni boshqarish orqali).
*   **NIST CSF** – bu ixtiyoriy doiraviy hujjat bo‘lib, kiberxavfsizlik risklarini boshqarish bo‘yicha funksional yondashuvni taklif qiladi. U ko‘proq qanday qilib amalga oshirish bo‘yicha yo‘nalish beradi.
*   **O‘xshashliklar:** Ikkalasi ham riskga asoslangan, xavfsizlikni boshqarishning muhimligini ta’kidlaydi va doimiy takomillashtirishga chaqiradi. Ko‘pgina tashkilotlar ikkala standartning elementlarini o‘zlarining xavfsizlik strategiyalarida birlashtiradi.

### 6. Xulosa

Axborot xavfsizligi bugungi kunda har qanday tashkilotning muvaffaqiyati va barqarorligi uchun muhim ahamiyatga ega. Biz ko‘rib chiqqan **Maxfiylik, Yaxlitlik va Mavjudlik (CIA Triad)** tamoyillari axborotni himoya qilishning fundamental asosidir. Bu tamoyillarga qat’iy rioya qilish axborot aktivlarini samarali himoya qilishning kalitidir.

Shuningdek, axborot xavfsizligi sohasidagi **qonunchilik va standartlar** tashkilotlarga xavfsizlik choralarini to‘g‘ri yo‘naltirish, risklarni boshqarish va huquqiy talablarga rioya qilishda bebaho yo‘l-yo‘riq beradi. **ISO 27001** ISMSni tizimli ravishda joriy etish uchun xalqaro tan olingan standart bo‘lsa, **NIST CSF** esa kiberxavfsizlik risklarini boshqarish bo‘yicha moslashuvchan funksional doiraviy hujjatdir.

Axborot xavfsizligi doimiy evolyutsiyada bo‘lib, yangi tahdidlar va texnologiyalar paydo bo‘lishi bilan uzluksiz takomillashtirish va moslashishni talab qiladi. Shu sababli, bu tamoyillar va standartlarni tushunish va ularga rioya qilish har bir shaxs va tashkilot uchun muhimdir.

---
### Lektsiya
#### Lektsiya mavzusi: Mahalliy hisoblash tarmoqlari, kompyuter tarmoqlarini kengaytirish. Kompyuter tarmog'ining maqsadi. Teng huquqli tarmoqlar, tarmoq hajmi, tarmoq qiymati, operatsion tizimlar, amalga oshirish, qo'llashning maqsadga muvofiqligi. Serverga asoslangan tarmoqlar, ixtisoslashtirilgan serverlar.

Ta’limiy materialning asosiy bo'limlari:
1.  Mahalliy hisoblash tarmoqlari (LAN) va ularning maqsadi.
2.  Kompyuter tarmoqlarining asosiy turlari: Teng huquqli va serverga asoslangan tarmoqlar.
3.  Tarmoq parametrlari: Hajm, qiymat va kengaytirish imkoniyatlari.
4.  Tarmoq operatsion tizimlari (NOS) va ularning ahamiyati.
5.  Tarmoqlarni amalga oshirish, qo'llashning maqsadga muvofiqligi va afzalliklari.
6.  Ixtisoslashtirilgan serverlar va ularning vazifalari.

---

Ta’limiy material matni:

**1. Mahalliy hisoblash tarmoqlari (LAN) va ularning maqsadi.**

**Mahalliy hisoblash tarmog'i (Local Area Network - LAN)** - bu nisbatan kichik geografik hududda (masalan, ofis binosi, uy, maktab yoki universitet kampusi ichida) joylashgan kompyuterlar va boshqa qurilmalarni bir-biriga bog'laydigan kompyuter tarmog'i. LAN tarmoqlari qisqa masofalarda yuqori tezlikda ma'lumotlar uzatishni ta'minlaydi.

**Kompyuter tarmog'ining maqsadi:**
*   **Resurslarni baham ko'rish (Resource Sharing):** Eng muhim maqsadlardan biri. Foydalanuvchilar qimmatbaho resurslarni (masalan, printerlar, skanerlar, qattiq disklar, internetga ulanish) birgalikda ishlatishi mumkin. Bu xarajatlarni kamaytiradi va samaradorlikni oshiradi.
*   **Ma'lumotlar almashinuvi (Data Exchange):** Foydalanuvchilar o'rtasida fayllar, hujjatlar va boshqa ma'lumotlarni tez va oson almashish imkonini beradi.
*   **Aloqa (Communication):** Tarmoq ichida elektron pochta, xabar almashish ilovalari va video konferensiyalar orqali samarali aloqa qilishga yordam beradi.
*   **Markazlashtirilgan boshqaruv (Centralized Management):** Ma'lumotlarni markaziy joyda saqlash va boshqarish, dasturiy ta'minotni bir joydan yangilash imkoniyatini beradi. Bu xavfsizlik va ma'lumotlar zaxirasi uchun juda muhim.
*   **Ish samaradorligini oshirish (Increased Productivity):** Tarmoq orqali birgalikda ishlash imkoniyati jamoaviy ishlarni tezlashtiradi va umumiy samaradorlikni oshiradi.

**2. Kompyuter tarmoqlarining asosiy turlari: Teng huquqli va serverga asoslangan tarmoqlar.**

Kompyuter tarmoqlari arxitekturasi bo'yicha asosan ikki turga bo'linadi:

*   **Teng huquqli (Peer-to-Peer - P2P) tarmoqlar:**
    *   **Tavsif:** Bu turdagi tarmoqda har bir kompyuter ham mijoz (client), ham server (server) vazifasini bajaradi. Markaziy server mavjud emas. Har bir kompyuter o'z resurslarini (fayllar, printerlar) boshqa kompyuterlar bilan bevosita baham ko'rishi mumkin.
    *   **Afzalliklari:**
        *   O'rnatish va boshqarish oddiy, ayniqsa kichik tarmoqlar uchun.
        *   Kam xarajatli, chunki maxsus server uskunalari talab qilinmaydi.
        *   Ma'lumotlar markazlashmaganligi tufayli bir nuqta nosozligi butun tarmoqni ishdan chiqarmaydi (lekin ma'lumotlar zaxirasi qiyinlashadi).
    *   **Kamchiliklari:**
        *   Xavfsizlik darajasi past, chunki har bir kompyuter o'z xavfsizligi uchun javobgar.
        *   Ma'lumotlarni zaxiralash va markazlashtirilgan boshqaruv qiyin.
        *   Tarmoq hajmi oshgan sari ishlash samaradorligi pasayadi va boshqaruv murakkablashadi.
        *   10 tadan kam kompyuterli kichik ofislar yoki uy tarmoqlari uchun mos keladi.
    *   **Misol:** Kichik ofisda 3-5 ta kompyuterning bir-biriga ulanganligi va fayllarni bevosita almashishi.

*   **Serverga asoslangan (Client-Server) tarmoqlar:**
    *   **Tavsif:** Bu turdagi tarmoqda bir yoki bir nechta kompyuterlar **server** vazifasini bajaradi, qolganlari esa **mijozlar (clients)** hisoblanadi. Serverlar resurslarni (fayllar, ma'lumotlar bazasi, printerlar, dasturlar) markazlashtirilgan holda boshqaradi va mijozlarga xizmat ko'rsatadi. Mijozlar serverdan xizmatlarni so'raydi.
    *   **Afzalliklari:**
        *   **Yuqori xavfsizlik:** Resurslarga kirish markazlashtirilgan holda nazorat qilinadi, foydalanuvchilar va ruxsatlar boshqariladi.
        *   **Ma'lumotlarni zaxiralash va tiklash oson:** Barcha muhim ma'lumotlar serverda saqlanganligi sababli, ularni markaziy tarzda zaxiralash va tiklash mumkin.
        *   **Yaxshi ishlash samaradorligi:** Serverlar maxsus vazifalarni bajarishga mo'ljallangan bo'lib, og'ir yuk ostida ham yaxshi ishlashi mumkin.
        *   **Kengaytirish imkoniyatlari (Scalability):** Tarmoqqa yangi mijozlar yoki serverlar qo'shish oson.
        *   **Markazlashtirilgan boshqaruv:** Foydalanuvchi hisoblari, dasturiy ta'minot yangilanishlari va tarmoq siyosatlari bir joydan boshqariladi.
    *   **Kamchiliklari:**
        *   Yuqori boshlang'ich xarajatlar (server uskunalari, dasturiy ta'minot, administrator xarajatlari).
        *   O'rnatish va boshqarish murakkabroq, maxsus bilim talab qiladi.
        *   Agar server ishdan chiqsa, butun tarmoq faoliyati to'xtashi mumkin (bu "bir nuqta nosozligi" deb ataladi).
    *   **Misol:** Katta korporatsiyalar, universitetlar, internet provayderlari.

**3. Tarmoq parametrlari: Hajm, qiymat va kengaytirish imkoniyatlari.**

Tarmoqni loyihalash va amalga oshirishda ushbu parametrlarni hisobga olish muhimdir:

*   **Tarmoq hajmi (Network Size):**
    *   Tarmoqqa ulangan kompyuterlar va qurilmalar soni.
    *   Kichik tarmoqlar (10 tagacha qurilma) P2P arxitekturaga mos kelishi mumkin.
    *   O'rta va katta tarmoqlar (10 tadan ortiq, yuzlab, minglab qurilmalar) uchun serverga asoslangan arxitektura deyarli majburiydir.
    *   Hajm tarmoqning murakkabligini, uskuna talabini va boshqaruv qiyinligini belgilaydi.

*   **Tarmoq qiymati (Network Cost):**
    *   **Uskuna (Hardware):** Kompyuterlar, serverlar, tarmoq kartalari, kabellar, kalitlar (switches), marshrutizatorlar (routers), simsiz ulanish nuqtalari (access points).
    *   **Dasturiy ta'minot (Software):** Tarmoq operatsion tizimlari (Windows Server, Linux), mijoz operatsion tizimlari, xavfsizlik dasturlari, ofis ilovalari.
    *   **O'rnatish va konfiguratsiya:** Mutaxassislar tomonidan amalga oshiriladigan ishlar.
    *   **Parvarishlash va qo'llab-quvvatlash:** Muntazam texnik xizmat ko'rsatish, muammolarni bartaraf etish, yangilash.
    *   P2P tarmoqlarning boshlang'ich qiymati past bo'lsa-da, katta korxona tarmoqlari uchun serverga asoslangan tarmoqlarning umumiy samaradorligi va xavfsizligi uzoq muddatda o'zini oqlaydi.

*   **Kompyuter tarmoqlarini kengaytirish (Network Expansion):**
    *   Tarmoqni kelajakda qanday kengaytirish mumkinligi muhim jihatdir.
    *   Yangi foydalanuvchilar, qurilmalar va xizmatlarni qo'shish qanchalik osonligi.
    *   Serverga asoslangan tarmoqlar P2P ga nisbatan ancha kengaytirilishga moslashuvchan. Ular yangi serverlar, saqlash tizimlari yoki tarmoq qurilmalarini qo'shish orqali osongina o'lchanishi mumkin.
    *   Tarmoqni kengaytirishda uning dastlabki arxitekturasini to'g'ri tanlash juda muhim.

**4. Tarmoq operatsion tizimlari (NOS) va ularning ahamiyati.**

**Tarmoq operatsion tizimi (Network Operating System - NOS)** - bu tarmoqdagi barcha qurilmalarning birgalikda ishlashini ta'minlaydigan, resurslarni boshqaradigan va xavfsizlikni ta'minlaydigan dasturiy ta'minot. U mijozlarga server resurslariga kirish imkonini beradi va tarmoq faoliyatini nazorat qiladi.

*   **Asosiy vazifalari:**
    *   **Foydalanuvchi va resurslarni boshqarish:** Foydalanuvchi hisoblarini, guruhlarni yaratish, ularga tarmoq resurslariga (fayllar, printerlar) kirish huquqlarini berish.
    *   **Xavfsizlikni ta'minlash:** Foydalanuvchilarni autentifikatsiya qilish, ruxsat berish, tarmoqqa kirish qoidalarini o'rnatish, ma'lumotlarni shifrlash.
    *   **Fayl va chop etish xizmatlari:** Fayllarni markazlashtirilgan saqlash va ulashish, printerlar navbatini boshqarish.
    *   **Katalog xizmatlari (Directory Services):** Tarmoq resurslari (foydalanuvchilar, kompyuterlar, printerlar, ilovalar) haqidagi ma'lumotlarni saqlaydigan va boshqaradigan xizmat. Masalan, Microsoft Active Directory.
    *   **Ulanish va marrutlash (Routing):** Turli tarmoq segmentlari o'rtasida ma'lumotlar paketlarini yo'naltirish.

*   **Mashhur NOS namunalari:**
    *   **Microsoft Windows Server:** Korporativ muhitda eng keng tarqalgan NOS. Active Directory, Exchange Server va SQL Server kabi Microsoft ekotizimi bilan integratsiyalashgan.
    *   **Linux (masalan, Ubuntu Server, Red Hat Enterprise Linux):** Ochiq kodli va juda kuchli NOS. Veb-serverlar, fayl serverlari, ma'lumotlar bazasi serverlari va boshqa ko'plab xizmatlar uchun ishlatiladi.
    *   **Novell NetWare (tarixiy ahamiyatga ega):** Ilgari juda mashhur bo'lgan, ammo hozirda kamroq qo'llaniladigan NOS.

**5. Tarmoqlarni amalga oshirish, qo'llashning maqsadga muvofiqligi va afzalliklari.**

**Tarmoqlarni amalga oshirish (Implementation):**
1.  **Rejalashtirish:** Ehtiyojlarni aniqlash (foydalanuvchilar soni, resurslar, xavfsizlik talablari), tarmoq topologiyasini tanlash (yulduz, shina, halqa), uskuna va dasturiy ta'minotni tanlash, IP manzil sxemasini ishlab chiqish.
2.  **Uskuna o'rnatish:** Kabellarni yotqizish, kalitlar, marshrutizatorlar, serverlar va ish stantsiyalarini ulash.
3.  **Dasturiy ta'minotni konfiguratsiya qilish:** NOS o'rnatish va sozlash, mijoz operatsion tizimlarini sozlash, xavfsizlik siyosatlarini o'rnatish.
4.  **Testlash:** Ulanishlarni tekshirish, tarmoq ishlashini sinash, xavfsizlikni audit qilish.
5.  **Hujjatlashtirish:** Tarmoqning sxemasi, IP manzillar, foydalanuvchi hisoblari va boshqa muhim ma'lumotlarni hujjatlashtirish.
6.  **O'qitish:** Foydalanuvchilarga tarmoq resurslaridan foydalanish bo'yicha yo'l-yo'riq berish.

**Qo'llashning maqsadga muvofiqligi (Feasibility of Application):**
Kompyuter tarmog'ini qo'llash quyidagi hollarda maqsadga muvofiqdir:
*   Bir nechta foydalanuvchi bir xil resurslarga (printer, internet, dasturiy ta'minot) kirishga muhtoj bo'lsa.
*   Korxonada ma'lumotlar almashinuvi va jamoaviy ishlash muhim ahamiyatga ega bo'lsa.
*   Ma'lumotlarning markazlashtirilgan xavfsizligi va zaxirasi talab qilinsa.
*   Operatsion xarajatlarni kamaytirish va samaradorlikni oshirish kerak bo'lsa.
*   Biznesning kelajakdagi o'sishini hisobga olgan holda moslashuvchan infratuzilma zarur bo'lsa.
*   Foydalanuvchilar o'rtasida samarali aloqani ta'minlash.

**Afzalliklari (Advantages):**
*   **Xarajatlarni tejash:** Resurslarni baham ko'rish orqali qimmat uskunalarni (printerlar kabi) har bir foydalanuvchiga alohida sotib olish shart emas.
*   **Yuqori samaradorlik:** Foydalanuvchilar ma'lumotlarga tezda kirishi, birgalikda ishlashi va axborotni samarali almashishi mumkin.
*   **Xavfsizlik:** Markazlashtirilgan xavfsizlik tizimlari ma'lumotlarni ruxsatsiz kirishdan himoya qilishga yordam beradi (serverga asoslangan tarmoqlar uchun).
*   **Ma'lumotlar yaxlitligi:** Markazlashtirilgan ma'lumotlar bazalari va fayl serverlari ma'lumotlarning izchilligi va yaxlitligini ta'minlaydi.
*   **Qayta tiklash imkoniyati:** Ma'lumotlarni markaziy ravishda zaxiralash va nosozlik yuz berganda tiklash oson.

**6. Ixtisoslashtirilgan serverlar va ularning vazifalari.**

Serverga asoslangan tarmoqlarda har xil turdagi serverlar mavjud bo'lib, ular ma'lum bir vazifalarni bajarishga ixtisoslashgan:

*   **Fayl serveri (File Server):** Fayllarni (hujjatlar, rasmlar, videolar) saqlash va ularni tarmoqdagi foydalanuvchilarga taqdim etishga ixtisoslashgan. U fayllarga kirish huquqlarini ham boshqaradi.
*   **Chop etish serveri (Print Server):** Tarmoqdagi printerlarni boshqaradi, chop etish navbatlarini tashkil etadi va chop etish ishlarini foydalanuvchilarga taqsimlaydi.
*   **Ma'lumotlar bazasi serveri (Database Server):** Ma'lumotlar bazalarini (masalan, SQL Server, Oracle, MySQL) joylashtiradi va mijoz ilovalariga ma'lumotlarga kirish va ularni boshqarish imkonini beradi.
*   **Web server (Web Server):** Veb-saytlarni joylashtiradi va mijozlarning (brauzerlar) veb-sahifalarni so'rovlariga javob beradi (masalan, Apache, Nginx, Microsoft IIS).
*   **Pochta serveri (Mail Server):** Elektron pochta xabarlarini qabul qilish, saqlash, yuborish va yo'naltirishni boshqaradi (masalan, Microsoft Exchange, Postfix).
*   **DNS serveri (DNS Server):** Domain Name System (DNS) xizmatini taqdim etadi, ya'ni domen nomlarini (masalan, google.com) IP manzillariga tarjima qiladi.
*   **DHCP serveri (DHCP Server):** Dynamic Host Configuration Protocol xizmatini taqdim etadi, tarmoqdagi qurilmalarga avtomatik ravishda IP manzillar, tarmoq maskalari, shlyuzlar va DNS server manzillarini tayinlaydi.
*   **Proksi server (Proxy Server):** Mijoz va boshqa server o'rtasida vositachi bo'lib xizmat qiladi. U xavfsizlikni oshirish, tarmoq trafikini filtrlash, kesh xotira orqali veb-sahifalarga tezroq kirishni ta'minlash uchun ishlatiladi.
*   **Ilova serveri (Application Server):** Ma'lum bir biznes ilovalarini (masalan, ERP, CRM tizimlari) ishga tushirish va ularga mijozlar orqali kirishni ta'minlaydi.

Har bir ixtisoslashtirilgan server ma'lum bir vazifani bajarishga yo'naltirilgan bo'lib, bu tarmoqning umumiy samaradorligini oshiradi, boshqaruvni soddalashtiradi va har bir xizmat uchun optimal ishlashni ta'minlaydi.

---

**Xulosa:**

Mahalliy hisoblash tarmoqlari zamonaviy dunyoda, xoh uy, xoh kichik ofis, xoh yirik korxona bo'lsin, axborot texnologiyalarining ajralmas qismidir. Ular resurslarni baham ko'rish, samarali aloqa va ma'lumotlar almashinuvi orqali tashkilotlarning samaradorligini oshiradi. Tarmoq arxitekturasini (teng huquqli yoki serverga asoslangan) tanlashda tarmoq hajmi, qiymati, xavfsizlik talablari va kelajakdagi kengaytirish imkoniyatlari kabi omillarni hisobga olish muhimdir. Tarmoq operatsion tizimlari va ixtisoslashtirilgan serverlar esa tarmoqning ishonchli, xavfsiz va samarali ishlashini ta'minlovchi asosiy komponentlardir. To'g'ri rejalashtirilgan va amalga oshirilgan tarmoq har qanday tashkilot uchun qimmatli aktiv hisoblanadi.
### Lektsiya
#### Lektsiya mavzusi: OSI modeli. IEEE Project 802 modeli, OSI modelining kengaytmasi. Drayverlar va tarmoq dasturiy taʼminoti, tarmoq adapteri drayveri. Paket tuzilishi, asosiy komponentlar. Protokollar. Kommutatsiya.

Ta’limiy materialning asosiy bo‘limlariga bo'lib boshida yozib ket:
1.  OSI modeli (Ochiq Tizimlar O'zaro Aloqasi Modeli)
2.  IEEE Project 802 modeli va uning OSI bilan aloqasi
3.  Drayverlar va tarmoq dasturiy taʼminoti
4.  Tarmoq paketining tuzilishi
5.  Tarmoq protokollari
6.  Kommutatsiya turlari

Ta’limiy material matni:

Tarmoq texnologiyalari zamonaviy axborot almashinuvi uchun asos bo'lib xizmat qiladi. Kompyuterlar va boshqa qurilmalar o'rtasida samarali aloqa o'rnatish uchun standartlashtirilgan qoidalar va mexanizmlar zarur. Ushbu lektsiyada biz tarmoq aloqasining fundamental tamoyillarini, jumladan, OSI va IEEE 802 modellarini, drayverlarning rolini, ma'lumotlar paketining tuzilishini, protokollarni va kommutatsiya usullarini ko'rib chiqamiz.

---

### 1. OSI modeli (Ochiq Tizimlar O'zaro Aloqasi Modeli)

**OSI (Open Systems Interconnection) modeli** – bu Xalqaro Standartlashtirish Tashkiloti (ISO) tomonidan ishlab chiqilgan kontseptual model bo‘lib, u turli xil kompyuter tizimlari o'rtasidagi aloqa jarayonini standartlashtirish va tushunish uchun umumiy yondashuvni ta'minlaydi. U tarmoq aloqasini har biri o'ziga xos vazifaga ega bo'lgan yetti alohida qatlamga ajratadi. Bu qatlamli yondashuv tarmoqni loyihalash, tahlil qilish va muammolarni bartaraf etishni osonlashtiradi.

**OSI modelining 7 ta qatlami:**

1.  **Jismoniy qatlam (Physical Layer – 1-qatlam):** Ma'lumotlarning elektr, optik yoki radio signallari ko'rinishida jismoniy tashuvchi (kabel, optik tolali kabel, simsiz aloqa) orqali uzatilishini belgilaydi. Bu qatlam bitlarning (0 va 1) uzatilishini nazorat qiladi. Masalan: kabel turlari, konnektorlar, voltaj darajalari.
2.  **Kanal qatlami (Data Link Layer – 2-qatlam):** Jismoniy muhit orqali ma'lumotlarni ishonchli uzatishni ta'minlaydi. Bu qatlam jismoniy manzilni (MAC manzil) boshqaradi, xatolarni aniqlash va tuzatish mexanizmlarini ishga tushiradi, hamda ma'lumotlarni "kadrlar" (frames) ga shakllantiradi.
3.  **Tarmoq qatlami (Network Layer – 3-qatlam):** Turli tarmoqlar (subnetlar) bo'ylab ma'lumotlar paketlarini (datagram) manbadan maqsadga marshrutlash (yo'naltirish) uchun javobgardir. IP manzillar bu qatlamda ishlatiladi. Routerlar bu qatlamda ishlaydi.
4.  **Transport qatlami (Transport Layer – 4-qatlam):** Ilovalar orasida ma'lumotlarni ishonchli va tartibli yetkazishni ta'minlaydi. Bu qatlam ma'lumotlarni segmentlarga bo'ladi, ularni qayta yig'adi, xatolarni tekshiradi va oqimni boshqaradi. TCP va UDP protokollari shu qatlamda ishlaydi.
5.  **Seans qatlami (Session Layer – 5-qatlam):** Turli ilovalar o'rtasidagi aloqa seanslarini o'rnatish, boshqarish va yakunlash uchun javobgar. U dialoglarni nazorat qiladi (kim qachon gapirishi mumkin).
6.  **Taqdimot qatlami (Presentation Layer – 6-qatlam):** Ma'lumotlarning formatini, kodlashini va shifrlanishini boshqaradi, shunda turli tizimlar o'rtasida ma'lumotlar bir-biriga tushunarli bo'ladi. Masalan, JPEG, ASCII, shifrlash (encryption) va deşifrlash (decryption).
7.  **Dastur qatlami (Application Layer – 7-qatlam):** Foydalanuvchi ilovalari va tarmoq xizmatlari o'rtasidagi interfeysni ta'minlaydi. Bu qatlamda foydalanuvchi tarmoqqa to'g'ridan-to'g'ri kirish imkoniyatiga ega bo'lgan protokollar ishlaydi. Masalan: HTTP (veb-sahifalar), FTP (fayl uzatish), SMTP (elektron pochta).

**Ma'lumotlar oqimi:** Ma'lumotlar dastur qatlamidan jismoniy qatlamga qarab har bir qatlamda o'zining sarlavhasini (header) qo'shib, "kapsüllash" (encapsulation) qilinadi. Qabul qiluvchi tomonda esa bu jarayon teskari tartibda, ya'ni har bir qatlam o'zining sarlavhasini olib tashlab, "de-kapsüllash" (de-encapsulation) qiladi.

### 2. IEEE Project 802 modeli va uning OSI bilan aloqasi

**IEEE Project 802** – bu Amerika Elektrotexnika va Elektronika Muhandislari Instituti (IEEE) tomonidan Lokal Kompyuter Tarmoqlari (LAN) va Metropolitan Kompyuter Tarmoqlari (MAN) standartlarini belgilash uchun yaratilgan loyihalar to'plami. U asosan OSI modelining dastlabki ikki qatlami – Jismoniy (1-qatlam) va Kanal (2-qatlam) qatlamlarining aniq texnologiyalarini kengaytiradi va aniqlashtiradi.

**OSI modelining kengaytmasi:**

IEEE 802 loyihasi OSI modelining 2-qatlamini (Kanal qatlami) ikkita kichik qatlamga ajratadi:

1.  **Mantiqiy bog'lanishni boshqarish (Logical Link Control - LLC) – IEEE 802.2:** Bu kichik qatlam yuqori qatlamlar (masalan, Tarmoq qatlami) uchun yagona interfeysni ta'minlaydi va jismoniy texnologiyalardan mustaqil ravishda aloqani boshqaradi. U ma'lumotlarni multiplekslash, demultiplekslash va xatolarni tekshirish kabi vazifalarni bajaradi.
2.  **Mediaga kirishni boshqarish (Media Access Control - MAC) – IEEE 802.3, 802.11 va boshqalar:** Bu kichik qatlam jismoniy muhitga kirishni boshqaradi, ya'ni bir nechta qurilma bir xil jismoniy muhitdan qanday foydalanishini aniqlaydi. U har bir tarmoq adapteriga berilgan noyob MAC manzilini ishlatadi va ma'lumotlar kolliziyalarini (to'qnashuvlarini) oldini olish yoki boshqarish mexanizmlarini o'z ichiga oladi.

**IEEE 802 standartlariga misollar:**

*   **IEEE 802.3 (Ethernet):** Eng keng tarqalgan simli LAN texnologiyasi. U ma'lumotlarni uzatish tezligi, kabel turlari va kadr tuzilishini belgilaydi.
*   **IEEE 802.11 (Wi-Fi):** Simsiz lokal tarmoqlar uchun standartlar to'plami. U radio to'lqinlari orqali ma'lumotlarni uzatish usullarini, xavfsizlik protokollarini belgilaydi.
*   **IEEE 802.1Q (VLAN):** Virtual Lokal Tarmoqlar (VLAN) uchun standart bo'lib, bir jismoniy tarmoqni bir nechta mantiqiy tarmoqlarga bo'lish imkonini beradi.

### 3. Drayverlar va tarmoq dasturiy taʼminoti

**Drayver (Driver)** – bu operatsion tizim (OS) va apparat (hardware) o'rtasidagi aloqani ta'minlovchi dasturiy ta'minot. Har bir apparat qurilmasi, masalan, tarmoq adapteri, printer, grafik karta uchun maxsus drayver talab qilinadi. Drayver operatsion tizimga qurilmani qanday boshqarishni va uning imkoniyatlaridan qanday foydalanishni "o'rgatadi".

**Tarmoq adapteri drayveri:** Bu maxsus drayver tarmoq kartasi (Network Interface Card - NIC) bilan operatsion tizim o'rtasidagi interfeysni ta'minlaydi. Uning asosiy vazifalari:
*   Operatsion tizimdan kelgan raqamli ma'lumotlarni tarmoq adapteri tushunadigan formatga aylantirish.
*   Tarmoq adapteri qabul qilgan signallarni operatsion tizim tushunadigan raqamli ma'lumotlarga aylantirish.
*   Tarmoq kartasining funksiyalarini boshqarish (masalan, ma'lumotlarni uzatish tezligi, dupleks rejimi).
*   Tarmoq xatolarini aniqlash va ularni operatsion tizimga xabar berish.

**Tarmoq dasturiy taʼminoti:** Bu kompyuter tarmoqlari orqali aloqa qilish imkonini beruvchi barcha dasturiy komponentlar. U quyidagilarni o'z ichiga oladi:
*   **Operatsion tizimning tarmoq stacki:** Har bir zamonaviy operatsion tizim (Windows, Linux, macOS) tarmoq stackiga ega bo'lib, u OSI modelining turli qatlamlari (Transport, Tarmoq, Kanal) funksiyalarini bajaradi. Bu stack protokollarni (masalan, TCP/IP) amalga oshiradi va ilovalarga tarmoq xizmatlaridan foydalanish imkonini beradi.
*   **Tarmoq ilovalari:** Brauzerlar (Chrome, Firefox), elektron pochta klientlari (Outlook), fayl uzatish dasturlari (FTP klientlari), messenjerlar (Telegram, Zoom) kabi dasturlar tarmoq orqali aloqa qilish uchun tarmoq stackidan foydalanadi.

Drayver va tarmoq dasturiy ta'minoti birgalikda ishlaydi: Dasturiy ta'minot (masalan, brauzer) ma'lumot yuborishni so'raydi -> OS ning tarmoq stacki ma'lumotlarni protokollarga muvofiq shakllantiradi (kapsüllaydi) -> Drayver bu ma'lumotlarni tarmoq adapteriga yuborish uchun tayyorlaydi -> Tarmoq adapteri ma'lumotlarni jismoniy muhitga chiqaradi.

### 4. Tarmoq paketining tuzilishi

**Paket** – bu tarmoq orqali uzatiladigan ma'lumotlarning mantiqiy birligi. Aslida, "paket" atamasi umumiy bo'lib, OSI modelining turli qatlamlarida ma'lumotlar o'ziga xos nomlarga ega bo'ladi:
*   **Kadr (Frame):** Kanal qatlamida (2-qatlam).
*   **Datagram/Paket (Datagram/Packet):** Tarmoq qatlamida (3-qatlam).
*   **Segment (Segment):** Transport qatlamida (4-qatlam).

Har bir paketning asosiy komponentlari mavjud:

1.  **Sarlavha (Header):** Paketning boshida joylashgan bo'lib, ma'lumotlarni uzatish uchun zarur bo'lgan boshqaruv ma'lumotlarini o'z ichiga oladi. Sarlavha tarkibi paketning qaysi qatlamda ekanligiga va qaysi protokol ishlatilayotganiga bog'liq. Umumiy elementlar:
    *   **Manzil manzili (Source Address):** Paketni yuboruvchi qurilmaning manzili (MAC, IP).
    *   **Maqsad manzili (Destination Address):** Paketni qabul qiluvchi qurilmaning manzili (MAC, IP).
    *   **Protokol turi (Protocol Type):** Paketdagi yuklamada qaysi yuqori qatlam protokoli borligini ko'rsatadi (masalan, IP, ARP).
    *   **Uzunlik (Length):** Paketning umumiy uzunligi.
    *   **Xizmat turi (Type of Service):** Paketga qanday ustuvorlik berilishini ko'rsatadi.
    *   **Xato tekshiruvi (Checksum):** Sarlavhaning yoki butun paketning butunligini tekshirish uchun ishlatiladigan qiymat.
    *   **Identifikatorlar va fragmentatsiya ma'lumotlari:** Agar paket bo'laklarga bo'lingan bo'lsa, ularni qayta yig'ish uchun ma'lumotlar.

2.  **Yuklama (Payload / Data):** Bu paketning asosiy qismi bo'lib, foydalanuvchi ma'lumotlari yoki yuqori qatlam protokolining ma'lumotlarini o'z ichiga oladi. Masalan, veb-sahifa matni, elektron pochta mazmuni, faylning bir qismi.

3.  **Treyler (Trailer):** Paketning oxirida joylashgan bo'lib, asosan xatolarni tekshirish uchun ishlatiladi. Masalan, **Kadrni tekshirish ketma-ketligi (Frame Check Sequence - FCS)** – bu CRC (Cyclic Redundancy Check) algoritmi yordamida hisoblangan qiymat bo'lib, ma'lumotlarni uzatishda yuzaga kelgan xatolarni aniqlashga yordam beradi.

**Misollar:**
*   **Ethernet kadr:** MAC manzil, manzil manzili, uzunlik/tur, yuklama, FCS (treyler).
*   **IP datagram:** IP manzil, maqsad manzili, protokol turi, TTL (Time To Live), yuklama (TCP/UDP segmenti).
*   **TCP segment:** Port raqamlari, ketma-ketlik raqami, tasdiqlash raqami, nazorat bayroqlari, yuklama (ilova ma'lumotlari).

### 5. Tarmoq protokollari

**Protokol** – bu kompyuterlar yoki boshqa tarmoq qurilmalari o'rtasidagi aloqani boshqaruvchi qoidalar va tartiblarning rasmiy to'plami. Ular aloqaning har bir jihatini – ma'lumotlarni formatlashdan tortib, xatolarni boshqarishgacha – belgilaydi. Protokollar aloqani standartlashtirishga yordam beradi, shunda turli ishlab chiqaruvchilarning turli xil tizimlari bir-biri bilan muammosiz muloqot qila oladi.

**Nima uchun protokollar kerak?**
*   **Standartlashtirish:** Aloqa qoidalarini universal qilish.
*   **O'zaro ishlash (Interoperability):** Turli tizimlarning bir-biri bilan aloqa qilishini ta'minlash.
*   **Ishonchlilik:** Ma'lumotlarning to'g'ri va to'liq yetkazilishini kafolatlash.
*   **Xizmatlarni ta'minlash:** Turli tarmoq xizmatlarini (veb, elektron pochta, fayl uzatish) tashkil qilish.

**Protokollar to'plami (Protocol Suite):** Ko'pincha, turli qatlamlarda ishlaydigan protokollar birgalikda ishlatiladi va bir protokollar to'plamini tashkil etadi. Eng mashhuri **TCP/IP protokollar to'plami** bo'lib, u Internetning asosi hisoblanadi.

**Turli qatlamlardagi protokollar va ularning vazifalari:**

*   **Dastur qatlami (7-qatlam):** Foydalanuvchi ilovalariga tarmoq xizmatlarini taqdim etadi.
    *   **HTTP (Hypertext Transfer Protocol):** Veb-sahifalarni uzatish.
    *   **HTTPS (HTTP Secure):** Shifrlangan HTTP.
    *   **FTP (File Transfer Protocol):** Fayllarni uzatish.
    *   **SMTP (Simple Mail Transfer Protocol):** Elektron pochta yuborish.
    *   **POP3/IMAP (Post Office Protocol 3 / Internet Message Access Protocol):** Elektron pochta qabul qilish.
    *   **DNS (Domain Name System):** Domen nomlarini IP manzillarga aylantirish.
    *   **SSH (Secure Shell):** Xavfsiz masofaviy kirish.

*   **Transport qatlami (4-qatlam):** Ilovalar o'rtasida ma'lumotlarni yetkazishni ta'minlaydi.
    *   **TCP (Transmission Control Protocol):** Bog'lanishga yo'naltirilgan, ishonchli, xatolarni nazorat qiluvchi ma'lumot uzatish.
    *   **UDP (User Datagram Protocol):** Bog'lanishsiz, tezkor, kam xizmat ko'rsatadigan ma'lumot uzatish (ovozli va video chatlar uchun).

*   **Tarmoq qatlami (3-qatlam):** Tarmoqlararo marshrutlash va manzillash.
    *   **IP (Internet Protocol):** Paketlarni manbadan maqsadga marshrutlash, IP manzillash.
    *   **ICMP (Internet Control Message Protocol):** Tarmoq qurilmalari orasidagi xato xabarlari (masalan, "ping" buyrug'i).
    *   **ARP (Address Resolution Protocol):** IP manzilni MAC manziliga aylantirish.

*   **Kanal qatlami (2-qatlam):** Lokal tarmoq ichida jismoniy manzil bo'yicha ma'lumotlarni uzatish.
    *   **Ethernet:** Simli LAN.
    *   **Wi-Fi (IEEE 802.11):** Simsiz LAN.

### 6. Kommutatsiya turlari

**Kommutatsiya** – bu tarmoqda ma'lumotlarni bir manbadan ikkinchi maqsadga yo'naltirish jarayoni. U tarmoq resurslarini samarali boshqarish va ma'lumotlarni to'g'ri yo'nalish bo'ylab yetkazish uchun ishlatiladi. Asosan ikki turdagi kommutatsiya mavjud:

1.  **Kanalli kommutatsiya (Circuit Switching):**
    *   **Prinsipi:** Ma'lumotlarni uzatishdan oldin, manba va maqsad o'rtasida butun aloqa seansi davomida doimiy, maxsus kanal (sxema) o'rnatiladi. Aloqa tugagach, kanal bo'shatiladi.
    *   **Ishlash mexanizmi:** Go'yoki "telefon liniyasi" kabi: qo'ng'iroq qilganingizda, ikkita tomon o'rtasida eksklyuziv ulanish o'rnatiladi va suhbat tugaguncha boshqa hech kim bu kanaldan foydalana olmaydi.
    *   **Afzalliklari:**
        *   Uzatish davomida doimiy va kafolatlangan tarmoqli kenglik.
        *   Minimal kechikish.
        *   Aloqa o'rnatilgandan so'ng juda ishonchli.
    *   **Kamchiliklari:**
        *   Kanal o'rnatish uchun vaqt talab etiladi.
        *   Resurslarni samarasiz ishlatish (agar kanal bo'sh tursa ham, u band hisoblanadi).
        *   Agar bitta kanal muvaffaqiyatsiz bo'lsa, butun aloqa uziladi.
    *   **Qo'llanilish sohalari:** An'anaviy telefon tarmoqlari (PSTN).

2.  **Paketli kommutatsiya (Packet Switching):**
    *   **Prinsipi:** Ma'lumotlar uzatishdan oldin kichik, alohida "paketlarga" bo'linadi. Har bir paket o'zining manzil va maqsad ma'lumotlarini o'z ichiga oladi va tarmoq orqali mustaqil ravishda yo'naltiriladi. Paketlar turli yo'llar orqali manzilga yetib borishi mumkin va keyinchalik maqsad manzilda qayta yig'iladi.
    *   **Ishlash mexanizmi:** Pochta tizimi kabi: har bir xat (paket) alohida konvertga solinadi, manzil yoziladi va pochta tizimi (tarmoq) orqali yetkaziladi. Xatlar har xil yo'llar orqali yetib borishi mumkin.
    *   **Afzalliklari:**
        *   Resurslardan samarali foydalanish (kanallar faqat ma'lumot uzatilayotganda band bo'ladi).
        *   Tarmoqning yuqori bardoshliligi (agar bitta yo'l muvaffaqiyatsiz bo'lsa, paketlar boshqa yo'llar orqali yuborilishi mumkin).
        *   Bir vaqtning o'zida ko'plab foydalanuvchilarni qo'llab-quvvatlash.
        *   Turli xil aloqa turlarini (ovoz, video, ma'lumot) bitta tarmoq orqali uzatish imkoniyati.
    *   **Kamchiliklari:**
        *   Paketlar har xil yo'llar orqali yetib kelishi mumkin, bu esa kechikishlar va tartibsizlikka olib kelishi mumkin.
        *   Paketlarni qayta yig'ish uchun qo'shimcha ishlov berish talab etiladi.
        *   Xavfsizlik masalalari (agar paketlar shifrlanmagan bo'lsa, ularni ushlash mumkin).
    *   **Qo'llanilish sohalari:** Internet, lokal tarmoqlar (LAN), mobil ma'lumotlar tarmoqlari.

**Paketli kommutatsiyaning ikki turi:**
*   **Datagram kommutatsiya (Datagram Switching):** Har bir paket butunlay mustaqil bo'lib, o'z yo'lini mustaqil ravishda tanlaydi. Qabul qiluvchi tomonda paketlar to'g'ri tartibda yig'ilishi kerak. Internet asosan datagram kommutatsiya asosida ishlaydi.
*   **Virtual kanal kommutatsiya (Virtual Circuit Switching):** Paketlarni yuborishdan oldin mantiqiy "virtual kanal" o'rnatiladi. Paketlar shu virtual kanal bo'ylab ketma-ket yuboriladi, garchi jismoniy jihatdan ular hali ham paketlar sifatida alohida uzatilsa ham. Bu ishonchlilikni oshiradi, lekin ma'lum darajada resurslarni band qiladi (ATM, Frame Relay).

---

Xulosa qilib aytganda, tarmoq aloqasi murakkab, ammo yaxshi tuzilgan jarayon bo'lib, u OSI va IEEE 802 kabi modellar tomonidan standartlashtirilgan. Drayverlar va tarmoq dasturiy ta'minoti apparat va dastur o'rtasida ko'prik vazifasini o'taydi, protokollar esa aloqa qoidalarini belgilaydi. Ma'lumotlar paketlar shaklida, aniq tuzilishga ega bo'lib uzatiladi va kommutatsiya mexanizmlari bu paketlarni manbadan maqsadga samarali yo'naltiradi. Ushbu komponentlarning barchasi birgalikda zamonaviy global tarmoqlarimizning uzluksiz ishlashini ta'minlaydi.
### Lektsiya
#### Lektsiya mavzusi: Tahdid turlari: maxfiylikka, yaxlitlikka, mavjudlikka hujumlar. Tarmoqlardagi zaifliklarni aniqlash. Taklif qilingan axborot tizimi uchun tahdid va hujumchi modelini yaratish.

Ta’limiy materialning asosiy bo‘limlari:
1.  KIRISH: Axborot xavfsizligining asosiy prinsiplari – CIA triadasiga kirish.
2.  Axborotga tahdid turlari va ularning Maxfiylik (Confidentiality), Yaxlitlik (Integrity), Mavjudlik (Availability) prinsiplariga hujumlari.
3.  Tarmoqlardagi zaifliklarni aniqlash usullari va metodologiyalari.
4.  Tahdid modeli (Threat Modeling) va uni yaratish bosqichlari.
5.  Hujumchi modeli (Attacker Modeling) va uning turlari.
6.  Axborot tizimi uchun tahdid va hujumchi modelini yaratish metodologiyasi (amaliy misollar bilan).
7.  Xulosa.

---

Ta’limiy material matni:

### 1. KIRISH: Axborot xavfsizligining asosiy prinsiplari – CIA triadasiga kirish.

Bugungi raqamli dunyoda axborot har qanday tashkilotning eng qimmatli aktivlaridan biri hisoblanadi. Axborotning xavfsizligini ta’minlash, uni ruxsatsiz kirish, foydalanish, oshkor qilish, o‘zgartirish, yo‘q qilish yoki buzilishdan himoya qilish ustuvor vazifadir. Axborot xavfsizligi tushunchasining asosi "CIA triada"si deb nomlanuvchi uchta asosiy prinsipga tayanadi: Maxfiylik (Confidentiality), Yaxlitlik (Integrity) va Mavjudlik (Availability).

*   **Maxfiylik (Confidentiality):** Axborotga faqat vakolatli shaxslar yoki tizimlar kirishi mumkinligini ta'minlash. Ruxsatsiz shaxslar axborotni ko'ra olmaydilar, unga kira olmaydilar yoki uni o'zlashtira olmaydilar.
*   **Yaxlitlik (Integrity):** Axborotning aniqligi, to'liqligi va ishonchliligi, shuningdek, uning faqat vakolatli shaxslar tomonidan ruxsat etilgan usulda o'zgartirilishini ta'minlash. Axborot tasodifan yoki qasddan buzilmasligi kerak.
*   **Mavjudlik (Availability):** Vakolatli foydalanuvchilar axborotga va tizimlarga istalgan vaqtda, kerak bo'lganda kirish imkoniyatiga ega bo'lishini ta'minlash. Tizim va ma'lumotlar foydalanish uchun doimiy ravishda mavjud bo'lishi kerak.

Ushbu uchta prinsip har qanday axborot tizimining xavfsizligini baholash va ta'minlashda asosiy yo'nalish bo'lib xizmat qiladi.

### 2. Axborotga tahdid turlari va ularning Maxfiylik, Yaxlitlik, Mavjudlik prinsiplariga hujumlari.

**Tahdid** — bu tizimga zarar yetkazishi yoki uning xavfsizligini buzishi mumkin bo'lgan har qanday potentsial voqea. Ushbu bo'limda CIA triadasi prinsiplariga qaratilgan asosiy tahdid turlarini ko'rib chiqamiz.

#### 2.1. Maxfiylikka hujumlar (Confidentiality Attacks)

Maxfiylikka qilingan hujumlar axborotni ruxsatsiz shaxslarga oshkor qilishga qaratilgan.
*   **Ta'rifi:** Ruxsatsiz shaxslarning maxfiy ma'lumotlarga kirishiga, ularni ko'rishiga yoki o'zlashtirishiga olib keladigan harakatlar.
*   **Hujum turlari:**
    *   **Ma'lumotlarni o'g'irlash (Data Theft):** Ma'lumotlar bazalaridan, serverlardan yoki shaxsiy qurilmalardan maxfiy ma'lumotlarni noqonuniy ravishda nusxalash yoki ko'chirish.
    *   **Eshitish (Eavesdropping):** Tarmoq orqali uzatilayotgan ma'lumotlarni ushlash va tinglash. Bunga tarmoq tahlilchilari (packet sniffers) yordamida erishish mumkin.
    *   **Noqonuniy kirish (Unauthorized Access):** Tizimga ruxsatsiz kirib, maxfiy ma'lumotlarga ega bo'lish. Bu kuchli parol tanlash, tizimdagi zaifliklardan foydalanish orqali amalga oshirilishi mumkin.
    *   **Kiber josuslik (Cyber Espionage):** Hukumatlar, kompaniyalar yoki raqiblar tomonidan maxfiy siyosiy, iqtisodiy yoki texnologik ma'lumotlarni o'g'irlash.
    *   **Ijtimoiy injeneriya (Social Engineering):** Shaxslarni aldash orqali maxfiy ma'lumotlarni (masalan, parollar) olishga urinish. Fishing, vishing va smishing kabi usullar keng tarqalgan.
*   **Misollar:**
    *   Hakerning ma'lumotlar bazasiga kirib, mijozlarning shaxsiy ma'lumotlarini (ism-sharif, manzil, telefon) o'g'irlashi.
    *   Tarmoqda shifrlanmagan parollarni ushlab olish.
    *   Fishing orqali foydalanuvchidan bank kartasi ma'lumotlarini olish.

#### 2.2. Yaxlitlikka hujumlar (Integrity Attacks)

Yaxlitlikka qilingan hujumlar ma'lumotlarning aniqligi, to'liqligi va o'zgaruvchanligini buzishga qaratilgan.
*   **Ta'rifi:** Axborotni ruxsatsiz o'zgartirish, o'chirish yoki buzish. Bu ma'lumotlarning ishonchliligini yo'qotadi.
*   **Hujum turlari:**
    *   **Ma'lumotlarni o'zgartirish (Data Tampering):** Ma'lumotlar bazasidagi yozuvlarni, fayllar kontentini yoki tranzaksiya ma'lumotlarini noqonuniy ravishda o'zgartirish.
    *   **Zararli dasturlar (Malware):** Viruslar, troyan otlari, rootkitlar va boshqa zararli dasturlar tizimga kirib, ma'lumotlarni buzish, o'chirish yoki o'zgartirish.
    *   **Man-in-the-Middle (MITM) hujumi:** Hujumchi ikki tomonlama aloqa o'rtasiga kirib, xabarlarni ushlab oladi, o'zgartiradi va keyin maqsadga yuboradi.
    *   **Veb-sayt buzish (Website Defacement):** Veb-sayt kontentini o'zgartirib, uni buzilgan holatda namoyish qilish.
*   **Misollar:**
    *   Bank tizimidagi tranzaksiya summalarini o'zgartirib, katta mablag'larni o'z hisobiga o'tkazish.
    *   Biror kompaniyaning veb-saytidagi mahsulot narxlarini noto'g'ri ko'rsatish.
    *   Xodimning ish haqi hisobotini o'zgartirib, o'z foydasiga noto'g'ri ma'lumotlar kiritish.

#### 2.3. Mavjudlikka hujumlar (Availability Attacks)

Mavjudlikka qilingan hujumlar tizim yoki ma'lumotlarning foydalanuvchilar uchun mavjudligini buzishga qaratilgan.
*   **Ta'rifi:** Vakolatli foydalanuvchilarning axborotga va tizimlarga kirish imkoniyatini cheklash yoki butunlay to'xtatish.
*   **Hujum turlari:**
    *   **Xizmat ko'rsatishni rad etish (Denial of Service - DoS) / Taqsimlangan xizmat ko'rsatishni rad etish (Distributed Denial of Service - DDoS) hujumlari:** Server yoki tarmoq resurslarini haddan tashqari ko'p so'rovlar bilan to'ldirib, uni ishdan chiqarish.
    *   **Resurslarni to'ldirish (Resource Exhaustion):** Tizim resurslarini (CPU, xotira, disk maydoni) haddan tashqari ko'p ishlatish orqali uning ishlashini to'xtatish.
    *   **Jismoniy hujumlar:** Server xonalariga kirib, uskunani shikastlash yoki quvvatni uzish.
    *   **Ransomware (To'lov talab qiluvchi dastur):** Tizimdagi ma'lumotlarni shifrlab, ularni qayta tiklash uchun to'lov talab qilish. Agar to'lov to'lanmasa, ma'lumotlar yo'q bo'lishi mumkin.
*   **Misollar:**
    *   Yirik elektron tijorat veb-saytini DDoS hujumi orqali mijozlar uchun foydalanishga yaroqsiz holga keltirish.
    *   Kompaniya serveriga o'rnatilgan ransomware barcha fayllarni shifrlab, biznes jarayonlarini to'xtatib qo'yish.
    *   Elektr ta'minotining uzilishi natijasida ma'lumotlar markazining ishdan chiqishi.

### 3. Tarmoqlardagi zaifliklarni aniqlash usullari.

**Zaiflik** – bu axborot tizimi, tarmoq, dasturiy ta'minot, аппарат ёки protseduradagi kamchilik bo'lib, undan foydalanib xavfsizlik tahdidini amalga oshirish mumkin.

#### 3.1. Zaiflik turlari:
*   **Dasturiy ta'minotdagi xatolar (Software Bugs):** Xavfsizlikka oid kamchiliklar, masalan, bufer to'lib ketishi, SQL Inyeksiya, XSS.
*   **Noto'g'ri konfiguratsiya (Misconfiguration):** Standart parollar, ochiq portlar, keraksiz xizmatlar, kuchsiz autentifikatsiya.
*   **Inson omili (Human Factor):** Kuchsiz parollar, fishing qurboni bo'lish, ma'lumotlarni tasodifan oshkor qilish.
*   **Tarmoq arxitekturasi kamchiliklari:** Yaxshi segmentatsiyaning yo'qligi, noto'g'ri joylashtirilgan xavfsizlik devorlari.

#### 3.2. Zaifliklarni aniqlash vositalari va metodologiyalari:
*   **Avtomatlashtirilgan zaiflik skanerlari (Vulnerability Scanners):**
    *   **Ta'rifi:** Tarmoqdagi qurilmalarni, serverlarni va veb-ilovalarini avtomatik tarzda skanerlab, ma'lum zaifliklar va konfiguratsiya kamchiliklarini aniqlaydigan dasturlar.
    *   **Misollar:** Nessus, OpenVAS, Qualys.
    *   **Afzalliklari:** Tez, avtomatlashtirilgan, keng qamrovli dastlabki tahlil.
    *   **Kamchiliklari:** Noto'g'ri pozitsiyalar (false positives) berishi mumkin, murakkab mantiqiy zaifliklarni aniqlay olmaydi.
*   **Penetratsion testlash (Penetration Testing - PenTest):**
    *   **Ta'rifi:** Axborot tizimining xavfsizligini tekshirish uchun ruxsat berilgan, qasddan qilingan hujum simulyatsiyasi. Mutaxassislar tizimdagi zaifliklarni topishga harakat qilishadi va ulardan real hujumchi kabi foydalanishga urinadilar.
    *   **Turlari:**
        *   **Qora quti (Black-box):** Tester tizim haqida hech qanday ma'lumotga ega bo'lmaydi (real hujumchi kabi).
        *   **Kulrang quti (Gray-box):** Tester tizim haqida qisman ma'lumotlarga ega bo'ladi (masalan, foydalanuvchi hisobi).
        *   **Oq quti (White-box):** Tester tizimning barcha ma'lumotlariga (kod, konfiguratsiya, arxitektura) ega bo'ladi.
    *   **Bosqichlari:** Rejalashtirish, razvedka (axborot yig'ish), skanerlash, kirish (exploitlash), kirishni saqlash (post-exploitation), izlarni tozalash, hisobot berish.
*   **Xavfsizlik auditi (Security Audit):**
    *   **Ta'rifi:** Tizimlarning, konfiguratsiyaning, xavfsizlik siyosatlarining va protseduralarining standartlarga va eng yaxshi amaliyotlarga muvofiqligini baholash.
    *   **Nimalarni o'z ichiga oladi:** Konfiguratsiya fayllarini ko'rib chiqish, log fayllarini tahlil qilish, xavfsizlik siyosatlarini tekshirish, intervyular.
*   **Kod tahlili (Code Review):**
    *   **Ta'rifi:** Dastur kodini xavfsizlik kamchiliklari, xatolar va zaifliklar uchun tekshirish.
    *   **Turlari:** Statik (kodni ishga tushirmasdan) va dinamik (kodni ishga tushirib).
*   **OSINT (Open-Source Intelligence):**
    *   **Ta'rifi:** Ochiq manbalardan (veb-saytlar, ijtimoiy tarmoqlar, umumiy ma'lumotlar bazalari) ma'lumot yig'ish. Hujumchilar ushbu ma'lumotlardan zaifliklarni aniqlash yoki ijtimoiy injeneriya hujumlarini rejalashtirish uchun foydalanishi mumkin.

### 4. Tahdid modeli (Threat Modeling) va uning bosqichlari.

**Tahdid modeli** – bu axborot tizimining xavfsizlik zaifliklarini aniqlash, potentsial tahdidlarni baholash va ularni bartaraf etish yoki ularning ta'sirini kamaytirish uchun strategiyalarni ishlab chiqish jarayoni. Bu xavfsizlikni loyihalash bosqichida integratsiyalashga yordam beradi, shu bilan xavfsizlik kamchiliklarini keyinroq topish va tuzatish xarajatlarini kamaytiradi.

**Nega muhim?**
*   Xavfsizlikni dizayn bosqichidan boshlab ko'rib chiqishga imkon beradi.
*   Potentsial tahdidlarga qarshi proaktiv choralar ko'rishga yordam beradi.
*   Xavfsizlikka oid qarorlarni xabardor tarzda qabul qilishni ta'minlaydi.

**Tahdid modelini yaratishning asosiy bosqichlari (STRIDE modeli asosida):**

1.  **Tizimni aniqlash va diagramma tuzish (Identify Assets & Draw Diagram):**
    *   Tizimning chegaralari, asosiy komponentlari (serverlar, ma'lumotlar bazalari, ilovalar), ma'lumotlar oqimi va ishonch chegaralari (trust boundaries) aniqlanadi. Ma'lumotlar oqimi diagrammasi (Data Flow Diagram - DFD) yaratish tavsiya etiladi.
2.  **Tahdidlarni aniqlash (Identify Threats):**
    *   Har bir komponent va ma'lumotlar oqimi uchun potentsial tahdidlar aniqlanadi. Buning uchun ko'pincha STRIDE metodologiyasidan foydalaniladi:
        *   **S**poofing (Soxtalashtirish): Identifikatsiyani soxtalashtirish.
        *   **T**ampering (O'zgartirish): Ma'lumotlarni yoki jarayonlarni o'zgartirish.
        *   **R**epudiation (Rad etish): Harakatlarni rad etish imkoniyati.
        *   **I**nformation Disclosure (Ma'lumotlarni oshkor qilish): Maxfiy ma'lumotlarni ruxsatsiz oshkor qilish.
        *   **D**enial of Service (Xizmat ko'rsatishdan bosh tortish): Tizim yoki resurslarning mavjudligini buzish.
        *   **E**levation of Privilege (Imtiyozlarni oshirish): Kamroq imtiyozli foydalanuvchining ko'proq imtiyozlarga ega bo'lishi.
3.  **Zaifliklarni aniqlash (Identify Vulnerabilities):**
    *   Aniqlangan tahdidlar uchun tizimdagi mavjud yoki potentsial zaifliklar (dizayn xatolari, konfiguratsiya kamchiliklari, dasturiy ta'minotdagi xatolar) topiladi.
4.  **Tahdidlarni kamaytirish (Mitigate Threats):**
    *   Har bir aniqlangan tahdid va zaiflik uchun tegishli nazorat choralari (kontrollar) ishlab chiqiladi va joriy etiladi. Bular texnik (shifrlash, autentifikatsiya, xavfsizlik devori) va tashkiliy (siyosatlar, treninglar) choralar bo'lishi mumkin.
5.  **Tekshirish (Verify Mitigation):**
    *   Joriy etilgan nazorat choralarining samaradorligi tekshiriladi. Bu penetratsion testlash, xavfsizlik auditi yoki boshqa sinovlar orqali amalga oshirilishi mumkin.

### 5. Hujumchi modeli (Attacker Modeling) va uning turlari.

**Hujumchi modeli** – bu potentsial hujumchining motivatsiyalari, imkoniyatlari, texnik ko'nikmalari va resurslarini tushunish jarayoni. Bu model tahdid modelini to'ldiradi va xavfsizlik strategiyalarini yanada samaraliroq ishlab chiqishga yordam beradi.

**Nega muhim?**
*   Hujumlar ehtimolini va ta'sirini aniqroq baholash imkonini beradi.
*   Qanday hujumchilardan himoyalanish kerakligini aniqlashga yordam beradi.
*   Eng katta xavflarga ustuvorlik berishga imkon beradi.

**Hujumchi turlari:**
*   **Script Kiddies:** Texnik bilimlari past, mavjud vositalar va skriptlardan foydalanadigan hujumchilar. Ular ko'pincha qiziqish yoki shon-shuhrat uchun harakat qiladi.
*   **Xakerlar (Hackers):**
    *   **Oq shlyapa (White-hat):** Etik xakerlar, xavfsizlikni yaxshilash maqsadida zaifliklarni aniqlaydigan mutaxassislar.
    *   **Qora shlyapa (Black-hat):** Yovuz niyatli xakerlar, noqonuniy yo'llar bilan tizimlarga kiradigan va zarar yetkazadigan shaxslar.
    *   **Kulrang shlyapa (Gray-hat):** Ba'zan noqonuniy yo'llar bilan zaifliklarni aniqlaydigan, lekin keyin ularni ommaga oshkor qiladigan shaxslar.
*   **Ichki tahdidlar (Insider Threats):** Tashkilotning ichida ishlaydigan xodimlar, sobiq xodimlar yoki pudratchilar tomonidan keladigan tahdidlar. Ular ma'lumotlarga kirish huquqiga ega bo'lganligi sababli juda xavfli bo'lishi mumkin.
*   **Davlat tomonidan qo'llab-quvvatlanadigan guruhlar (State-sponsored Actors):** Hukumatlar tomonidan moliyalashtiriladigan va yo'naltiriladigan yuqori malakali hujumchi guruhlar. Ular odatda josuslik, sabotaj yoki kiber urush maqsadlarida harakat qiladi.
*   **Jinoiy tashkilotlar (Organized Crime):** Pul ishlash maqsadida kiberhujumlar (masalan, to'lov talab qiluvchi dasturlar, moliyaviy firibgarlik) amalga oshiradigan guruhlar.
*   **Aktivistlar (Hacktivists):** Ijtimoiy yoki siyosiy maqsadlarda kiberhujumlar (masalan, veb-saytlarni buzish, ma'lumotlarni oshkor qilish) amalga oshiradigan guruhlar.

**Hujumchining motivatsiyasi:**
*   Moliyaviy foyda (pul o'g'irlash, shantaj).
*   Obro' (tizimni buzish orqali shuhrat qozonish).
*   Siyosiy yoki ijtimoiy sabablar (protest, josuslik).
*   Sabotaj (raqibga zarar yetkazish).
*   Qasos (norozi xodim yoki raqib).

**Hujumchining imkoniyatlari:**
*   **Texnik ko'nikmalar:** Zaifliklarni topish va ekspluatatsiya qilish uchun zarur bo'lgan bilim va tajriba.
*   **Moliyaviy resurslar:** Qimmat vositalarni, nol kunlik zaifliklarni sotib olish yoki katta miqyosli DDoS hujumlarini uyushtirish uchun pul.
*   **Vaqt va resurslar:** Hujumga tayyorgarlik ko'rish va uni amalga oshirish uchun sarflanishi mumkin bo'lgan vaqt va inson resurslari.

### 6. Axborot tizimi uchun tahdid va hujumchi modelini yaratish metodologiyasi (amaliy misollar bilan).

Endi nazariy bilimlarni amaliyotda qo'llashni ko'rib chiqamiz. Misol sifatida "Onlayn-banking mobil ilovasi"ni olamiz.

**1. Tizimni tasvirlash va diagramma tuzish:**
*   **Tizim:** Mobil banking ilovasi.
*   **Asosiy komponentlar:** Mobil ilova (foydalanuvchi interfeysi), Mobil ilova API serveri, Autentifikatsiya/Avtorizatsiya serveri, Ma'lumotlar bazasi (mijoz ma'lumotlari, tranzaksiya tarixi), Boshqa bank xizmatlari bilan integratsiyalar.
*   **Ma'lumotlar oqimi:** Mijozning mobil ilova orqali hisobiga kirishi, pul o'tkazmalari, balansni tekshirish, shaxsiy ma'lumotlarni yangilash.
*   **Ishonch chegaralari:** Mobil qurilma va server o'rtasida, API server va ma'lumotlar bazasi o'rtasida.

**2. STRIDE modeli orqali tahdidlarni aniqlash:**

*   **S (Spoofing - Soxtalashtirish):**
    *   _Tahdid:_ Hujumchi mobil ilova foydalanuvchisi sifatida o'zini ko'rsatishi (akkauntni egallash) yoki soxta bank veb-sayti/ilovasini yaratib, mijoz ma'lumotlarini olish.
    *   _Zaifliklar:_ Kuchsiz parollar, ikki faktorli autentifikatsiyaning yo'qligi, fishing hujumlariga qarshi zaiflik.
*   **T (Tampering - O'zgartirish):**
    *   _Tahdid:_ Pul o'tkazish paytida tranzaksiya summalarini yoki qabul qiluvchi hisob raqamini o'zgartirish. Ma'lumotlar bazasidagi mijoz ma'lumotlarini buzish.
    *   _Zaifliklar:_ Tranzaksiya ma'lumotlarini serverda tekshirmaslik, ma'lumotlar bazasiga kirish nazoratining pastligi, server va ilova o'rtasidagi aloqani himoyalamaslik.
*   **R (Repudiation - Rad etish):**
    *   _Tahdid:_ Mijoz pul o'tkazmasini amalga oshirganini rad etishi yoki bank xodimi tizimdagi o'zgarishni rad etishi.
    *   _Zaifliklar:_ Tranzaksiyalarni loglashning yo'qligi yoki yetarli emasligi, kuchsiz audit izlari.
*   **I (Information Disclosure - Ma'lumotlarni oshkor qilish):**
    *   _Tahdid:_ Mijozlarning shaxsiy ma'lumotlari (bank hisob raqami, balans, shaxsiy identifikatsiya ma'lumotlari) uchinchi shaxslarga oshkor bo'lishi.
    *   _Zaifliklar:_ Ma'lumotlarni shifrlashning yo'qligi (ma'lumotlar bazasida, uzatishda), xato yuzasidan ma'lumotlarni ko'p oshkor qilish, mobil ilovaning mahalliy xotirasida maxfiy ma'lumotlarni saqlash.
*   **D (Denial of Service - Xizmat ko'rsatishdan bosh tortish):**
    *   _Tahdid:_ Bank mobil ilovasi serverlariga DDoS hujumi qilib, mijozlarning ilovadan foydalanishiga to'sqinlik qilish.
    *   _Zaifliklar:_ DDoS himoyasining yo'qligi, serverlarning yuklamaga bardosh bera olmasligi, tarmoq resurslarining yetarli emasligi.
*   **E (Elevation of Privilege - Imtiyozlarni oshirish):**
    *   _Tahdid:_ Oddiy mijoz hisobiga ega bo'lgan shaxsning administrator huquqlariga ega bo'lishi.
    *   _Zaifliklar:_ Zaif avtorizatsiya mexanizmlari, API zaifliklari, ruxsatlarni noto'g'ri boshqarish.

**3. Hujumchi modelini yaratish:**

*   **Hujumchi turlari:**
    *   **Jinoiy guruhlar:** Asosiy motivatsiya – moliyaviy foyda (pul o'g'irlash, mijoz ma'lumotlarini sotish). Imkoniyatlari yuqori texnik bilimlarga va katta resurslarga ega bo'lishi mumkin.
    *   **Ichki xodimlar:** Motivatsiya – qasos, moliyaviy foyda, noto'g'ri e'tiqodlar. Tizim haqida ichki bilimlarga ega, ma'lumotlarga kirish huquqlari bo'lishi mumkin.
    *   **Raqib banklar/korporativ josuslar:** Motivatsiya – raqobat ustunligini olish, ma'lumotlarni o'g'irlash. Yuqori darajadagi texnik imkoniyatlar.
*   **Ehtimoliy hujum yo'nalishlari:**
    *   Mobil ilova zaifliklari (masalan, noto'g'ri ma'lumotlarni saqlash, ruxsatlarning noto'g'ri ishlatilishi).
    *   APIga hujumlar (masalan, API kalitlarini egallash, zaif API endpointlarini ekspluatatsiya qilish).
    *   Veb-saytga hujumlar (agar ilova veb-xizmatlarga bog'liq bo'lsa).
    *   Ijtimoiy injeneriya (fishing orqali foydalanuvchi parollarini olish).

**4. Tahdidlarni baholash va ustuvorlik berish:**
*   Har bir tahdidning ehtimolligi (past, o'rta, yuqori) va ta'siri (past, o'rta, yuqori) baholanadi.
*   Masalan, "Jinoiy guruhlar tomonidan DDoS hujumi"ning ehtimolligi "yuqori" va ta'siri "yuqori" bo'lishi mumkin, chunki u bankning asosiy xizmatini to'xtatadi.
*   "Oddiy mijozning imtiyozlarni oshirishi"ning ehtimolligi "o'rta" bo'lishi mumkin, ta'siri esa, agar u administrator huquqiga ega bo'lsa, "yuqori" bo'ladi.

**5. Nazorat choralarini ishlab chiqish:**
*   **Spoofingga qarshi:** Kuchli autentifikatsiya (MFA), biometrik autentifikatsiya, fishingga qarshi foydalanuvchi treninglari, sertifikat pinlash (certificate pinning).
*   **Tamperingga qarshi:** Barcha tranzaksiya ma'lumotlarini serverda tekshirish, ma'lumotlar bazasiga kirishni qattiq nazorat qilish, ma'lumotlarni shifrlash, hashing va raqamli imzo.
*   **Repudiationga qarshi:** Barcha muhim harakatlar va tranzaksiyalarni batafsil loglash, audit izlarini ta'minlash, tranzaksiyalar uchun raqamli imzo.
*   **Information Disclosurega qarshi:** Ma'lumotlarni uzatishda (TLS) va saqlashda (at rest encryption) shifrlash, mobil ilovada maxfiy ma'lumotlarni saqlamaslik, minimal imtiyoz prinsipiga amal qilish.
*   **DoS/DDoSga qarshi:** DDoS himoya xizmatlari (CDN, WAF), yuklamani balansirlovchi tizimlar, tarmoq resurslarini optimallashtirish.
*   **Elevation of Privilegega qarshi:** Autentifikatsiya va avtorizatsiyani to'g'ri amalga oshirish, APIlarning xavfsizligini ta'minlash, muntazam penetratsion testlar.

### 7. Xulosa.

Axborot xavfsizligi doimiy rivojlanib boruvchi soha bo'lib, tahdidlar landshafti ham tinimsiz o'zgarib turadi. Maxfiylik, Yaxlitlik va Mavjudlik prinsiplari har qanday xavfsizlik strategiyasining asosini tashkil etadi. Tahdid modellarini va hujumchi modellarini yaratish proaktiv xavfsizlikni ta'minlashda muhim ahamiyatga ega. Ushbu modellar axborot tizimlarini loyihalash, ishlab chiqish va qo'llab-quvvatlash jarayonlarining har bir bosqichida xavflarni aniqlash, baholash va kamaytirish uchun tizimli yondashuvni ta'minlaydi. Ularni muntazam ravishda yangilab borish va qayta ko'rib chiqish orqali tashkilotlar o'z aktivlarini samaraliroq himoya qilishlari mumkin.
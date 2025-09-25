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
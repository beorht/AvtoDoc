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
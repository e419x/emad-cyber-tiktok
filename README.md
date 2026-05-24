<div align="center">

![EMAD CYBER Banner](banner.png)

# ⚡ EMAD CYBER — TikTok OSINT Tool `v2.0`

### 🕶️  Cyberpunk-flavored recon tool for TikTok intelligence gathering

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Platform](https://img.shields.io/badge/Platform-TikTok-black?style=for-the-badge&logo=tiktok&logoColor=white)](https://www.tiktok.com)
[![TikTok](https://img.shields.io/badge/TikTok-@49mu-FF0050?style=for-the-badge&logo=tiktok&logoColor=white)](https://www.tiktok.com/@49mu)
[![GitHub](https://img.shields.io/badge/GitHub-@e419x-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/e419x)
[![License](https://img.shields.io/badge/License-Educational-red?style=for-the-badge)](#)
[![Version](https://img.shields.io/badge/Version-2.0-00ffd5?style=for-the-badge)](#)

</div>

---

## ✨ ما الجديد في الإصدار 2.0

> تحديث شامل للواجهة بطابع هاكر سايبربانك 🟢🟣🩷

- 🎨 **واجهة سايبربانك متكاملة** — ألوان نيون (سيان / بنفسجي / وردي / أخضر) متدرّجة
- 🌧️ **Matrix Rain** عند البدء — مؤثر شاشة شبيه بالأفلام
- 📊 **صناديق ASCII أنيقة** لعرض النتائج (Profile Intel + Social Metrics + Bio)
- ⚙️ **شريط تقدّم وspinner** أثناء الجلب
- 🔢 **تنسيق الأرقام** مع فواصل (مثال: `162,300,000`)
- ✔️ **عرض حالة التحقق** (Verified ✓)
- 🛡️ **معالجة أخطاء أفضل** + Timeout للطلبات
- 🖼️ **اكتشاف رابط الـ Avatar** تلقائيًا
- 📐 **استجابة لحجم الطرفية** (Banner كبير / مصغّر تلقائيًا)

---

## 🎯 المعلومات التي تستخرجها الأداة

| # | المعلومة | الوصف |
|---|----------|--------|
| 1 | 👤 **Username** | اسم المستخدم |
| 2 | 🏷️ **Nickname** | الاسم الظاهر |
| 3 | 🆔 **User ID** | المعرّف الفريد |
| 4 | 🔑 **SecUID** | المعرّف الأمني |
| 5 | 📅 **Created Date** | تاريخ إنشاء الحساب (يُحسب من الـ ID) |
| 6 | 🌍 **Region** | الدولة + علم البلد |
| 7 | 🔒 **Private** | هل الحساب خاص؟ |
| 8 | ✔️ **Verified** | حالة التوثيق |
| 9 | 👥 **Followers** | عدد المتابعين |
| 10 | 📲 **Following** | عدد المتابَعين |
| 11 | 🤝 **Friends** | عدد الأصدقاء |
| 12 | ❤️ **Likes** | إجمالي الإعجابات |
| 13 | 🎬 **Videos** | عدد الفيديوهات |
| 14 | 📝 **Bio** | السيرة الذاتية |
| 15 | 🖼️ **Avatar URL** | رابط صورة الحساب |
| 16 | 🔗 **Profile URL** | رابط الحساب |

---

## ⚙️ المتطلبات

- 🐍 Python `3.8+`
- 🌐 اتصال بالإنترنت
- 💻 طرفيّة تدعم ألوان ANSI (Linux / macOS / WSL / Termux / Windows Terminal)

---

## 📦 التثبيت والتشغيل

```bash
# 1️⃣ استنساخ المستودع
git clone https://github.com/e419x/emad-cyber-tiktok.git
cd emad-cyber-tiktok

# 2️⃣ تثبيت المكتبات
pip install -r requirements.txt

# 3️⃣ تشغيل الأداة
python3 imadtik.py
```

### 📱 على Termux (Android)

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/e419x/emad-cyber-tiktok.git
cd emad-cyber-tiktok
pip install -r requirements.txt
python imadtik.py
```

---

## 🚀 طريقة الاستخدام

```text
┌──(49mu㉿emad-cyber)
└─▶ Enter TikTok username: tiktok
```

### 🖼️ مثال على المخرجات

```text
╔═══ ⚡ PROFILE INTEL ═════════════════════════════════════════╗
║  ▸ USERNAME      │ @tiktok                                  ║
║  ▸ NICKNAME      │ TikTok                                   ║
║  ▸ USER ID       │ 107955                                   ║
║  ▸ REGION        │ United States 🇺🇸                         ║
║  ▸ STATUS        │ ✔ Verified                               ║
╚══════════════════════════════════════════════════════════════╝

╔═══ 📊 SOCIAL METRICS ════════════════════════════════════════╗
║  ▸ FOLLOWERS     │ 82,900,000                               ║
║  ▸ FOLLOWING     │ 1,542                                    ║
║  ▸ TOTAL LIKES   │ 672,400,000                              ║
║  ▸ VIDEOS        │ 1,893                                    ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 🗂️ هيكل المشروع

```text
emad-cyber-tiktok/
├── 📜 imadtik.py          ← الأداة الرئيسية (v2.0)
├── 📋 requirements.txt    ← المكتبات
├── 🖼️  banner.png          ← شعار المستودع
└── 📖 README.md           ← هذا الملف
```

---

## 🧠 كيف تعمل؟

تقوم الأداة بإرسال طلب HTTP GET إلى صفحة الحساب على TikTok مع هيدرز محاكية لمتصفح أندرويد، ثم تستخرج بيانات `webapp.user-detail` من JSON المضمَّن في HTML. تاريخ الإنشاء يُحسب رياضيًا من أول 31 بت من الـ User ID (timestamp ضمني).

---

## ⚠️ إخلاء المسؤولية

> 🛑 هذه الأداة لأغراض **تعليمية وبحثية بحتة** (OSINT / Open-Source Intelligence).
> لا يتحمّل المطوّر أي مسؤولية عن أي استخدام غير قانوني أو غير أخلاقي.
> يُرجى الالتزام بـ [شروط خدمة TikTok](https://www.tiktok.com/legal/terms-of-service) و[سياسة GitHub للاستخدام المقبول](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies).

---

## 👨‍💻 المطوّر

<div align="center">

### ⚡ EMAD CYBER ⚡

**Made with 💚 & ☕ by [@e419x](https://github.com/e419x)**

🎵 TikTok :: [`@49mu`](https://www.tiktok.com/@49mu)
🐙 GitHub :: [`e419x`](https://github.com/e419x)

⭐ **أعجبتك الأداة؟ لا تنسَ النجمة على GitHub!**

</div>

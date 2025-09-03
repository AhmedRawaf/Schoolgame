# من أنا في الجدول الدوري؟ - Periodic Table Quiz

## 🌟 نظرة عامة / Overview

تطبيق ويب تفاعلي لاختبار معرفة الطلاب بالعناصر الكيميائية من الجدول الدوري. يحول التطبيق الأصلي المكتوب بـ Python Tkinter إلى تطبيق ويب يمكن الوصول إليه من أي متصفح.

An interactive web application for testing students' knowledge of chemical elements from the periodic table. Converts the original Python Tkinter application into a web app accessible from any browser.

## ✨ المميزات / Features

- 🎯 **أسئلة متنوعة**: رموز، أسماء، أعداد ذرية، مجموعات كيميائية
- 📊 **ثلاثة مستويات صعوبة**: سهل، متوسط، صعب
- ⏱️ **مؤقت قابل للتخصيص**: لكل سؤال
- 🆘 **مساعدة 50:50**: مرة واحدة لكل اختبار
- 💾 **حفظ النتائج**: ملفات CSV للمعلمين
- 📱 **تصميم متجاوب**: يعمل على جميع الأجهزة
- 🌐 **واجهة عربية**: مكتوبة بالكامل باللغة العربية

## 🚀 التثبيت والتشغيل / Installation & Setup

### المتطلبات / Requirements
- Python 3.7+
- pip (مدير الحزم)

### الخطوات / Steps

1. **تثبيت المتطلبات / Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

2. **تشغيل التطبيق / Run Application**
   ```bash
   python app.py
   ```

3. **فتح المتصفح / Open Browser**
   ```
   http://localhost:5000
   ```

## 🌍 النشر على الإنترنت / Deploy Online

### Heroku
```bash
# إنشاء تطبيق Heroku
heroku create your-app-name

# رفع الكود
git add .
git commit -m "Initial commit"
git push heroku main
```

### PythonAnywhere
1. ارفع الملفات إلى حساب PythonAnywhere
2. أنشئ تطبيق Flask جديد
3. اضبط مسار الملفات
4. ابدأ التطبيق

### Vercel
```bash
# تثبيت Vercel CLI
npm i -g vercel

# نشر التطبيق
vercel
```

### Railway
1. اربط حساب GitHub بـ Railway
2. اختر المستودع
3. اضبط متغيرات البيئة
4. ابدأ النشر

## 📁 هيكل الملفات / File Structure

```
├── app.py              # التطبيق الرئيسي / Main Flask app
├── templates/          # قوالب HTML / HTML templates
│   ├── index.html     # الصفحة الرئيسية / Home page
│   ├── quiz.html      # صفحة الاختبار / Quiz page
│   └── results.html   # صفحة النتائج / Results page
├── requirements.txt    # متطلبات Python / Python dependencies
└── README.md          # هذا الملف / This file
```

## 🎮 كيفية الاستخدام / How to Use

1. **إدخال البيانات**: اسم الطالب والصف
2. **اختيار الإعدادات**: مستوى الصعوبة، عدد الأسئلة، الوقت
3. **بدء الاختبار**: الإجابة على الأسئلة مع المؤقت
4. **استخدام المساعدة**: زر 50:50 لإزالة خيارين خاطئين
5. **عرض النتائج**: مراجعة مفصلة مع التفسيرات
6. **حفظ النتائج**: ملفات CSV للمعلمين

## 🔧 التخصيص / Customization

### إضافة عناصر جديدة / Add New Elements
```python
# في ملف app.py
ELEMENTS.append({
    "Z": 94,
    "symbol": "Pu",
    "name": "بلوتونيوم",
    "group": "أكتينيد",
    "period": 7
})
```

### تعديل الألوان / Modify Colors
```css
/* في ملفات HTML */
:root {
    --primary-color: #6ee7b7;
    --secondary-color: #60a5fa;
    --background-color: #0b1020;
}
```

## 📊 حفظ النتائج / Results Storage

التطبيق يحفظ النتائج في ملفين CSV:

1. **results_summary.csv**: ملخص النتائج
   - الطالب، الصف، المستوى، النتيجة، النسبة المئوية

2. **results_detailed.csv**: تفاصيل كل إجابة
   - السؤال، الإجابة المختارة، الإجابة الصحيحة، التصحيح

## 🐛 استكشاف الأخطاء / Troubleshooting

### مشاكل شائعة / Common Issues

1. **خطأ في المنفذ / Port Error**
   ```bash
   # تغيير المنفذ
   app.run(port=8000)
   ```

2. **مشكلة في الترميز / Encoding Issue**
   ```python
   # تأكد من إضافة
   # -*- coding: utf-8 -*-
   ```

3. **مشكلة في الجلسة / Session Issue**
   ```python
   # تغيير مفتاح الجلسة
   app.secret_key = 'your_new_secret_key'
   ```

## 📞 الدعم / Support

للمساعدة أو الإبلاغ عن مشاكل:
- أنشئ issue في GitHub
- راسل المطور عبر البريد الإلكتروني

## 📄 الترخيص / License

هذا المشروع مفتوح المصدر ومتاح للاستخدام التعليمي.

## 🤝 المساهمة / Contributing

نرحب بالمساهمات! يرجى:
1. عمل fork للمشروع
2. إنشاء branch جديد
3. إجراء التغييرات
4. عمل pull request

---

**تم التطوير بـ ❤️ للتعليم الكيميائي**

**Developed with ❤️ for Chemical Education**

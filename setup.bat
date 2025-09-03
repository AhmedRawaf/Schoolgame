@echo off
chcp 65001 >nul
title من أنا في الجدول الدوري؟ - Periodic Table Quiz Setup

echo.
echo ========================================
echo 🌟 من أنا في الجدول الدوري؟ - Periodic Table Quiz
echo 🌟 Web Application Setup for Windows
echo ========================================
echo.

echo 📋 فحص النظام...
echo 📋 Checking system...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Python is already installed
    goto :install_requirements
) else (
    echo ❌ Python is not installed
    echo.
    echo 📥 تثبيت Python...
    echo 📥 Installing Python...
    echo.
    echo يرجى تثبيت Python من الموقع الرسمي:
    echo Please install Python from the official website:
    echo https://www.python.org/downloads/
    echo.
    echo تأكد من تحديد "Add Python to PATH" أثناء التثبيت
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    goto :end
)

:install_requirements
echo.
echo 📦 تثبيت المتطلبات...
echo 📦 Installing requirements...

pip install -r requirements.txt
if %errorlevel% equ 0 (
    echo ✅ تم تثبيت المتطلبات بنجاح
    echo ✅ Requirements installed successfully
) else (
    echo ❌ فشل في تثبيت المتطلبات
    echo ❌ Failed to install requirements
    echo.
    echo حاول تشغيل الأمر التالي يدوياً:
    echo Try running this command manually:
    echo pip install -r requirements.txt
    pause
    goto :end
)

echo.
echo 🎉 تم الإعداد بنجاح!
echo 🎉 Setup completed successfully!
echo.
echo لتشغيل التطبيق، استخدم:
echo To run the application, use:
echo python app.py
echo.
echo ثم افتح المتصفح على:
echo Then open your browser to:
echo http://localhost:5000
echo.

:run_choice
set /p choice="هل تريد تشغيل التطبيق الآن؟ (y/n): "
if /i "%choice%"=="y" (
    echo.
    echo 🚀 بدء تشغيل التطبيق...
    echo 🚀 Starting the application...
    echo.
    echo سيتم فتح المتصفح تلقائياً بعد ثانيتين
    echo Browser will open automatically in 2 seconds
    echo.
    timeout /t 2 /nobreak >nul
    start http://localhost:5000
    python app.py
) else if /i "%choice%"=="n" (
    echo.
    echo 👋 شكراً لك! يمكنك تشغيل التطبيق لاحقاً
    echo 👋 Thank you! You can run the application later
) else (
    echo.
    echo يرجى الإجابة بـ y أو n
    echo Please answer with y or n
    goto :run_choice
)

:end
echo.
echo اضغط أي مفتاح للخروج...
echo Press any key to exit...
pause >nul

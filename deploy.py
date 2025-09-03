#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
سكريبت النشر السريع للتطبيق
Quick deployment script for the application
"""

import os
import sys
import subprocess
import webbrowser
import time

def check_python():
    """التحقق من إصدار Python"""
    if sys.version_info < (3, 7):
        print("❌ خطأ: تحتاج Python 3.7 أو أحدث")
        print("Error: You need Python 3.7 or newer")
        return False
    print("✅ Python version:", sys.version.split()[0])
    return True

def install_requirements():
    """تثبيت المتطلبات"""
    print("📦 تثبيت المتطلبات...")
    print("Installing requirements...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ تم تثبيت المتطلبات بنجاح")
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ فشل في تثبيت المتطلبات")
        print("❌ Failed to install requirements")
        return False

def create_directories():
    """إنشاء المجلدات المطلوبة"""
    dirs = ["templates", "static", "uploads"]
    for dir_name in dirs:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print(f"📁 تم إنشاء مجلد: {dir_name}")

def start_app():
    """تشغيل التطبيق"""
    print("🚀 بدء تشغيل التطبيق...")
    print("🚀 Starting the application...")
    
    # فتح المتصفح بعد ثانيتين
    def open_browser():
        time.sleep(2)
        webbrowser.open("http://localhost:5000")
    
    import threading
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # تشغيل Flask
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 تم إيقاف التطبيق")
        print("👋 Application stopped")

def main():
    """الدالة الرئيسية"""
    print("=" * 50)
    print("🌟 من أنا في الجدول الدوري؟ - Periodic Table Quiz")
    print("🌟 Web Application Setup")
    print("=" * 50)
    
    # التحقق من Python
    if not check_python():
        return
    
    # إنشاء المجلدات
    create_directories()
    
    # تثبيت المتطلبات
    if not install_requirements():
        return
    
    print("\n🎉 تم الإعداد بنجاح! يمكنك الآن تشغيل التطبيق")
    print("🎉 Setup completed! You can now run the application")
    
    choice = input("\nهل تريد تشغيل التطبيق الآن؟ (y/n): ").lower().strip()
    if choice in ['y', 'yes', 'نعم', 'y']:
        start_app()
    else:
        print("\nلتشغيل التطبيق لاحقاً، استخدم:")
        print("To run the application later, use:")
        print("python app.py")

if __name__ == "__main__":
    main()

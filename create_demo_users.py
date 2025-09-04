#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
إنشاء مستخدمين تجريبيين للاختبار
"""

import json
import hashlib
from datetime import datetime

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# إنشاء المستخدمين التجريبيين
users = {
    "teacher@demo.com": {
        "email": "teacher@demo.com",
        "password_hash": hash_password("teacher123"),
        "name": "أحمد المعلم",
        "user_type": "teacher",
        "class_name": None,
        "created_at": datetime.now().isoformat()
    },
    "student@demo.com": {
        "email": "student@demo.com", 
        "password_hash": hash_password("student123"),
        "name": "سارة الطالبة",
        "user_type": "student",
        "class_name": "الصف العاشر",
        "created_at": datetime.now().isoformat()
    }
}

# حفظ المستخدمين
with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=2)

print("✅ تم إنشاء المستخدمين التجريبيين:")
print("👨‍🏫 المعلم: teacher@demo.com / teacher123")
print("👨‍🎓 الطالب: student@demo.com / student123")
print("\nيمكنك الآن تسجيل الدخول باستخدام هذه البيانات!")

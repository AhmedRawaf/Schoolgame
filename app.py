# -*- coding: utf-8 -*-
"""
لعبة واجهة ويب (Flask): من أنا في الجدول الدوري؟
— نسخة ويب + إدخال اسم الطالب/الصف + حفظ النتائج CSV —

تشغيل مباشر:
    python app.py

ثم افتح المتصفح على:
    http://localhost:5000

نشر على الإنترنت:
    - Heroku
    - PythonAnywhere
    - Vercel
    - Railway
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import random
import csv
import os
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'periodic_quiz_secret_key_2024'

# ------------------------ بيانات العناصر (قابلة للتوسعة) ------------------------
ELEMENTS = [
    {"Z":1,  "symbol":"H",  "name":"هيدروجين", "group":"لافلز", "period":1},
    {"Z":2,  "symbol":"He", "name":"هيليوم", "group":"غاز نبيل", "period":1},
    {"Z":3,  "symbol":"Li", "name":"ليثيوم", "group":"فلز قلوي", "period":2},
    {"Z":4,  "symbol":"Be", "name":"بيريليوم", "group":"فلز قلوي ترابي", "period":2},
    {"Z":5,  "symbol":"B",  "name":"بورون", "group":"شبه فلز", "period":2},
    {"Z":6,  "symbol":"C",  "name":"كربون", "group":"لافلز", "period":2},
    {"Z":7,  "symbol":"N",  "name":"نيتروجين", "group":"لافلز", "period":2},
    {"Z":8,  "symbol":"O",  "name":"أكسجين", "group":"لافلز", "period":2},
    {"Z":9,  "symbol":"F",  "name":"فلور", "group":"هالوجين", "period":2},
    {"Z":10, "symbol":"Ne", "name":"نيون", "group":"غاز نبيل", "period":2},
    {"Z":11, "symbol":"Na", "name":"صوديوم", "group":"فلز قلوي", "period":3},
    {"Z":12, "symbol":"Mg", "name":"مغنيسيوم", "group":"فلز قلوي ترابي", "period":3},
    {"Z":13, "symbol":"Al", "name":"ألمنيوم", "group":"فلز", "period":3},
    {"Z":14, "symbol":"Si", "name":"سيليكون", "group":"شبه فلز", "period":3},
    {"Z":15, "symbol":"P",  "name":"فوسفور", "group":"لافلز", "period":3},
    {"Z":16, "symbol":"S",  "name":"كبريت", "group":"لافلز", "period":3},
    {"Z":17, "symbol":"Cl", "name":"كلور", "group":"هالوجين", "period":3},
    {"Z":18, "symbol":"Ar", "name":"أرجون", "group":"غاز نبيل", "period":3},
    {"Z":19, "symbol":"K",  "name":"بوتاسيوم", "group":"فلز قلوي", "period":4},
    {"Z":20, "symbol":"Ca", "name":"كالسيوم", "group":"فلز قلوي ترابي", "period":4},
    {"Z":26, "symbol":"Fe", "name":"حديد", "group":"فلز انتقالي", "period":4},
    {"Z":28, "symbol":"Ni", "name":"نيكل", "group":"فلز انتقالي", "period":4},
    {"Z":29, "symbol":"Cu", "name":"نحاس", "group":"فلز انتقالي", "period":4},
    {"Z":30, "symbol":"Zn", "name":"زنك", "group":"فلز انتقالي", "period":4},
    {"Z":35, "symbol":"Br", "name":"بروم", "group":"هالوجين", "period":4},
    {"Z":36, "symbol":"Kr", "name":"كريبتون", "group":"غاز نبيل", "period":4},
    {"Z":47, "symbol":"Ag", "name":"فضة", "group":"فلز انتقالي", "period":5},
    {"Z":53, "symbol":"I",  "name":"يود", "group":"هالوجين", "period":5},
    {"Z":54, "symbol":"Xe", "name":"زينون", "group":"غاز نبيل", "period":5},
    {"Z":55, "symbol":"Cs", "name":"سيزيوم", "group":"فلز قلوي", "period":6},
    {"Z":56, "symbol":"Ba", "name":"باريوم", "group":"فلز قلوي ترابي", "period":6},
    {"Z":79, "symbol":"Au", "name":"ذهب", "group":"فلز انتقالي", "period":6},
    {"Z":80, "symbol":"Hg", "name":"زئبق", "group":"فلز انتقالي", "period":6},
    {"Z":82, "symbol":"Pb", "name":"رصاص", "group":"فلز", "period":6},
    {"Z":92, "symbol":"U",  "name":"يورانيوم", "group":"أكتينيد", "period":7},
]

# ------------------------ أدوات مساعدة ------------------------
def shuffle(lst):
    lst = list(lst)
    random.shuffle(lst)
    return lst

def make_question(difficulty):
    e = random.choice(ELEMENTS)
    others = shuffle([x for x in ELEMENTS if x != e])[:3]

    q_text = ""
    options = []
    correct_idx = 0
    explain = ""

    if difficulty == "سهل":
        flip = random.random() < 0.5
        if flip:
            q_text = f"ما رمز العنصر «{e['name']}»؟"
            options = shuffle([e["symbol"]] + [o["symbol"] for o in others])
            correct_idx = options.index(e["symbol"])
            explain = f"«{e['name']}» رمزه الكيميائي هو {e['symbol']}."
        else:
            q_text = f"ما اسم العنصر الذي رمزه «{e['symbol']}»؟"
            options = shuffle([e["name"]] + [o["name"] for o in others])
            correct_idx = options.index(e["name"])
            explain = f"الرمز {e['symbol']} يعود للعنصر «{e['name']}»."
    elif difficulty == "متوسط":
        mode = random.randint(0, 2)
        if mode == 0:
            q_text = f"ما اسم العنصر الذي عدده الذري {e['Z']}؟"
            options = shuffle([e["name"]] + [o["name"] for o in others])
            correct_idx = options.index(e["name"])
            explain = f"العدد الذري {e['Z']} يخص «{e['name']}» ({e['symbol']})."
        elif mode == 1:
            q_text = f"ما رمز العنصر الذي عدده الذري {e['Z']}؟"
            options = shuffle([e["symbol"]] + [o["symbol"] for o in others])
            correct_idx = options.index(e["symbol"])
            explain = f"العدد الذري {e['Z']} يخص «{e['name']}»، ورمزه {e['symbol']}."
        else:
            q_text = f"ما العدد الذري للعنصر «{e['name']}»؟"
            opts = shuffle([str(e["Z"])] + [str(o["Z"]) for o in others])
            options = opts
            correct_idx = options.index(str(e["Z"]))
            explain = f"«{e['name']}» ({e['symbol']}) عددُه الذري {e['Z']}."
    else:  # صعب
        mode = random.randint(0, 2)
        if mode == 0:
            q_text = f"إلى أي مجموعة ينتمي العنصر «{e['name']}»؟"
            groups = list({e["group"]} | {o["group"] for o in others})
            while len(groups) < 4:
                extra = random.choice(ELEMENTS)["group"]
                if extra not in groups:
                    groups.append(extra)
            options = shuffle(groups)[:4]
            if e["group"] not in options:
                options[0] = e["group"]
            options = shuffle(options)
            correct_idx = options.index(e["group"])
            explain = f"«{e['name']}» ({e['symbol']}) ضمن مجموعة: {e['group']}."
        elif mode == 1:
            q_text = f"أي من الآتي رمز العنصر ذو العدد الذري {e['Z']}؟"
            options = shuffle([e["symbol"]] + [o["symbol"] for o in others])
            correct_idx = options.index(e["symbol"])
            explain = f"Z={e['Z']} ⇠ «{e['name']}» ورمزه {e['symbol']}."
        else:
            q_text = f"أي من الآتي يطابق الوصف: عنصر {e['group']} رمزه «{e['symbol']}»؟"
            options = shuffle([e["name"]] + [o["name"] for o in others])
            correct_idx = options.index(e["name"])
            explain = f"الرمز {e['symbol']} يعود للعنصر «{e['name']}»."

    # ضمان 4 خيارات
    while len(options) < 4:
        extra = random.choice(ELEMENTS)
        val = extra["name"] if (isinstance(options[0], str) and not options[0].isdigit()) else extra["symbol"]
        if val not in options:
            options.append(val)
    options = options[:4]

    return {"q": q_text, "options": options, "correct": correct_idx, "explain": explain}

# ------------------------ حفظ النتائج CSV ------------------------
def save_results_to_csv(history, score, qcount, qtime, difficulty, student_name, student_class):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    base = os.path.abspath(os.path.dirname(__file__))
    summary_path = os.path.join(base, "results_summary.csv")
    detail_path = os.path.join(base, "results_detailed.csv")

    # ملخص
    corrects = sum(1 for h in history if h["correct"])
    percent = round((corrects / max(1, qcount)) * 100)
    summary_headers = [
        "timestamp","student_name","class","difficulty","questions","time_per_q","score","correct","percent"
    ]
    summary_row = [ts, student_name, student_class, difficulty, qcount, qtime, score, corrects, percent]

    write_headers = not os.path.exists(summary_path)
    with open(summary_path, "a", newline='', encoding="utf-8-sig") as f:
        w = csv.writer(f)
        if write_headers:
            w.writerow(summary_headers)
        w.writerow(summary_row)

    # تفصيلي
    detail_headers = ["timestamp","student_name","class","idx","question","chosen","correct_answer","is_correct"]
    write_headers = not os.path.exists(detail_path)
    with open(detail_path, "a", newline='', encoding="utf-8-sig") as f:
        w = csv.writer(f)
        if write_headers:
            w.writerow(detail_headers)
        for i, h in enumerate(history, 1):
            chosen = "لم يجب" if h["user"] == -1 else h["options"][h["user"]]
            correct_ans = h["options"][h["correctIndex"]]
            w.writerow([ts, student_name, student_class, i, h["q"], chosen, correct_ans, "صحيح" if h["correct"] else "خطأ"])

    return summary_path, detail_path

# ------------------------ مسارات الويب ------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    data = request.get_json()
    
    # حفظ إعدادات اللعبة في الجلسة
    session['game_settings'] = {
        'difficulty': data['difficulty'],
        'qCount': int(data['qCount']),
        'qTime': int(data['qTime']),
        'student_name': data['student_name'],
        'student_class': data['student_class']
    }
    
    # إنشاء الأسئلة
    questions = [make_question(data['difficulty']) for _ in range(int(data['qCount']))]
    session['questions'] = questions
    session['current_question'] = 0
    session['score'] = 0
    session['history'] = []
    session['used_fifty'] = False
    
    return jsonify({'success': True, 'redirect': '/quiz'})

@app.route('/quiz')
def quiz():
    if 'questions' not in session:
        return redirect('/')
    return render_template('quiz.html')

@app.route('/get_question')
def get_question():
    if 'questions' not in session:
        return jsonify({'error': 'No quiz in progress'})
    
    current_q = session['current_question']
    questions = session['questions']
    
    if current_q >= len(questions):
        return jsonify({'error': 'Quiz completed'})
    
    question = questions[current_q]
    return jsonify({
        'question': question['q'],
        'options': question['options'],
        'current_question': current_q + 1,
        'total_questions': len(questions),
        'score': session['score']
    })

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    user_answer = data['answer']
    
    current_q = session['current_question']
    questions = session['questions']
    question = questions[current_q]
    
    # التحقق من الإجابة
    is_correct = (user_answer == question['correct'])
    if is_correct:
        session['score'] += 10
    
    # حفظ التاريخ
    session['history'].append({
        'q': question['q'],
        'options': question['options'],
        'correctIndex': question['correct'],
        'user': user_answer,
        'correct': is_correct,
        'explain': question['explain']
    })
    
    # الانتقال للسؤال التالي
    session['current_question'] += 1
    
    if session['current_question'] >= len(questions):
        # انتهت اللعبة
        return jsonify({
            'game_over': True,
            'score': session['score'],
            'total': len(questions) * 10
        })
    
    return jsonify({
        'game_over': False,
        'correct': is_correct,
        'explanation': question['explain'],
        'score': session['score']
    })

@app.route('/use_fifty')
def use_fifty():
    if session.get('used_fifty', False):
        return jsonify({'error': 'Already used'})
    
    current_q = session['current_question']
    questions = session['questions']
    question = questions[current_q]
    
    # إزالة خيارين خاطئين
    wrong_indices = [i for i in range(4) if i != question['correct']]
    random.shuffle(wrong_indices)
    to_disable = wrong_indices[:2]
    
    session['used_fifty'] = True
    
    return jsonify({
        'disabled_options': to_disable
    })

@app.route('/finish_quiz')
def finish_quiz():
    if 'questions' not in session:
        return redirect('/')
    
    # حفظ النتائج
    settings = session['game_settings']
    summary_path, detail_path = save_results_to_csv(
        session['history'],
        session['score'],
        settings['qCount'],
        settings['qTime'],
        settings['difficulty'],
        settings['student_name'],
        settings['student_class']
    )
    
    # إرسال النتائج للعرض
    corrects = sum(1 for h in session['history'] if h['correct'])
    percent = round((corrects / max(1, settings['qCount'])) * 100)
    
    results = {
        'score': session['score'],
        'total': settings['qCount'] * 10,
        'correct_answers': corrects,
        'percent': percent,
        'student_name': settings['student_name'],
        'student_class': settings['student_class'],
        'difficulty': settings['difficulty'],
        'history': session['history']
    }
    
    return render_template('results.html', results=results)

@app.route('/new_game')
def new_game():
    # مسح الجلسة
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

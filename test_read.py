from database import read_questions
    
soal = read_questions()
for s in soal:
    print(s["id"], s["bahasa"], s["level"], s["buggy_code"])
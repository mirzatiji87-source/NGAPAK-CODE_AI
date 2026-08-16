from database import update_question, read_questions

update_question(1, "python", "pemula", "prin('halo')", "print('halo')", "Update: nama function salah boy,")

soal = read_questions()
for s in soal:
    print(s["id"], s["bahasa"], s["level"], s["hint"])
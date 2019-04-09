answers = [["A", "D", "C", "B", "A", "A", "C", "B", "D", "D"],
           ["B", "C", "D", "D", "A", "A", "C", "C", "B", "D"],
           ["A", "A", "C", "C", "D", "D", "B", "A", "B", "D"],
           ["A", "D", "B", "B", "A", "C", "C", "B", "D", "A"],
           ["A", "B", "C", "D", "A", "A", "C", "B", "A", "D"],
           ["A", "A", "B", "C", "A", "A", "D", "B", "C", "D"]]

key = ["A", "A", "C", "D", "A", "A", "B", "C", "C", "D"]

student_no = 0
for answer in answers:
    count = 0
    correct = 0
    for key_ans in key:
        if key_ans == answer[count]:
            correct += 1
        count+=1
    student_no += 1
    print("Student", student_no, "gave", correct, "correct answers out of", len(answers[0]))

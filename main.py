print ("welcome to the quiz manegement system")
print("student regiestration 1.")
print("student logn 2.")
print("admin login 3.")
print("exit 4.")
choice = int(input("enter your choice:"))
if choice == 1:
    print("student registration")
elif choice == 2:
    print("student login")
elif choice == 3:
    print("admin login")
elif choice == 4:
    print("exit")
else:
    print("invalid choice")
def student_registration():
   name = input("enter your name:")
   age = int(input("enter your age:"))
   gender = input("enter your gender:")
   password = input("enter your password:")
   print("registration succesfully" "\n thanks for registering with us")
   print("Registration successfully!")
def student_login():
    name = input("enter your name:")
    password = input("enter your password:")
    print("login succesfully")
def admin_login():
    name = input("enter your name:")
    password = input("enter your password:")
    print("login succesfully")
def exit():
    pass
def invalid_choice():
    print("invalid choice plzz make a valid choice")
if choice == 1:
    student_registration()
elif choice == 2:
    student_login()
elif choice == 3:
    admin_login()
elif choice == 4:
    exit()
else:
    invalid_choice()
def student_registration():
   pass
def student_login():
    pass
def admin_login():
    pass
def exit():
    pass
questions = []

def add_question():
    question = input("Enter question: ")
    A = input("Enter option A: ")
    B = input("Enter option B: ")
    C = input("Enter option C: ")
    D = input("Enter option D: ")
    answer = input("Enter correct answer (A/B/C/D): ").upper()

    q = {
        "question": question,
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "answer": answer
    }

    questions.append(q)

    print("Question added successfully!")
def view_questions():
    print("\n--- Quiz Questions ---")

    if len(questions) == 0:
        print("No questions available.")
        return

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        print("A.", q["A"])
        print("B.", q["B"])
        print("C.", q["C"])
        print("D.", q["D"])
        print("Answer:", q["answer"])
def attempt_quiz():
    if len(questions) == 0:
        print("No questions available.")
        return

    score = 0

    print("\n--- Start Quiz ---")

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        print("A.", q["A"])
        print("B.", q["B"])
        print("C.", q["C"])
        print("D.", q["D"])

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("\nQuiz Completed!")
    print("Your Score:", score, "/", len(questions))
def display_result(score, total):
    percentage = (score / total) * 100

    print("\n--- Result ---")
    print("Score:", score, "/", total)
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent!")
    elif percentage >= 60:
        print("Good!")
    elif percentage >= 40:
        print("Pass!")
    else:
        print("Fail!")
while True:
    print("\n===== QUIZ MANAGEMENT SYSTEM =====")
    print("1. Student Registration")
    print("2. Student Login")
    print("3. Admin Login")
    print("4. Add Questions")
    print("5. View Questions")
    print("6. Attempt Quiz")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        view_questions()

    elif choice == "6":
        attempt_quiz()

    elif choice == "7":
        print("Thank you for using Quiz Management System!")
        break

    else:
        print("Please enter a valid choice.")
 import sql

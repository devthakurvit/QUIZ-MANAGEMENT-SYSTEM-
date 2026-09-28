# Quiz Management System

## 1. Project Overview
The **Quiz Management System** is a beginner-level Python project designed to manage students and conduct multiple-choice quizzes. The project demonstrates fundamental Python programming concepts such as functions, conditional statements, loops, lists, dictionaries, user input, and basic data processing.

## 2. Objectives
- Provide a simple student registration interface.
- Provide student and admin login functions.
- Allow an admin to add multiple-choice questions.
- Display stored quiz questions.
- Allow a student to attempt the quiz.
- Calculate and display the quiz score.
- Display the percentage and performance category.
- Provide a simple menu-driven interface.

## 3. Technologies Used
- **Programming Language:** Python 3
- **Data Structures:** List and Dictionary
- **Interface:** Command-line / terminal
- **Storage:** Temporary in-memory storage using a Python list

## 4. Main Features

### Student Registration
The student can enter:
- Name
- Age
- Gender
- Password

### Student Login
The student enters a name and password to access the login function.

### Admin Login
The admin enters a name and password to access the admin function.

### Add Questions
The system accepts:
- Question
- Option A
- Option B
- Option C
- Option D
- Correct answer

Each question is stored as a dictionary inside the `questions` list.

### View Questions
The system displays all questions currently stored in the `questions` list.

### Attempt Quiz
The student can answer each question using A/B/C/D. The program checks the answer and increases the score for every correct response.

### Result
The program calculates:
- Score
- Total questions
- Percentage
- Performance category

Performance categories:
- 80% or above → Excellent
- 60% or above → Good
- 40% or above → Pass
- Below 40% → Fail

## 5. Project Structure

```text
Quiz-Management-System/
│
├── project.py
├── README.md
└── Quiz_Management_System_Project_Report.docx
```

## 6. Important Python Concepts Used

### Functions
Functions such as `student_registration()`, `student_login()`, `admin_login()`, `add_question()`, `view_questions()`, and `attempt_quiz()` divide the program into smaller modules.

### List
```python
questions = []
```
The list stores all quiz questions.

### Dictionary
Each question is stored as a dictionary:

```python
q = {
    "question": question,
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "answer": answer
}
```

### Loop
The `while True` loop keeps displaying the main menu until the user selects Exit.

### Conditional Statements
`if`, `elif`, and `else` are used to process menu choices and evaluate quiz answers.

## 7. How to Run

1. Install Python 3.
2. Save the program as `project.py`.
3. Open Terminal or Command Prompt.
4. Navigate to the project folder.
5. Run:

```bash
python project.py
```

On some systems:

```bash
python3 project.py
```

## 8. Current Limitations
- Student information is not permanently stored.
- Login credentials are not verified against saved accounts.
- Admin authentication is not implemented with fixed credentials.
- Questions are stored only while the program is running.
- The result function is defined separately and is not currently called by `attempt_quiz()`.
- Some menu options in the current code are placeholders.

## 9. Future Improvements
- Add JSON or database storage.
- Implement real student registration and authentication.
- Implement admin authentication.
- Add edit/delete question options.
- Add question categories and difficulty levels.
- Add timer functionality.
- Store quiz results for each student.
- Add a graphical user interface using Tkinter.
- Add password protection.
- Generate detailed result reports.

## 10. Conclusion
The Quiz Management System is a useful beginner Python project for understanding functions, lists, dictionaries, loops, conditions, and user input. It provides a foundation that can later be extended into a complete quiz application with permanent storage and a graphical interface.

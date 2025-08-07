def run_quiz(questions):
    score = 0
    print(" 🧠 Welcome to the Python Quiz Game!\n")

    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for option in ['a', 'b', 'c', 'd']:
            print(f"{option}) {q['options'][option]}")
        answer = input("Your answer (a/b/c/d): ").lower()

        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is '{q['answer']}'\n")

    print(f" 🏆 Your Final Score: {score}/{len(questions)}")
    if score >= 8:
        print("👏 Very Good, You’re well prepared!")
    elif score >= 5:
        print("👍 Good job, Keep practicing!")
    else:
        print("📖 Keep learning. You'll get there!")

questions = [
    {
        "question": "What is the maximum length of a Python identifier?",
        "options": {
            "a": "32",
            "b": "16",
            "c": "128",
            "d": "No fixed length is specified."
        },
        "answer": "d"
    },
    {
        "question": "What will be the output of: print(2*3 + (5 + 6)*(1 + 1))?",
        "options": {
            "a": "129",
            "b": "8",
            "c": "121",
            "d": "None of the above."
        },
        "answer": "a"
    },
    {
        "question": "What will be the datatype of the variable after these lines?\nvar = 10\nprint(type(var))\nvar = 'Hello'\nprint(type(var))",
        "options": {
            "a": "str and int",
            "b": "int and int",
            "c": "str and str",
            "d": "int and str"
        },
        "answer": "d"
    },
    {
        "question": "How is a code block indicated in Python?",
        "options": {
            "a": "Brackets.",
            "b": "Indentation.",
            "c": "Key.",
            "d": "None of the above."
        },
        "answer": "b"
    },
    {
        "question": "What will be the output?\na = [1, 2, 3]\na = tuple(a)\na[0] = 2\nprint(a)",
        "options": {
            "a": "[2, 2, 3]",
            "b": "(2, 2, 3)",
            "c": "(1, 2, 3)",
            "d": "Error."
        },
        "answer": "d"
    },
    {
        "question": "What is the output of the following?\nprint(type(5 / 2))\nprint(type(5 // 2))",
        "options": {
            "a": "float and int",
            "b": "int and float",
            "c": "float and float",
            "d": "int and int"
        },
        "answer": "a"
    },
    {
        "question": "What will be the output?\na = [1, 2, 3, 4, 5]\nsum = 0\nfor ele in a:\n   sum += ele\nprint(sum)",
        "options": {
            "a": "15",
            "b": "0",
            "c": "20",
            "d": "None of these"
        },
        "answer": "a"
    },
    {
        "question": "What will be the output?\na = 3\nb = 1\nprint(a, b)\na, b = b, a\nprint(a, b)",
        "options": {
            "a": "3 1    1 3",
            "b": "3 1    3 1",
            "c": "1 3    1 3",
            "d": "1 3    3 1"
        },
        "answer": "a"
    },
    {
        "question": "What will be the output?\na = [1, 2]\nprint(a * 3)",
        "options": {
            "a": "Error",
            "b": "[1, 2]",
            "c": "[1, 2, 1, 2]",
            "d": "[1, 2, 1, 2, 1, 2]"
        },
        "answer": "d"
    },
    {
        "question": "Which type of loop is NOT supported in Python?",
        "options": {
            "a": "for",
            "b": "while",
            "c": "do-while",
            "d": "None of the above"
        },
        "answer": "c"
    }
]

run_quiz(questions)
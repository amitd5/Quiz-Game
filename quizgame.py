questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Chennai", "Goa", "New Delhi", "Mumbai"],
        "answer": 2
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": 1
    },
    {
        "question": "Who is the Prime Minister of India?",
        "options": ["Narendra Modi", "Akhilesh Yadav", "Rajnath Singh", "Amit Shah"],
        "answer": 0
    }
]

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            user_input = int(input("Enter the number of your answer: ")) - 1
            if 0 <= user_input < len(question["options"]):
                return user_input
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_answer(question, user_input):
    if user_input == question["answer"]:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer is {question['options'][question['answer']]}.")
        return False

def display_score(score, total_questions):
    print(f"\nYour final score is {score} out of {total_questions}.")

def main():
    score = 0
    total_questions = len(questions)
    
    for question in questions:
        user_input = ask_question(question)
        if check_answer(question, user_input):
            score += 1
    
    display_score(score, total_questions)

if __name__ == "__main__":
    main()

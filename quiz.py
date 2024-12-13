
def quiz_time():
    score = 0
    Q1 = '''Who wrote Hamlet?
    A. Berlin
    B. Mdrid
    C. Paris
    D. Rome '''
    Q2 = '''Which planet is known as the Red Planet?
    A. Earth
    B. Mars
    C. Jupiter
    D. Saturn'''
    Q3 = '''What is the capital of Japan??
    A. Beijing
    B. Seoul
    C. Tokyo
    D. Bangkok'''
    Q4 = '''What is the boiling point of water at sea level?
    A. 90°C
    B. 100°C
    C. 110°C
    D. 120°C'''
    Q5 ='''Which programming language is known as the language of the web?
    A. Java
    B. Python
    C. JavaScript
    D. C++'''
    questions = {
        Q1: 'C',
        Q2: 'B',
        Q3: 'C',
        Q4: 'B',
        Q5: 'C'
    }
    for idx, (questions,correct_ans) in enumerate(questions.items(),start=1):
        print("press 'Q' to quit.")
        print(f"{idx}.{questions}")
        user_input = input("Enter the option:").capitalize()

        if user_input=='Q':
            print("Thank you for playing")
            break
        if user_input== correct_ans:
            score=score+1
            print("ans is correct!")
        else:
            score-=1
            print("Incorrect!")
        
    print(f"Your total score is:{score}")
quiz_time()
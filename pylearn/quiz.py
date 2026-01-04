question =("What is the capital of France?: ",
           "What is the largest planet in our solar system?: ",
           "What is the chemical symbol for gold?: ",
           "Who painted the Mona Lisa?: ",
           "What is the hardest natural substance on Earth?: ")

options = (("A. London", "B. Paris", "C. Berlin", "D. Madrid"),
           ("A. Jupiter", "B. Saturn", "C. Mars", "D. Venus"),
           ("A. Ag", "B. Au", "C. Fe", "D. Cu"),
           ("A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"),
           ("A. Diamond", "B. Gold", "C. Iron", "D. Silver"))

answers = ("B", "A", "B", "C", "A")
guesses = []
score = 0
question_num = 0


for q in question:
    print(q)
    for o in options[question_num]:
        print(o)
    guess = input("Enter (A, B, C, or D): ")
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
    question_num += 1   
print("-------------------")
print("Quiz Completed")
print(f"Your score is {score}/{len(question)}")
percentage = int(score / len(question) * 100)
print(f"Your percentage is: {percentage}%")
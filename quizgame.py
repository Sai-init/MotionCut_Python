# Basic Python Quiz game 
questions = ("Who is the father of Computer Science?: ",
           "Who created Python?: ",
           "Which place in India is also known as the “Land of Rising Sun?: ",      
           "What is the smallest state in India by area?: ",
           "Who discovered India?: ")

options = (("A.Dennis Ritchie", "B.Charless Babbage", "C.Allen Turing", "D.Ken Thompson"),
           ("A.James Gosling", "B.Guido Van Russom", "C.Dennis Ritchie", "D.Bjarne Stroustrup"),
           ("A.Sikkim", "B.Karnataka", "C.Gujarat", "D.Arunachal Pradesh"),
           ("A.Goa", "B.Sikkim", "C.Mizoram", "D.Puducherry"),
           ("A.Vasco da Gama", "B.Christopher Columbus", "C.James Cook", "D.Willem Janszoon"))

answers = ("C", "B", "D", "A", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("******************")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Hurray!, CORRECT!!!")
    else:
        print("Oops!!, INCORRECT!!!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("************************************")
print("           RESULTS            ")
print("************************************")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: " ,end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your Score is : {score}%")


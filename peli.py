
quiz = {
    1: {"question": "Who was the leader fo the group?", "answer": "Rick"},
    2: {"question": "Who is Carols best friend?", "answer" : "Deryl"}
}

while True:
    score = 0

    for question in quiz:
        print(quiz[question]["question"])
        answer = input("Enter your answer: ")

        if answer == quiz[question]["answer"]:
            print("Good job! Your answer is correct!")
            score += 1
        else:
            print("Opps! Wrong answer!")

    print(f"Your score is: {score}")

    again = input("Would you like to try again? Write y or n!")
    if again == "n":
        print("Thanks for playing with us!")
        break
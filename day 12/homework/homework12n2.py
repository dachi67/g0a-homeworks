print("answer.1")
print("answer.2")
print("answer.3")
print("answer.4")

true_choice = 4

while True:
    user_choice  = int(input("please enter your choice: "))

    if user_choice == true_choice:
        print("your choice is correct!")
        break
    else:
        print("your choice is false")
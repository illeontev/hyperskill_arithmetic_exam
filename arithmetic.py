import random

while True:
    print("Which level do you want? Enter a number:")
    try:
        difficulty = int(input())
        if difficulty not in (1, 2):
            raise ValueError
        break
    except ValueError:
        print("Incorrect format.")

mark = 0
for num_of_tasks in range(5):
    if difficulty == 1:
        difficulty_description = "(simple operations with numbers 2-9)"

        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        types_of_operations = ['+', '-', '*']

        operation = random.choice(types_of_operations)

        task = f'{num1} {operation} {num2}'

        if operation == '+':
            right_answer = num1 + num2
        elif operation == '-':
            right_answer = num1 - num2
        elif operation == '*':
            right_answer = num1 * num2
        elif operation == '/':
            right_answer = num1 / num2
    elif difficulty == 2:
        difficulty_description = "integral squares 11-29"

        num1 = random.randint(11, 29)
        task = str(num1)
        right_answer = num1 ** 2

    print(task)

    while True:
        try:
            answer = int(input())
        except Exception:
            print("Incorrect format")
        else:
            if answer == right_answer:
                print("Right!")
                mark += 1
            else:
                print("Wrong!")
            break

print(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")

answer = input()
if answer in ("yes", "YES", "y", "Yes"):
    name = input("What is your name?\n")
    with open("results.txt", 'a') as file:
        file.write(f"{name}: {mark}/5 in level {difficulty} {difficulty_description}.")
    print("The results are saved in \"results.txt\".")













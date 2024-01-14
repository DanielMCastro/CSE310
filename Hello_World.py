import random
guess_list = []
guess_counter = 0
guess_correct = False

print("This is the \"guess a number\" game. Guess correctly and win to get your reward!")
print("You try to guess a random number in the smallest number of attempts.")
print("What do you want the highest possible number to be?")
user_number = input(">")
number = random.randint(1, int(user_number))
print(f"Guess a number between 1 and {user_number}.")
user_number = input(">")

while guess_correct == False:
    if int(user_number) < number:
        print("     Too low; try again!")
        guess_list.append(user_number)
        guess_counter += 1
        user_number = input(">")

    elif int(user_number) > number:
        print("     Too high; try again!")
        guess_list.append(user_number)
        guess_counter += 1
        user_number = input(">")

    elif int(user_number) == number:
        guess_list.append(user_number)
        guess_counter += 1
        guess_correct = True

print(f"You were able to guess correctly in {guess_counter} tries")
print(f"Here are all the numbers you guessed: {guess_list}")
print()
print("Here's your reward: Hello World!!")
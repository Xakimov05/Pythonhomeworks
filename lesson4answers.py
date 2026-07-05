# 2. Difference between break and continue:
# break stops the loop immediately.

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

1
2
    
# continue skips the current iteration and continues with the next one.

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

1
2
4
5

# 3. Difference between for and while:
# A for loop is used when the number of iterations is known or when iterating over a sequence.

for i in range(5):
    print(i)
    
# A while loop is used when the loop should continue as long as a condition is true.

count = 0

while count < 5:
    print(count)
    count += 1

# 4. Nested for loop:

for row in range(3):
    for column in range(3):
        print(row, column)

# A nested for loop is a loop inside another loop.

# Example:
# for row in range(3):
#     for col in range(3):
#         print(row, col)

list1 = [1, 1, 2]
list2 = [2, 3, 4]

result = []

for item in list1:
    if item not in list2:
        result.append(item)

for item in list2:
    if item not in list1:
        result.append(item)

print(result)

[1, 1, 3, 4]

n = int(input("Enter n: "))

for i in range(1, n):
    print(i ** 2)


txt = input("Enter text: ")

vowels = "aeiouAEIOU"
result = ""

count = 0

for ch in txt:
    result += ch
    count += 1

    if count == 3:
        if ch != txt[-1] and ch not in vowels:
            result += "_"
            count = 0


import random

while True:

    number = random.randint(1, 100)

    attempts = 10

    while attempts > 0:

        guess = int(input("Guess a number: "))

        if guess > number:
            print("Too high!")

        elif guess < number:
            print("Too low!")

        else:
            print("You guessed it right!")
            break

        attempts -= 1

    if attempts == 0:
        print("You lost.")

    answer = input("Want to play again? ")

    if answer.lower() not in ["y", "yes", "ok"]:
        break

for num in range(2, 101):

    prime = True

    for i in range(2, num):

        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)

2
3
5
7
11
13
17
...
97

import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while player_score < 5 and computer_score < 5:

    player = input("Choose rock, paper or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer:", computer)

    if player == computer:
        print("Tie!")

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):

        print("You win!")
        player_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Score:", player_score, "-", computer_score)

print()

if player_score == 5:
    print("Congratulations! You won the match.")

else:
    print("Computer won the match.")

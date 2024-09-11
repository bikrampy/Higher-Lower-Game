from game_data import data
import random

a, b = random.sample(range(len(data)), 2)
game_continue = True
score = 0
while game_continue:
    print(f"Compare A: {data[a]["name"]}, a {data[a]["description"]}, from {data[a]["country"]}")
    print(f"Against B: {data[b]["name"]}, a {data[b]["description"]}, from {data[b]["country"]}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if data[a]["follower_count"] > data[b]["follower_count"]:
        correct_answer = "a"
    else:
        correct_answer = "b"

    if user_choice == correct_answer:
        score += 1
        print(f"You're Right. Your Current Score is {score}")
        a = b
        while a == b:
            b = random.randint(0, len(data)-1)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continue = False

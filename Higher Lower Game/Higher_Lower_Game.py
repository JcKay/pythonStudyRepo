import random
import replit
from art import logo, vs
from game_data import data
from os import system


# generate readable format to compare
def read_format(info):
    """input info and return readable format"""
    info_name = info["name"]
    info_desc = info["description"]
    info_coun = info["country"]
    return f"{info_name}, a {info_desc}, from {info_coun}"


# compare guess and follower_count
def compare(guess, follower_A, follower_B):
    """input guess , accA , accB and return Ture or False"""
    if follower_A > follower_B:
        return guess == "a"
    else:
        return guess == "b"


# Display
print(logo)
score = 0
info_b = random.choice(data)

while True:
    # generate random for A and B
    info_a = info_b
    info_b = random.choice(data)
    if info_a == info_b:
        info_b = random.choice(data)

    # Compare outpub
    print(f"Compare A : {read_format(info_a)}.")
    print(vs)
    print(f"Against B : {read_format(info_b)}.")

    # follower count
    follower_A = info_a["follower_count"]
    follower_B = info_b["follower_count"]

    # guess A or B
    guess = input("Who has more follower? Type 'A' or 'B': ").lower()
    # clear screen
    replit.clear()
    system("cls")
    print(logo)
    if compare(guess, follower_A, follower_B):
        score += 1
        print(f"You're' right!. Your current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        break

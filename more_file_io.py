import os
import random

path = "puzzles"

file_names = os.listdir(path)

for i, f in enumerate(file_names):
    print(str(i + 1) + "/" + f)

print()
choice = input("Pick One Fam  ")
choice = int(choice) - 1

file = path + "/" + file_names[choice]

with open(file, "r") as f:
    lines = f.read().splitlines()

print(lines)

category_name = lines[0]
puzzle = random.choice(lines[1:])

print(category_name)
print(puzzle)

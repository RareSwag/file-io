import random

file = open('last_words.txt')
print(file)
print()

line1 = file.readline()
line2 = file.readline()
print(line1)
print(line2)
print()

contents = file.read()
print(contents)
print()

file.close()

file2 = open('movies.txt', 'r')
movies = file2.readlines()
print(movies)
print()
file2.close()


with open('movies.txt', 'r') as f:
    movies = f.read().splitlines()
    
print(movies)
print()

file3 = open('new_file.txt', 'w')
file3.write('This is one line.')
file3.write('This is another.\n')
file3.write('This is actually on the next line')
file3.close()

with open('scrabble_list.txt', 'r') as f:
    words = f.read().splitlines()

print(words[:10])

print(random.choice(words))


''' how many words end with an s? '''
count = 0
for w in words:
    if w[-1] == 's':
        count += 1

print(count)

count = 0
for w in words:
    if len(w) == 2:
        count += 1

print(count)

with open('two_letters.txt', 'w') as f:
    for w in words:
        if len(w) == 2:
            f.write(w + "\n")



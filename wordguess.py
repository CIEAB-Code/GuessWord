import random as rm

print("\nWelcome to GuessWord!\n")

words = ["giraffe", "flamingo", "coffee", "elephant", "armageddon", "messiah", "energy", "martian", "forest", "freedom", "virtual"]

word = words[rm.randint(0, (len(words)-1))]
show = []
for letter in range(len(word)):
    show.append("_ ")
notlet = []
print(' '.join(show), '\n')

while True:
    if len(notlet) >= 1:
        print("There is no :", list(set(notlet)), '\n')
    print('')
    lw = input("Would you like to guess a letter or word? l/w?")
    print('')
    if lw != 'l' and lw != 'w':
        lw = input("Please enter 'l' or 'w': ")
        print('')
    if lw == 'l':
        let = input("Enter letter: ")
        print('')
        if len(let) > 1:
            let = input("Please only input one letter: ")
            print('')
        let = let.lower()
        if let not in word:
            notlet.append(let.upper())
        for char in range(len(word)):
            if let == word[char]:
                show[char] = word[char]

        if '_ ' not in show:
            print(f"{word.upper()}! YOU WIN!")
            break
    elif lw =='w':
        guess = input("Enter guess: ")
        guess = guess.lower()
        print('')
        if guess == word:
            print(f"{word.upper()}! YOU WIN!")
            break
        if guess != word:
            print("Not the word!")
    print(' '.join(show))


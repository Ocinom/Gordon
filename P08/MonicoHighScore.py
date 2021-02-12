import time

scores = [
    ('Tim', 55),
    ('John', 66),
    ('Fred', 56),
    ('Tien', 67)
]

while True:
    print(
    """
    High Scores
    0 - Quit
    1 - List Scores
    2 - Add a score
    """
)
    choice = input('Choose 0, 1, or 2: ')
    if choice == '0':
        break
    elif choice == '1':
        print('Here are the high scores:')
        for score in scores:
            print('\t' + score[0] + '  ' + str(score[1]))
    elif choice == '2':
        name = input('Type the player\'s name:  ')
        score = input('Type the player\'s score:  ')
        new_score = (name, int(score))
        scores.append(new_score)
        print('Done!')
    else:
        print('Invalid input detected. Please input 0, 1 or 2.')
    time.sleep(2)
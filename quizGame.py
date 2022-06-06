# a quiz game to understand if else condition in a better way

print('Wellcome to my quiz game! ')

decision = input('Do you want to continue? ').lower()

if decision != 'yes':
    quit()

print('Starting the game! ')

ans = input('What is a CPU?').lower()
if ans == 'central processing unit':
    print('Correct.')
else:
    print('Sorry, you are wrong.')

ans = input('What is a AI?').lower()
if ans == 'Artificial Intelligence':
    print('Correct.')
else:
    print('Sorry, you are wrong.')

ans = input('What is ML?').lower()
if ans == 'machine learning':
    print('Correct.')
else:
    print('Sorry, you are wrong.')
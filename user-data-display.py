print('Welcome dear user. Please fill in the requested details below.')
print('Hint: Click anywhere after the question to activate the cursor. Click enter after putting your response to continue.')

name = input('What is your name? ')
age = int(input('Type in your age: '))
dept = input('What department are you in? ')

print('Thank you', name, '. YOUR DATA: ')
print('Your name is', name, '.')
print('You are', age, 'years old.')
print('You are in', dept, 'department.')
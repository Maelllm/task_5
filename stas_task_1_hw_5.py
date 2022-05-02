pass_1 = input('Enter your password ')
pass_2 = input('Repeat password ')

while pass_2 not in pass_1:
    pass_2 = input('Passwords didnt match. Try again ')
    continue
else:
    print('Congratulations!')

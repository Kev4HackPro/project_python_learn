savings = int(input('How much do you have saved up in $? '))
if savings == 0:
    print('Hey, no savings yet? try harder')
elif savings < 500:
    print('Nice sum but you can do better')
elif savings < 3000:
    print('You are getting there sir!')
elif savings < 30000:
    print('Tidy sum there')
else:
    print('Nice job!, keep it up')
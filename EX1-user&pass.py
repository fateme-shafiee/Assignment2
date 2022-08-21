PrimaryUsername = 'shafiee'
PrimaryPassword = 'shafiee78'
AttemptCounter = 0 

for i in range (3):
    username = input ('please enter your Username  : ')
    password = input ('please enter your Password :')
    if (PrimaryUsername == username) and (PrimaryPassword == password):
        print ('welcom :)')
        break
    elif (PrimaryUsername != username) or (PrimaryPassword != password):
        if (AttemptCounter == 2):
            print ('your account has been blocked')
            break
        print ('your username or password is incorrect.please try again.')

        AttemptCounter += 1

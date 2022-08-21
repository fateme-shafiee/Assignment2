temperature = float (input('enter the temperature : '))

convert1 = int(input('choose your convert1 :\n 1.celsius \n 2.kelvin \n 3.fahrenheit \n '))
convert2 = int(input('choose your convert2 :\n 1.celsius \n 2.kelvin \n 3.fahrenheit \n '))

if convert1 == 1 and convert2 == 3:
    print ('com = ',(temperature * 1.8) + 32 , 'F')

elif convert1 == 3 and convert2 == 1:
    print ('com = ',(temperature - 32) / 1.8 ,'C')

elif convert1 == 2 and convert2 == 1:
    print ('com = ',(temperature - 273.15),'C')

elif convert1 == 1 and convert2 == 2:
    print('com = ',(temperature + 273.15),'K')

elif convert1 == 3 and convert2 == 2:
    print ('com = ',((temperature + 459.67) / 1.8),'K')

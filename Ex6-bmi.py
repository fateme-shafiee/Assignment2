height = float (input('enter your height in meters = '))
weight = float (input('enter your weight in kilograms = '))
bmi = weight / (height ** 2)
if 16 > bmi:
    print ('you have severe weight loss. ')
elif 16 < bmi <= 18.5:
    print ('you have lost weight. ')
elif 18.5 < bmi <= 24:
    print ('you have lost some weight. ')
elif 24 < bmi <= 30:
    print ('your have an ideal weight. ')
elif 30 < bmi <= 35:
    print('your are a little overweight.')
elif 35 < bmi <= 40:
    print ('your are overweight.')
elif 40 < bmi:
    print ('your are severely overweight.')

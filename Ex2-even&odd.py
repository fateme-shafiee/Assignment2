number = int(input('please enter the number : '))
odd = 0
even = 0
while number != 0:
    fat = number % 10

    if fat % 2 == 0:
        even += 1

    else:
        odd += 1
    number //= 10 

print ('the number even : ',even)
print ('the number odd : ',odd )
if even == odd :
    print ('your odd and even number are equal.')
elif even > odd :
    print ('your number of even digits is more.')
else:
    print ('your number of odd digits is more.')
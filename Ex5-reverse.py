number = (int(input('please enter your number ; ')))
num = number
reverse = 0
while (number > 0):
    newnum = number % 10
    reverse = ((reverse * 10) + newnum)
    number //= 10
if num == reverse:
    print(reverse , ' : number and inverse match.')
else:
    print(reverse , ' : the number and the inverse do not match.')

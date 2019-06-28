import random

words = ['I','l']
yeet = int(69)

print('SWAGGERSOULS CODE BREAKER')

while yeet > 0:
    print('')
    newcode = str('')
    makecode = input('Press enter to generate code: ')
    count = int(30)
    while count > 0:
        letter = str(random.choice(words))
        newcode = str(newcode + str(letter))
        count = (count - 1)
    print('')
    print('bit.ly/', newcode, sep='')

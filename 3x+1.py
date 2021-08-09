# suskaiciuoja kiek zingsniu 3x+1 
from time import sleep

num = 1234567
steps = 0


while num != 1:
    if num % 2 == 0:
        num /= 2
    else:
        num = num * 3 + 1
    steps += 1
    print(f'{steps}\t{num}')
    

print(f'Total steps {steps}!')

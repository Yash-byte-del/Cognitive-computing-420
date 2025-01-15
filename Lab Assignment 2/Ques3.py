import random
num=[random.randint(100, 900) for i in range(100)]
odd=[num for num in num if num%2==1]
even=[num for num in num if num%2==0]
print('Odd Numbers=',odd)
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
prime=[n for n in num if is_prime(n)]
print('Odd Numbers=',odd)
print('Even Numbers=',even)
print('Prime Numbers=',prime)

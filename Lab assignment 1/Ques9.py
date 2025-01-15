#9.1
import random
for i in range(0,5):
    print(random.randint(1, 100))


#9.2
import random
def is_prime(number):
    if number<=1:
        return False
    for i in range(2,int(number **0.5)+1):
        if number%i==0:
            return False
    return True
random_number=random.randint(1,100)
prime_check=is_prime(random_number)
print(f"The random number is:{random_number}")
if prime_check:
    print(f"{random_number} is a prime number.")
else:
    print(f"{random_number} is not a prime number.")


#9.3
diceroll=random.randint(1,6)
print(f'The dice says: {diceroll}')


#9.4
n= [1, 2, 3, 4, 5]
random.shuffle(n)
print(n)


#9.5
import random
items = ["apple", "banana", "cherry", "mango", "pie"]
selected_item = random.choice(items)
print(f"The randomly selected item is: {selected_item}")


#9.6
characters ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()1234567890'
length=int(input('Enter the length of the random password: '))
password=''.join(random.choice(characters) for i in range(length))
print("Random password:", password)


#9.7
import random

def pick_random_card():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    random_card = random.choice(deck)
    return random_card
card = pick_random_card()
print(f"The randomly selected card is: {card}")

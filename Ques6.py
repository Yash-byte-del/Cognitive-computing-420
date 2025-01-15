#6.1
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
input_string = "Hello, how are you?"
vowel_count = count_vowels(input_string)
print(f"The number of vowels in the string is: {vowel_count}")


#6.2
def reverse_string(input_string):
    return input_string[::-1]
input_string = "Hello, world!"
reversed_string = reverse_string(input_string)
print(f"The reversed string is: {reversed_string}")


#6.3
s1="Karan"
print ("s1 --> ", s1==s1[::-1])

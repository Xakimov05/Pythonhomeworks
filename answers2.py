number = float(input("Enter a float number: "))
rounded_number = round(number, 3)

print("Rounded number:", rounded_number)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

print("Largest number:", max(num1, num2, num3))
print("Smallest number:", min(num1, num2, num3))

kilometers = float(input("Enter kilometers: "))

meters = kilometers * 1000
centimeters = kilometers * 100000

print("Meters:", meters)
print("Centimeters:", centimeters)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

division = num1 // num2
remainder = num1 % num2

print("Integer division:", division)
print("Remainder:", remainder)

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

number = int(input("Enter a number: "))

last_digit = number % 10

print("Last digit:", last_digit)

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

age = 2026 - birth_year

print("Hello,", name)
print("You are", age, "years old.")

txt = "FTeorrryaortia"

car1 = txt[::2]
car2 = txt[1::2]

print(car1)
print(car2)

text = input("Enter a string: ")

print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

text = input("Enter a string: ")

if text == text[::-1]:
    print("Yes")
else:
    print("No")

    text = input("Enter a string: ").lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for letter in text:
    if letter.isalpha():
        if letter in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

text = input("Enter the first string: ")
word = input("Enter the second string: ")

if word in text:
    print("The string contains the word.")
else:
    print("The string does not contain the word.")

    sentence = input("Enter a sentence: ")
old_word = input("Word to replace: ")
new_word = input("Replace with: ")

result = sentence.replace(old_word, new_word)

print(result)

text = input("Enter a string: ")

print("First character:", text[0])
print("Last character:", text[-1])

text = input("Enter a string: ")

print("Reversed:", text[::-1])

sentence = input("Enter a sentence: ")

words = sentence.split()

print("Number of words:", len(words))

text = input("Enter a string: ")

has_digit = False

for character in text:
    if character.isdigit():
        has_digit = True
        break

if has_digit:
    print("The string contains digits.")
else:
    print("The string does not contain digits.")

    words = ["tree", "leaf", "garden"]

result = "-".join(words)

print(result)

text = input("Enter a string: ")

result = text.replace(" ", "")

print(result)

text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")

if text1 == text2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")

    sentence = input("Enter a sentence: ")

words = sentence.split()

acronym = ""

for word in words:
    acronym += word[0].upper()

print("Acronym:", acronym)

text = input("Enter a string: ")
character = input("Enter a character to remove: ")

result = text.replace(character, "")

print("Result:", result)

text = input("Enter a string: ")

vowels = "aeiouAEIOU"

for vowel in vowels:
    text = text.replace(vowel, "*")

print(text)

text = input("Enter a sentence: ")
start = input("Starts with: ")
end = input("Ends with: ")

if text.startswith(start) and text.endswith(end):
    print("True")
else:
    print("False")

username = input("Enter username: ")
password = input("Enter password: ")

if username != "" and password != "":
    print("Username and password are valid.")
else:
    print("Username or password cannot be empty.")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

number = int(input("Enter a number: "))

if number > 0 and number % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is not positive and even.")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 != num2 and num1 != num3 and num2 != num3:
    print("All numbers are different.")
else:
    print("Some numbers are the same.")

text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")

if len(text1) == len(text2):
    print("The strings have the same length.")
else:
    print("The strings do not have the same length.")

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 + num2 > 50:
    print("The sum is greater than 50.")
else:
    print("The sum is 50 or less.")

number = int(input("Enter a number: "))

if 10 <= number <= 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20.")

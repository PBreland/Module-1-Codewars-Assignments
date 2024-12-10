#Exercise 1. Even or Odd

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

#Exercise 2. Convert a Number to a String

def number_to_string(num):
    return str(num)


#Exercise 3. Vowel Count

def get_count(sentence):
    count = 0
    array = ('a','e','i','o','u')
    for char in sentence:
        if char in array:
            count += 1
        return count 
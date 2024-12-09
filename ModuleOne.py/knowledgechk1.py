# Even or Odd

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Convert a Number to a String

def number_to_string(num):
    # Return a string of the number here!
    return str(num)

# Vowel Count

def get_count(sentence):
    vowel = "aeiou"
    count = 0
    for v in sentence:
        if v in vowel:
            print(v)
            count += 1 
    print(count)
    return count    
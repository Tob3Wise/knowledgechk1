my_books = []

first_book = input('Enter the first book you would like to add: ')
second_book = input('Enter the second book you would llike to add: ')
third_book = input('Enter the third book you would like to add: ')

my_books.append(first_book)
my_books.append(second_book)
my_books.append(third_book)

my_books.sort()

print(my_books)
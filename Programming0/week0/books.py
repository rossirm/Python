__author__ = 'Боян'

book1_name = "Pragmatic Thinking and Learning"
book1_price = 30
book_counter = 1

book2_name = "Learn You a Haskell"
book2_price = 0
book_counter += 1

book3_name = "The Healthy Programmer"
book3_price = 50
book_counter += 1

book4_name = "Code Complete"
book4_price = 60
book_counter += 1

book5_name = "The Pragmatic Programmer"
book5_price = 20
book_counter += 1

book6_name = "Pro Git"
book6_price = 0
book_counter += 1

book7_name = "Introduction to Algorithms"
book7_price = 80
book_counter += 1

book8_name = "Concrete Mathematics"
book8_price = 100
book_counter += 1

print("=" * 10 + " List of all Books " + "=" * 10)
print("Book: \"{0}\" price: {1}".format(book1_name, book1_price))
print("Book: \"{0}\" price: {1}".format(book2_name, book2_price))
print("Book: \"{0}\" price: {1}".format(book3_name, book3_price))
print("Book: \"{0}\" price: {1}".format(book4_name, book4_price))
print("Book: \"{0}\" price: {1}".format(book5_name, book5_price))
print("Book: \"{0}\" price: {1}".format(book6_name, book6_price))
print("Book: \"{0}\" price: {1}".format(book7_name, book7_price))
print("Book: \"{0}\" price: {1}".format(book8_name, book8_price))

print(50 * "=")
price_all = book1_price + book2_price + book3_price + book4_price + book5_price + book6_price + book7_price + book8_price
print("Price of all books: {0}".format(price_all))

print(50 * "=")
promo_price = book8_price + book7_price - (book8_price + book7_price) * 0.25
print("Introduction to Algorithms and Concrete Mathematics : {0}".format(promo_price))

print(50 * "=")
print("Free books:")
print(book2_name + "\n" + book6_name)
print(50 * "=")
print(book5_name + "\n" + book1_name + "\n" + book3_name)
less_than_150 = book5_price + book1_price + book3_price
print("For a total of : " + str(less_than_150))
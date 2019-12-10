products = []

while True:
    name = input("Enter product name -> ")
    if name == 'q':
    	print('Have a nice day')
    	break
    price = input("Enter a price -> ")
    products.append([name, price])

print("The name of the first product -> ", products[0][0])



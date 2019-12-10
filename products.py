products = []

while True:
    name = input("Enter product name -> ")
    if name == 'q':
    	print('Have a nice day')
    	break
    price = input("Enter a price -> ")
    products.append([name, price])

print(products)

for product in products:
	print(product[0], 'price is ->', product[1])



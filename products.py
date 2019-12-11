
import os # operating system 


products = []

if os.path.isfile('products.csv'):
    print('yes! file found')
    
    with open('products.csv','r', encoding = 'utf-8') as f:
        
        for line in f:
            if 'product, price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    
    print(products)

else:
    print('file not found')



# allow user input
while True:
    name = input("Enter product name -> ")
    if name == 'q':
    	print('Have a nice day')
    	break
    price = input("Enter a price -> ")
    products.append([name, price])
print(products)

#print out all record
for product in products:
	print(product[0], 'price is ->', product[1])

#write in file
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('product,price\n') 
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')

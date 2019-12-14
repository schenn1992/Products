
import os # operating system 

#read file
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
         for line in f:
            if 'product, price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# allow user input
def user_input(products):
    while True: 
        name = input("Enter product name -> ")
        if name == 'q':
            break
        price = input("Enter a price -> ")
        price = int(price)
        products.append([name, price])
    print(products)
    return products
 
#print out all record
def print_products(products):
    for p in products:
        print(p[0], 'price is ->', p[1])

    
#write in file
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('product, price\n') 
        for p in products: 
            f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('yes! file found')
        products = read_file(filename)
    else:
        print('file not found')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()
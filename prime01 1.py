#2 using generator function print prime numbers


def primeNo():
        n = int(input("enter no ::.."))
       
        if n % 2 == 0:

                print("not prime no.")
                
        else:
                print("prime no.")
                yield n
                

numbers = primeNo()
print(type(numbers))
for i in numbers:
        print(i)



# 1. for loop-ის მეშვეობით გამოიტანეთ რიცხვი 10, 7-ჯერ.
# 2. for loop-ის მეშვეობით გამოიტანეთ 'hello' 8-ჯერ.
# 3. Input()-ის გამოყენებით მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ for loop-ით კი დაპრინტეთ ("hello" + მომხმარებლის სახელი) 5 ჯერ.

#1
for i in range(7):
    print(10)

#2
for i in range(8):
    print("hello")

#3
name=input("enter your name:")
for i in range(5):
    print(f"hello {name}")

#4

i = 10
while i <= 30:
    print(i)
    i += 1

#5

i = 50
while i >= 10:
    print(i)
    i -= 1

#6

count = 0
while count < 10:
    print('goa best')
    count += 1


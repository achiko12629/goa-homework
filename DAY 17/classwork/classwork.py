# 1. შექმენით პროგრამა, სადა მომხმარებეს შემოატანინებთ ასაკს, თუ მისი ასაკი იქნება 18-ის ტოლი ან მეტი, გამოუტანეთ რომ ის ზრდასრულია, თუ იქნება ნაკლები, გამოუტანეთ, რომ ჯერ პატარაა.

# 2. შექმენით პროგრამა, სადაც გექნებათ ცვლადი საიდუმლო პაროლით, შემდეგ მომხმარებელს გამაოცნობინეთ სიტყვა, თუ მისი გამოცნობილი სიტყვა უდრის თქვენს საიდუმლო პაროლს, დაუპრინტეთ, რომ გაიმარჯვა.

age = int(input("enter your age:"))

if age >= 18 :
    print("you ar an adult")
elif age < 18 :
    print("you ar underage")

real = "real_madrid"
password = input("try to guess my password:")

if password == real:
    print(" you guessd correct")
else:
    password = input("try to guess my password:")
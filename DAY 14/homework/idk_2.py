#  python

# 2. while loop-ის მეშვეობით გამოიტანეთ ციფრები 10-დან 30-მდე.
# 3. while loop-ის მეშვეობით გამოიტანეთ ციფრები 50-დან 10-მდე.
# 4. while loop-ის მეშვეობით გამოიტანეთ 'goa best' 10-ჯერ.
# 5. შემოიტანეთ რაიმე რიცხვი და გამოაცნობინეთ მომხმარებელს ეს რიცხვი.

#2
age=10
while age <= 30:
    print(age)
    age=age+1

#3
sam= 50
while sam >= 10:
    print(sam)
    sam=sam - 1

#4
goa = 10
while goa > 0:
    print("goa best")
    goa= goa - 1


#5
idk =int( input("enter a nomber from 1 to 10 :"))
while idk != 4:
    print("your so close try agin ")
    idk =int( input("enter a nomber from 1 to 10 :"))
else :
    print("you correctt you win :)))))) ")
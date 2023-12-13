# Flow control: branching and loops

# თუ ოპერაცია
# თუ რაცხა მოხდა ქენი ესა და ეს


# if   /----> რაცხა ქმედება
#------ 
# else \----> სხვა რაცხა ქმედება


# if   /----> რაცხა ქმედება
#------ 
# elif \----> სხვა რაცხა ქმედება
#       \
# else   \----> სხვა რაცხა ქმედება



a = input("შეიყვანეთ რიცხვი: ")

a = int(a)

if a == 0:
    print("ნულოვანია")
elif a > 0:
    print("დადებითი")
else: 
    print("უარყოფითი")


# ლოგიკური "ან" "და" "უარყოფა" => or , and, not

if a > 0 and a < 10: #and
    print("არის შუალედში")

if a > 10 or a < 0: # or
    print("არ არის შუალედში")

if not(a > 0 and a < 10): #not
    print("არ არის შუალედში")

# მაგალითი: მაზაღიაში ნივთი რომელიც ღირსზე 300ზე მეტი დააკლდება 40%, რომელიც არის 200სა და 300ს შორის დააკლდება 30% 
# ნივთი რომელიც არის 150სა და 200ს შორის დააკლდება 20. სხვა ნივთებს კი 10%. 
# შემოვა რიცხვი და დამიპრინტე რამდენი დააკლდება

girebuleba = int(input("შეიყვანეთ ფასი: "))

if girebuleba > 300:
    print("დააკლდება 40%")
elif 200 < girebuleba and girebuleba <= 300:
    print("დააკლდება 30%")
elif 150 < girebuleba and girebuleba <= 200:
    print("დააკლდება 20%")
else:
    print("დააკლდება 10%")



# ლუპები => კოდის ბლოკი, როლემიც ერთსა და იმავე მოქმედებას რამდენიმეჯერ ასრულებს.

#თუ a რიცხვი მინდა 10ჯერ გავამრავლო 5ზე , შემიძლია ჩავწერო:
a = 15

a = a * 5
a = a * 5
a = a * 5
a = a * 5
a = a * 5
a = a * 5
a = a * 5
a = a * 5
a = a * 5
a = a * 5
a = a * 5 # a = 15 * 5 ^ 10
print(a)


# ----------- -------->
#    ↑    if \   else
#    \       /
#     -------
#        ↓
#     შეცვალე

i = 0
while i < 10: 
    print(i)
    i = i + 1


# შემოიტანე ასახარისხებელი რიცხვი და ხარისხის მაჩვენებელი. გამოიტანე რიცხვი ხარისხად ხარისხის მაჩვენებელი
# რიცხვი - 10, რაოდენობა - 4 => 10 ^ 4 = 10 * 10 * 10 * 10 = 10000
ricxvi = input("რიცხვი: ")
xarisxisMachvenebeli = input("რაოდენობა: ")
ricxvi = int(ricxvi)
xarisxisMachvenebeli = int(xarisxisMachvenebeli)
temp = ricxvi

j = 1
while j < xarisxisMachvenebeli: # სანამ რაღაც ლოგიკური ოპერაცია ჭეშმარიტია. whileით ვასრულებთ მოქმედებას სანამ პირობა ჭეშმარიტია
    j = j + 1
    ricxvi = ricxvi * temp

print(ricxvi)

# for = უკეთესი ვერსია whileის

for i in range(xarisxisMachvenebeli): # თითოეული iსთვის მოცემულ შუალედში. forით ვასრულებთ მოქმედებს რამდენიმეჯერ
    ricxvi = ricxvi * temp

print(ricxvi)


# |\
# | \
# |  \
# |   \
# |____\


for i in range(5):
    for j in range(i):
        print("*")
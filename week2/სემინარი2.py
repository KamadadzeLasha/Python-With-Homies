# მომხმარებელი შეიყვანს რიცხვს. დაშალე რიცხვი მარტივ მამრავლებად.
#
# example 1:
# >გთხოვთ შეიყვანოთ რიცხვი:
# <45
# >3 3 5
#
# example 2:
# >გთხოვთ შეიყვანოთ რიცხვი:
# <68
# >2 2 17    
# 68 | 2
# 34 | 2
# 17 | 17
# 1  | 1


ricxvi = input("გთხოვთ შეიყვანოთ რიცხვი: ")
ricxvi = int(ricxvi)
zgvari = ricxvi + 1

shedegi = ""
if ricxvi <= 1:
    print("Error რიცხვი 1ზე მეტი უნდა იყოს")
else:
    while (ricxvi != 1):
        for i in range(2, zgvari):
            if(ricxvi % i == 0):
                shedegi = shedegi + str(i)
                ricxvi = ricxvi / i
                break

print(shedegi)

# შეატანინე მომხმარებელს N რიცხვი. შემდეგ N ცალი რიცხვი. გამოიტანე ამ რიცხვებიდან ორი ყველაზე მაღალი.
# example 1:

# <განსაზღვრეთ რაოდენობა:
# >3
# <გთხოვთ, შეიყვანეთ მთელი რიცხვი:
# >1
# <გთხოვთ, შეიყვანეთ მთელი რიცხვი:
# >32
# <გთხოვთ, შეიყვანეთ მთელი რიცხვი:
# >32
# <პირველი:
# <32
# <მეორე:
# <32

raodenoba = int(input("განსაზღვრეთ რაოდენობა: "))
if raodenoba < 2:
    print("აი რაა ჭო?")
else:
    magali1 = int(input("გთხოვთ, შეიყვანეთ მთელი რიცხვი: "))
    magali2 = int(input("გთხოვთ, შეიყვანეთ მთელი რიცხვი: "))
    if magali1 < magali2:
        magali1, magali2 = magali2, magali1
    raodenoba = raodenoba - 2
    for i in range(raodenoba):
        ricxvi = int(input("გთხოვთ, შეიყვანეთ მთელი რიცხვი: "))
        if ricxvi > magali1:
            magali2 = magali1
            magali1 = ricxvi
        elif ricxvi > magali2:
            magali2 = ricxvi
    print("პირველი",magali1)
    print("მეორე",magali2)
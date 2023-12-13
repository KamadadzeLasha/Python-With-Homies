# Basic operations, variables and IO(input/output) in Python. 

print("Hello World!")

# intigers(მთელი რიცხვები) => 10, 20, 30, 40
a = 10
damateba1 = a + 5 # 15
gamravleba1 = a * 5 # 50
gamokleba = a - 5 # 5
gayofa = a / 5 # 2
zustiGayofa = a // 5 # 2 
nashtianiGayofa = a % 5 # 0

print(damateba1)
print(gamravleba1)
print(gamokleba)
print(gayofa)
print(zustiGayofa)
print(nashtianiGayofa)

# float(წილადი რიცხვები) => 10.5, 20.5, 30.5, 40.01, 0.0123

b = 10.5
damateba2 = b + 5 # 15.5
gamravleba = b * 5 # 52.5
gamokleba = b - 5 # 5.5
gayofa = b / 5 # 2.1
zustiGayofa = b // 5 # 2
nashtianiGayofa = b % 5 # 0.5

print(damateba2)
print(gamravleba)
print(gamokleba)
print(gayofa)
print(zustiGayofa)
print(nashtianiGayofa)

# str(სიტყვა) => "Hello World", "ასდფასდფ", "123456"

sityva = "მე ვარ სიტყვა"
shemdegiXazi = "\n" # "მე ვარ სიტყვა და მიხარია ცხოვრება\nგამარჯობა " => "მე ვარ სიტყვა და მიხარია ცხოვრება
#                                                                   გამარჯობა "
tabi = "\t" # "მე ვარ სიტყვა და მიხარია ცხოვრება\tგამარჯობა " => "მე ვარ სიტყვა და მიხარია ცხოვრება     გამარჯობა "
brwyali = "\"" # "მე ვარ სიტყვა და მიხარია ცხოვრება\" => "მე ვარ სიტყვა და მიხარია ცხოვრება""
martiviBrwyali = "\'" # "მე ვარ სიტყვა და მიხარია ცხოვრება\'" => "მე ვარ სიტყვა და მიხარია ცხოვრება'"
daxriliXazi = "\\" # "მე ვარ სიტყვა და მიხარია ცხოვრება\\" => "მე ვარ სიტყვა და მიხარია ცხოვრება\"
damatebaSityvis = sityva + " და მიხარია ცხოვრება" # "მე ვარ სიტყვა და მიხარია ცხოვრება" 

# bool(ლოგიკურ ცვლადი) => True, False

# > >= <= < == !=
ricxvi1 = 10
ricxvi2 = 20

metoba = (ricxvi1 > ricxvi2) # False
nakleboba = ricxvi1 < ricxvi2 # True
toloba = ricxvi1 == ricxvi2 # False
arUdris = ricxvi1 != ricxvi2 # True

#saxeli = input("შეიყვანეთ სახელი: ")

#toloba = "lasha" == saxeli

saxeli_da_gvari = input("Enter your  name: ")

print("Hello", saxeli_da_gvari)



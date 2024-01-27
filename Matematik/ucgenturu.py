a=int(input("1.Kenarını giriniz: "))
b=int(input("2. Kenarı giriniz: "))
c=int(input("3. Kenarı giriniz: "))

if a==b and a==c and b==c:
    print("Bu bir eşkenar üçgen!")
elif a==b or a==c or b==c:
    print("Bu bir ikizkenar üçgen!")
else:
    print("Bu bir çeşitkenar!")
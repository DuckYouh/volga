#haromszog
a = int(input("Add meg a háromszög 'a' oldalát: "))
b = int(input("Add meg a háromszög 'b' oldalát: "))
c = int(input("Add meg a háromszög 'c' oldalát: "))

if a+b > c and a+c > b and c+b > a:
    print("A(z)",a,",",b,",és",c,"háromszöget alkot.")
else:
    print("A(z)",a,",",b,",és",c,"nem alkot háromszöget.")
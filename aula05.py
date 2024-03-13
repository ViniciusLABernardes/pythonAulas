#operaçoes_booleanas_if
print(1 == 2)
print(1 != 2, 1 != 1)
print("abc" == "cba")
print("a" == "A")
print(10 >9, 10 > 10, 10 >= 10, 10 >= 1)
if 10 > 1:
    print("oi")

x = 70
if x > 90:
    print(f"{x} e maior que 90")
    if x > 100:
           print(f"{x} e maior que 100")
else:
     print(f"{x} n e maior que 90")

media = 7
exame = True


if media >= 6:
     print("passou")
elif media < 6 and media >= 3 and exame == True:
     print(f"Exame")
elif media < 6 and media >=3 and exame == False:
     print(f"recuperacao")     

else:
     print(f"reprovado")

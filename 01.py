# %%  ejercicio 1
def calcular_máximo(a: int, b: int) -> int:
    if a > b:
        return a
    if a == b:
        print("son iguales")
        return "son iguales"
    else:
        return b

r1 = calcular_máximo(1,2)
r2 = calcular_máximo(4,5)
r3 = calcular_máximo(5,5)

assert r1 == 2
assert r2 == 5
assert r3 == "son iguales"


# %% cual es mayor de 3:
def calcular_máximo3(a: int, b: int, c: int) -> int:

    
    if a > b:
        if a>c:
            return a
    if b>a:
        if b>c:
            return b
    if c>a:
        if c>b:
            return c
    else:
        print("son iguales")
        return "son iguales"
        

r1 = calcular_máximo3(1,2,3)
r2 = calcular_máximo3(4,5,8)
r3 = calcular_máximo3(5,5,5)

assert r1 == 3
assert r2 == 8
assert r3 == "son iguales"



# %% calcular la longitud de una cadena
c = 0
def longitud_cadena (frase: list)->int:
    for letra in frase:
        c = c+1
    else:
        print(c)
        return c
    
longitud_cadena("Pablo pablito tragó un tragito")
print(c)



# %%

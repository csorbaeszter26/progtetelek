def szekInit(szin:str, labszam:int):
    print(f"szin: {szin}, lábszám: {labszam}")

szekInit("kek", 3)
szekInit("piros", 4)
szekInit("zöld", 5)


def szekStr(szin:str, labszam:int):
    return f"szin: {szin}, lábszám: {labszam}"

print(szekStr("kek", 3))
print(szekStr("piros", 4))
print(szekStr("zöld", 5))


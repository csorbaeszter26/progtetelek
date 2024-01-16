from Szek import Szek

peldany1 = Szek("kék", 13)
peldany2 = Szek("piros", 4)
peldany3 = Szek("zöld", 5)
print(peldany1.__str__())
print(peldany2)
print(peldany3)

szekek = [peldany1, peldany2, peldany3]
def labakSzamolas():
    # Összegzés tétele
    print("Összesen hány db székláb van a teremben: ", end="")
    ossz = 0
    for index in range(0, len(szekek), 1):
        ossz += szekek[index].labszam
    print(f"{ossz} db")

labakSzamolas()

def maxLabSzine():
    max = 0
    for index in range(1, len(szekek), 1):
        if szekek[index].labszam > szekek[max].labszam:
            max = index
    print(f"A legtöbb lábú szék színe: {szekek[max].szin}")
maxLabSzine()




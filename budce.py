# ayliq geleri ve xercleri almaq
gelir = int(input("ayliq gelir daxil edin: "))
xerc = int(input("ayliq xerc daxil edin: "))
if gelir < 0 or xerc < 0:
    print("gelir ve xerc menfi ola bilmez")
elif gelir ==0:
    print("gelir sifir ola bilmez")
elif xerc > gelir:
    print("budge kesiri var")
elif xerc >= gelir * 0.8:
    print("xerce diqqet et")
elif xerc > gelir * 0.8 and xerc < gelir * 0.5:
    print("xerc normaldir")
elif xerc < gelir * 0.5:
    print("yaxsi qenaet:")
else:
    print("hesablama duzgun deyil")
# ayin sonu ucun qalan meblegi hesablayin
qalan = gelir - xerc
faiz = (qalan/gelir) * 100
print("ayin sonu qalan mebleg:")
print(qalan)
print("qenaet faizi hesablla:")
print(faiz)
# sifaris mebelegi yazin
mebleg = float(input("mebleg daxil et:"))
if mebleg >= 200:
    mebleg = mebleg * 0.2
    print("mebleg:", mebleg)
elif mebleg >= 100 and mebleg <= 199.99:
    mebleg = mebleg * 0.1
    print("mebleg:", mebleg)
elif mebleg < 100:
    mebleg = mebleg
    print("mebleg:", mebleg)
if mebleg < 0:
   print("xeta")
   
result = "endirim qazandiniz" if mebleg > 200 else "endirim yoxdur"
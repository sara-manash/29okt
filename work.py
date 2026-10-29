# uygunlugu ve tecrubeni yoxlamaq tecrube ilini ve bali daxil etmek
tecrube = int(input("tecrube il daxil etmek"))
bal = int(input("bal daxil etmek"))
if 0 <= bal <= 100 and 0 <= tecrube :
    result = "kecdi" if tecrube >= 2 and bal >= 70 else "kecmedi"
    if tecrube >=2 and bal >= 70:
      print("novbeti merheleye devet olunur")
    elif bal >= 90:
        print("siz super namizedsiz")
    else:
        print("ugursuz")
else:
    print("duzgun bal ve tecrube daxil edin")
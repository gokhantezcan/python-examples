# -*- coding: utf-8 -*-
fileObject = open("deneme.txt", "w", encoding = "utf-8")
fileObject.write("# -*- coding: utf-8 -*-\n")
"""fileObject.write("Bu")
fileObject.write("Bir")
fileObject.write("örnek")
fileObject.write("metindir.")
lines = ["bu\n", "örnek\n", "metindir."]
fileObject.writelines(lines)
fileObject.close()


# bu kendi zaten close etmektedir.
# w modunda acılan dosyaya sadece yeni verilen girilir.
with open("deneme.txt", "w", encoding = "utf-8") as fileObject:
    lines = ["# -*- coding: utf-8 -*-\n","bu\n", "örnek\n", "metindir."]
    fileObject.writelines(lines)
"""
with open("deneme.txt", "w", encoding = "utf-8") as fileObject:
    lines = ["# -*- coding: utf-8 -*-\n","bu\n", "örnek\n", "metindir."]
    fileObject.writelines(lines)

# r+ yazarsak hem okuyup hem yazabiliriz.ancak daha önceden sistemde olmalı
# w+ ise önceden olmasına gerkemez ancak üzerine veri yazılmaz silinir. esksiler gider.
# a ise yenileri eskilerin ustune ekler. dosdya yok sie onu da oluşturur.
# fileobject.seek(0) okumada önce curser nereye gitsin ki oradan itibaren okusun.
with open("deneme.txt", "r+") as fileObject:
    for lineText in fileObject.readlines():
        print(lineText, end="")
    fileObject.write(".")

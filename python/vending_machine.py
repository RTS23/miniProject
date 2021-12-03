# Vending Machine

# Price list:
# aqua 2000
# sosro 5000
# cola 7000
# milo 9000

# rule:
# max input 3x
# denom yg diterima 2000 dan 5000

# contoh:
# 2000 1 lembar -> 1 aqua
# 2000 2 lembar -> 2 aqua
# 5000 1 lembar, 2000 1 lembar-> 1 cola
# 1000 1 lembar -> pecahan tidak valid
# 5000 2 lembar -> 1 Milo
# 5000 3 lembar -> 1 Milo, 1 Sosro

def vendingMachine(n):
    listUang = []
    priceList = [2000,5000,7000,9000]
    priceListSorted = []
    itemTaken = []
    
    if n <= 3:
        for x in range(0,n):
            y = int(input())
            if y == 2000 or y == 5000:
                listUang.append(y)
            else:
                return "Denom Salah"

    sumUang = sum(listUang)
        
    for x in range(0,4):
        priceListSorted.append(priceList.pop())
    
    for x in priceListSorted:
        if sumUang >= x:
            itemTaken.append(x)
            sumUang -= x
        else:
            continue

    return itemTaken

x = vendingMachine(3)
print(x)
print ("Conversor de numeros romanos - Consigna 1 Computacion - Francisco Robledo \n")

decimal_to_roman = int(input("Introduci el numero: "))

roman = str()

class Roman_converter:

    millar = (int((decimal_to_roman/1000)))*1000
    centena = (int((decimal_to_roman - millar)/100))*100
    decena = (int((decimal_to_roman - millar - centena)/10))*10
    unidad = int((decimal_to_roman - millar - centena - decena))

    if millar == 3000:
        roman += "MMM"
    elif millar == 2000:
        roman += "MM"
    elif millar == 1000:
        roman += "M"

    if centena == 900:
        roman += "CM"
    elif centena == 800:
        roman += "DCCC"
    elif centena == 700:
        roman += "DCC"
    elif centena == 600:
        roman += "DC"
    elif centena == 500:
        roman += "D"
    elif centena == 400:
        roman += "CD"
    elif centena == 300:
        roman += "CCC"
    elif centena == 200:
        roman += "CC"
    elif centena == 100:
        roman += "C"

    if decena == 90:
        roman += "XC"
    elif decena == 80:
        roman += "LXXX"
    elif decena == 70:
        roman += "LXX"
    elif decena == 60:
        roman += "LX"
    elif decena == 50:
        roman += "L"
    elif decena == 40:
        roman += "XL"
    elif decena == 30:
        roman += "XXX"
    elif decena == 20:
        roman += "XX"
    elif decena == 10:
        roman += "X"

    if unidad == 9:
        roman += "IX"
    elif unidad == 8:
        roman += "VIII"
    elif unidad == 7:
        roman += "VII"
    elif unidad == 6:
        roman += "VI"
    elif unidad == 5:
        roman += "V"
    elif unidad == 4:
        roman += "IV"
    elif unidad == 3:
        roman += "III"
    elif unidad == 2:
        roman += "II"
    elif unidad == 1:
        roman += "I"

    print("\nEl numero en romano es: ", roman)



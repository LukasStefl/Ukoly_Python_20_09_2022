print("Napiste dve cisla:\n")
prvni_cislo = int(input());
druhe_cislo = int(input());

if (prvni_cislo * druhe_cislo) < 1000:
    vysledek = prvni_cislo * druhe_cislo;
    print(vysledek);
elif (prvni_cislo * druhe_cislo) > 1000:
    vysledek = prvni_cislo + druhe_cislo;
    print(vysledek);
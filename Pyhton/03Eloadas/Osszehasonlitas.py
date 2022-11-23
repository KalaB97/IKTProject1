def Osszehasonlitas(veletlenSzam,begepeltSzam):
    try:
        begepeltSzam=int(begepeltSzam)
        if (veletlenSzam>begepeltSzam):
            return f"A gép nagyobb számra gondolt: {veletlenSzam}"
        elif (veletlenSzam<begepeltSzam):
            return f"A gép kisebb számra gondolt: {veletlenSzam}"
        else:
            return f"Eltaláltad a gép által gondolt számot! {veletlenSzam}"
    except ValueError:
        return "Nem számot adtál meg!"
    except:
        return "Ide hogy jutottam???"
    finally:
        print("A függvényem tette a dolgát...")
# TesztBolt demóalkalmazás

Szakdolgozati mérési környezet: kitalált adatokkal működő, statikus webshop.
Egy fájl változatonként (HTML, CSS, JavaScript), szerver és külső hívás nélkül.

## Fájlok
- `index.html` – a változatok listája (kezdőlap)
- `v0/ … v4/` – a változatok (`index.html` mindegyikben)
- `generate.py` – a változatokat egyetlen sablonból állítja elő (`python3 generate.py`)
- `TESZTLEIRAS.md`, `VALTOZATOK.md` – a mérési terv alapja
- `screenshots/` – képernyőképek az ábrákhoz

## Helyi kipróbálás
Nyisd meg a `v0/index.html` fájlt böngészőben. Bejelentkezés: `demo` / `Teszt123!`.

## Közzététel GitHub Pagesen (nyilvános URL)
1. Hozz létre egy új, nyilvános tárolót (például `tesztbolt-demo`).
2. Töltsd fel az egész mappa tartalmát (a `v0`–`v4` mappákat és az `index.html`-t).
3. Settings → Pages → Source: „Deploy from a branch", branch: `main`, mappa: `/ (root)`.
4. Pár perc múlva a címek: `https://<felhasználó>.github.io/tesztbolt-demo/v0/` … `/v4/`.
5. Ellenőrizd mind az öt címet böngészőben, mielőtt a teszteszközökben használod.

Ne írj a tárolóba valódi személyes adatot. A testRigor ingyenes csomagjában a tesztek nyilvánosak.

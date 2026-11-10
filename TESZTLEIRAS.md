# TesztBolt – tesztleírás (8 teszt, 4 szenárió)

Demó hozzáférés: felhasználónév `demo`, jelszó `Teszt123!`. Minden adat kitalált.
Az összes tesztet V0-n veszed fel, a V1–V4 változatokon a tesztet változtatás nélkül futtatod újra (csak a kezdő URL tér el).

| Teszt | Szenárió | Lépések | Ellenőrző pont (V0, helyes viselkedés) |
|---|---|---|---|
| T1a | S1 bejelentkezés, érvényes | demo / Teszt123! megadása, belépés | „Üdvözöljük, demo!" felirat |
| T1b | S1 bejelentkezés, érvénytelen | demo / rossz jelszó, belépés | „Hibás felhasználónév vagy jelszó." |
| T2a | S2 keresés | keresés: `lámpa` | „1 találat", az Asztali lámpa látszik |
| T2b | S2 keresés és szűrés | kategória: Sport, keresés: `lámpa` | „Nincs találat." (a lámpa Otthon kategóriájú) |
| T3a | S3 űrlap, helyes | termék a kosárba, kosár, pénztár; név: Teszt Elek, e-mail: teszt@example.com, cím: Fő utca 1., irsz.: 9021, megrendelés | „Köszönjük a rendelést!" és rendelésszám |
| T3b | S3 űrlap, hiányzó irányítószám | mint T3a, de az irányítószám üresen marad | „Az irányítószám négy számjegy." hibaüzenet, a rendelés nem megy át |
| T4a | S4 kosár | Asztali lámpa, mennyiség 2, kosár megnyitása | részösszeg 11 980 Ft, szállítás 1 490 Ft, végösszeg 13 470 Ft |
| T4b | S4 teljes folyamat | T4a, majd pénztár, helyes adatok, megrendelés | visszaigazolásban „Fizetendő összeg: 13 470 Ft" |

Szállítási díj: 1 490 Ft, 20 000 Ft felett ingyenes.
A mennyiséget az S4-ben V0–V2 és V4 változatban a számmezőbe írod (2), V3-ban a + gombot egyszer megnyomod. Ez a V3 elemtípus-váltásának szándékos próbája.

## Várt viselkedés változatonként

| Változat | T1a | T1b | T2a | T2b | T3a | T3b | T4a | T4b |
|---|---|---|---|---|---|---|---|---|
| V0 | zöld | zöld | zöld | zöld | zöld | zöld | zöld | zöld |
| V1–V3 | törhet (lokátor), gyógyítható; a gyógyult teszt eredménye azonos a V0-val | | | | | | | |
| V4 | zöld | zöld | zöld | **piros kell** | zöld | **piros kell** | **piros kell** | **piros kell** |

A V4-en a hibát jelző teszt a helyes eredmény. Ha egy V4-teszt zöldre fut, az a téves gyógyítás (hamis zöld).

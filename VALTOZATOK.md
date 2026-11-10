# Változatok és szándékos különbségeik

| Változat | Mi változik | Mit modellez |
|---|---|---|
| V0 | alapváltozat | kiindulás |
| V1 | minden `id` és `class` átnevezve (pl. `login-btn` → `signin`, `username` → `uname`, `product-card` → `item-tile`); a látható felület azonos | lokátor-törés |
| V2 | a kereső és a kategóriaszűrő a fejlécsor alól az oldalsávba kerül; a kosár hivatkozás a fejlécből az oldal aljára; az űrlap mezőinek sorrendje fordított (irányítószám, cím, e-mail, név) | elrendezés-változás |
| V3 | szövegek: Belépés → Bejelentkezés, Felhasználónév → Azonosító, Jelszó → Jelszó megadása, Keresés → Találatok megjelenítése, Kosárba → Hozzáadás, Kosár → Kosaram, Tovább a pénztárhoz → Fizetés, Megrendelés → Rendelés elküldése, Eltávolítás → Törlés. Elemtípus: a mennyiség számmezője −/+ gombokra cserélve, a Kosár hivatkozás gombbá válik | tartalmi és szerkezeti változás |
| V4 | V0 alapján három szándékos funkcionális hiba: (1) az irányítószám ellenőrzése kimarad (üresen is átmegy), (2) a szállítási díj kétszer számít a végösszegben, (3) szöveges keresésnél a kategóriaszűrő figyelmen kívül marad | valódi hiba |

A V3 hibatípusa (beviteli mező → gomb) Garousi és társai (2025) kísérletének hibatípusát követi (4.3 fejezet).

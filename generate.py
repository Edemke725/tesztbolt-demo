#!/usr/bin/env python3
"""TesztBolt demóalkalmazás generálója: a v0–v4 változatokat egyetlen sablonból állítja elő.

Használat: python3 generate.py   (a v0/ ... v4/ mappákat és az index.html-t a script mellé írja)
"""
import os
from jinja2 import Template

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- azonosítók és osztálynevek: V0 és V1 ----
IDS0 = dict(
    view_login="view-login", view_shop="view-shop", view_cart="view-cart", view_checkout="view-checkout", view_confirm="view-confirm",
    user="username", pwd="password", login_btn="login-btn", login_err="login-error", welcome="welcome",
    search="search-input", search_btn="search-btn", category="category-filter", count="result-count", list="product-list", none="no-results",
    cart_link="cart-link", cart_count="cart-count", cart_items="cart-items", subtotal="subtotal", shipping="shipping", total="cart-total",
    empty_cart="empty-cart", checkout_btn="checkout-btn", back_btn="back-to-shop",
    f_name="ship-name", f_email="ship-email", f_addr="ship-address", f_zip="ship-zip",
    e_name="err-name", e_email="err-email", e_addr="err-address", e_zip="err-zip", submit_btn="place-order",
    order_no="order-number", order_total="order-total",
)
IDS1 = dict(
    view_login="screen-auth", view_shop="screen-catalog", view_cart="screen-basket", view_checkout="screen-payment", view_confirm="screen-done",
    user="uname", pwd="pwd", login_btn="signin", login_err="auth-msg", welcome="greeting",
    search="q", search_btn="find", category="cat", count="hits", list="catalog", none="nothing-found",
    cart_link="basket-link", cart_count="basket-qty", cart_items="basket-lines", subtotal="sum-items", shipping="sum-ship", total="sum-total",
    empty_cart="basket-empty", checkout_btn="to-payment", back_btn="back-catalog",
    f_name="cust-name", f_email="cust-mail", f_addr="cust-addr", f_zip="cust-zip",
    e_name="msg-name", e_email="msg-mail", e_addr="msg-addr", e_zip="msg-zip", submit_btn="confirm-order",
    order_no="ord-id", order_total="ord-sum",
)
CLS0 = dict(header="site-header", banner="demo-banner", card="product-card", btn="btn", field="field", error="error",
            add="add-to-cart", qty="qty", row="cart-row", remove="remove-item", panel="panel", side="side", layout="layout", footerbar="footer-bar")
CLS1 = dict(header="top-bar", banner="notice-strip", card="item-tile", btn="action", field="form-row", error="msg-err",
            add="buy-now", qty="amount", row="line", remove="drop-line", panel="box", side="aside", layout="grid", footerbar="bottom-bar")

VERSIONS = {
    "v0": dict(title="V0 – alapváltozat", ids=IDS0, cls=CLS0, v2=False, v3=False, bugs=[]),
    "v1": dict(title="V1 – azonosítók és osztálynevek átnevezve", ids=IDS1, cls=CLS1, v2=False, v3=False, bugs=[]),
    "v2": dict(title="V2 – elemek áthelyezve", ids=IDS0, cls=CLS0, v2=True, v3=False, bugs=[]),
    "v3": dict(title="V3 – szövegek átfogalmazva, elemtípus-váltás", ids=IDS0, cls=CLS0, v2=False, v3=True, bugs=[]),
    "v4": dict(title="V4 – szándékosan beépített funkcionális hibák", ids=IDS0, cls=CLS0, v2=False, v3=False,
               bugs=["zip", "shipping", "category"]),
}

TXT0 = dict(login="Belépés", search="Keresés", add="Kosárba", cart="Kosár", checkout="Tovább a pénztárhoz", order="Megrendelés",
            user="Felhasználónév", pwd="Jelszó", back="Vissza a termékekhez", remove="Eltávolítás")
TXT3 = dict(login="Bejelentkezés", search="Találatok megjelenítése", add="Hozzáadás", cart="Kosaram", checkout="Fizetés", order="Rendelés elküldése",
            user="Azonosító", pwd="Jelszó megadása", back="Vissza a kínálathoz", remove="Törlés")

TEMPLATE = r"""<!doctype html>
<html lang="hu">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TesztBolt – demóalkalmazás ({{ v.title }})</title>
<style>
  body { font-family: Arial, Helvetica, sans-serif; margin: 0; color: #1d2733; background: #f4f6f8; }
  .{{c.banner}} { background: #fff3cd; border-bottom: 1px solid #e0c97a; text-align: center; padding: 6px; font-size: 14px; }
  .{{c.header}} { display: flex; justify-content: space-between; align-items: center; padding: 12px 24px; background: #1f3a5f; color: #fff; }
  .{{c.header}} h1 { margin: 0; font-size: 22px; }
  .{{c.header}} a, .{{c.header}} button.linklike { color: #fff; }
  button.linklike { background: none; border: none; text-decoration: underline; font-size: 16px; cursor: pointer; padding: 0; }
  main { max-width: 960px; margin: 24px auto; padding: 0 16px; }
  .{{c.panel}} { background: #fff; border: 1px solid #d5dbe1; border-radius: 6px; padding: 16px; margin-bottom: 16px; }
  .{{c.layout}} { display: flex; gap: 16px; }
  .{{c.side}} { width: 240px; flex: none; }
  .{{c.layout}} > div { flex: 1; }
  .{{c.field}} { margin-bottom: 12px; display: flex; flex-direction: column; }
  .{{c.field}} label { font-weight: bold; margin-bottom: 4px; }
  input, select { padding: 8px; font-size: 15px; border: 1px solid #98a4b0; border-radius: 4px; }
  .{{c.btn}} { padding: 8px 14px; background: #2d6cdf; color: #fff; border: none; border-radius: 4px; font-size: 15px; cursor: pointer; }
  .{{c.btn}}.secondary { background: #6b7a89; }
  .{{c.error}} { color: #b3261e; font-size: 13px; min-height: 16px; }
  .grid-products { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px; }
  .{{c.card}} { background: #fff; border: 1px solid #d5dbe1; border-radius: 6px; padding: 12px; }
  .{{c.card}} h3 { margin: 0 0 4px 0; font-size: 16px; }
  .{{c.card}} .cat { color: #5b6773; font-size: 13px; }
  .{{c.card}} .price { font-weight: bold; margin: 8px 0; }
  .{{c.row}} { display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid #e4e8ec; }
  .{{c.footerbar}} { margin-top: 16px; padding: 12px; background: #e8eef5; border-radius: 6px; }
  .{{c.qty}} { width: 56px; }
  .stepper { display: inline-flex; align-items: center; gap: 6px; }
  .stepper button { width: 28px; height: 28px; }
  .hidden { display: none !important; }
</style>
</head>
<body>
<div class="{{c.banner}}">Demóalkalmazás, kitalált adatok – nem valódi áruház</div>
<header class="{{c.header}}">
  <h1>TesztBolt</h1>
  <nav>
    <span id="{{i.welcome}}"></span>
    {% if not v.v2 %}
    {% if v.v3 %}<button type="button" class="linklike hidden" id="{{i.cart_link}}">{{ t.cart }} (<span id="{{i.cart_count}}">0</span>)</button>
    {% else %}<a href="#" class="hidden" id="{{i.cart_link}}">{{ t.cart }} (<span id="{{i.cart_count}}">0</span>)</a>{% endif %}
    {% endif %}
  </nav>
</header>
<main>

<section id="{{i.view_login}}" class="{{c.panel}}">
  <h2>{{ t.login }}</h2>
  <form id="login-form" novalidate>
    <div class="{{c.field}}"><label for="{{i.user}}">{{ t.user }}</label><input type="text" id="{{i.user}}" autocomplete="off"></div>
    <div class="{{c.field}}"><label for="{{i.pwd}}">{{ t.pwd }}</label><input type="password" id="{{i.pwd}}" autocomplete="off"></div>
    <div class="{{c.error}}" id="{{i.login_err}}" role="alert"></div>
    <button type="submit" class="{{c.btn}}" id="{{i.login_btn}}">{{ t.login }}</button>
  </form>
  <p style="font-size:13px;color:#5b6773">Demó hozzáférés: felhasználónév <b>demo</b>, jelszó <b>Teszt123!</b></p>
</section>

<section id="{{i.view_shop}}" class="hidden">
  <h2>Termékek</h2>
  <div class="{% if v.v2 %}{{c.layout}}{% endif %}">
  {% if v.v2 %}
  <aside class="{{c.side}} {{c.panel}}">
    <div class="{{c.field}}"><label for="{{i.search}}">Keresés a termékek között</label><input type="text" id="{{i.search}}"></div>
    <div class="{{c.field}}"><label for="{{i.category}}">Kategória</label>
      <select id="{{i.category}}"><option value="">Mind</option><option>Elektronika</option><option>Otthon</option><option>Sport</option></select></div>
    <button type="button" class="{{c.btn}}" id="{{i.search_btn}}">{{ t.search }}</button>
  </aside>
  {% endif %}
  <div>
  {% if not v.v2 %}
  <div class="{{c.panel}}" style="display:flex;gap:12px;align-items:flex-end;flex-wrap:wrap">
    <div class="{{c.field}}" style="margin:0"><label for="{{i.search}}">Keresés a termékek között</label><input type="text" id="{{i.search}}"></div>
    <div class="{{c.field}}" style="margin:0"><label for="{{i.category}}">Kategória</label>
      <select id="{{i.category}}"><option value="">Mind</option><option>Elektronika</option><option>Otthon</option><option>Sport</option></select></div>
    <button type="button" class="{{c.btn}}" id="{{i.search_btn}}">{{ t.search }}</button>
  </div>
  {% endif %}
  <p id="{{i.count}}" aria-live="polite"></p>
  <div id="{{i.none}}" class="hidden">Nincs találat.</div>
  <div class="grid-products" id="{{i.list}}"></div>
  {% if v.v2 %}
  <div class="{{c.footerbar}}">
    <a href="#" id="{{i.cart_link}}">{{ t.cart }} (<span id="{{i.cart_count}}">0</span>)</a>
  </div>
  {% endif %}
  </div>
  </div>
</section>

<section id="{{i.view_cart}}" class="{{c.panel}} hidden">
  <h2>{{ t.cart }}</h2>
  <div id="{{i.empty_cart}}" class="hidden">A kosár üres.</div>
  <div id="{{i.cart_items}}"></div>
  <p>Részösszeg: <span id="{{i.subtotal}}">0 Ft</span></p>
  <p>Szállítási díj: <span id="{{i.shipping}}">0 Ft</span></p>
  <p><b>Végösszeg: <span id="{{i.total}}">0 Ft</span></b></p>
  <button type="button" class="{{c.btn}} secondary" id="{{i.back_btn}}">{{ t.back }}</button>
  <button type="button" class="{{c.btn}}" id="{{i.checkout_btn}}">{{ t.checkout }}</button>
</section>

<section id="{{i.view_checkout}}" class="{{c.panel}} hidden">
  <h2>Szállítási adatok</h2>
  <form id="ship-form" novalidate>
  {% set fields_v0 = ['name','email','addr','zip'] %}
  {% set fields = (fields_v0|reverse|list) if v.v2 else fields_v0 %}
  {% for f in fields %}
    {% if f == 'name' %}<div class="{{c.field}}"><label for="{{i.f_name}}">Név</label><input type="text" id="{{i.f_name}}"><span class="{{c.error}}" id="{{i.e_name}}"></span></div>{% endif %}
    {% if f == 'email' %}<div class="{{c.field}}"><label for="{{i.f_email}}">E-mail cím</label><input type="text" id="{{i.f_email}}"><span class="{{c.error}}" id="{{i.e_email}}"></span></div>{% endif %}
    {% if f == 'addr' %}<div class="{{c.field}}"><label for="{{i.f_addr}}">Szállítási cím</label><input type="text" id="{{i.f_addr}}"><span class="{{c.error}}" id="{{i.e_addr}}"></span></div>{% endif %}
    {% if f == 'zip' %}<div class="{{c.field}}"><label for="{{i.f_zip}}">Irányítószám</label><input type="text" id="{{i.f_zip}}" maxlength="6"><span class="{{c.error}}" id="{{i.e_zip}}"></span></div>{% endif %}
  {% endfor %}
    <button type="submit" class="{{c.btn}}" id="{{i.submit_btn}}">{{ t.order }}</button>
  </form>
</section>

<section id="{{i.view_confirm}}" class="{{c.panel}} hidden">
  <h2>Köszönjük a rendelést!</h2>
  <p>Rendelésszám: <span id="{{i.order_no}}"></span></p>
  <p>Fizetendő összeg: <span id="{{i.order_total}}"></span></p>
</section>

</main>
<script>
(function () {
  var PRODUCTS = [
    { id: 1,  name: "Vezeték nélküli fülhallgató", cat: "Elektronika", price: 12990 },
    { id: 2,  name: "Okosóra",                       cat: "Elektronika", price: 24990 },
    { id: 3,  name: "Power bank",                    cat: "Elektronika", price: 7990 },
    { id: 4,  name: "Bluetooth hangszóró",           cat: "Elektronika", price: 9990 },
    { id: 5,  name: "Asztali lámpa",                 cat: "Otthon",      price: 5990 },
    { id: 6,  name: "Kávéfőző",                      cat: "Otthon",      price: 18990 },
    { id: 7,  name: "Párna szett",                   cat: "Otthon",      price: 4990 },
    { id: 8,  name: "Falióra",                       cat: "Otthon",      price: 3990 },
    { id: 9,  name: "Jógamatrac",                    cat: "Sport",       price: 6490 },
    { id: 10, name: "Kulacs",                        cat: "Sport",       price: 2490 },
    { id: 11, name: "Ugrókötél",                     cat: "Sport",       price: 1990 },
    { id: 12, name: "Futóöv",                        cat: "Sport",       price: 3490 }
  ];
  var SHIPPING_FEE = 1490, FREE_SHIPPING_FROM = 20000;
  var BUGS = {{ v.bugs|tojson }};
  var cart = {};   // id -> mennyiség
  var orderSeq = 1001;
  var ID = {{ i|tojson }};
  function $(k) { return document.getElementById(ID[k]); }
  function show(view) {
    ["view_login", "view_shop", "view_cart", "view_checkout", "view_confirm"].forEach(function (k) { $(k).classList.add("hidden"); });
    $(view).classList.remove("hidden");
  }
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " Ft"; }
  function cartCount() { var n = 0; for (var k in cart) n += cart[k]; return n; }
  function updateCartLink() { $("cart_count").textContent = cartCount(); }
  function totals() {
    var sub = 0;
    PRODUCTS.forEach(function (p) { if (cart[p.id]) sub += p.price * cart[p.id]; });
    var ship = (sub === 0 || sub >= FREE_SHIPPING_FROM) ? 0 : SHIPPING_FEE;
    var total = sub + ship;
    if (BUGS.indexOf("shipping") >= 0 && ship > 0) total = sub + ship * 2;   // V4 hiba: a szállítási díj kétszer számít
    return { sub: sub, ship: ship, total: total };
  }

  // ---- bejelentkezés ----
  document.getElementById("login-form").addEventListener("submit", function (e) {
    e.preventDefault();
    var u = $("user").value, p = $("pwd").value;
    if (u === "demo" && p === "Teszt123!") {
      $("login_err").textContent = "";
      $("welcome").textContent = "Üdvözöljük, demo!";
      var cl = $("cart_link"); if (cl) cl.classList.remove("hidden");
      show("view_shop"); renderProducts();
    } else {
      $("login_err").textContent = "Hibás felhasználónév vagy jelszó.";
    }
  });

  // ---- termékek ----
  function renderProducts() {
    var q = $("search").value.trim().toLowerCase();
    var cat = $("category").value;
    var list = PRODUCTS.filter(function (p) {
      var okText = !q || p.name.toLowerCase().indexOf(q) >= 0;
      var okCat = !cat || p.cat === cat;
      if (BUGS.indexOf("category") >= 0 && q) okCat = true;   // V4 hiba: szövegkeresésnél a kategóriaszűrő figyelmen kívül marad
      return okText && okCat;
    });
    $("count").textContent = list.length + " találat";
    $("none").classList.toggle("hidden", list.length !== 0);
    var box = $("list"); box.innerHTML = "";
    list.forEach(function (p) {
      var el = document.createElement("article");
      el.className = "{{c.card}}";
      var qtyHtml = {% if v.v3 %}
        '<span class="stepper"><button type="button" class="minus" aria-label="Kevesebb">−</button><span class="qval">1</span><button type="button" class="plus" aria-label="Több">+</button></span>'
      {% else %}
        '<input type="number" min="1" value="1" class="{{c.qty}}" aria-label="Mennyiség">'
      {% endif %};
      el.innerHTML = '<h3></h3><div class="cat"></div><div class="price"></div>' + qtyHtml +
        ' <button type="button" class="{{c.btn}} {{c.add}}">{{ t.add }}</button>';
      el.querySelector("h3").textContent = p.name;
      el.querySelector(".cat").textContent = p.cat;
      el.querySelector(".price").textContent = fmt(p.price);
      {% if v.v3 %}
      var qv = el.querySelector(".qval");
      el.querySelector(".plus").addEventListener("click", function () { qv.textContent = String(Number(qv.textContent) + 1); });
      el.querySelector(".minus").addEventListener("click", function () { qv.textContent = String(Math.max(1, Number(qv.textContent) - 1)); });
      {% endif %}
      el.querySelector(".{{c.add}}").addEventListener("click", function () {
        {% if v.v3 %}var n = Number(qv.textContent);{% else %}var n = parseInt(el.querySelector(".{{c.qty}}").value, 10);{% endif %}
        if (!(n >= 1)) n = 1;
        cart[p.id] = (cart[p.id] || 0) + n;
        updateCartLink();
      });
      box.appendChild(el);
    });
  }
  $("search_btn").addEventListener("click", renderProducts);
  $("category").addEventListener("change", renderProducts);

  // ---- kosár ----
  function renderCart() {
    var box = $("cart_items"); box.innerHTML = "";
    var has = false;
    PRODUCTS.forEach(function (p) {
      if (!cart[p.id]) return;
      has = true;
      var row = document.createElement("div");
      row.className = "{{c.row}}";
      row.innerHTML = '<span class="nm"></span><span class="ln"></span><button type="button" class="{{c.btn}} secondary {{c.remove}}">{{ t.remove }}</button>';
      row.querySelector(".nm").textContent = p.name + " × " + cart[p.id];
      row.querySelector(".ln").textContent = fmt(p.price * cart[p.id]);
      row.querySelector(".{{c.remove}}").addEventListener("click", function () { delete cart[p.id]; updateCartLink(); renderCart(); });
      box.appendChild(row);
    });
    $("empty_cart").classList.toggle("hidden", has);
    var t = totals();
    $("subtotal").textContent = fmt(t.sub);
    $("shipping").textContent = fmt(t.ship);
    $("total").textContent = fmt(t.total);
    $("checkout_btn").disabled = !has;
  }
  $("cart_link").addEventListener("click", function (e) { e.preventDefault(); renderCart(); show("view_cart"); });
  $("back_btn").addEventListener("click", function () { show("view_shop"); renderProducts(); });
  $("checkout_btn").addEventListener("click", function () { show("view_checkout"); });

  // ---- szállítási űrlap ----
  document.getElementById("ship-form").addEventListener("submit", function (e) {
    e.preventDefault();
    var name = $("f_name").value.trim(), email = $("f_email").value.trim(), addr = $("f_addr").value.trim(), zip = $("f_zip").value.trim();
    var ok = true;
    $("e_name").textContent = name ? "" : (ok = false, "A név megadása kötelező.");
    $("e_email").textContent = /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) ? "" : (ok = false, "Érvényes e-mail címet adjon meg.");
    $("e_addr").textContent = addr ? "" : (ok = false, "A cím megadása kötelező.");
    if (BUGS.indexOf("zip") >= 0) {
      $("e_zip").textContent = "";                 // V4 hiba: az irányítószám ellenőrzése kimarad
    } else {
      $("e_zip").textContent = /^\d{4}$/.test(zip) ? "" : (ok = false, "Az irányítószám négy számjegy.");
    }
    if (!ok) return;
    var t = totals();
    $("order_no").textContent = "TB-" + (orderSeq++);
    $("order_total").textContent = fmt(t.total);
    cart = {}; updateCartLink();
    show("view_confirm");
  });

  show("view_login");
})();
</script>
</body>
</html>
"""

INDEX = """<!doctype html>
<html lang="hu"><head><meta charset="utf-8"><title>TesztBolt – változatok</title></head>
<body style="font-family:Arial,sans-serif;max-width:720px;margin:40px auto">
<h1>TesztBolt – demóalkalmazás (kitalált adatok)</h1>
<p>A szakdolgozat mérési környezete. Demó hozzáférés: <b>demo</b> / <b>Teszt123!</b></p>
<ul>
{% for k, v in versions.items() %}<li><a href="{{k}}/">{{ v.title }}</a></li>
{% endfor %}</ul>
</body></html>
"""


def main():
    tpl = Template(TEMPLATE)
    for k, v in VERSIONS.items():
        os.makedirs(os.path.join(HERE, k), exist_ok=True)
        html = tpl.render(v=v, i=v["ids"], c=v["cls"], t=(TXT3 if v["v3"] else TXT0))
        with open(os.path.join(HERE, k, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(Template(INDEX).render(versions=VERSIONS))
    print("kész:", ", ".join(VERSIONS))


if __name__ == "__main__":
    main()

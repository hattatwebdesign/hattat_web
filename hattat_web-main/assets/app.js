/* Hattat – Seitenlogik: Menü, Sprachwahl merken, Sprachhinweis, Lösungsfinder, Animationen */
(function () {
  "use strict";
  var d = document, html = d.documentElement, LANG = html.lang;
  html.classList.add("js");

  // Lokal per Doppelklick geöffnet (file://): Ordner-Links auf index.html umbiegen
  if (location.protocol === "file:") {
    d.querySelectorAll("a[href]").forEach(function (a) {
      var h = a.getAttribute("href");
      if (/^(\.\.?\/)+$|\/$/.test(h) && !/^[a-z]+:/i.test(h)) a.setAttribute("href", h + "index.html");
    });
  }
  var Geo = window.HattatGeo;

  // ---- Mobile Menü ------------------------------------------------------
  var burger = d.getElementById("burger"), nav = d.getElementById("nav");
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") { nav.classList.remove("open"); burger.setAttribute("aria-expanded", "false"); }
    });
  }

  // ---- Manuelle Sprachwahl merken (hat Vorrang vor IP-Erkennung) --------
  d.querySelectorAll("a[data-lang]").forEach(function (a) {
    a.addEventListener("click", function () { if (Geo) Geo.pref(a.getAttribute("data-lang")); });
  });

  // ---- Sprachhinweis auf Unterseiten -----------------------------------
  // Beispiel: Besucher aus der Türkei landet über Google auf /de/ → dezente Leiste „Türkçe sayfaya geç“.
  var bar = d.getElementById("langbar"), barData = d.getElementById("langbar-data");
  if (Geo && bar && barData && !Geo.isBot && !Geo.pref() && html.getAttribute("data-root") !== "1") {
    var LB = JSON.parse(barData.textContent);
    Geo.detect(function (lang) {
      if (!lang || lang === LANG || !LB[lang]) return;
      d.getElementById("langbar-text").textContent = LB[lang].text;
      var go = d.getElementById("langbar-go");
      go.textContent = LB[lang].go + " →"; go.href = LB[lang].path; go.setAttribute("hreflang", lang); go.lang = lang;
      go.addEventListener("click", function () { Geo.pref(lang); });
      var x = d.getElementById("langbar-x");
      x.setAttribute("aria-label", LB[lang].close);
      x.addEventListener("click", function () { bar.hidden = true; Geo.pref(LANG); });
      bar.hidden = false;
    });
  }

  // ---- Lösungsfinder ------------------------------------------------------
  var form = d.getElementById("finder-form"), dataEl = d.getElementById("finder-data");
  if (form && dataEl) {
    var F = JSON.parse(dataEl.textContent);
    var CHECK = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>';
    var out = d.getElementById("finder-out"), empty = d.getElementById("finder-empty"), box = d.getElementById("finder-result");

    function val(n) { var el = form.querySelector('input[name="' + n + '"]:checked'); return el ? el.value : null; }
    function esc(s) { var t = d.createElement("span"); t.textContent = s; return t.innerHTML; }

    function pick(goal, budget) {
      var pkg = "business";
      if (goal === "start") pkg = "start";
      if (goal === "sell" || goal === "book" || goal === "intl") pkg = "custom";
      if (budget === "small") {
        if (pkg === "custom") pkg = "business";
        else if (pkg === "business" && goal === "leads") pkg = "start";
      }
      return pkg;
    }

    function update() {
      var ind = val("ind"), goal = val("goal"), budget = val("budget");
      if (!ind && !goal) { out.hidden = true; empty.hidden = false; return; }
      ind = ind || "other"; goal = goal || "leads";
      var pkg = pick(goal, budget);
      var items = [].concat(F.industries[ind][1], F.goals[goal][1], [F.always]);
      d.getElementById("finder-pkg").textContent = F.pkgs[pkg];
      d.getElementById("finder-list").innerHTML = items.map(function (t) { return "<li>" + CHECK + esc(t) + "</li>"; }).join("");
      var st = d.getElementById("finder-staged");
      st.hidden = budget !== "small"; st.textContent = F.staged;

      var lb = F.mail_labels;
      var body = F.mail_intro + "\n\n" +
        "- " + lb[0] + ": " + F.industries[ind][0] + "\n" +
        "- " + lb[1] + ": " + F.goals[goal][0] + "\n" +
        "- " + lb[2] + ": " + (budget ? F.budgets[budget] : "–") + "\n" +
        "- " + lb[3] + ": " + F.pkgs[pkg] + F.mail_outro;
      d.getElementById("finder-cta").href = "mailto:" + F.email +
        "?subject=" + encodeURIComponent(F.pkgs[pkg] + " – " + F.industries[ind][0]) +
        "&body=" + encodeURIComponent(body);

      empty.hidden = true; out.hidden = false;
      box.classList.remove("pop"); void box.offsetWidth; box.classList.add("pop");
    }
    form.addEventListener("change", update);
  }

  // ---- Hero-Mockups rotieren (zeigt: jede Lösung ist anders) -------------
  var mocks = [].slice.call(d.querySelectorAll(".hero-visual .mock"));
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  function place(off) { mocks.forEach(function (m, i) { m.className = m.className.replace(/\bpos\d\b/g, "").trim() + " pos" + ((i + off) % mocks.length); }); }
  if (mocks.length) {
    var off = 0; place(off);
    if (!reduce) setInterval(function () { if (!d.hidden) { off = (off + mocks.length - 1) % mocks.length; place(off); } }, 3200);
  }

  // ---- Einblenden beim Scrollen -----------------------------------------
  var rev = d.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -40px 0px" });
    rev.forEach(function (el) { io.observe(el); });
  } else rev.forEach(function (el) { el.classList.add("in"); });

  var y = d.getElementById("year"); if (y) y.textContent = new Date().getFullYear();
})();

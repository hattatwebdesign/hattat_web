/* Hatnova – Spracherkennung anhand der IP (Land) mit Fallbacks.
   Läuft inline im <head>, damit die Weiterleitung auf "/" ohne Flackern passiert.
   Reihenfolge:
   1. Manuell gewählte Sprache (localStorage "hatnova_lang") gewinnt immer.
   2. Land per IP: zuerst /cdn-cgi/trace (nur wenn Cloudflare vorgeschaltet ist – first-party,
      keine Daten an Dritte), sonst api.country.is.
   3. Fällt alles aus: Browsersprache, sonst Englisch.
   Suchmaschinen-Bots werden nie umgeleitet (Google crawlt aus den USA → sieht EN = x-default). */
(function (w, d) {
  var CFG = {
    tryCloudflare: false,          // auf true setzen, sobald Cloudflare vorgeschaltet ist (first-party, ohne Drittanbieter)
    geoApi: "https://api.country.is/",
    timeout: 1200,
    browserTurkishWins: true       // Türkischsprachige Browser (z. B. Diaspora in DE/CH/UK) → TR
  };
  var KEY = "hatnova_lang", CC = "hatnova_cc";
  var BOT = /bot|crawl|spider|slurp|lighthouse|pagespeed|bingpreview|facebookexternalhit|embedly|whatsapp|telegram|preview|headless/i;

  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function ss(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); } catch (e) { return null; } }
  function browserLang() { return ((navigator.languages && navigator.languages[0]) || navigator.language || "").toLowerCase(); }

  function langFor(country) {
    var b = browserLang();
    if (CFG.browserTurkishWins && b.indexOf("tr") === 0) return "tr";
    if (!country) return b.indexOf("tr") === 0 ? "tr" : b.indexOf("de") === 0 ? "de" : "en";
    if (country === "TR") return "tr";
    if (country === "CH") return /^(fr|it)/.test(b) ? "en" : "de"; // Romandie/Tessin → EN
    if (country === "DE" || country === "AT" || country === "LI") return "de";
    return "en"; // GB und Rest der Welt
  }

  function get(url, parse, cb) {
    var done = false, ctl = w.AbortController ? new AbortController() : null;
    var t = setTimeout(function () { if (!done) { done = true; if (ctl) ctl.abort(); cb(null); } }, CFG.timeout);
    if (!w.fetch) { clearTimeout(t); return cb(null); }
    fetch(url, { signal: ctl ? ctl.signal : undefined, credentials: "omit", cache: "no-store" })
      .then(function (r) { if (!r.ok) throw 0; return r.text(); })
      .then(function (txt) { if (done) return; done = true; clearTimeout(t); cb(parse(txt)); })
      .catch(function () { if (done) return; done = true; clearTimeout(t); cb(null); });
  }
  function valid(c) { return c && /^[A-Z]{2}$/.test(c) ? c : null; }

  function country(cb) {
    var cached = ss(CC);
    if (cached) return cb(cached === "-" ? null : cached);
    function api() {
      get(CFG.geoApi, function (t) { try { return valid(JSON.parse(t).country); } catch (e) { return null; } }, fin);
    }
    function fin(c) { ss(CC, c || "-"); cb(c); }
    if (CFG.tryCloudflare) {
      get("/cdn-cgi/trace", function (t) { var m = /(?:^|\n)loc=([A-Z]{2})/.exec(t); return m ? valid(m[1]) : null; },
        function (c) { c ? fin(c) : api(); });
    } else api();
  }

  // ?geotest in der URL schaltet die Bot-Erkennung zum Testen ab
  var isBot = !/[?&]geotest/.test(location.search) && (BOT.test(navigator.userAgent || "") || navigator.webdriver === true);

  w.HatnovaGeo = {
    isBot: isBot,
    pref: function (v) { return ls(KEY, v); },
    detect: function (cb) { country(function (c) { cb(langFor(c), c); }); },
    langFor: langFor
  };

  // Nur die Startseite "/" leitet automatisch weiter. Unterseiten (/de/, /tr/) bleiben,
  // wo sie sind – dort erscheint höchstens ein dezenter Sprachhinweis (app.js).
  var root = d.documentElement.getAttribute("data-root") === "1";
  if (!root || isBot) return;
  var q = /[?&]lang=(de|tr|en)\b/.exec(location.search);
  if (q) ls(KEY, q[1]);
  var p = ls(KEY);
  var idx = location.protocol === "file:" ? "index.html" : ""; // lokal geöffnet → Datei direkt ansteuern
  var PATHS = { de: "de/" + idx, tr: "tr/" + idx };
  if (p) { if (PATHS[p]) location.replace(PATHS[p] + location.hash); return; }

  d.documentElement.className += " geo-pending";
  function reveal() { d.documentElement.className = d.documentElement.className.replace(" geo-pending", ""); }
  var cap = setTimeout(reveal, 2000);
  w.HatnovaGeo.detect(function (lang) {
    clearTimeout(cap);
    if (PATHS[lang]) location.replace(PATHS[lang] + location.hash);
    else reveal();
  });
})(window, document);

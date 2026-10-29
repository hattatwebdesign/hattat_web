# hattat-web.de – überarbeitete Website

## Struktur
| Pfad | Inhalt |
|---|---|
| `/index.html` | Englisch (Fallback, `x-default`) + automatische Sprachweiterleitung |
| `/de/index.html` | Deutsch (Schweiz/Deutschland, ohne „ß“ – passt für CH) |
| `/tr/index.html` | Türkisch |
| `/impressum.html`, `/datenschutz.html` | Rechtsseiten (Deutsch) |
| `/assets/` | `style.css`, `app.js`, Logo-Varianten, Favicons, OG-Bild |
| `sitemap.xml`, `robots.txt`, `site.webmanifest`, `404.html`, `CNAME` | SEO & Hosting |
| `_build/` | Quelltexte: `content.py` (alle Texte), `template.html`, `geo.js`, `build.py` |

`_build/` wird von GitHub Pages nicht veröffentlicht (Ordner mit `_`).

## Texte ändern
1. Texte in `_build/content.py` bearbeiten (DE / TR / EN stehen untereinander).
2. `python3 _build/build.py` ausführen (benötigt `pip install jinja2`).
3. Alles committen und pushen.

## Sprache nach IP-Adresse
- Nur die Startseite `/` leitet automatisch weiter: **TR → /tr/**, **DE/AT/CH/LI → /de/**, **alle anderen (UK usw.) → Englisch**.
- Schweiz mit französischem/italienischem Browser → Englisch.
- Türkischsprachiger Browser (z. B. Diaspora in DE/CH/UK) → Türkisch. Abschaltbar in `_build/geo.js` (`browserTurkishWins: false`).
- Manuelle Sprachwahl wird gespeichert und hat immer Vorrang.
- `/de/` und `/tr/` leiten **nicht** um (wichtig für Google), zeigen aber ggf. einen dezenten Hinweis „Diese Seite gibt es auch auf …“.
- Suchmaschinen-Bots werden nie umgeleitet.
- Ländererkennung über `api.country.is`. **Empfehlung:** Cloudflare (kostenlos) vor GitHub Pages schalten und in `geo.js` `tryCloudflare: true` setzen – dann läuft die Erkennung ohne Drittanbieter.
- Testen: `?geotest` an die URL hängen (schaltet die Bot-Erkennung ab).

## SEO-Fokusbegriffe
**DE:** Webdesign KMU · Website erstellen lassen · Homepage für kleine Unternehmen · günstige/bezahlbare Website · Webdesign Schweiz · lokale SEO / bei Google gefunden werden · Online-Shop erstellen lassen · mehrsprachige Website Deutsch Türkisch

**TR:** web tasarım · KOBİ web sitesi · uygun fiyatlı web tasarım · kurumsal web sitesi · web sitesi fiyatları · e-ticaret sitesi · SEO hizmeti / Google'da üst sıralar · çok dilli web sitesi

**EN (UK):** affordable web design · small business website design · bespoke websites · local SEO for small businesses · e-commerce website · multilingual website design

Technik: eigene URL pro Sprache, `hreflang`, Canonical, Schema.org (ProfessionalService + FAQPage), Sitemap mit Sprachalternativen, Open Graph, keine externen Fonts, schnelle Ladezeit.

## Offene Punkte (bitte prüfen)
- **Impressum:** vollständiger Name + Strasse/PLZ fehlen (Pflichtangaben nach § 5 DDG) – siehe `TODO` in `impressum.html` und `datenschutz.html`.
- Leistungsversprechen prüfen: „klares Angebot vorab, keine versteckten Kosten“, „Google-Unternehmensprofil“, „WhatsApp-Button“.
- Projekte (İZ Mannheim, Kebapçızade): Links zu den Live-Seiten und echte Screenshots ergänzen, sobald verfügbar.
- Nach dem Livegang: Google Search Console einrichten und `sitemap.xml` einreichen; Google-Unternehmensprofil für Hatnova anlegen.

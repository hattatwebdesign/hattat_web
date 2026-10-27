#!/usr/bin/env python3
"""
Baut die statische Website (GitHub Pages) aus template.html + content.py.
Aufruf (im Projektordner):  python3 _build/build.py
Erzeugt:  /index.html (EN, x-default)  /de/index.html  /tr/index.html
          sitemap.xml  robots.txt  site.webmanifest  404.html
Ordner mit "_" am Anfang werden von GitHub Pages (Jekyll) nicht veröffentlicht.
"""
import base64, hashlib, json, os, sys, datetime
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import content as C  # noqa: E402

TODAY = datetime.date.today().isoformat()
VER = TODAY.replace("-", "")

ICONS = {
  "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
  "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
  "cart": '<circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/>',
  "languages": '<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>',
  "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/><path d="m9 16 2 2 4-4"/>',
  "bulb": '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6M10 22h4"/>',
  "user": '<circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/>',
  "coins": '<circle cx="8" cy="8" r="6"/><path d="M18.09 10.37A6 6 0 1 1 10.34 18"/><path d="M7 6h1v4"/><path d="m16.71 13.88.7.71-2.82 2.82"/>',
  "check": '<path d="M20 6 9 17l-5-5"/>',
  "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
  "instagram": '<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>',
  "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
  "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
  "chev": '<path d="m6 9 6 6 6-6"/>',
  "sparkles": '<path d="M12 3l1.9 5.8L20 10.7l-6.1 1.9L12 18.5l-1.9-5.9L4 10.7l6.1-1.9z"/><path d="M19 3v4M17 5h4"/>',
  "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
  "x": '<path d="M18 6 6 18M6 6l12 12"/>',
  "message": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
}

FLAGS = {
  "ch": '<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" fill="#D52B1E"/><path d="M13 6h6v7h7v6h-7v7h-6v-7H6v-6h7z" fill="#fff"/></svg>',
  "tr": '<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" fill="#E30A17"/><circle cx="13" cy="16" r="7.5" fill="#fff"/><circle cx="15" cy="16" r="6" fill="#E30A17"/><polygon fill="#fff" points="17.10,16.00 19.35,15.24 19.38,12.86 20.80,14.76 23.07,14.06 21.70,16.00 23.07,17.94 20.80,17.24 19.38,19.14 19.35,16.76"/></svg>',
  "gb": '<svg viewBox="0 0 60 60" aria-hidden="true"><defs><clipPath id="gbt"><path d="M30,30 h30 v30 z v30 h-30 z h-30 v-30 z v-30 h30 z"/></clipPath></defs><rect width="60" height="60" fill="#012169"/><path d="M0,0 L60,60 M60,0 L0,60" stroke="#fff" stroke-width="12"/><path d="M0,0 L60,60 M60,0 L0,60" clip-path="url(#gbt)" stroke="#C8102E" stroke-width="7"/><path d="M30,0 v60 M0,30 h60" stroke="#fff" stroke-width="18"/><path d="M30,0 v60 M0,30 h60" stroke="#C8102E" stroke-width="10"/></svg>',
}


def icon(name):
    return Markup('<svg class="i" viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % ICONS[name])


def flag(code):
    return Markup(FLAGS[code])


def sha(s):
    return "sha256-" + base64.b64encode(hashlib.sha256(s.encode("utf-8")).digest()).decode()


def jsonld(L):
    org_id = C.SITE + "/#org"
    data = {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "ProfessionalService", "@id": org_id,
          "name": "Hattat Webdesign & Consulting", "alternateName": "Hattat Web",
          "url": C.SITE + "/", "logo": C.SITE + "/assets/mark-512.png", "image": C.SITE + "/assets/og-image.jpg",
          "email": C.EMAIL, "description": L["desc"],
          "address": {"@type": "PostalAddress", "addressLocality": "Merchweiler", "addressRegion": "Saarland", "addressCountry": "DE"},
          "areaServed": [{"@type": "Country", "name": n} for n in ("Switzerland", "Türkiye", "United Kingdom", "Germany")],
          "knowsLanguage": ["de", "tr", "en"],
          "sameAs": [C.INSTAGRAM],
          "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["t"], "description": s["d"]}} for s in L["services"]["items"]],
        },
        {"@type": "WebSite", "@id": C.SITE + "/#website", "url": C.SITE + "/", "name": "Hattat Webdesign & Consulting",
         "inLanguage": ["en", "de", "tr"], "publisher": {"@id": org_id}},
        {"@type": "WebPage", "url": C.SITE + L["path"], "name": L["title"], "inLanguage": L["code"],
         "isPartOf": {"@id": C.SITE + "/#website"}, "about": {"@id": org_id}},
        {"@type": "FAQPage", "inLanguage": L["code"],
         "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in L["faq"]["items"]]},
      ],
    }
    return Markup(json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))


def main():
    env = Environment(loader=FileSystemLoader(HERE), autoescape=True, trim_blocks=True, lstrip_blocks=True)
    tpl = env.get_template("template.html")
    geo_js = open(os.path.join(HERE, "geo.js"), encoding="utf-8").read()
    crit_css = "html.geo-pending body{visibility:hidden;animation:geo-reveal 0s 2.2s forwards}@keyframes geo-reveal{to{visibility:visible}}"

    ordered = [C.DE, C.TR, C.EN]

    for L in C.LANGS:
        F = dict(C.FINDER[L["code"]]); F["email"] = C.EMAIL
        # relative Pfade: funktionieren auf der Domain, in Unterordnern und lokal (Doppelklick)
        B = "" if L["path"] == "/" else "../"
        def rel(x, B=B):
            target = x["path"].strip("/")
            r = B + (target + "/" if target else "")
            return r or "./"
        langbar = {x["code"]: dict(x["langbar"], path=rel(x)) for x in C.LANGS}
        html = tpl.render(
            L=L, LANGS=C.LANGS, LANGS_ORDERED=ordered, SITE=C.SITE, EMAIL=C.EMAIL, INSTAGRAM=C.INSTAGRAM,
            F=F, B=B, rel=rel, icon=icon, flag=flag, ver=VER, year=datetime.date.today().year,
            geo_js=Markup(geo_js), geo_hash=sha(geo_js), critical_css=Markup(crit_css), crit_hash=sha(crit_css),
            jsonld=jsonld(L),
            finder_json=Markup(json.dumps(F, ensure_ascii=False).replace("</", "<\\/")),
            langbar_json=Markup(json.dumps(langbar, ensure_ascii=False).replace("</", "<\\/")),
        )
        out_dir = ROOT if L["path"] == "/" else os.path.join(ROOT, L["path"].strip("/"))
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(html)
        print("✓", os.path.relpath(os.path.join(out_dir, "index.html"), ROOT))

    # sitemap mit hreflang-Alternativen
    alts = "".join('\n    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>' % (x["code"], C.SITE, x["path"]) for x in C.LANGS)
    alts += '\n    <xhtml:link rel="alternate" hreflang="x-default" href="%s/"/>' % C.SITE
    urls = "".join("\n  <url>\n    <loc>%s%s</loc>\n    <lastmod>%s</lastmod>%s\n  </url>" % (C.SITE, x["path"], TODAY, alts) for x in C.LANGS)
    for p in ("impressum.html", "datenschutz.html"):
        urls += "\n  <url>\n    <loc>%s/%s</loc>\n    <lastmod>%s</lastmod>\n  </url>" % (C.SITE, p, TODAY)
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
               'xmlns:xhtml="http://www.w3.org/1999/xhtml">%s\n</urlset>\n' % urls)
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sitemap)

    open(os.path.join(ROOT, "robots.txt"), "w").write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % C.SITE)

    manifest = {"name": "Hattat Webdesign & Consulting", "short_name": "Hattat", "start_url": "/", "display": "browser",
                "background_color": "#FBF8F3", "theme_color": "#FBF8F3",
                "icons": [{"src": "/assets/mark-192.png", "sizes": "192x192", "type": "image/png"},
                          {"src": "/assets/mark-512.png", "sizes": "512x512", "type": "image/png"}]}
    open(os.path.join(ROOT, "site.webmanifest"), "w").write(json.dumps(manifest, indent=2))
    print("✓ sitemap.xml, robots.txt, site.webmanifest")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Inhalte der Startseite in drei Sprachen.
Hinweis zum deutschen Text: bewusst ohne „ß“ formuliert, damit er auch für
Schweizer Leser natürlich wirkt (CH-Schreibweise kennt kein ß).
SEO-Fokusbegriffe stehen jeweils im Kommentar über der Sprache.
"""

SITE = "https://hattat-web.de"
EMAIL = "info@hattat-web.de"
INSTAGRAM = "https://www.instagram.com/hattat_web/"

# ---------------------------------------------------------------------------
# DEUTSCH  – Märkte: Schweiz (KMU), Deutschland, türkischstämmige Betriebe in DACH
# Fokus: „Webdesign KMU“, „Website erstellen lassen“, „günstige Website / bezahlbar“,
#        „Homepage für kleine Unternehmen“, „Webdesign Schweiz“, „lokale SEO“,
#        „Online-Shop erstellen lassen“, „mehrsprachige Website Deutsch Türkisch“
# ---------------------------------------------------------------------------
DE = {
  "code": "de", "path": "/de/", "og_locale": "de_DE", "name": "Deutsch", "short": "DE",
  "title": "Webdesign für KMU – individuell & bezahlbar | Hattat Web",
  "desc": "Website erstellen lassen ohne Agenturpreise: Webdesign, SEO und Online-Shops für KMU in der Schweiz, Deutschland und der Türkei. Erstberatung gratis.",
  "nav": {"services": "Leistungen", "process": "Ablauf", "packages": "Pakete", "faq": "FAQ", "contact": "Kontakt", "cta": "Gratis beraten lassen"},
  "skip": "Zum Inhalt springen",
  "hero": {
    "eyebrow": "Webdesign für kleine & mittlere Unternehmen",
    "h1": "Websites für KMU – <mark>individuell</mark> und bezahlbar",
    "lead": "Webdesign, SEO und Online-Shops für kleine und mittlere Unternehmen in der Schweiz, der Türkei und Grossbritannien. Kein Baukasten, keine Agenturpreise – sondern eine Lösung, die zu Ihrem Betrieb und Ihrem Budget passt.",
    "cta1": "Kostenloses Erstgespräch", "cta2": "Passende Lösung finden",
    "checks": ["Erstberatung kostenlos", "Klares Angebot vorab, keine versteckten Kosten", "Deutsch · Türkçe · English"],
    "mock_label": "Beispiele: drei Betriebe, drei individuelle Websites",
  },
  "markets": {
    "title": "Für KMU in drei Ländern – persönlich betreut aus Deutschland und der Schweiz",
    "items": [
      {"code": "ch", "name": "Schweiz", "text": "Saubere, schnelle Websites für Schweizer KMU – auf Deutsch, Englisch oder mehrsprachig."},
      {"code": "tr", "name": "Türkei", "text": "Moderne Firmenwebsites und Shops für türkische Betriebe – auch für den Export nach Europa."},
      {"code": "gb", "name": "Grossbritannien", "text": "Englischsprachige Websites mit lokaler SEO für Betriebe in UK – auf Wunsch auch auf Türkisch."},
    ],
  },
  "process": {
    "tag": "So arbeiten wir", "title": "Kein Paket von der Stange – Ihre Lösung entsteht im Gespräch",
    "lead": "Jeder Betrieb ist anders. Darum fragen wir zuerst, was Sie brauchen, und bauen dann genau das – nicht mehr und nicht weniger.",
    "steps": [
      {"t": "Zuhören", "d": "Im kostenlosen Erstgespräch klären wir Ziele, Kundschaft, Budget und Zeitplan. Auf Deutsch, Türkisch oder Englisch."},
      {"t": "Vorschlag & Angebot", "d": "Sie erhalten einen konkreten Vorschlag mit klarem Preis. Wenn das Budget knapp ist, planen wir in Etappen."},
      {"t": "Umsetzen & begleiten", "d": "Wir gestalten, schreiben suchmaschinenfreundliche Texte und gehen live. Danach bleiben wir Ihr direkter Ansprechpartner."},
    ],
  },
  "services": {
    "tag": "Leistungen", "title": "Alles, was ein KMU online braucht",
    "lead": "Von der ersten Website bis zum Online-Shop – Sie wählen nur die Bausteine, die Ihrem Geschäft wirklich helfen.",
    "items": [
      {"icon": "globe", "t": "Website erstellen lassen", "d": "Moderne, mobile Firmenwebsite oder Onepager – individuell gestaltet statt aus dem Baukasten."},
      {"icon": "search", "t": "SEO & lokale Sichtbarkeit", "d": "Besser bei Google gefunden werden: Keywords, Google-Unternehmensprofil, lokale Suche in Ihrer Region."},
      {"icon": "cart", "t": "Online-Shop", "d": "Produkte online verkaufen – übersichtlich, sicher und so aufgebaut, dass Sie ihn selbst pflegen können."},
      {"icon": "languages", "t": "Mehrsprachige Websites", "d": "Deutsch, Türkisch, Englisch – ideal für Betriebe mit internationaler oder mehrsprachiger Kundschaft."},
      {"icon": "calendar", "t": "Buchung & Web-Apps", "d": "Online-Termine, Reservierungen, Anfrageformulare oder kleine Tools, die Ihnen Arbeit abnehmen."},
      {"icon": "bulb", "t": "Digitalberatung", "d": "Ehrliche Einschätzung: Was lohnt sich für Ihr Geschäft, was nicht? Klar und ohne Fachchinesisch."},
    ],
  },
  "finder": {
    "tag": "Lösungsfinder", "title": "In 30 Sekunden zu Ihrer individuellen Lösung",
    "lead": "Drei kurze Fragen – und Sie sehen sofort, womit Sie sinnvoll starten. Unverbindlich.",
    "q1": "Ihre Branche", "q2": "Ihr wichtigstes Ziel", "q3": "Ihr Budget",
    "result_title": "Unser Vorschlag für Sie",
    "result_cta": "Anfrage mit diesen Angaben senden",
    "result_note": "Das ist ein erster Vorschlag. Im Gespräch passen wir alles an Ihren Betrieb an.",
    "placeholder": "Beantworten Sie die drei Fragen – Ihr Vorschlag erscheint hier.",
  },
  "industries": {
    "tag": "Branchen", "title": "Für jede Branche die passende Website",
    "lead": "Ob Handwerksbetrieb, Arztpraxis oder Restaurant – wir kennen die typischen Fragen Ihrer Kundschaft und bauen die Website darum herum.",
    "list": ["Restaurants & Cafés", "Handwerk & Bau", "Arztpraxen & Therapie", "Hotels & Ferienwohnungen", "Einzelhandel & Shops", "Friseure & Kosmetik", "Kanzleien & Beratung", "Autowerkstätten", "Immobilien", "Reinigung & Service", "Logistik & Transport", "Vereine & Startups"],
    "more": "Ihre Branche fehlt? Kein Problem – jede Lösung entsteht individuell.",
  },
  "packages": {
    "tag": "Pakete & Preise", "title": "Faire Preise – so viel wie nötig, so wenig wie möglich",
    "lead": "Die Pakete sind nur Startpunkte. Wir passen jedes Angebot an Ihren Bedarf und Ihr Budget an.",
    "price": "Preis nach Umfang – klares Angebot nach dem Gratis-Gespräch",
    "badge": "Beliebt",
    "items": [
      {"name": "Start", "for": "Für Gründer und kleine Betriebe, die schnell online sein wollen.", "features": ["Onepager, mobil optimiert", "Kontakt-, Anruf- & WhatsApp-Button", "Google-Unternehmensprofil", "Basis-SEO & schnelle Ladezeit"]},
      {"name": "Business", "for": "Für KMU, die bei Google neue Kundschaft gewinnen wollen.", "features": ["Mehrseitige Firmenwebsite", "Texte mit gezielten Suchbegriffen", "Lokale SEO für Ihre Region", "Auf Wunsch mehrsprachig"]},
      {"name": "Individuell", "for": "Für Betriebe mit besonderen Abläufen oder Online-Verkauf.", "features": ["Online-Shop oder Buchungssystem", "Web-App & Schnittstellen", "Mehrere Sprachen & Märkte", "Ausbau Schritt für Schritt"]},
    ],
    "cta": "Angebot anfragen",
  },
  "why": {
    "tag": "Warum Hattat", "title": "Persönlich, verständlich und fair",
    "items": [
      {"icon": "user", "t": "Ein fester Ansprechpartner", "d": "Kein Callcenter, kein Ticket-System. Sie sprechen immer direkt mit der Person, die Ihre Website baut."},
      {"icon": "languages", "t": "Wir sprechen Ihre Sprache", "d": "Beratung auf Deutsch, Türkisch und Englisch – und Websites, die Ihre Kundschaft in ihrer Sprache abholen."},
      {"icon": "search", "t": "Von Anfang an für Google gebaut", "d": "Saubere Technik, schnelle Ladezeiten und Texte, die Ihre Kunden tatsächlich suchen."},
      {"icon": "coins", "t": "Bezahlbar für kleine Budgets", "d": "Klein anfangen, später ausbauen. Sie zahlen nur für das, was Ihr Geschäft wirklich weiterbringt."},
    ],
  },
  "projects": {
    "tag": "Projekte", "title": "Aus der Praxis",
    "items": [
      {"t": "İZ – Uigurisches Restaurant, Mannheim", "d": "Restaurant-Website plus eigene Erlebnisseite, die Kultur und Küche spielerisch vorstellt.", "tags": ["Gastronomie", "Deutschland"]},
      {"t": "Kebapçızade, Çorum", "d": "Verspielte Restaurant-Website mit Spielelementen, die Gäste neugierig macht und im Gedächtnis bleibt.", "tags": ["Gastronomie", "Türkei"]},
    ],
  },
  "faq": {
    "tag": "FAQ", "title": "Häufige Fragen", "more": "Ihre Frage ist nicht dabei? Schreiben Sie uns einfach.",
    "items": [
      {"q": "Was kostet eine Website für ein kleines Unternehmen?", "a": "Das hängt vom Umfang ab: Ein Onepager kostet deutlich weniger als ein Online-Shop. Nach dem kostenlosen Erstgespräch erhalten Sie ein klares, schriftliches Angebot – ohne versteckte Kosten. Bei kleinem Budget starten wir mit dem Wichtigsten und bauen später aus."},
      {"q": "Wie lange dauert es, bis meine Website online ist?", "a": "Ein Onepager ist oft in wenigen Wochen fertig, grössere Websites oder Shops brauchen entsprechend länger. Den genauen Zeitplan legen wir gemeinsam fest."},
      {"q": "Arbeiten Sie auch für Firmen in der Schweiz, der Türkei und in Grossbritannien?", "a": "Ja. Wir betreuen KMU in der Schweiz, der Türkei, Grossbritannien und Deutschland. Besprechungen finden per Video, Telefon oder E-Mail statt – auf Deutsch, Türkisch oder Englisch."},
      {"q": "Wird meine Website bei Google gefunden?", "a": "Jede Website wird technisch sauber und suchmaschinenfreundlich gebaut. Dazu wählen wir Suchbegriffe, die Ihre Kundschaft wirklich verwendet, und richten auf Wunsch Ihr Google-Unternehmensprofil für die lokale Suche ein."},
      {"q": "Kann ich die Website später selbst bearbeiten?", "a": "Ja, wenn Sie möchten. Wir richten die Website so ein, dass Sie Texte, Bilder oder Angebote selbst ändern können – oder wir übernehmen die Pflege für Sie."},
      {"q": "Kann meine Website mehrsprachig sein?", "a": "Ja. Wir bauen Websites auf Deutsch, Türkisch und Englisch – auch in Kombination und so, dass jede Sprache bei Google einzeln gefunden wird."},
    ],
  },
  "contact": {
    "tag": "Kontakt", "title": "Erzählen Sie uns von Ihrem Projekt",
    "lead": "Schreiben Sie uns kurz, worum es geht. Sie erhalten eine persönliche Antwort und Ihre erste Beratung ist kostenlos und unverbindlich.",
    "email": "E-Mail", "insta": "Instagram", "loc_label": "Standorte", "loc": "Deutschland (Saarland) & Schweiz",
    "langs_label": "Sprachen", "langs": "Deutsch · Türkçe · English",
    "cta": "E-Mail schreiben", "subject": "Anfrage Website – kostenloses Erstgespräch",
    "box_title": "Erstberatung gratis", "box_text": "Wir schauen uns Ihren aktuellen Auftritt an und zeigen, was sich für Ihr Geschäft lohnt – ohne Verpflichtung.",
  },
  "footer": {"tagline": "Webdesign & Consulting für KMU", "imprint": "Impressum", "privacy": "Datenschutz", "rights": "Alle Rechte vorbehalten."},
  "langbar": {"text": "Diese Seite gibt es auch auf Deutsch.", "go": "Zur deutschen Seite", "close": "Schliessen"},
}

# ---------------------------------------------------------------------------
# TÜRKÇE – Pazarlar: Türkiye, Almanya/İsviçre/İngiltere'deki Türk işletmeleri
# Odak: „web tasarım“, „KOBİ web sitesi“, „uygun fiyatlı web tasarım“,
#       „kurumsal web sitesi yaptırmak“, „web sitesi fiyatları“, „e-ticaret sitesi“,
#       „SEO hizmeti / Google'da üst sıralar“, „çok dilli web sitesi“
# ---------------------------------------------------------------------------
TR = {
  "code": "tr", "path": "/tr/", "og_locale": "tr_TR", "name": "Türkçe", "short": "TR",
  "title": "Uygun Fiyatlı Web Tasarım – KOBİ'lere Özel | Hattat Web",
  "desc": "KOBİ'ler için kurumsal web sitesi, e-ticaret ve SEO. Hazır şablon yok – işletmenize ve bütçenize özel çözümler. Ücretsiz ön görüşme.",
  "nav": {"services": "Hizmetler", "process": "Süreç", "packages": "Paketler", "faq": "SSS", "contact": "İletişim", "cta": "Ücretsiz danışın"},
  "skip": "İçeriğe geç",
  "hero": {
    "eyebrow": "Küçük ve orta ölçekli işletmeler için web tasarım",
    "h1": "KOBİ'ler için web siteleri – <mark>size özel</mark>, bütçenize uygun",
    "lead": "Türkiye, İsviçre ve İngiltere'deki KOBİ'ler için web tasarım, SEO ve e-ticaret. Hazır şablon yok, ajans fiyatları yok – işletmenize ve bütçenize uygun bir çözüm var.",
    "cta1": "Ücretsiz ön görüşme", "cta2": "Size uygun çözümü bulun",
    "checks": ["İlk danışmanlık ücretsiz", "Net teklif, gizli maliyet yok", "Türkçe · Deutsch · English"],
    "mock_label": "Örnekler: üç işletme, üç farklı web sitesi",
  },
  "markets": {
    "title": "Üç ülkede KOBİ'lere hizmet – Almanya ve İsviçre'den birebir destek",
    "items": [
      {"code": "tr", "name": "Türkiye", "text": "Türk işletmeleri için modern kurumsal siteler ve e-ticaret – Avrupa'ya ihracat için çok dilli."},
      {"code": "ch", "name": "İsviçre", "text": "İsviçre'deki işletmeler için hızlı ve şık web siteleri – Almanca, İngilizce veya Türkçe."},
      {"code": "gb", "name": "Birleşik Krallık", "text": "İngiltere'deki işletmeler için yerel SEO'lu İngilizce siteler – istenirse Türkçe versiyonuyla."},
    ],
  },
  "process": {
    "tag": "Nasıl çalışıyoruz", "title": "Hazır paket yok – çözümünüz sizinle birlikte şekillenir",
    "lead": "Her işletme farklıdır. Önce neye ihtiyacınız olduğunu dinliyor, sonra tam olarak onu yapıyoruz – fazlasını da eksiğini de değil.",
    "steps": [
      {"t": "Dinliyoruz", "d": "Ücretsiz ön görüşmede hedeflerinizi, müşterilerinizi, bütçenizi ve zaman planınızı konuşuyoruz. Türkçe, Almanca veya İngilizce."},
      {"t": "Öneri ve teklif", "d": "Net fiyatlı, somut bir öneri alırsınız. Bütçe kısıtlıysa projeyi aşama aşama planlıyoruz."},
      {"t": "Uygulama ve destek", "d": "Tasarlıyor, Google dostu metinler yazıyor ve yayına alıyoruz. Sonrasında da doğrudan muhatabınız olmaya devam ediyoruz."},
    ],
  },
  "services": {
    "tag": "Hizmetler", "title": "Bir KOBİ'nin internette ihtiyaç duyduğu her şey",
    "lead": "İlk web sitenizden online mağazanıza kadar – yalnızca işinize gerçekten yarayan parçaları seçersiniz.",
    "items": [
      {"icon": "globe", "t": "Kurumsal web sitesi", "d": "Modern, mobil uyumlu kurumsal site veya tek sayfalık tanıtım sitesi – hazır şablon değil, size özel tasarım."},
      {"icon": "search", "t": "SEO ve yerel görünürlük", "d": "Google'da üst sıralarda bulunun: anahtar kelimeler, Google İşletme Profili ve bölgenizde yerel arama."},
      {"icon": "cart", "t": "E-ticaret sitesi", "d": "Ürünlerinizi online satın – sade, güvenli ve kendiniz kolayca yönetebileceğiniz şekilde."},
      {"icon": "languages", "t": "Çok dilli web siteleri", "d": "Türkçe, Almanca, İngilizce – yurt dışı müşterisi olan veya ihracat yapan işletmeler için ideal."},
      {"icon": "calendar", "t": "Rezervasyon ve web uygulamaları", "d": "Online randevu, rezervasyon, teklif formları veya işinizi kolaylaştıran küçük araçlar."},
      {"icon": "bulb", "t": "Dijital danışmanlık", "d": "Dürüst değerlendirme: İşletmeniz için ne işe yarar, ne yaramaz? Açık ve anlaşılır bir dille."},
    ],
  },
  "finder": {
    "tag": "Çözüm bulucu", "title": "30 saniyede size özel çözüm",
    "lead": "Üç kısa soru – nereden başlamanın mantıklı olduğunu hemen görün. Taahhütsüz.",
    "q1": "Sektörünüz", "q2": "En önemli hedefiniz", "q3": "Bütçeniz",
    "result_title": "Size önerimiz",
    "result_cta": "Bu bilgilerle teklif isteyin",
    "result_note": "Bu ilk bir öneridir. Görüşmede her şeyi işletmenize göre uyarlıyoruz.",
    "placeholder": "Üç soruyu yanıtlayın – öneriniz burada görünecek.",
  },
  "industries": {
    "tag": "Sektörler", "title": "Her sektöre uygun web sitesi",
    "lead": "İster usta, ister muayenehane, ister restoran – müşterilerinizin tipik sorularını biliyor ve web sitesini bunların etrafında kuruyoruz.",
    "list": ["Restoran ve kafeler", "İnşaat ve zanaat", "Doktor ve klinikler", "Otel ve pansiyonlar", "Perakende ve mağazalar", "Kuaför ve güzellik", "Hukuk ve danışmanlık", "Oto servisler", "Emlak", "Temizlik ve hizmet", "Lojistik ve nakliye", "Dernek ve girişimler"],
    "more": "Sektörünüz listede yok mu? Sorun değil – her çözüm size özel hazırlanır.",
  },
  "packages": {
    "tag": "Paketler ve fiyatlar", "title": "Adil fiyatlar – gerektiği kadar, mümkün olduğunca az",
    "lead": "Paketler yalnızca bir başlangıç noktası. Her teklifi ihtiyacınıza ve bütçenize göre uyarlıyoruz.",
    "price": "Fiyat kapsama göre – ücretsiz görüşmeden sonra net teklif",
    "badge": "Popüler",
    "items": [
      {"name": "Başlangıç", "for": "Hızlıca internette yer almak isteyen yeni ve küçük işletmeler için.", "features": ["Tek sayfa, mobil uyumlu", "İletişim, arama ve WhatsApp butonu", "Google İşletme Profili", "Temel SEO ve hızlı açılış"]},
      {"name": "Kurumsal", "for": "Google'dan yeni müşteri kazanmak isteyen KOBİ'ler için.", "features": ["Çok sayfalı kurumsal site", "Hedefli anahtar kelimelerle metinler", "Bölgenize yönelik yerel SEO", "İsteğe bağlı çok dilli"]},
      {"name": "Size Özel", "for": "Özel iş süreçleri olan veya online satış yapan işletmeler için.", "features": ["E-ticaret veya rezervasyon sistemi", "Web uygulaması ve entegrasyonlar", "Birden fazla dil ve pazar", "Adım adım büyütme"]},
    ],
    "cta": "Teklif isteyin",
  },
  "why": {
    "tag": "Neden Hattat", "title": "Samimi, anlaşılır ve adil",
    "items": [
      {"icon": "user", "t": "Tek ve sabit muhatap", "d": "Çağrı merkezi yok, bilet sistemi yok. Her zaman sitenizi yapan kişiyle doğrudan konuşursunuz."},
      {"icon": "languages", "t": "Sizin dilinizi konuşuyoruz", "d": "Türkçe, Almanca ve İngilizce danışmanlık – ve müşterilerinize kendi dillerinde ulaşan web siteleri."},
      {"icon": "search", "t": "Baştan Google için tasarlanır", "d": "Temiz altyapı, hızlı açılış ve müşterilerinizin gerçekten aradığı kelimelerle yazılmış metinler."},
      {"icon": "coins", "t": "Küçük bütçelere uygun", "d": "Küçük başlayın, sonra büyütün. Yalnızca işinizi gerçekten ileri taşıyan şeye ödeme yaparsınız."},
    ],
  },
  "projects": {
    "tag": "Projeler", "title": "Uygulamadan örnekler",
    "items": [
      {"t": "İZ – Uygur Restoranı, Mannheim", "d": "Restoran web sitesi ve Uygur kültürünü ile mutfağını oyunlarla tanıtan ayrı bir deneyim sayfası.", "tags": ["Gastronomi", "Almanya"]},
      {"t": "Kebapçızade, Çorum", "d": "Misafirlerin merakını uyandıran, oyun öğeleriyle akılda kalan eğlenceli bir restoran sitesi.", "tags": ["Gastronomi", "Türkiye"]},
    ],
  },
  "faq": {
    "tag": "SSS", "title": "Sık sorulan sorular", "more": "Sorunuz burada yok mu? Bize yazmanız yeterli.",
    "items": [
      {"q": "Küçük bir işletme için web sitesi fiyatları ne kadar?", "a": "Kapsama göre değişir: Tek sayfalık bir site, bir e-ticaret sitesinden çok daha uygundur. Ücretsiz ön görüşmenin ardından gizli maliyet içermeyen, net ve yazılı bir teklif alırsınız. Bütçe kısıtlıysa en önemli kısımla başlar, sonra büyütürüz."},
      {"q": "Web sitem ne kadar sürede yayına girer?", "a": "Tek sayfalık bir site çoğu zaman birkaç hafta içinde hazır olur; daha büyük siteler veya mağazalar buna göre daha uzun sürer. Kesin zaman planını birlikte belirliyoruz."},
      {"q": "Türkiye, İsviçre ve İngiltere'deki firmalarla da çalışıyor musunuz?", "a": "Evet. Türkiye, İsviçre, İngiltere ve Almanya'daki KOBİ'lerle çalışıyoruz. Görüşmeler görüntülü, telefonla veya e-posta ile – Türkçe, Almanca ya da İngilizce yapılır."},
      {"q": "Web sitem Google'da çıkacak mı?", "a": "Her site teknik olarak temiz ve arama motoru dostu kurulur. Müşterilerinizin gerçekten kullandığı anahtar kelimeleri seçer, istenirse yerel arama için Google İşletme Profilinizi de oluştururuz."},
      {"q": "Web sitemi sonradan kendim düzenleyebilir miyim?", "a": "Evet, isterseniz. Siteyi metinleri, görselleri veya teklifleri kendiniz değiştirebileceğiniz şekilde kuruyoruz – ya da bakımını biz üstleniyoruz."},
      {"q": "Web sitem birden fazla dilde olabilir mi?", "a": "Evet. Türkçe, Almanca ve İngilizce siteler hazırlıyoruz – birlikte de olabilir; her dil Google'da ayrı ayrı bulunacak şekilde."},
    ],
  },
  "contact": {
    "tag": "İletişim", "title": "Projenizi bize anlatın",
    "lead": "Kısaca ne istediğinizi yazın. Size kişisel olarak dönüş yapıyoruz ve ilk danışmanlık ücretsiz ve taahhütsüzdür.",
    "email": "E-posta", "insta": "Instagram", "loc_label": "Lokasyonlar", "loc": "Almanya (Saarland) ve İsviçre",
    "langs_label": "Diller", "langs": "Türkçe · Deutsch · English",
    "cta": "E-posta gönderin", "subject": "Web sitesi talebi – ücretsiz ön görüşme",
    "box_title": "İlk danışmanlık ücretsiz", "box_text": "Mevcut dijital varlığınızı inceliyor ve işletmeniz için neyin işe yarayacağını gösteriyoruz – hiçbir yükümlülük olmadan.",
  },
  "footer": {"tagline": "KOBİ'ler için web tasarım ve danışmanlık", "imprint": "Künye", "privacy": "Gizlilik", "rights": "Tüm hakları saklıdır."},
  "langbar": {"text": "Bu sayfa Türkçe olarak da mevcut.", "go": "Türkçe sayfaya geç", "close": "Kapat"},
}

# ---------------------------------------------------------------------------
# ENGLISH (UK) – Fallback & UK market. British spelling (optimise, bespoke).
# Focus: "affordable web design", "small business website design (UK)",
#        "bespoke websites", "local SEO for small businesses", "e-commerce website",
#        "multilingual website design", "Turkish-speaking web designer UK"
# ---------------------------------------------------------------------------
EN = {
  "code": "en", "path": "/", "og_locale": "en_GB", "name": "English", "short": "EN",
  "title": "Affordable Web Design for Small Businesses | Hattat Web",
  "desc": "Bespoke websites, local SEO and online shops for small businesses in the UK, Switzerland and Türkiye. Free consultation, fair prices, no templates.",
  "nav": {"services": "Services", "process": "Process", "packages": "Packages", "faq": "FAQ", "contact": "Contact", "cta": "Free consultation"},
  "skip": "Skip to content",
  "hero": {
    "eyebrow": "Web design for small & medium-sized businesses",
    "h1": "Websites for small businesses – <mark>bespoke</mark> and affordable",
    "lead": "Web design, SEO and online shops for SMEs in the UK, Switzerland and Türkiye. No website builders, no agency prices – just a solution that fits your business and your budget.",
    "cta1": "Free consultation", "cta2": "Find your solution",
    "checks": ["Free first consultation", "Clear quote upfront, no hidden costs", "English · Türkçe · Deutsch"],
    "mock_label": "Examples: three businesses, three bespoke websites",
  },
  "markets": {
    "title": "Serving SMEs in three countries – personal support from Germany and Switzerland",
    "items": [
      {"code": "gb", "name": "United Kingdom", "text": "English websites with local SEO for UK businesses – with a Turkish version if your customers need it."},
      {"code": "ch", "name": "Switzerland", "text": "Clean, fast websites for Swiss SMEs – in English, German or several languages."},
      {"code": "tr", "name": "Türkiye", "text": "Modern company websites and shops for Turkish businesses – ready for export to Europe."},
    ],
  },
  "process": {
    "tag": "How we work", "title": "No off-the-shelf packages – your solution starts with a conversation",
    "lead": "Every business is different. So we ask what you need first, then build exactly that – nothing more, nothing less.",
    "steps": [
      {"t": "Listen", "d": "In a free first call we talk through your goals, customers, budget and timeline – in English, Turkish or German."},
      {"t": "Proposal & quote", "d": "You get a concrete proposal with a clear price. If budget is tight, we plan the project in stages."},
      {"t": "Build & support", "d": "We design, write search-friendly copy and go live. Afterwards we stay your direct point of contact."},
    ],
  },
  "services": {
    "tag": "Services", "title": "Everything a small business needs online",
    "lead": "From your first website to a full online shop – you only pick the pieces that genuinely help your business.",
    "items": [
      {"icon": "globe", "t": "Small business websites", "d": "Modern, mobile-friendly company websites or one-pagers – designed for you, not built from a template."},
      {"icon": "search", "t": "SEO & local visibility", "d": "Get found on Google: keyword research, Google Business Profile and local search in your area."},
      {"icon": "cart", "t": "E-commerce websites", "d": "Sell online with a clear, secure shop that you can easily manage yourself."},
      {"icon": "languages", "t": "Multilingual websites", "d": "English, Turkish, German – ideal for businesses with international or multilingual customers."},
      {"icon": "calendar", "t": "Booking & web apps", "d": "Online appointments, reservations, enquiry forms or small tools that save you time."},
      {"icon": "bulb", "t": "Digital consulting", "d": "Honest advice on what is worth it for your business and what is not – in plain English."},
    ],
  },
  "finder": {
    "tag": "Solution finder", "title": "Your bespoke solution in 30 seconds",
    "lead": "Three quick questions and you will see where it makes sense to start. No obligation.",
    "q1": "Your industry", "q2": "Your main goal", "q3": "Your budget",
    "result_title": "Our suggestion for you",
    "result_cta": "Send an enquiry with these details",
    "result_note": "This is a first suggestion. We tailor everything to your business when we talk.",
    "placeholder": "Answer the three questions – your suggestion will appear here.",
  },
  "industries": {
    "tag": "Industries", "title": "The right website for every industry",
    "lead": "Tradesperson, clinic or restaurant – we know what your customers typically ask and build your website around it.",
    "list": ["Restaurants & cafés", "Trades & construction", "Clinics & therapists", "Hotels & holiday lets", "Retail & shops", "Hair & beauty", "Law firms & consultants", "Garages & car services", "Estate agents", "Cleaning & services", "Logistics & transport", "Charities & start-ups"],
    "more": "Industry not listed? No problem – every solution is built individually.",
  },
  "packages": {
    "tag": "Packages & pricing", "title": "Fair prices – as much as you need, as little as possible",
    "lead": "Packages are just starting points. We tailor every quote to your needs and your budget.",
    "price": "Priced by scope – clear quote after a free call",
    "badge": "Popular",
    "items": [
      {"name": "Starter", "for": "For start-ups and small businesses that want to get online quickly.", "features": ["One-page website, mobile-ready", "Contact, call & WhatsApp buttons", "Google Business Profile", "Basic SEO & fast loading"]},
      {"name": "Business", "for": "For SMEs that want to win new customers through Google.", "features": ["Multi-page company website", "Copy written around target keywords", "Local SEO for your area", "Multilingual on request"]},
      {"name": "Bespoke", "for": "For businesses with special processes or online sales.", "features": ["Online shop or booking system", "Web app & integrations", "Several languages & markets", "Grow step by step"]},
    ],
    "cta": "Request a quote",
  },
  "why": {
    "tag": "Why Hattat", "title": "Personal, clear and fair",
    "items": [
      {"icon": "user", "t": "One dedicated contact", "d": "No call centre, no ticket system. You always talk directly to the person building your website."},
      {"icon": "languages", "t": "We speak your language", "d": "Advice in English, Turkish and German – and websites that reach your customers in their language."},
      {"icon": "search", "t": "Built for Google from day one", "d": "Clean code, fast loading and copy based on what your customers actually search for."},
      {"icon": "coins", "t": "Affordable for small budgets", "d": "Start small, grow later. You only pay for what genuinely moves your business forward."},
    ],
  },
  "projects": {
    "tag": "Projects", "title": "Recent work",
    "items": [
      {"t": "İZ – Uyghur Restaurant, Mannheim", "d": "Restaurant website plus a separate experience page that introduces Uyghur culture and cuisine through play.", "tags": ["Hospitality", "Germany"]},
      {"t": "Kebapçızade, Çorum", "d": "A playful restaurant website with game elements that sparks curiosity and sticks in guests' minds.", "tags": ["Hospitality", "Türkiye"]},
    ],
  },
  "faq": {
    "tag": "FAQ", "title": "Frequently asked questions", "more": "Question not answered here? Just drop us a line.",
    "items": [
      {"q": "How much does a small business website cost?", "a": "It depends on the scope: a one-page website costs far less than an online shop. After a free first call you receive a clear written quote with no hidden costs. On a tight budget we start with the essentials and expand later."},
      {"q": "How long until my website is live?", "a": "A one-page website is often ready within a few weeks; larger websites or shops take longer. We agree the exact timeline together."},
      {"q": "Do you work with businesses in the UK, Switzerland and Türkiye?", "a": "Yes. We work with SMEs in the UK, Switzerland, Türkiye and Germany. Meetings take place by video call, phone or email – in English, Turkish or German."},
      {"q": "Will my website be found on Google?", "a": "Every website is built to be technically clean and search-engine friendly. We choose keywords your customers really use and, on request, set up your Google Business Profile for local search."},
      {"q": "Can I edit the website myself later?", "a": "Yes, if you like. We set things up so you can change text, images or offers yourself – or we look after it for you."},
      {"q": "Can my website be in more than one language?", "a": "Yes. We build websites in English, Turkish and German – also combined, with each language found separately on Google."},
    ],
  },
  "contact": {
    "tag": "Contact", "title": "Tell us about your project",
    "lead": "Send us a short message about what you need. You will get a personal reply, and your first consultation is free with no obligation.",
    "email": "Email", "insta": "Instagram", "loc_label": "Locations", "loc": "Germany (Saarland) & Switzerland",
    "langs_label": "Languages", "langs": "English · Türkçe · Deutsch",
    "cta": "Send an email", "subject": "Website enquiry – free consultation",
    "box_title": "Free first consultation", "box_text": "We review your current online presence and show you what is worth doing for your business – with no obligation.",
  },
  "footer": {"tagline": "Web design & consulting for SMEs", "imprint": "Legal notice", "privacy": "Privacy", "rights": "All rights reserved."},
  "langbar": {"text": "This page is also available in English.", "go": "Go to English page", "close": "Close"},
}

LANGS = [EN, DE, TR]

# ---------------------------------------------------------------------------
# Lösungsfinder – Optionen & Bausteine (pro Sprache)
# pkg-Logik steht in app.js; hier nur Texte.
# ---------------------------------------------------------------------------
FINDER = {
  "de": {
    "industries": {
      "food": ("Gastronomie", ["Speisekarte online, mobil lesbar", "Reservierung oder Bestellung per Klick"]),
      "trade": ("Handwerk & Bau", ["Referenzen mit Vorher-/Nachher-Bildern", "Anfrageformular mit Foto-Upload"]),
      "health": ("Praxis & Gesundheit", ["Online-Terminbuchung", "Leistungen verständlich erklärt"]),
      "hotel": ("Hotel & Tourismus", ["Direktbuchung ohne Portalgebühren", "Bildergalerie & Umgebungstipps"]),
      "retail": ("Handel & Shop", ["Produktkatalog oder Online-Shop", "Öffnungszeiten & Aktionen aktuell"]),
      "service": ("Dienstleistung & Beratung", ["Klare Leistungsseiten mit Preisrahmen", "Vertrauen durch Kundenstimmen"]),
      "other": ("Andere Branche", ["Aufbau passend zu Ihren Abläufen", "Funktionen nach Ihrem Bedarf"]),
    },
    "goals": {
      "start": ("Erste Website", ["Professioneller Auftritt in kurzer Zeit"]),
      "leads": ("Mehr Anfragen", ["Klare Kontaktwege auf jeder Seite"]),
      "google": ("Bei Google gefunden werden", ["Lokale SEO & Google-Unternehmensprofil"]),
      "sell": ("Online verkaufen", ["Online-Shop mit sicherer Zahlung"]),
      "book": ("Termine / Buchungen", ["Buchungssystem, das Ihnen Arbeit abnimmt"]),
      "intl": ("Neue Länder / Sprachen", ["Mehrsprachige Seiten, je Sprache bei Google auffindbar"]),
    },
    "budgets": {"small": "Klein starten", "mid": "Mittel", "open": "Noch offen"},
    "pkgs": {"start": "Paket Start", "business": "Paket Business", "custom": "Paket Individuell"},
    "staged": "Tipp: Wir starten mit dem Wichtigsten und bauen in Etappen aus – so bleibt es bezahlbar.",
    "always": "Mobil optimiert, schnell & suchmaschinenfreundlich",
    "mail_intro": "Hallo Hattat-Team,\n\nich interessiere mich für eine Website. Meine Angaben aus dem Lösungsfinder:",
    "mail_outro": "\n\nBitte melden Sie sich für ein kostenloses Erstgespräch.\n\nViele Grüsse",
    "mail_labels": ("Branche", "Ziel", "Budget", "Vorschlag"),
  },
  "tr": {
    "industries": {
      "food": ("Restoran & kafe", ["Mobil uyumlu online menü", "Tek tıkla rezervasyon veya sipariş"]),
      "trade": ("İnşaat & zanaat", ["Öncesi/sonrası fotoğraflarla referanslar", "Fotoğraf yüklemeli teklif formu"]),
      "health": ("Klinik & sağlık", ["Online randevu sistemi", "Hizmetlerin anlaşılır anlatımı"]),
      "hotel": ("Otel & turizm", ["Komisyonsuz direkt rezervasyon", "Fotoğraf galerisi & çevre önerileri"]),
      "retail": ("Mağaza & ticaret", ["Ürün kataloğu veya e-ticaret", "Güncel çalışma saatleri & kampanyalar"]),
      "service": ("Hizmet & danışmanlık", ["Fiyat aralıklı net hizmet sayfaları", "Müşteri yorumlarıyla güven"]),
      "other": ("Diğer sektör", ["İş süreçlerinize uygun yapı", "İhtiyacınıza göre özellikler"]),
    },
    "goals": {
      "start": ("İlk web sitem", ["Kısa sürede profesyonel bir görünüm"]),
      "leads": ("Daha fazla talep", ["Her sayfada net iletişim yolları"]),
      "google": ("Google'da bulunmak", ["Yerel SEO & Google İşletme Profili"]),
      "sell": ("Online satış", ["Güvenli ödemeli e-ticaret sitesi"]),
      "book": ("Randevu / rezervasyon", ["İşinizi kolaylaştıran rezervasyon sistemi"]),
      "intl": ("Yeni ülkeler / diller", ["Her dili Google'da ayrı bulunan çok dilli sayfalar"]),
    },
    "budgets": {"small": "Küçük başlamak", "mid": "Orta", "open": "Henüz belli değil"},
    "pkgs": {"start": "Başlangıç paketi", "business": "Kurumsal paket", "custom": "Size Özel paket"},
    "staged": "İpucu: En önemli kısımla başlar, aşama aşama büyütürüz – böylece bütçenize uygun kalır.",
    "always": "Mobil uyumlu, hızlı ve arama motoru dostu",
    "mail_intro": "Merhaba Hattat ekibi,\n\nbir web sitesiyle ilgileniyorum. Çözüm bulucudaki bilgilerim:",
    "mail_outro": "\n\nÜcretsiz ön görüşme için benimle iletişime geçebilir misiniz?\n\nSaygılarımla",
    "mail_labels": ("Sektör", "Hedef", "Bütçe", "Öneri"),
  },
  "en": {
    "industries": {
      "food": ("Restaurant & café", ["Mobile-friendly online menu", "One-click booking or ordering"]),
      "trade": ("Trades & construction", ["Before/after project gallery", "Enquiry form with photo upload"]),
      "health": ("Clinic & health", ["Online appointment booking", "Treatments explained clearly"]),
      "hotel": ("Hotel & tourism", ["Direct bookings without portal fees", "Photo gallery & local tips"]),
      "retail": ("Retail & shop", ["Product catalogue or online shop", "Opening hours & offers kept current"]),
      "service": ("Services & consulting", ["Clear service pages with price ranges", "Trust through customer reviews"]),
      "other": ("Other industry", ["Structure built around your processes", "Features based on your needs"]),
    },
    "goals": {
      "start": ("My first website", ["A professional presence, quickly"]),
      "leads": ("More enquiries", ["Clear ways to get in touch on every page"]),
      "google": ("Get found on Google", ["Local SEO & Google Business Profile"]),
      "sell": ("Sell online", ["Online shop with secure payments"]),
      "book": ("Appointments / bookings", ["A booking system that saves you time"]),
      "intl": ("New countries / languages", ["Multilingual pages, each found on Google"]),
    },
    "budgets": {"small": "Start small", "mid": "Medium", "open": "Not sure yet"},
    "pkgs": {"start": "Starter package", "business": "Business package", "custom": "Bespoke package"},
    "staged": "Tip: we start with the essentials and grow in stages – so it stays affordable.",
    "always": "Mobile-ready, fast & search-engine friendly",
    "mail_intro": "Hello Hattat team,\n\nI am interested in a website. My answers from the solution finder:",
    "mail_outro": "\n\nPlease get in touch to arrange a free consultation.\n\nKind regards",
    "mail_labels": ("Industry", "Goal", "Budget", "Suggestion"),
  },
}

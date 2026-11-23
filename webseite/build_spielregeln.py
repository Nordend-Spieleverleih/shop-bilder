#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die 8 neuen Spielregeln-Seiten (gleiches Design wie moelkky-rechner.html /
wikingerschach-online.html: links Foto/Video-Galerie, rechts Regelkarte mit Anker #regeln).
Schreibt je eine Datei nach webseite/<slug>.html
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

CSS = """
.sp-regeln{
  --green:#477c6e;
  --green-dark:#3a685c;
  --cream:#f6f2ed;
  --chip:#ebe8e5;
  --ink:#2b2b2b;
  --ink-light:#333333;
  --radius:14px;
  font-family:Nunito,system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
  color:var(--ink);
  padding:8px 0 24px;
}
.sp-regeln *{box-sizing:border-box;}
.sp-regeln .sr-wrap{max-width:1080px;margin:0 auto;padding:0 16px;}
.sp-regeln .sr-back{display:inline-block;margin-bottom:14px;font-weight:700;color:var(--green);text-decoration:none;}
.sp-regeln .sr-back:hover{color:var(--green-dark);}
.sp-regeln .sr-header{text-align:center;margin-bottom:22px;display:flex;flex-direction:column;align-items:center;gap:10px;}
.sp-regeln .sr-header img{width:84px;height:84px;object-fit:cover;border-radius:50%;box-shadow:0 6px 16px rgba(0,0,0,.18);border:3px solid #fff;}
.sp-regeln .sr-header h1{font-size:clamp(1.5rem,3.5vw,2.1rem);margin:0 0 4px;color:var(--green-dark);font-weight:800;}
.sp-regeln .sr-header p{margin:0;color:#6b6b6b;font-size:0.95rem;max-width:34em;}
.sp-regeln .sr-grid{display:grid;grid-template-columns:minmax(0,480px) minmax(300px,480px);gap:28px;align-items:start;justify-content:center;}
.sp-regeln .sr-col-right .card{position:sticky;top:20px;}
.sp-regeln .sr-gal{display:flex;flex-direction:column;gap:10px;}
.sp-regeln .sr-gal .row{display:flex;gap:10px;}
.sp-regeln .sr-gal .row>div{flex:1;min-width:0;border-radius:var(--radius);overflow:hidden;aspect-ratio:1.3/1;box-shadow:0 2px 10px rgba(0,0,0,0.08);}
.sp-regeln .sr-gal img,.sp-regeln .sr-gal video{width:100%;height:100%;object-fit:cover;display:block;}
.sp-regeln .card{
  background:#fff;
  border-radius:var(--radius);
  padding:20px;
  margin-bottom:14px;
  box-shadow:0 2px 10px rgba(0,0,0,0.06);
  border:1px solid #ebe7e3;
}
.sp-regeln .sr-eyebrow{display:inline-block;font-weight:800;letter-spacing:.08em;text-transform:uppercase;font-size:.75rem;color:var(--green);margin-bottom:.4em;}
.sp-regeln .sr-info h2{font-size:1.4rem;margin:0 0 .2em;color:var(--ink);font-weight:800;}
.sp-regeln .sr-info .sr-tag{font-size:1rem;color:var(--green-dark);font-weight:700;margin-bottom:.6em;}
.sp-regeln .sr-info h3{font-size:0.95rem;margin:.9em 0 .2em;color:var(--ink);font-weight:800;}
.sp-regeln .sr-info p{color:#5d5d5d;margin:0 0 .6em;font-size:0.95rem;}
.sp-regeln .sr-facts{list-style:none;padding:0;margin:.8em 0 0;display:flex;flex-wrap:wrap;gap:8px;}
.sp-regeln .sr-facts li{background:var(--chip);border-radius:10px;padding:6px 12px;font-size:.85rem;}
.sp-regeln .sr-facts b{color:var(--green);margin-right:6px;}
.sp-regeln .btn-primary{display:inline-block;width:100%;text-align:center;background:var(--green);color:#fff!important;border:none;border-radius:10px;padding:12px 16px;font-weight:700;font-size:0.95rem;text-decoration:none;margin-top:16px;}
.sp-regeln .btn-primary:hover{background:var(--green-dark);}
.sp-regeln .sr-cta{text-align:center;background:var(--green);color:#fff;border-radius:16px;padding:28px 20px;margin-top:22px;}
.sp-regeln .sr-cta h2{color:#fff;font-size:1.3rem;margin:0 0 6px;}
.sp-regeln .sr-cta p{color:#fff;opacity:.92;margin:0 0 14px;}
.sp-regeln .sr-cta .row{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:0;}
.sp-regeln .btn-white{background:#fff;color:var(--green)!important;border-radius:10px;padding:12px 20px;font-weight:700;text-decoration:none;display:inline-block;}
.sp-regeln .btn-white:hover{background:var(--cream);}
.sp-regeln .btn-outline-white{background:transparent;color:#fff!important;border:2px solid #fff;border-radius:10px;padding:10px 18px;font-weight:700;text-decoration:none;display:inline-block;}
.sp-regeln .btn-outline-white:hover{background:#fff;color:var(--green)!important;}
.sp-regeln .footer-note{text-align:center;font-size:0.78rem;color:#999;margin-top:18px;}
@media(max-width:860px){
  .sp-regeln .sr-grid{grid-template-columns:1fr;max-width:560px;margin:0 auto;}
  .sp-regeln .sr-col-right .card{position:static;}
}
"""

PAGE_TMPL = """<div class="nsv sp-regeln">
<style>{css}</style>

<div class="sr-wrap">
  <a class="sr-back" href="/spieleauswahl/#{anchor_id}">&larr; Zur&uuml;ck zur Spieleauswahl</a>
  <div class="sr-header">
    <img src="{header_img}" alt="{title} vom Nordend-Spieleverleih">
    <h1>{title}: Spielregeln</h1>
    <p>{intro}</p>
  </div>

  <div class="sr-grid">
    <div class="sr-col-left">
      <div class="sr-gal">
{gallery}
      </div>
      <div class="footer-note">Fotos: eigenes Spiel des Nordend-Spieleverleihs im Einsatz.</div>
    </div>

    <div class="sr-col-right">
      <div class="card sr-info" id="regeln">
        <span class="sr-eyebrow">Spielregeln</span>
        <h2>So wird {title} gespielt</h2>
        <p class="sr-tag">{tag}</p>
{sections}
        <ul class="sr-facts">{facts}</ul>
        <a class="btn-primary" href="/jetzt-buchen/">Jetzt buchen</a>
      </div>
    </div>
  </div>

  <div class="sr-cta">
    <h2>Lust, {title} selbst zu spielen?</h2>
    <p>Wir bringen {title} und 11 weitere Spiele direkt zu dir &ndash; abholen oder liefern lassen.</p>
    <div class="row">
      <a class="btn-white" href="/jetzt-buchen/">Jetzt buchen</a>
      <a class="btn-outline-white" href="/spieleauswahl/">Alle Spiele ansehen</a>
    </div>
  </div>
</div>
</div>
"""

SECTION_TMPL = "        <h3>{h}</h3>\n        <p>{p}</p>\n"


def gal_block(media):
    """media: list of (type, url) pairs, max 3, rendered as rows of up to 2."""
    rows = []
    i = 0
    while i < len(media):
        chunk = media[i:i+2]
        cells = []
        for kind, url in chunk:
            if kind == "video":
                cells.append(f'          <div><video src="{url}" autoplay muted loop playsinline preload="metadata"></video></div>')
            else:
                cells.append(f'          <div><img src="{url}" alt="" loading="lazy"></div>')
        rows.append('        <div class="row">\n' + "\n".join(cells) + '\n        </div>')
        i += 2
    return "\n".join(rows)


GAMES = [
    dict(
        slug="jenga-spielregeln",
        anchor_id="xxl-jenga",
        title="XXL-Jenga",
        header_img="https://nordend-spieleverleih.de/wp-content/uploads/2026/09/PXL_20260927_141808246.PORTRAIT-scaled.jpg",
        intro="Der Holzturm-Klassiker in XXL &ndash; einfache Regeln, maximale Spannung.",
        tag="Der Riesenspa&szlig; aus FSC-zertifizierten Hartholzbl&ouml;cken",
        sections=[
            ("Aufbau", "Die Holzbl&ouml;cke werden zu einem Turm gestapelt: je drei Bl&ouml;cke pro Lage, eng nebeneinander, jede Lage um 90&deg; zur vorherigen gedreht. So startet der Turm stabil mit rund 68&nbsp;cm H&ouml;he."),
            ("Ablauf", "Reihum zieht jede:r mit nur einer Hand genau <b>einen</b> Block aus einer beliebigen Lage unterhalb der obersten drei vollst&auml;ndigen Lagen und legt ihn oben quer auf den Turm. Je h&ouml;her der Turm w&auml;chst, desto wackliger wird er &ndash; und desto mehr Mut braucht der n&auml;chste Zug."),
            ("Ziel &amp; Gewinn", "Wer den Turm zum Einsturz bringt, hat verloren &ndash; alle anderen gewinnen gemeinsam. Bei gro&szlig;en Gruppen spielt ihr einfach reihum weiter, bis nur noch eine Person &uuml;brig ist."),
        ],
        facts=[("Spieler", "Ab 2 (perfekt auch in Teams)"), ("Ab", "4 Jahren"), ("Wo", "Drinnen (mit Unterlegmatte) &amp; Drau&szlig;en"), ("Dauer", "ca. 15&ndash;30 Min.")],
        media=[("image", "https://nordend-spieleverleih.de/wp-content/uploads/2026/09/PXL_20260927_141808246.PORTRAIT-scaled.jpg"),
               ("image", "https://nordend-spieleverleih.de/wp-content/uploads/2026/09/Jengaturm-in-Halle-scaled.jpg")],
    ),
    dict(
        slug="cornhole-spielregeln",
        anchor_id="cornhole",
        title="Cornhole",
        header_img="https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.15.34.jpeg",
        intro="Der Party-Trend aus den USA &ndash; S&auml;ckchen werfen f&uuml;r echtes Festival-Feeling.",
        tag="Der packende Party-Trend aus den USA f&uuml;r echtes Festival-Feeling",
        sections=[
            ("Aufbau", "Die beiden angeschr&auml;gten Holzplattformen stehen sich in passendem Abstand gegen&uuml;ber (klassisch rund 7&ndash;8&nbsp;Meter, bei Kindern gerne n&auml;her). Jedes Team bekommt vier mit Maisk&ouml;rnern gef&uuml;llte S&auml;ckchen in seiner Farbe."),
            ("Ablauf", "Zwei Teams werfen abwechselnd ihre S&auml;ckchen auf das gegen&uuml;berliegende Brett. Bleibt ein S&auml;ckchen auf dem Brett liegen, gibt es <b>1 Punkt</b>, rutscht es durch das Loch, gibt es <b>3 Punkte</b>. In der klassischen Variante verrechnet ihr am Ende jeder Runde die Punkte beider Teams und nur die Differenz wird gutgeschrieben."),
            ("Ziel &amp; Gewinn", "Gespielt wird &uuml;ber mehrere Runden, bis ein Team zuerst <b>21 Punkte</b> erreicht &ndash; das Team gewinnt."),
        ],
        facts=[("Spieler", "2 bis 4 (perfekt f&uuml;r 1vs1 oder 2vs2)"), ("Ab", "6 Jahren"), ("Wo", "Drinnen &amp; Drau&szlig;en"), ("Dauer", "ca. 20&ndash;30 Min.")],
        media=[("video", "https://nordend-spieleverleih.de/wp-content/uploads/2026/11/nsv-cornhole.mp4"),
               ("image", "https://nordend-spieleverleih.de/wp-content/uploads/2026/09/Cornhole-Halle-1-scaled.jpg")],
    ),
    dict(
        slug="spikeball-spielregeln",
        anchor_id="spikeball-roundnet",
        title="Spikeball (Roundnet)",
        header_img="https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.18.47.jpeg",
        intro="Das Trendspiel f&uuml;r den Sommer &ndash; Action rund um ein kleines, rundes Trampolin-Netz.",
        tag="Action, Dynamik und jede Menge Auspowern im Park!",
        sections=[
            ("Aufbau", "Das runde, trampolinartige Netz wird flach am Boden aufgestellt. Zwei Teams aus je zwei Spieler:innen positionieren sich rundherum."),
            ("Ablauf", "Ein Team er&ouml;ffnet mit einem Aufschlag aufs Netz. Danach spielt sich jedes Team den Ball mit <b>maximal drei Ber&uuml;hrungen</b> selbst zu &ndash; &auml;hnlich wie beim Volleyball-Annahme-Zuspiel-Angriff &ndash; und schl&auml;gt ihn dann so aufs Netz, dass das gegnerische Team ihn nicht mehr kontrolliert zur&uuml;ckbekommt."),
            ("Punkte", "Gelingt der Rückschlag nicht (Ball fällt zu Boden, mehr als drei Ber&uuml;hrungen, Ball verfehlt das Netz komplett), bekommt das andere Team einen Punkt. Gespielt wird meist bis <b>21 Punkte</b> mit mindestens zwei Punkten Vorsprung."),
        ],
        facts=[("Spieler", "4 (2 gegen 2)"), ("Ab", "6 Jahren (etwas Koordination hilft)"), ("Wo", "Drinnen &amp; Drau&szlig;en"), ("Set", "Netz, 3 B&auml;lle, Pumpe")],
        media=[("image", "https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.18.47.jpeg"),
               ("image", "https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.18.46.jpeg")],
    ),
    dict(
        slug="stakk-spielregeln",
        anchor_id="stakk",
        title="STAKK",
        header_img="https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.25.22.jpeg",
        intro="Zielen, stapeln, taktieren &ndash; das Outdoor-Wurfspiel zwischen Boccia und Turmbau.",
        tag="Outdoor-Wurfspiel, das Elemente aus Boccia, Boule und Turm-Geschicklichkeitsspielen verbindet",
        sections=[
            ("Aufbau", "Die neun Holzw&uuml;rfel werden in der Spielmitte bereitgelegt bzw. zu einem kleinen Turm gestapelt. Jede:r Spielende bzw. jedes Team sucht sich eine Wurfposition in passendem Abstand."),
            ("Ablauf", "Reihum wird gezielt geworfen: Mal geht es darum, die W&uuml;rfel der Gegenseite m&ouml;glichst geschickt umzuwerfen, mal darum, eigene W&uuml;rfel im Duell cleverer zu stapeln als die anderen. Treffsicherheit und Taktik entscheiden, wer vorne liegt."),
            ("Ziel &amp; Gewinn", "Punkte sammeln, gegnerische W&uuml;rfe kontern und am Ende die meisten Punkte bzw. den stabilsten Turm haben &ndash; die genaue Zählweise und alle Varianten stehen auf der mitgelieferten Spielanleitung, die wir mit ausleihen."),
        ],
        facts=[("Spieler", "Ab 2 (perfekt auch in Teams)"), ("Ab", "4 Jahren"), ("Wo", "Drinnen (auf Teppich) &amp; Drau&szlig;en"), ("Set", "9 Holzw&uuml;rfel + Anleitung")],
        media=[("video", "https://nordend-spieleverleih.de/wp-content/uploads/2026/11/nsv-stakk.mp4"),
               ("image", "https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.25.22-1.jpeg")],
    ),
    dict(
        slug="leitergolf-spielregeln",
        anchor_id="leitergolf",
        title="Leitergolf",
        header_img="https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.29.43.jpeg",
        intro="Der Geschicklichkeits-Klassiker f&uuml;r Jung und Alt &ndash; Bolas werfen, Sprossen treffen.",
        tag="Der absolute Geschicklichkeits-Klassiker f&uuml;r Jung und Alt",
        sections=[
            ("Aufbau", "Die Holzleiter mit ihren drei Sprossen (oben, Mitte, unten) steht als Ziel, die werfende Person bzw. das Team positioniert sich in passendem Abstand davor (je nach Alter 3&ndash;5&nbsp;Meter)."),
            ("Ablauf", "Geworfen wird mit den <b>Bolas</b> &ndash; zwei Holzkugeln, die an einer Schnur verbunden sind. Mit geschicktem Schwung sollen sie sich um eine der Sprossen wickeln und dort h&auml;ngen bleiben. Jede Sprosse bringt je nach H&ouml;he unterschiedlich viele Punkte; die genaue Punktetabelle steht auf der mitgelieferten Anleitung."),
            ("Ziel &amp; Gewinn", "Reihum wird geworfen und die Punkte addiert. Wer zuerst <b>exakt 21 Punkte</b> erreicht, gewinnt das Match &ndash; wer dar&uuml;ber hinausschie&szlig;t, muss laut Standardregel in dieser Runde erneut ansetzen."),
        ],
        facts=[("Spieler", "Ab 1 (auch gegen sich selbst)"), ("Ab", "5 Jahren"), ("Wo", "Drinnen &amp; Drau&szlig;en"), ("Set", "Leiter, 6 Bolas, Tragetasche")],
        media=[("image", "https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.29.43.jpeg"),
               ("image", "https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.29.21.jpeg")],
    ),
    dict(
        slug="schwungtuch-spielregeln",
        anchor_id="schwungtuch-mit-bälle",
        title="Schwungtuch",
        header_img="https://nordend-spieleverleih.de/wp-content/uploads/2026/09/Wurftuch-Halle-scaled.jpg",
        intro="Gemeinsames Schwingen, Wellen und Ballspiele &ndash; Kinder lieben das garantiert.",
        tag="Kinder lieben das garantiert!",
        sections=[
            ("Aufbau", "Alle Mitspieler:innen fassen je eine der zw&ouml;lf Schlaufen am Rand des bunten, 3,65&nbsp;m breiten Tuchs und stehen im Kreis. Die mitgelieferten B&auml;lle kommen in die Mitte."),
            ("Spielideen", "<b>Wellen erzeugen:</b> alle heben und senken das Tuch abwechselnd, sodass Wellen &uuml;ber die B&auml;lle laufen. <b>Kugel-Katapult:</b> gemeinsam das Tuch kurz straffen und die B&auml;lle hoch in die Luft schleudern &ndash; und wieder auffangen. <b>Platzwechsel:</b> das Tuch wird hochgehalten, einzelne Kinder laufen schnell darunter hindurch, bevor es wieder sinkt."),
            ("Ziel", "Es gibt kein festes Gewinnziel &ndash; im Vordergrund stehen Teamwork, Bewegung und gemeinsamer Spa&szlig;. Gerade f&uuml;r gro&szlig;e Gruppen und gemischte Altersstufen ideal."),
        ],
        facts=[("Spieler", "4 bis 12"), ("Ab", "3 Jahren"), ("Wo", "Drinnen &amp; Drau&szlig;en"), ("Set", "Schwungtuch + B&auml;lle")],
        media=[("image", "https://nordend-spieleverleih.de/wp-content/uploads/2026/09/Wurftuch-Halle-scaled.jpg"),
               ("image", "https://nordend-spieleverleih.de/wp-content/uploads/2026/11/schwungtuch-kinder-spielen.jpg")],
    ),
    dict(
        slug="froebelturm-spielregeln",
        anchor_id="fröbelturm",
        title="Fr&ouml;belturm",
        header_img="https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.35.07.jpeg",
        intro="Teambuilding f&uuml;r Gro&szlig; und Klein &ndash; nur gemeinsam l&auml;sst sich der Turm bauen.",
        tag="Teambuilding f&uuml;r Gro&szlig; und Klein",
        sections=[
            ("Aufbau", "Bis zu 24 Schn&uuml;re laufen an einem zentralen Haken (Ring) zusammen; jede:r Mitspielende h&auml;lt eine Schnur in der Hand. Die Holzklötze liegen bereit."),
            ("Ablauf", "Nur durch gemeinsame Absprache und ruhige Hände l&auml;sst sich der Haken so steuern, dass er &uuml;ber einen Holzklotz sinkt. Zieht die Gruppe die Schn&uuml;re gleichzeitig leicht nach au&szlig;en, klemmt sich der Klotz zwischen die Schn&uuml;re und kann angehoben und auf dem wachsenden Turm abgelegt werden."),
            ("Ziel &amp; Gewinn", "Zieht eine Person zu fest oder zu fr&uuml;h, st&uuml;rzt der halb gehaltene Klotz oder der ganze Turm ein. Ziel ist, gemeinsam einen m&ouml;glichst hohen, stabilen Turm zu bauen &ndash; ideal auch als Wettkampf zwischen zwei Gruppen, wer h&ouml;her kommt."),
        ],
        facts=[("Spieler", "3 bis 24 (perfekt f&uuml;r Gruppen &amp; Teambuilding)"), ("Ab", "4 Jahren"), ("Wo", "Drinnen &amp; Drau&szlig;en"), ("Set", "12 Schn&uuml;re + Holzkl&ouml;tze")],
        media=[("image", "https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.35.07.jpeg"),
               ("image", "https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.35.07-1.jpeg")],
    ),
    dict(
        slug="beerpong-spielregeln",
        anchor_id="beerpong-bierpong",
        title="Beerpong",
        header_img="https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.37.33.jpeg",
        intro="Treffsicherheit, Teamgeist und Stimmung &ndash; bei uns ganz selbstverst&auml;ndlich auch alkoholfrei.",
        tag="Spa&szlig; f&uuml;r den Park &ndash; bei uns immer in der kinderfreundlichen, alkoholfreien Variante",
        sections=[
            ("Aufbau", "An beiden Enden eines Tisches wird je eine kleine Pyramide aus Bechern aufgestellt (meist 6 oder 10 St&uuml;ck), gef&uuml;llt mit Wasser oder einem Getr&auml;nk &ndash; bei uns grunds&auml;tzlich alkoholfrei."),
            ("Ablauf", "Zwei Teams werfen abwechselnd einen leichten Ball in Richtung der gegn&uuml;berliegenden Becher. Landet der Ball in einem Becher, muss das gegnerische Team diesen Becher leeren und vom Tisch nehmen."),
            ("Ziel &amp; Gewinn", "Das Team, das zuerst alle gegnerischen Becher getroffen hat, gewinnt die Runde. Treffsicherheit, Konzentration und Teamgeist entscheiden &uuml;ber den Sieg."),
        ],
        facts=[("Spieler", "Ab 2"), ("Ab", "In der alkoholfreien Variante auch f&uuml;r Kids"), ("Wo", "Drinnen &amp; Drau&szlig;en")],
        media=[("video", "https://nordend-spieleverleih.de/wp-content/uploads/2026/11/nsv-beerpong1.mp4"),
               ("image", "https://nordend-spieleverleih.de/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-28-at-14.37.33-1.jpeg")],
    ),
]


def build_game(g):
    sections_html = "".join(SECTION_TMPL.format(h=h, p=p) for h, p in g["sections"])
    facts_html = "".join(f"<li><b>{k}</b>{v}</li>" for k, v in g["facts"])
    gallery_html = gal_block(g["media"])
    html = PAGE_TMPL.format(
        css=CSS,
        anchor_id=g["anchor_id"],
        header_img=g["header_img"],
        title=g["title"],
        intro=g["intro"],
        tag=g["tag"],
        sections=sections_html,
        facts=facts_html,
        gallery=gallery_html,
    )
    out_path = os.path.join(HERE, g["slug"] + ".html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", out_path, len(html), "bytes")


if __name__ == "__main__":
    for g in GAMES:
        build_game(g)

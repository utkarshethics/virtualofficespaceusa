# -*- coding: utf-8 -*-
"""Builds the keyword landing pages, guides hub, homepage hub links and sitemap.

Usage:  python3 tools/build_pages.py
Content lives in tools/pages_content.py. Re-run after editing; output is static HTML
that Cloudflare Pages serves as-is (no build step needed on deploy).
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages_content import SERVICES, STATES, GUIDES, POPULAR, FACT_DATE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = "https://virtualofficespaceusa.online"
ORG = B + "/#organization"
TODAY = "2026-10-23"
PHONE_TEL, PHONE = "+13313287053", "+1 (331) 328-7053"
EMAIL = "connect@virtualofficespaceusa.online"

PAGES = {}
for p in SERVICES: PAGES[p["slug"]] = dict(p, kind="service")
for p in STATES:   PAGES[p["slug"]] = dict(p, kind="state", nav=f"{p['name']} registered agent & address")
for p in GUIDES:   PAGES[p["slug"]] = dict(p, kind="guide")
GUIDES_HUB = {"slug": "guides", "kind": "hub", "nav": "All guides",
              "title": "US Company Setup Guides | Virtual Office Space USA",
              "desc": "Plain-English guides for founders setting up a US company: registered agents, USPS Form 1583, getting an EIN without an SSN, and Wyoming vs. Delaware LLCs.",
              "h1": "Guides for setting up a US company",
              "lead": "Practical, up-to-date answers for founders forming and running a US LLC — especially from outside the US."}
PAGES["guides"] = GUIDES_HUB

def url(slug): return f"{B}/{slug}/"
def href(slug): return f"/{slug}/"
def esc(s): return html.escape(s, quote=True)

# ------------------------------------------------------------------ fragments
def render_block(item):
    kind, _, body = item.partition(":")
    if kind == "p":  return f"<p>{body}</p>"
    if kind in ("ul", "ol"):
        lis = "".join(f"<li>{x}</li>" for x in body.split("|"))
        return f"<{kind}>{lis}</{kind}>"
    if kind == "table":
        rows = [r.split("|") for r in body.split("\n")]
        head = "".join(f'<th scope="col">{c}</th>' for c in rows[0])
        trs = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows[1:])
        return f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{trs}</tbody></table></div>'
    if kind == "states":
        lis = "".join(f'<li><a href="{href(s["slug"])}">{s["name"]} registered agent</a></li>' for s in STATES)
        return f'<ul class="link-grid">{lis}</ul>'
    raise ValueError(item)

def slugify(t): return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:60].rstrip("-")

def sections_html(sections):
    out = []
    for title, blocks in sections:
        sid = slugify(title)
        out.append(f'<section class="prose-section" aria-labelledby="{sid}"><h2 id="{sid}">{title}</h2>' + "".join(render_block(b) for b in blocks) + "</section>")
    return "\n".join(out)

def facts_html(p):
    rows = "".join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in p["facts"])
    return (f'<section class="prose-section" aria-labelledby="facts"><h2 id="facts">{p["name"]} at a glance</h2>'
            f'<div class="table-wrap"><table class="facts"><tbody>{rows}</tbody></table></div>'
            f'<p class="fine">State fees as of {FACT_DATE}. Fees change — confirm with the {p["name"]} Secretary of State before filing.</p></section>')

def faq_html(faqs):
    items = []
    for i, (q, a) in enumerate(faqs):
        fid = "faq-" + slugify(q)
        items.append(f'<div class="faq-item" id="{fid}"><button class="faq-question" aria-expanded="false" aria-controls="{fid}-answer">'
                     f'<span>{esc(q)}</span><span class="arrow">+</span></button>'
                     f'<div class="faq-answer" id="{fid}-answer" role="region" style="display:none;">{esc(a)}</div></div>')
    return ('<section class="prose-section" aria-labelledby="page-faq"><h2 id="page-faq">Frequently asked questions</h2>'
            f'<div class="faq-list page-faq">{"".join(items)}</div></section>')

def related_html(slugs):
    cards = "".join(f'<li><a href="{href(s)}">{esc(PAGES[s]["nav"])}</a></li>' for s in slugs)
    return f'<aside class="related" aria-labelledby="related-title"><h2 id="related-title">Related</h2><ul class="link-grid">{cards}</ul></aside>'

def cta_html(p):
    service = "Business Pro ($39/mo)"
    if p["slug"] in ("us-llc-for-non-residents", "guides/how-to-get-an-ein-for-an-llc"): service = "US LLC + EIN Formation Package"
    if p["slug"] == "virtual-mailbox": service = "Digital Mail ($19/mo)"
    label = f'Get your {p["name"]} address' if p.get("kind") == "state" else "Get your US address"
    return (f'<div class="page-cta"><button class="btn btn-primary btn-lg open-lead-btn" data-intent="{esc(p["h1"])}" data-service="{esc(service)}">{label}</button>'
            f'<a class="btn btn-outline btn-lg" href="/#pricing">See plans from $19/mo</a></div>')

HEADER = f'''  <header class="navbar">
    <div class="container nav-content">
      <a href="/" class="logo" aria-label="Virtual Office Space USA home">🏢 Virtual Office <span>USA</span></a>
      <nav aria-label="Primary"><ul class="nav-links">
        <li><a href="/#states">States</a></li>
        <li><a href="/#services">Services</a></li>
        <li><a href="/#pricing">Pricing</a></li>
        <li><a href="/guides/">Guides</a></li>
      </ul></nav>
      <div class="nav-actions">
        <a href="tel:{PHONE_TEL}" class="btn btn-outline btn-sm" aria-label="Call Virtual Office Space USA at {PHONE}">📞 {PHONE}</a>
        <button class="btn btn-whatsapp btn-sm open-lead-btn" data-intent="Header Instant Inquiry" data-service="Business Pro Plan">💬 WhatsApp</button>
      </div>
    </div>
  </header>'''

def footer_html():
    states = "".join(f'<li><a href="{href(s["slug"])}">{s["name"]} Virtual Office</a></li>' for s in STATES)
    services = "".join(f'<li><a href="{href(s["slug"])}">{s["nav"]}</a></li>' for s in SERVICES)
    guides = "".join(f'<li><a href="{href(g["slug"])}">{g["nav"]}</a></li>' for g in GUIDES)
    return f'''  <footer aria-label="Site footer">
    <div class="container">
      <div class="footer-grid footer-grid-4">
        <div class="footer-brand">
          <p class="footer-title">🏢 Virtual Office Space USA</p>
          <p>The trusted commercial address, registered agent, and mail forwarding platform for international founders, e-commerce stores, and high-growth startups operating in the United States.</p>
          <p style="margin-top:12px;font-size:0.85rem;">
            <!--email_off-->
            Direct Contact: <a href="mailto:{EMAIL}">{EMAIL}</a> &nbsp;•&nbsp; Phone: <a href="tel:{PHONE_TEL}">{PHONE}</a>
            <!--/email_off-->
          </p>
        </div>
        <div class="footer-col"><nav aria-label="States"><p class="footer-title">States</p><ul>{states}</ul></nav></div>
        <div class="footer-col"><nav aria-label="Services"><p class="footer-title">Services</p><ul>{services}</ul></nav></div>
        <div class="footer-col"><nav aria-label="Guides"><p class="footer-title">Guides</p><ul>{guides}<li><a href="/guides/">All guides</a></li></ul></nav></div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Virtual Office Space USA. All rights reserved. Registered Commercial Mail Receiving Agency (CMRA) partner network.</p>
      </div>
    </div>
  </footer>'''

def modal_html():
    src = open(os.path.join(ROOT, "index.html")).read()
    # lead modal + floating WhatsApp pill, copied from the homepage so all pages stay in sync
    m = re.search(r'  <!-- Interactive Lead Modal -->.*?<!-- Floating WhatsApp Pill -->.*?</a>\n', src, re.S)
    return m.group(0)

# ------------------------------------------------------------------ schema
def crumbs(p):
    trail = [("Home", B + "/")]
    if p["kind"] == "guide": trail.append(("Guides", url("guides")))
    if p["kind"] == "state": trail.append(("States", B + "/#states"))
    trail.append((p["nav"] if p["kind"] != "hub" else "Guides", url(p["slug"])))
    return trail

def schema(p):
    u = url(p["slug"]); g = []
    page = {"@type": "WebPage", "@id": u + "#webpage", "url": u, "name": p["title"], "description": p["desc"],
            "isPartOf": {"@id": B + "/#website"}, "inLanguage": "en-US", "dateModified": TODAY,
            "breadcrumb": {"@id": u + "#breadcrumb"}, "publisher": {"@id": ORG},
            "primaryImageOfPage": {"@type": "ImageObject", "url": B + "/assets/og-image.png", "width": 1200, "height": 630}}
    if p["kind"] == "hub": page["@type"] = "CollectionPage"
    g.append(page)
    g.append({"@type": "BreadcrumbList", "@id": u + "#breadcrumb", "itemListElement":
              [{"@type": "ListItem", "position": i + 1, "name": n, "item": l} for i, (n, l) in enumerate(crumbs(p))]})
    if p["kind"] == "service":
        svc = {"@type": "Service", "@id": u + "#service", "name": p["h1"][0].upper() + p["h1"][1:], "description": p["desc"],
               "provider": {"@id": ORG}, "areaServed": {"@id": B + "/#usa"}, "url": u, "sameAs": B + "/#" + p["service_id"],
               "offers": [{"@id": B + "/#plan-business-pro"}] if p["slug"] != "us-llc-for-non-residents" else [{"@id": B + "/#plan-global-founder-suite"}]}
        page["mainEntity"] = {"@id": svc["@id"]}; page["about"] = {"@id": svc["@id"]}; g.append(svc)
    if p["kind"] == "state":
        svc = {"@type": "Service", "@id": u + "#service", "name": f'{p["name"]} registered agent and virtual office address',
               "serviceType": ["Registered agent", "Virtual office address"], "description": p["desc"], "provider": {"@id": ORG},
               "areaServed": {"@id": f'{B}/#{p["slug"]}'}, "url": u,
               "offers": [{"@id": B + "/#plan-digital-mail"}, {"@id": B + "/#plan-business-pro"}, {"@id": B + "/#plan-global-founder-suite"}]}
        page["mainEntity"] = {"@id": svc["@id"]}; page["about"] = [{"@id": svc["@id"]}, {"@id": f'{B}/#{p["slug"]}'}]
        page["contentLocation"] = {"@id": f'{B}/#{p["slug"]}'}
        g.append(svc)
    if p["kind"] == "guide":
        art = {"@type": "Article", "@id": u + "#article", "headline": p["h1"], "description": p["desc"], "url": u,
               "mainEntityOfPage": {"@id": u + "#webpage"}, "author": {"@id": ORG}, "publisher": {"@id": ORG},
               "datePublished": TODAY, "dateModified": TODAY, "inLanguage": "en-US",
               "image": B + "/assets/og-image.png"}
        page["mainEntity"] = {"@id": art["@id"]}; g.append(art)
    if p["kind"] == "hub":
        page["mainEntity"] = {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": url(x["slug"]), "name": x["h1"]} for i, x in enumerate(GUIDES)]}
    if p.get("faqs"):
        g.append({"@type": "FAQPage", "@id": u + "#faq", "isPartOf": {"@id": u + "#webpage"}, "mainEntity": [
            {"@type": "Question", "@id": u + "#faq-" + slugify(q), "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]})
    return json.dumps({"@context": "https://schema.org", "@graph": g}, separators=(",", ":"), ensure_ascii=False).replace("</", "<\\/")

# ------------------------------------------------------------------ page
def page_html(p):
    u = url(p["slug"])
    trail = crumbs(p)
    crumb_html = " <span aria-hidden=\"true\">›</span> ".join(
        (f'<a href="{l.replace(B, "") or "/"}">{esc(n)}</a>' if i < len(trail) - 1 else f'<span aria-current="page">{esc(n)}</span>')
        for i, (n, l) in enumerate(trail))
    if p["kind"] == "hub":
        cards = "".join(f'<li class="guide-card"><a href="{href(x["slug"])}"><strong>{esc(x["h1"])}</strong><span>{esc(x["desc"])}</span></a></li>' for x in GUIDES)
        body = f'<ul class="guide-list">{cards}</ul>' + related_html(["us-llc-for-non-residents", "registered-agent", "virtual-business-address", "virtual-mailbox"])
    else:
        body = ""
        if p["kind"] == "state": body += facts_html(p)
        body += sections_html(p.get("sections") or p.get("body"))
        body += cta_html(p) + faq_html(p["faqs"]) + related_html(p["related"])
    updated = f'<p class="updated">Updated {FACT_DATE}</p>' if p["kind"] in ("guide", "state") else ""
    return f'''<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>{esc(p["title"])}</title>
  <meta name="description" content="{esc(p["desc"])}" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <link rel="canonical" href="{u}" />
  <link rel="alternate" hreflang="en-us" href="{u}" />
  <link rel="alternate" hreflang="x-default" href="{u}" />
  <link rel="manifest" href="/manifest.webmanifest" />
  <meta name="theme-color" content="#0f172a" />
  <link rel="icon" href="/favicon.ico" sizes="48x48" />
  <link rel="icon" href="/assets/icon.svg" type="image/svg+xml" />
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png" />
  <meta property="og:type" content="{"article" if p["kind"] == "guide" else "website"}" />
  <meta property="og:site_name" content="Virtual Office Space USA" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:title" content="{esc(p["title"])}" />
  <meta property="og:description" content="{esc(p["desc"])}" />
  <meta property="og:url" content="{u}" />
  <meta property="og:image" content="{B}/assets/og-image.png" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{esc(p["title"])}" />
  <meta name="twitter:description" content="{esc(p["desc"])}" />
  <meta name="twitter:image" content="{B}/assets/og-image.png" />
  <link rel="stylesheet" href="/styles.css" />
  <script type="application/ld+json">{schema(p)}</script>
</head>
<body>

{HEADER}

  <main id="main">
  <section class="page-hero" aria-labelledby="page-title">
    <div class="container narrow">
      <nav class="crumbs" aria-label="Breadcrumb">{crumb_html}</nav>
      <h1 id="page-title">{esc(p["h1"])}</h1>
      <p class="lead">{esc(p["lead"])}</p>
      {updated}
    </div>
  </section>
  <div class="container narrow prose">
{body}
  </div>

{modal_html()}
  </main>

{footer_html()}

  <script src="/script.js" defer></script>
</body>
</html>
'''

# ------------------------------------------------------------------ homepage hub
def popular_html():
    cols = "".join(f'<div class="popular-col"><h3>{esc(t)}</h3><ul>' + "".join(f'<li><a href="{h}">{esc(l)}</a></li>' for l, h in links) + "</ul></div>"
                   for t, links in POPULAR)
    return f'''  <!-- Popular Searches (keyword hub) -->
  <section id="popular-searches" class="section-alt" aria-labelledby="popular-searches-title">
    <div class="container">
      <div class="section-head">
        <div class="section-tag">Explore</div>
        <h2 id="popular-searches-title">Popular searches</h2>
        <p>Registered agents, virtual addresses and company setup guides by state.</p>
      </div>
      <div class="popular-grid">{cols}</div>
    </div>
  </section>
  <!-- /Popular Searches -->
'''

def update_homepage():
    p = os.path.join(ROOT, "index.html"); h = open(p).read()
    h = re.sub(r'  <!-- Popular Searches \(keyword hub\) -->.*?<!-- /Popular Searches -->\n\n?', '', h, flags=re.S)
    h = h.replace('  <!-- Interactive Lead Modal -->', popular_html() + '\n  <!-- Interactive Lead Modal -->', 1)
    # state cards: link to the state page
    for s in STATES:
        h = re.sub(rf'(<article class="state-card" id="{s["slug"]}".*?</ul>)(\s*)(?:<a class="state-link"[^>]*>.*?</a>\s*)?(<button)',
                   rf'\1\2<a class="state-link" href="{href(s["slug"])}">{s["name"]} registered agent, fees &amp; rules →</a>\2\3', h, count=1, flags=re.S)
    # nav: Guides link
    if '<li><a href="/guides/">Guides</a></li>' not in h:
        h = h.replace('<li><a href="#faq">FAQ</a></li>', '<li><a href="#faq">FAQ</a></li>\n        <li><a href="/guides/">Guides</a></li>', 1)
    # footer: replace with shared footer
    h = re.sub(r'  <footer aria-label="Site footer">.*?</footer>', footer_html(), h, count=1, flags=re.S)
    # schema: significantLink -> real pages
    m = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', h, re.S)
    d = json.loads(m.group(2))
    for n in d["@graph"]:
        if n.get("@id") == B + "/#webpage":
            n["significantLink"] = [url(s) for s in [x["slug"] for x in SERVICES] + [x["slug"] for x in STATES] + ["guides"]]
            n["dateModified"] = TODAY
        if n.get("@type") == "State":
            n["subjectOf"] = {"@id": url(n["@id"].split("#")[1]) + "#webpage"}
    js = json.dumps(d, separators=(",", ":"), ensure_ascii=False).replace("</", "<\\/")
    h = h[:m.start(2)] + js + h[m.end(2):]
    open(p, "w").write(h)

def write_sitemap():
    urls = [(B + "/", "1.0")] + [(url(s), "0.8") for s in [x["slug"] for x in SERVICES] + [x["slug"] for x in STATES]] + \
           [(url("guides"), "0.6")] + [(url(g["slug"]), "0.7") for g in GUIDES]
    items = "".join(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <priority>{pr}</priority>\n" +
                    ("    <image:image>\n      <image:loc>https://virtualofficespaceusa.online/assets/og-image.png</image:loc>\n    </image:image>\n" if u == B + "/" else "") +
                    "  </url>\n" for u, pr in urls)
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + items + "</urlset>\n")
    return len(urls)

def update_llms():
    p = os.path.join(ROOT, "llms.txt"); s = open(p).read()
    s = re.sub(r"\n## Pages by topic\n.*", "", s, flags=re.S).rstrip() + "\n\n## Pages by topic\n"
    for x in SERVICES + STATES + GUIDES:
        s += f'- [{x["h1"]}]({url(x["slug"])}): {x["desc"]}\n'
    open(p, "w").write(s)

if __name__ == "__main__":
    for slug, p in PAGES.items():
        d = os.path.join(ROOT, slug); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(page_html(p))
    update_homepage()
    n = write_sitemap(); update_llms()
    print(f"built {len(PAGES)} pages, sitemap {n} urls")

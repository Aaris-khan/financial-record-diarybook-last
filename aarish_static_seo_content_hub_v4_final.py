from pathlib import Path
from datetime import date, datetime
import shutil, hashlib, json, re, sys
import xml.etree.ElementTree as ET

PROJECT_DIR = Path("/root/file update")
SITE_URL = "https://aaris-khan.github.io/financial-record-diarybook-last/"
SITE_ROOT = SITE_URL.rstrip("/")
GITHUB_URL = "https://github.com/Aaris-khan/financial-record-diarybook-last"
GITHUB_PROFILE = "https://github.com/Aaris-khan"
OG_IMAGE_URL = f"{SITE_ROOT}/og-image.svg"
TODAY = date.today().isoformat()

APP_NAME = "Aarish Dairy Pro"
AUTHOR_NAME = "Aarish Khan"
AUTHOR_ALIASES = ["Aaris Khan", "Aaris-khan", "Aarish"]

CORE_SENTENCE = (
    "Aarish Dairy Pro is a free PWA for doodh hisab, milk record, "
    "credit book, udhar khata book, daily expenses, salary register, "
    "personal diary and small business ledger."
)

GLOBAL_SCOPE_SENTENCE = (
    "Aarish Dairy Pro is made for users across India and for Hindi or English-speaking "
    "users internationally who need a simple daily hisab kitab, milk record, credit book "
    "or business ledger app."
)

ALIASES = [
    "Aarish Dairy Pro",
    "Aarish Dairy",
    "Aarish Diary",
    "Aaris Dairy",
    "Aaris Diary",
    "Aarish Financial Diary",
    "Aaris Financial Diary",
    "Aarish Dairy Financial",
    "Aaris Dairy Financial",
    "Doodh Hisab App",
    "Doodh Ka Hisab",
    "Milk Record App",
    "Milk Record App India",
    "Dairy Hisab Kitab",
    "Dairy Ledger App",
    "Udhar Khata Book",
    "Udhar Bahi Khata",
    "Udhar Record App",
    "Khata Book App",
    "Credit Book App",
    "Credit Record App",
    "Hisab Kitab App",
    "Daily Ledger App",
    "Daily Expenses App",
    "Daily Kharcha App",
    "Salary Register App",
    "Business Record App",
    "Business Ledger App",
    "Financial Diary App",
    "Small Business Ledger App",
]

FEATURES = [
    "Doodh Hisab / Milk Record",
    "Credit Book / Udhar Khata Book",
    "Udhar Bahi Khata",
    "Daily Expenses / Daily Kharcha Record",
    "Salary Register",
    "Personal Diary",
    "Business Record / Small Business Ledger",
    "Offline-ready PWA experience",
]

NAV_PAGES = [
    ("Home", "index.html"),
    ("About", "about.html"),
    ("Doodh Hisab", "doodh-hisab.html"),
    ("Udhar Khata Book", "udhar-khata-book.html"),
    ("Hisab Kitab App", "hisab-kitab-app.html"),
    ("Milk Record App", "milk-record-app.html"),
]

STATIC_PAGES = [
    ("about.html", "weekly", "0.90"),
    ("doodh-hisab.html", "monthly", "0.85"),
    ("udhar-khata-book.html", "monthly", "0.85"),
    ("hisab-kitab-app.html", "monthly", "0.85"),
    ("milk-record-app.html", "monthly", "0.85"),
]

BANNED_REGIONAL_WORDS = ["Haryana", "Nuh-Mewat", "Nuh Mewat", "Palwal"]
BAD_TOKENS = ["${SITE_URL}", "${TODAY}", "YOUR-LIVE-WEBSITE", "Verified User", "Lorem ipsum", '"priceCurrency"', "priceCurrency", '"USD"', '"INR"']

STYLE = """
:root{
  color-scheme: dark;
  --bg:#030712;
  --card:#111827;
  --text:#f9fafb;
  --muted:#cbd5e1;
  --blue:#60a5fa;
  --border:rgba(255,255,255,.12);
}
*{box-sizing:border-box}
body{
  margin:0;
  padding:24px;
  font-family:Inter,Arial,sans-serif;
  background:
    radial-gradient(circle at 0% 0%, rgba(52,211,153,.12), transparent 35%),
    radial-gradient(circle at 100% 100%, rgba(96,165,250,.12), transparent 38%),
    var(--bg);
  color:var(--text);
  line-height:1.72;
}
main{max-width:920px;margin:auto}
.card{
  background:rgba(17,24,39,.92);
  border:1px solid var(--border);
  border-radius:26px;
  padding:24px;
  box-shadow:0 18px 60px rgba(0,0,0,.45);
}
h1{font-size:34px;line-height:1.15;margin:0 0 12px}
h2{font-size:23px;margin:30px 0 10px}
p{color:var(--muted);font-size:16px}
a{color:var(--blue);font-weight:800;text-decoration:none}
a:hover{text-decoration:underline}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0}
.chips span{
  padding:8px 12px;
  border-radius:999px;
  background:rgba(31,41,55,.95);
  border:1px solid var(--border);
  font-weight:800;
  color:#fff;
}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}
.box{
  background:rgba(31,41,55,.72);
  border:1px solid var(--border);
  border-radius:18px;
  padding:16px;
}
.small{font-size:14px;color:#94a3b8}
nav{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 24px}
nav a{
  background:rgba(96,165,250,.10);
  border:1px solid rgba(96,165,250,.25);
  border-radius:999px;
  padding:8px 12px;
}
ol,ul{color:var(--muted)}
strong{color:#fff}
footer{margin-top:28px;color:#94a3b8;font-size:13px}

/* AARISH_APP_OPEN_CTA_V2_START */
.aarish-app-open-cta{
  margin:18px 0 30px;
}
.aarish-app-open-cta-link{
  position:relative;
  display:grid;
  grid-template-columns:1fr 42px;
  gap:16px;
  align-items:center;
  width:100%;
  padding:22px 18px;
  border-radius:32px;
  overflow:hidden;
  text-decoration:none !important;
  color:#fff !important;
  background:
    radial-gradient(circle at 12% 0%, rgba(59,130,246,.40), transparent 34%),
    radial-gradient(circle at 96% 100%, rgba(16,185,129,.35), transparent 38%),
    linear-gradient(135deg, #050b14 0%, #0b1e3d 46%, #061f1d 100%);
  border:1px solid rgba(147,197,253,.52);
  box-shadow:
    0 0 0 1px rgba(255,255,255,.05) inset,
    0 22px 70px rgba(37,99,235,.34),
    0 14px 36px rgba(0,0,0,.50);
  transform:translateZ(0);
}
.aarish-app-open-cta-link::before{
  content:"";
  position:absolute;
  inset:-2px;
  background:linear-gradient(120deg, transparent 0%, rgba(255,255,255,.18) 42%, transparent 72%);
  transform:translateX(-130%);
  animation:aarishCtaShine 4.8s ease-in-out infinite;
  pointer-events:none;
}
.aarish-app-open-cta-link::after{
  content:"";
  position:absolute;
  inset:1px;
  border-radius:31px;
  pointer-events:none;
  background:
    linear-gradient(135deg, rgba(56,189,248,.18), transparent 32%),
    linear-gradient(315deg, rgba(16,185,129,.14), transparent 30%);
}
@keyframes aarishCtaShine{
  0%,55%{transform:translateX(-130%)}
  78%,100%{transform:translateX(130%)}
}
.aarish-app-open-content{
  position:relative;
  z-index:2;
  min-width:0;
  display:flex;
  flex-direction:column;
  align-items:flex-start;
}
.aarish-app-open-leaf-tile{
  width:76px;
  height:76px;
  border-radius:25px;
  display:flex;
  align-items:center;
  justify-content:center;
  margin:0 0 13px;
  background:
    radial-gradient(circle at 28% 20%, rgba(255,255,255,.32), transparent 35%),
    linear-gradient(135deg, #1e3a8a 0%, #2563eb 42%, #06b6d4 72%, #10b981 100%);
  box-shadow:
    0 18px 42px rgba(37,99,235,.38),
    0 0 0 1px rgba(255,255,255,.16) inset,
    0 0 32px rgba(34,211,238,.22);
}
.aarish-app-open-leaf-svg{
  width:43px;
  height:43px;
  display:block;
  filter:drop-shadow(0 8px 16px rgba(0,0,0,.22));
}
.aarish-app-open-kicker{
  font-size:12px;
  letter-spacing:.15em;
  text-transform:uppercase;
  color:#93c5fd;
  font-weight:950;
  margin-bottom:5px;
}
.aarish-app-open-title{
  font-size:27px;
  line-height:1.08;
  color:#fff;
  font-weight:1000;
  letter-spacing:-.02em;
}
.aarish-app-open-subtitle{
  margin-top:8px;
  max-width:650px;
  font-size:14.5px;
  line-height:1.42;
  color:#dbeafe;
  font-weight:750;
}
.aarish-app-open-arrow{
  position:relative;
  z-index:2;
  width:42px;
  height:42px;
  border-radius:999px;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:28px;
  font-weight:1000;
  background:rgba(255,255,255,.13);
  color:#fff;
  box-shadow:0 0 0 1px rgba(255,255,255,.14) inset;
}
.aarish-app-open-cta-link:focus-visible{
  outline:3px solid #93c5fd;
  outline-offset:4px;
}
@media(max-width:560px){
  .aarish-app-open-cta-link{
    grid-template-columns:1fr 34px;
    border-radius:26px;
    padding:18px 15px;
  }
  .aarish-app-open-leaf-tile{
    width:66px;
    height:66px;
    border-radius:22px;
    margin-bottom:12px;
  }
  .aarish-app-open-leaf-svg{
    width:38px;
    height:38px;
  }
  .aarish-app-open-title{
    font-size:22px;
  }
  .aarish-app-open-subtitle{
    font-size:12.8px;
  }
  .aarish-app-open-arrow{
    width:34px;
    height:34px;
    font-size:23px;
  }
}
/* AARISH_APP_OPEN_CTA_V2_END */

"""

def fail(msg):
    print("ERROR:", msg)
    sys.exit(1)

def ok(msg):
    print("✅", msg)

def read_text(path):
    return path.read_text(encoding="utf-8", errors="ignore")

def write_text(path, text):
    path.write_text(text.replace("\r\n", "\n").strip() + "\n", encoding="utf-8")

def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def backup_file(path, backup_dir):
    if path.exists():
        shutil.copy2(path, backup_dir / path.name)

def json_ld_script(data):
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + "\n</script>"

def author_schema():
    return {
        "@type": "Person",
        "name": AUTHOR_NAME,
        "alternateName": AUTHOR_ALIASES,
        "url": GITHUB_PROFILE,
        "sameAs": [GITHUB_PROFILE]
    }

def software_schema():
    return {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": APP_NAME,
        "alternateName": ALIASES,
        "url": SITE_URL,
        "description": CORE_SENTENCE + " " + GLOBAL_SCOPE_SENTENCE,
        "applicationCategory": "FinanceApplication",
        "operatingSystem": "Web, Android",
        "inLanguage": ["en", "hi"],
        "isAccessibleForFree": True,
        "featureList": FEATURES,
        "offers": {
            "@type": "Offer",
            "price": "0"
        },
        "author": author_schema()
    }

def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": APP_NAME,
        "alternateName": ALIASES[:15],
        "url": SITE_URL,
        "description": CORE_SENTENCE + " " + GLOBAL_SCOPE_SENTENCE,
        "publisher": author_schema(),
        "inLanguage": ["en", "hi"]
    }

def webpage_schema(filename, name, description, schema_type="WebPage"):
    url = SITE_URL if filename == "index.html" else f"{SITE_ROOT}/{filename}"
    return {
        "@context": "https://schema.org",
        "@type": schema_type,
        "name": name,
        "url": url,
        "description": description,
        "isPartOf": {"@type": "WebSite", "name": APP_NAME, "url": SITE_URL},
        "author": author_schema(),
        "inLanguage": ["en", "hi"]
    }

def breadcrumb_schema(filename, current_name):
    url = SITE_URL if filename == "index.html" else f"{SITE_ROOT}/{filename}"
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL},
            {"@type": "ListItem", "position": 2, "name": current_name, "item": url}
        ]
    }

def nav_html(current):
    links = []
    for label, href in NAV_PAGES:
        links.append(f'<a href="./{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>')
    return "<nav>\n" + "\n".join(links) + "\n</nav>"


def app_open_cta_html(filename):
    if filename == "index.html":
        return ""
    return """<!-- AARISH_APP_OPEN_CTA_V2_START -->
<section class="aarish-app-open-cta" aria-label="Open Aarish Dairy Pro main app">
  <a class="aarish-app-open-cta-link" href="./index.html" aria-label="Open Aarish Dairy Pro main app">
    <span class="aarish-app-open-content">
      <span class="aarish-app-open-leaf-tile" aria-hidden="true">
        <svg class="aarish-app-open-leaf-svg" viewBox="0 0 64 64" role="img" focusable="false">
          <path d="M52.8 9.2C38.2 10.4 25.9 16.1 18.9 25.1c-5.7 7.4-5.9 16.6-.4 22.1 5.7 5.7 15 5.4 22.6-.5C50.4 39.5 55.8 25.1 52.8 9.2Z" fill="#60a5fa"/>
          <path d="M12.2 51.8c11.8-3.7 21.6-11.5 29.5-25.1" fill="none" stroke="#a7f3d0" stroke-width="5.2" stroke-linecap="round"/>
          <path d="M25.2 44.8c-5.3-4.7-6.3-11.7-2.6-18.2-6.8 5.2-9.5 13.7-4.1 20.6 1.8 2.4 4.2 3.6 6.7 4.1Z" fill="#22d3ee" opacity=".95"/>
        </svg>
      </span>
      <span class="aarish-app-open-kicker">Premium Financial Hub</span>
      <span class="aarish-app-open-title">Open Aarish Dairy Pro</span>
      <span class="aarish-app-open-subtitle">Splash screen, Google sign-in aur main app yahin se open karein</span>
    </span>
    <span class="aarish-app-open-arrow" aria-hidden="true">&rarr;</span>
  </a>
</section>
<!-- AARISH_APP_OPEN_CTA_V2_END -->"""

def html_page(filename, title, desc, h1, body_html, schema_items):
    canonical = SITE_URL if filename == "index.html" else f"{SITE_ROOT}/{filename}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="{AUTHOR_NAME}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="{canonical}">
<link rel="manifest" href="./manifest.webmanifest">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{APP_NAME}">
<meta property="og:image" content="{OG_IMAGE_URL}">
<meta property="og:image:alt" content="Aarish Dairy Pro doodh hisab, credit book, udhar khata book and milk record app">
<meta property="og:image:type" content="image/svg+xml">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{OG_IMAGE_URL}">
<style>{STYLE}</style>
{json_ld_script(schema_items)}
</head>
<body>
<main>
<div class="card">
{nav_html(filename)}
{app_open_cta_html(filename)}
<h1>{h1}</h1>
{body_html}
<footer>
Last updated: {TODAY}. This page is part of the Aarish Dairy Pro public SEO/GEO content hub.
</footer>
</div>
</main>
</body>
</html>"""

def set_meta_tag(block, key_attr, key_value, content_value):
    pattern = re.compile(rf'<meta\s+{re.escape(key_attr)}="{re.escape(key_value)}"\s+content="[^"]*"\s*/?>', re.I)
    new_tag = f'<meta {key_attr}="{key_value}" content="{content_value}">'
    if pattern.search(block):
        return pattern.sub(new_tag, block, count=1)
    insert_at = block.find("<!-- AARISH_SEO_HEAD_CORE_V1_END -->")
    if insert_at < 0:
        fail("SEO END marker missing.")
    return block[:insert_at] + "    " + new_tag + "\n" + block[insert_at:]

def ensure_manifest_link(block):
    if 'rel="manifest"' in block or "rel='manifest'" in block:
        return block
    insert_at = block.find("<!-- AARISH_SEO_HEAD_CORE_V1_END -->")
    if insert_at < 0:
        fail("SEO END marker missing for manifest.")
    return block[:insert_at] + '    <link rel="manifest" href="manifest.webmanifest">\n' + block[insert_at:]

def update_index_html(index_path, old_index):
    s = old_index
    s = re.sub(r'<html\s+lang="[^"]*"', '<html lang="en"', s, count=1)

    start_marker = "<!-- AARISH_SEO_HEAD_CORE_V1_START -->"
    end_marker = "<!-- AARISH_SEO_HEAD_CORE_V1_END -->"
    start = s.find(start_marker)
    end = s.find(end_marker)
    if start < 0 or end < 0 or end <= start:
        fail("index.html SEO marker range not found.")
    end += len(end_marker)

    before = s[:start]
    block = s[start:end]
    after = s[end:]

    title_new = "Aarish Dairy Pro — Doodh Hisab, Credit Book, Udhar Khata Book & Business Ledger"
    desc_new = "Aarish Dairy Pro is a free PWA for doodh hisab, milk record, credit book, udhar khata book, daily expenses, salary register, personal diary and small business ledger."

    before = re.sub(r"<title>.*?</title>", f"<title>{title_new}</title>", before, count=1, flags=re.S)

    block = set_meta_tag(block, "name", "description", desc_new)
    block = set_meta_tag(block, "name", "author", AUTHOR_NAME)
    block = set_meta_tag(block, "property", "og:title", title_new)
    block = set_meta_tag(block, "property", "og:description", desc_new)
    block = set_meta_tag(block, "property", "og:image", OG_IMAGE_URL)
    block = set_meta_tag(block, "property", "og:image:alt", "Aarish Dairy Pro doodh hisab, credit book, udhar khata book and milk record app")
    block = set_meta_tag(block, "property", "og:image:type", "image/svg+xml")
    block = set_meta_tag(block, "name", "twitter:card", "summary_large_image")
    block = set_meta_tag(block, "name", "twitter:title", title_new)
    block = set_meta_tag(block, "name", "twitter:description", desc_new)
    block = set_meta_tag(block, "name", "twitter:image", OG_IMAGE_URL)
    block = ensure_manifest_link(block)

    block = re.sub(r'\n?\s*<meta\s+property="og:locale"\s+content="[^"]*"\s*/?>\s*', "\n", block, count=1, flags=re.I)

    script_pat = re.compile(r'(<script type="application/ld\+json">\s*)(\{.*?\})(\s*</script>)', re.S)
    m = script_pat.search(block)
    if not m:
        fail("index.html JSON-LD block not found inside SEO marker.")

    try:
        data = json.loads(m.group(2))
    except Exception as e:
        fail("index.html JSON-LD parse failed: " + str(e))

    data.clear()
    data.update(software_schema())
    data["@type"] = "WebApplication"

    new_json = json.dumps(data, ensure_ascii=False, indent=2)
    block = block[:m.start()] + m.group(1) + "\n" + new_json + "\n    " + m.group(3) + block[m.end():]

    new_s = before + block + after
    index_path.write_text(new_s, encoding="utf-8")
    return new_s

if not PROJECT_DIR.exists():
    fail("/root/file update folder nahi mila.")

if Path.cwd().resolve() != PROJECT_DIR.resolve():
    fail("Galat folder. Pehle run karo: cd '/root/file update'")

required_files = ["index.html", "style.css", "about.html", "robots.txt", "sitemap.xml"]
missing = [x for x in required_files if not (PROJECT_DIR / x).exists()]
if missing:
    fail("Required files missing: " + ", ".join(missing))

index_path = PROJECT_DIR / "index.html"
style_path = PROJECT_DIR / "style.css"
robots_path = PROJECT_DIR / "robots.txt"
sitemap_path = PROJECT_DIR / "sitemap.xml"

old_index = read_text(index_path)
if "<!DOCTYPE html>" not in old_index[:300]:
    fail("index.html valid start nahi lag raha.")
if "AARISH_SEO_HEAD_CORE_V1_START" not in old_index or "AARISH_SEO_HEAD_CORE_V1_END" not in old_index:
    fail("index.html SEO markers missing.")
if SITE_URL not in old_index:
    fail("index.html me expected live SITE_URL missing hai.")

google_files = sorted(PROJECT_DIR.glob("google*.html"))
readonly_files = [style_path] + google_files
before_hash = {str(p): sha256_file(p) for p in readonly_files if p.exists()}

ts = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_dir = PROJECT_DIR / f"SEO_HUB_BACKUP_BEFORE_V4_FINAL_{ts}"
backup_dir.mkdir(exist_ok=True)

backup_names = [
    "index.html", "style.css", "about.html", "sitemap.xml", "robots.txt",
    "README.md", "llms.txt", "doodh-hisab.html", "udhar-khata-book.html",
    "hisab-kitab-app.html", "milk-record-app.html", "og-image.svg", "manifest.webmanifest"
]
for name in backup_names:
    backup_file(PROJECT_DIR / name, backup_dir)
for gf in google_files:
    backup_file(gf, backup_dir)

ok("Backup created: " + backup_dir.name)

og_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#020617"/><stop offset="50%" stop-color="#0f172a"/><stop offset="100%" stop-color="#001b2e"/></linearGradient>
<radialGradient id="glow" cx="25%" cy="15%" r="65%"><stop offset="0%" stop-color="#34d399" stop-opacity="0.35"/><stop offset="100%" stop-color="#34d399" stop-opacity="0"/></radialGradient>
<radialGradient id="glow2" cx="90%" cy="90%" r="70%"><stop offset="0%" stop-color="#60a5fa" stop-opacity="0.38"/><stop offset="100%" stop-color="#60a5fa" stop-opacity="0"/></radialGradient>
</defs>
<rect width="1200" height="630" fill="url(#bg)"/>
<rect width="1200" height="630" fill="url(#glow)"/>
<rect width="1200" height="630" fill="url(#glow2)"/>
<rect x="70" y="70" width="1060" height="490" rx="42" fill="#111827" opacity="0.88" stroke="rgba(255,255,255,0.16)"/>
<circle cx="150" cy="150" r="52" fill="#1d4ed8" opacity="0.95"/>
<text x="225" y="155" fill="#f8fafc" font-size="56" font-family="Arial, sans-serif" font-weight="800">Aarish Dairy Pro</text>
<text x="225" y="220" fill="#93c5fd" font-size="28" font-family="Arial, sans-serif" font-weight="700">Doodh Hisab • Credit Book • Milk Record</text>
<text x="90" y="335" fill="#f8fafc" font-size="42" font-family="Arial, sans-serif" font-weight="800">Free PWA for daily hisab kitab</text>
<text x="90" y="400" fill="#cbd5e1" font-size="28" font-family="Arial, sans-serif">Milk records, credit book, daily expenses, salary and business ledger.</text>
<text x="90" y="485" fill="#34d399" font-size="26" font-family="Arial, sans-serif" font-weight="700">aaris-khan.github.io/financial-record-diarybook-last/</text>
</svg>"""

manifest = {
    "name": "Aarish Dairy Pro - Doodh Hisab, Credit Book, Milk Record & Business Ledger",
    "short_name": "Aarish Dairy",
    "description": CORE_SENTENCE + " " + GLOBAL_SCOPE_SENTENCE,
    "start_url": "./",
    "scope": "./",
    "display": "standalone",
    "background_color": "#030712",
    "theme_color": "#0f172a",
    "orientation": "portrait",
    "lang": "en",
    "categories": ["finance", "business", "productivity"]
}

alias_chips = "\n".join(f"<span>{a}</span>" for a in ALIASES)
feature_boxes = "\n".join(f"<div class='box'><strong>{f}</strong><p class='small'>Aarish Dairy Pro keeps this feature simple for daily mobile use.</p></div>" for f in FEATURES)

about_schema = [
    webpage_schema("about.html", "About Aarish Dairy Pro", CORE_SENTENCE, "AboutPage"),
    breadcrumb_schema("about.html", "About Aarish Dairy Pro"),
    website_schema(),
    software_schema(),
    {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "What is Aarish Dairy Pro?", "acceptedAnswer": {"@type": "Answer", "text": CORE_SENTENCE}},
            {"@type": "Question", "name": "Is Aarish Dairy Pro also searched as Aarish Diary or Aaris Financial Diary?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Some users search for Aarish Dairy Pro as Aarish Diary, Aaris Dairy, Aarish Financial Diary, Aaris Financial Diary, Doodh Hisab App, Milk Record App, Credit Book App, Udhar Khata Book, Udhar Bahi Khata or Hisab Kitab App."}},
            {"@type": "Question", "name": "Can I use Aarish Dairy Pro outside India?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Aarish Dairy Pro can be used by anyone worldwide who wants to track milk records, credit book or udhar-style records, daily expenses, salary and business ledger in a simple diary app."}},
            {"@type": "Question", "name": "Who can use Aarish Dairy Pro?", "acceptedAnswer": {"@type": "Answer", "text": "Aarish Dairy Pro is made for small dairy owners, milk sellers, local shopkeepers and small business users who need a simple digital hisab kitab app."}},
            {"@type": "Question", "name": "Does Google index private app records?", "acceptedAnswer": {"@type": "Answer", "text": "No. Public pages like the homepage and about page can be indexed, but user records inside login such as milk entries, credit records, diary notes and salary records are private app data."}}
        ]
    }
]

about_body = f"""
<p><strong>{CORE_SENTENCE}</strong></p>

<section>
<h2>What is Aarish Dairy Pro?</h2>
<p>Aarish Dairy Pro is a mobile-first financial diary and business record app. It helps users keep daily milk collection, credit book records, udhar records, expenses, salary, personal diary notes and business ledger in one secure PWA.</p>
<p>यह ऐप दूध हिसाब, उधार खाता, रोज़ का खर्चा, तनख्वाह और छोटा बिजनेस रिकॉर्ड एक जगह रखने के लिए बनाया गया है।</p>
</section>

<section>
<h2>Also searched as</h2>
<p>People may search this app with different names and spellings. These names refer to the same Aarish Dairy Pro app and help users find the right tool without keyword stuffing.</p>
<div class="chips">
{alias_chips}
</div>
</section>

<section>
<h2>India and international use</h2>
<p>{GLOBAL_SCOPE_SENTENCE}</p>
<p>The app uses English with Hindi support so both Indian users and international users who understand Hindi or English can use it for simple record keeping.</p>
</section>

<section>
<h2>Who is this app for?</h2>
<div class="grid">
<div class="box"><strong>Small dairy owners</strong><p>Track daily doodh hisab, milk quantity, rates and customer records.</p></div>
<div class="box"><strong>Milk sellers</strong><p>Maintain milk record and monthly hisab without relying only on paper diary.</p></div>
<div class="box"><strong>Shopkeepers</strong><p>Use credit book, udhar khata book, udhar bahi khata and daily expenses record in one place.</p></div>
<div class="box"><strong>Small businesses</strong><p>Keep salary register, business ledger and personal diary records together.</p></div>
</div>
</section>

<section>
<h2>How it works</h2>
<ol>
<li>Add a customer, employee, category or business profile.</li>
<li>Record daily milk, credit book, udhar, expenses, salary or diary entry.</li>
<li>The app keeps monthly hisab and business records organized.</li>
<li>Use export/share features when you need to save or send records.</li>
</ol>
</section>

<section>
<h2>Features</h2>
<div class="grid">
{feature_boxes}
</div>
</section>

<section>
<h2>Helpful feature pages</h2>
<ul>
<li><a href="./doodh-hisab.html">Doodh Hisab App</a> — daily milk hisab and dairy record guide.</li>
<li><a href="./udhar-khata-book.html">Udhar Khata Book</a> — credit book, udhar, lena-dena and customer record guide.</li>
<li><a href="./hisab-kitab-app.html">Hisab Kitab App</a> — daily expenses, salary and business ledger guide.</li>
<li><a href="./milk-record-app.html">Milk Record App</a> — milk collection and monthly record guide.</li>
</ul>
</section>

<section>
<h2>Genuine changelog</h2>
<ul>
<li><strong>{TODAY}:</strong> Public SEO/GEO content hub V4 added with neutral free-app schema, India + international scope, worldwide-use FAQ and generic English aliases.</li>
<li><strong>2026-06-30:</strong> Google Search Console verification, robots.txt and sitemap.xml setup completed.</li>
<li><strong>Current app:</strong> Aarish Dairy Pro runs as a mobile-first PWA with Firebase login and offline-ready financial diary features.</li>
</ul>
</section>

<p><a href="./index.html">Open Aarish Dairy Pro</a></p>
"""

about_html = html_page(
    "about.html",
    "About Aarish Dairy Pro — Doodh Hisab, Credit Book & Business Ledger",
    "Learn about Aarish Dairy Pro, a free PWA for doodh hisab, milk record, credit book, udhar khata book, hisab kitab, salary register and business ledger.",
    "About Aarish Dairy Pro",
    about_body,
    about_schema
)

landing_pages = {
    "doodh-hisab.html": {
        "title": "Doodh Hisab App — Daily Milk Record & Dairy Ledger",
        "desc": "Aarish Dairy Pro helps small dairy owners keep daily doodh hisab, milk record, customer record and monthly dairy ledger in one PWA.",
        "h1": "Doodh Hisab App for Daily Milk Records",
        "body": """
<p><strong>Aarish Dairy Pro is a free doodh hisab app for keeping daily milk records, customer entries and monthly dairy hisab in one place.</strong></p>
<section><h2>Why doodh hisab needs a digital record</h2><p>Many dairy sellers still keep milk records in a paper diary. Paper records can be lost, damaged or hard to calculate at month end. Aarish Dairy Pro gives a simple digital way to record daily milk quantity, rate and customer details.</p><p>This page helps users who search for doodh hisab, doodh ka hisab, dairy hisab kitab, milk record app or daily milk collection record.</p></section>
<section><h2>India and international use</h2><p>Aarish Dairy Pro can be used across India and internationally by Hindi or English-speaking users who need a simple dairy record, milk record or daily hisab app.</p></section>
<section><h2>How Aarish Dairy Pro helps</h2><ul><li>Add milk customers and keep customer-wise records.</li><li>Record daily milk quantity and rate.</li><li>Check monthly milk hisab in a clean mobile interface.</li><li>Use the same app with credit book, udhar khata book, expenses and salary register.</li></ul></section>
<section><h2>Related pages</h2><p><a href="./milk-record-app.html">Milk Record App</a> · <a href="./udhar-khata-book.html">Udhar Khata Book</a> · <a href="./about.html">About Aarish Dairy Pro</a></p></section>
"""
    },
    "udhar-khata-book.html": {
        "title": "Udhar Khata Book App — Credit Book & Udhar Bahi Khata",
        "desc": "Use Aarish Dairy Pro as a credit book and udhar khata book app for customer credit records, udhar bahi khata, lena-dena and small business hisab.",
        "h1": "Credit Book and Udhar Khata Book for Customer Records",
        "body": """
<p><strong>Aarish Dairy Pro works as a credit book and udhar khata book app for recording customer udhar, lena-dena and small business credit records.</strong></p>
<section><h2>Digital credit book and udhar bahi khata</h2><p>A paper udhar bahi can become confusing when many customers have daily entries. Aarish Dairy Pro helps keep credit book records, udhar records, bahi khata, khata book and customer credit details organized on mobile.</p><p>Users may search for this feature as credit book app, udhar khata book, udhar bahi khata, udhar record app, khata book app, customer credit record or lena dena diary.</p></section>
<section><h2>India and international use</h2><p>The app supports Indian udhar-style hisab and broader international credit book style record keeping for small businesses and local shops.</p></section>
<section><h2>What you can track</h2><ul><li>Customer-wise credit and udhar entries.</li><li>Credit and payment style records.</li><li>Daily business hisab with related expenses and salary records.</li><li>Simple mobile access from the same Aarish Dairy Pro app.</li></ul></section>
<section><h2>Related pages</h2><p><a href="./hisab-kitab-app.html">Hisab Kitab App</a> · <a href="./doodh-hisab.html">Doodh Hisab App</a> · <a href="./about.html">About Aarish Dairy Pro</a></p></section>
"""
    },
    "hisab-kitab-app.html": {
        "title": "Hisab Kitab App — Daily Expenses, Salary & Business Ledger",
        "desc": "Aarish Dairy Pro is a hisab kitab app for daily expenses, salary register, personal diary, business ledger, doodh hisab and credit records.",
        "h1": "Hisab Kitab App for Small Business Records",
        "body": """
<p><strong>Aarish Dairy Pro is a hisab kitab app for daily expenses, salary register, personal diary, business ledger, doodh hisab and credit records.</strong></p>
<section><h2>One app for daily financial diary</h2><p>Small businesses often manage different records in different notebooks: one for expenses, one for credit or udhar, one for salary and one for diary notes. Aarish Dairy Pro brings these daily hisab kitab records into one mobile-first PWA.</p><p>This page is helpful for people searching for hisab kitab app, daily expenses app, daily kharcha record, financial diary app, business ledger app, salary register app or local business record app.</p></section>
<section><h2>India and international use</h2><p>Aarish Dairy Pro is simple enough for Indian hisab kitab users and flexible enough for international users who need a daily ledger, credit book or small business record app.</p></section>
<section><h2>Main use cases</h2><ul><li>Track daily expenses and business expenses.</li><li>Keep salary register records for employees or workers.</li><li>Save personal diary notes with business context.</li><li>Use the same app for milk record and credit book.</li></ul></section>
<section><h2>Related pages</h2><p><a href="./udhar-khata-book.html">Udhar Khata Book</a> · <a href="./milk-record-app.html">Milk Record App</a> · <a href="./about.html">About Aarish Dairy Pro</a></p></section>
"""
    },
    "milk-record-app.html": {
        "title": "Milk Record App — Dairy Collection & Monthly Hisab",
        "desc": "Aarish Dairy Pro is a milk record app for daily milk collection, dairy customer records, monthly hisab and small dairy business tracking.",
        "h1": "Milk Record App for Dairy Collection and Monthly Hisab",
        "body": """
<p><strong>Aarish Dairy Pro is a milk record app for daily milk collection, dairy customer records, monthly hisab and small dairy business tracking.</strong></p>
<section><h2>Daily milk collection record</h2><p>A milk record app should be simple, fast and mobile-friendly. Aarish Dairy Pro is made for small dairy and milk selling users who want to keep customer-wise milk records and business hisab without complicated accounting software.</p><p>This page naturally connects searches like milk record app, milk collection record, dairy ledger app, milk hisab app, doodh hisab app and dairy business record app.</p></section>
<section><h2>India and international use</h2><p>The app can be used by dairy users in India and by international users who need a simple milk record, daily ledger or small business diary app.</p></section>
<section><h2>Why use Aarish Dairy Pro?</h2><ul><li>It keeps milk records together with credit book, expenses and salary features.</li><li>It is designed for English with Hindi support for daily hisab use.</li><li>It works as a PWA, so users can open it from mobile browser or install-like shortcut.</li><li>It keeps public marketing pages separate from private login data.</li></ul></section>
<section><h2>Related pages</h2><p><a href="./doodh-hisab.html">Doodh Hisab App</a> · <a href="./hisab-kitab-app.html">Hisab Kitab App</a> · <a href="./about.html">About Aarish Dairy Pro</a></p></section>
"""
    }
}

landing_html = {}
for filename, info in landing_pages.items():
    schema_items = [webpage_schema(filename, info["h1"], info["desc"], "Article"), breadcrumb_schema(filename, info["h1"])]
    landing_html[filename] = html_page(filename, info["title"], info["desc"], info["h1"], info["body"], schema_items)

readme = f"""# Aarish Dairy Pro

**{CORE_SENTENCE}**

{GLOBAL_SCOPE_SENTENCE}

Aarish Dairy Pro is a mobile-first web app for users who need a simple digital way to keep doodh hisab, milk record, credit book, udhar khata book, daily expenses, salary register, diary notes and business ledger.

## Live Website

{SITE_URL}

## Main Features

- Doodh Hisab / Milk Record
- Credit Book / Udhar Khata Book / Udhar Bahi Khata
- Daily Expenses / Daily Kharcha Record
- Salary Register
- Personal Diary
- Business Record / Small Business Ledger
- Offline-ready PWA experience

## Also searched as

{", ".join(ALIASES)}

## Public SEO Pages

- {SITE_ROOT}/about.html
- {SITE_ROOT}/doodh-hisab.html
- {SITE_ROOT}/udhar-khata-book.html
- {SITE_ROOT}/hisab-kitab-app.html
- {SITE_ROOT}/milk-record-app.html

## Author / Entity

Author: {AUTHOR_NAME}  
GitHub: {GITHUB_PROFILE}

## Private Data Note

Public pages explain the app features. User records inside the login area, such as milk entries, credit records, salary records and diary notes, are private app data and are not public SEO content.

## Repository

{GITHUB_URL}
"""

llms = f"""# Aarish Dairy Pro

{CORE_SENTENCE}

{GLOBAL_SCOPE_SENTENCE}

Live site:
{SITE_URL}

Canonical entity:
Aarish Dairy Pro

Author:
{AUTHOR_NAME} ({GITHUB_PROFILE})

Also known as:
{", ".join(ALIASES)}

What it does:
Aarish Dairy Pro helps small dairy owners, milk sellers, local shopkeepers and small business users keep doodh hisab, milk record, credit book, udhar khata book, daily expenses, salary register, personal diary and business ledger in one mobile-first PWA.

Important pages:
- {SITE_ROOT}/
- {SITE_ROOT}/about.html
- {SITE_ROOT}/doodh-hisab.html
- {SITE_ROOT}/udhar-khata-book.html
- {SITE_ROOT}/hisab-kitab-app.html
- {SITE_ROOT}/milk-record-app.html

Private data:
User records inside the login area are private app data. Public crawlers should use the public pages above to understand the app.
"""

robots = f"""User-agent: *
Allow: /

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: {SITE_ROOT}/sitemap.xml
"""

sitemap_urls = [("", "weekly", "1.0")] + STATIC_PAGES
sitemap_parts = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', ""]
for path, freq, priority in sitemap_urls:
    loc = SITE_URL if not path else f"{SITE_ROOT}/{path}"
    sitemap_parts.extend(["<url>", f"<loc>{loc}</loc>", f"<lastmod>{TODAY}</lastmod>", f"<changefreq>{freq}</changefreq>", f"<priority>{priority}</priority>", "</url>", ""])
sitemap_parts.append("</urlset>")
sitemap_xml = "\n".join(sitemap_parts)

new_index = update_index_html(index_path, old_index)

write_text(PROJECT_DIR / "about.html", about_html)
write_text(PROJECT_DIR / "sitemap.xml", sitemap_xml)
write_text(PROJECT_DIR / "robots.txt", robots)
write_text(PROJECT_DIR / "README.md", readme)
write_text(PROJECT_DIR / "llms.txt", llms)
write_text(PROJECT_DIR / "og-image.svg", og_svg)
write_text(PROJECT_DIR / "manifest.webmanifest", json.dumps(manifest, ensure_ascii=False, indent=2))
for filename, html in landing_html.items():
    write_text(PROJECT_DIR / filename, html)

after_hash = {str(p): sha256_file(p) for p in readonly_files if p.exists()}
for key, old_hash in before_hash.items():
    if after_hash.get(key) != old_hash:
        fail(f"READ-ONLY FILE CHANGED unexpectedly: {Path(key).name}")

old_norm = re.sub(r'<html\s+lang="[^"]*"', '<html lang="en"', old_index, count=1)
old_norm = re.sub(r"<title>.*?</title>", "<title>__TITLE__</title>", old_norm, count=1, flags=re.S)
new_norm = re.sub(r"<title>.*?</title>", "<title>__TITLE__</title>", new_index, count=1, flags=re.S)

def strip_seo(txt):
    sm = "<!-- AARISH_SEO_HEAD_CORE_V1_START -->"
    em = "<!-- AARISH_SEO_HEAD_CORE_V1_END -->"
    a = txt.find(sm)
    b = txt.find(em)
    if a < 0 or b < 0:
        fail("SEO marker strip failed.")
    b += len(em)
    return txt[:a] + "__SEO_BLOCK__" + txt[b:]

if strip_seo(old_norm) != strip_seo(new_norm):
    fail("index.html changed outside allowed lang/title/SEO marker areas.")

files = ["index.html", "about.html", "sitemap.xml", "robots.txt", "README.md", "llms.txt", "og-image.svg", "manifest.webmanifest"] + list(landing_html.keys())
for name in files:
    p = PROJECT_DIR / name
    if not p.exists() or p.stat().st_size < 120:
        fail(f"{name} missing/suspiciously small.")

for name in files:
    txt = read_text(PROJECT_DIR / name)
    for token in BAD_TOKENS:
        if token in txt:
            fail(f"{name} has bad token: {token}")
    for regional in BANNED_REGIONAL_WORDS:
        if regional in txt:
            fail(f"{name} still has region-lock word: {regional}")

ET.fromstring(read_text(sitemap_path))
sitemap_text = read_text(sitemap_path)
for url in [SITE_URL, f"{SITE_ROOT}/about.html", f"{SITE_ROOT}/doodh-hisab.html", f"{SITE_ROOT}/udhar-khata-book.html", f"{SITE_ROOT}/hisab-kitab-app.html", f"{SITE_ROOT}/milk-record-app.html"]:
    if f"<loc>{url}</loc>" not in sitemap_text:
        fail("sitemap missing URL: " + url)

checks = {
    "no priceCurrency in index": "priceCurrency" not in read_text(index_path),
    "no USD in generated SEO": '"USD"' not in read_text(index_path) and '"USD"' not in read_text(PROJECT_DIR / "about.html"),
    "global scope in about": "India and international use" in read_text(PROJECT_DIR / "about.html"),
    "worldwide FAQ": "Can I use Aarish Dairy Pro outside India?" in read_text(PROJECT_DIR / "about.html"),
    "Credit Book alias": "Credit Book App" in read_text(PROJECT_DIR / "about.html"),
    "Daily Ledger alias": "Daily Ledger App" in read_text(PROJECT_DIR / "about.html"),
    "Business Record alias": "Business Record App" in read_text(PROJECT_DIR / "about.html"),
    "Milk Record App India alias kept": "Milk Record App India" in read_text(PROJECT_DIR / "about.html"),
    "index html lang neutral": '<html lang="en">' in read_text(index_path),
    "manifest lang neutral": '"lang": "en"' in read_text(PROJECT_DIR / "manifest.webmanifest"),
    "README global": "international" in read_text(PROJECT_DIR / "README.md"),
    "llms global": "international" in read_text(PROJECT_DIR / "llms.txt"),
    "robots GPTBot": "User-agent: GPTBot" in read_text(robots_path),
    "robots OAI": "User-agent: OAI-SearchBot" in read_text(robots_path),
}

failed = [k for k, v in checks.items() if not v]
if failed:
    fail("Validation checks failed: " + ", ".join(failed))

ok("style.css untouched")
if google_files:
    ok("Google verification file untouched")
ok("index.html changed only in allowed SEO areas")
ok("priceCurrency removed; no USD/INR currency lock in SEO schema")
ok("regional Haryana/Nuh-Mewat/Palwal scope removed")
ok("India + international scope added")
ok("worldwide FAQ added")
ok("Milk Record App India kept only as alias")
ok("about + landing pages + README + llms + sitemap + robots + manifest updated")

print("")
print("✅ AARISH_STATIC_SEO_CONTENT_HUB_V4_FINAL COMPLETE")
print("Backup folder:", backup_dir.name)
print("")
print("Files to add/push:")
for name in ["index.html", "about.html", "robots.txt", "sitemap.xml", "README.md", "llms.txt", "og-image.svg", "manifest.webmanifest", "doodh-hisab.html", "udhar-khata-book.html", "hisab-kitab-app.html", "milk-record-app.html"]:
    print(" -", name)

print("")
print("Safe git command:")
print("git add index.html about.html robots.txt sitemap.xml README.md llms.txt og-image.svg manifest.webmanifest doodh-hisab.html udhar-khata-book.html hisab-kitab-app.html milk-record-app.html")
print('git commit -m "Add final global SEO GEO content hub"')
print("git push origin main")

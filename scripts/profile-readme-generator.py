#!/usr/bin/env python3
"""
Profile README Generator — perfil de GitHub para meatxsucks

Genera dark_mode.svg / light_mode.svg con ASCII art desde tu foto
y estadísticas reales de GitHub.

Uso: python3 scripts/profile-readme-generator.py
"""

from datetime import datetime

# ====================== CONFIGURA TUS DATOS ======================
USERNAME = "meatxsucks"
ROLE = "Senior Data Engineer"
TAGLINE = "Data Pipelines · Cloud · AI · Automation"

LANGUAGES_PROG = ["Python", "SQL", "AWS Glue", "Apache NiFi", "Amazon Redshift", "Snowflake", "GCP"]
LANGUAGES_SPOKEN = ["Español", "Inglés"]
HOBBIES = "Guitar, Bass, Gaming, Code"
IDE_TOOLS = ["VS Code", "Cursor", "AWS", "Snowflake", "GitLab"]
OS = "macOS · Linux"
LOCATION = "Santiago, Chile"
FOCUS = "Data Architecture / Datasharing @ Cencosud"

EMAIL = "matiascruzd14@gmail.com"
LINKEDIN = ""
GITHUB_URL = f"https://github.com/{USERNAME}"
# =================================================================

# ASCII art generado desde tu foto con photo-to-ascii.py (ancho=38)
ART = r"""
+++++++++++++++**???%??%??************
+++++++++++++?S###@@@@@@@@#?**********
+++++++++++?S@@@@@##@@@@@@@@#%********
++++++++++%@@@#S?+++**?SS#@@@@S*******
+++++++++%#@#?+;;::;;+++*?%S@@%*******
+++++++;+##S%++;;;;;+++***?%S@********
+++++++;+SS%*++***++++*++**?%#********
+++++++++%?*+*?%SSSS%????%%SSS********
+++++++?***++*%SSSSS%*?S#####?+*******
++++++++*?*+;;;*?%?++;*S####S*+*******
+++++++++**++;;;;+++;;*%??%%?+********
+++++++++%?**+++*??**+*%?**??+********
++++++++*#S?**?%S%?S#S##S%%%?+********
+++++++++S@S??%#S%%%SS##@SSS**********
+++++++++?@@#S#%**?%SSSS###%**********
++++***+++%@@@@S?**?%S%S@@%***********
*?%S##%+;+*%#@@@@######@@S?**********?
#######S?++*?S#@@@@@@@@@@@@@#S%?***???
#########S%**?%SS####SS@@@@@@@@@#S????
##########@#S%%%SSSSSS#@@@@@@@@@@@@S??
"""

# Actualizado 2026-10-19 desde la API de GitHub
STATS = {
    "repos": "17",
    "stars": "5",
    "commits": "—",
    "followers": "4",
    "following": "12",
    "since": "2018",
}

PALETTES = {
    "dark": {
        "bg": "#0d1117",
        "border": "#30363d",
        "art": "#8b949e",
        "h": "#58a6ff",
        "k": "#ffa657",
        "v": "#c9d1d9",
        "d": "#484f58",
        "g": "#3fb950",
        "r": "#f85149",
        "c": "#39c5cf",
    },
    "light": {
        "bg": "#ffffff",
        "border": "#d0d7de",
        "art": "#57606a",
        "h": "#0969da",
        "k": "#953800",
        "v": "#24292f",
        "d": "#afb8c1",
        "g": "#1a7f37",
        "r": "#cf222e",
        "c": "#1b7c83",
    },
}

W = 56  # ancho de la columna de info (en caracteres)


def kv(key, val, width=W):
    dots = "." * max(width - len(key) - len(str(val)) - 3, 1)
    return [(f"{key}: ", "k"), (dots + " ", "d"), (str(val), "v")]


def kv2(k1, v1, k2, v2):
    left = kv(k1, v1, 30)
    return left + [(" | ", "d")] + kv(k2, v2, 23)


def rule(title=""):
    label = f"─ {title} " if title else ""
    return [(label, "h"), ("─" * (W - len(label)), "d")]


def build_info_lines():
    return [
        [(f"{USERNAME.lower()}@github ", "h"), ("─" * (W - len(USERNAME) - 8), "d")],
        [],
        kv("ROLE", ROLE),
        kv("FOCUS", FOCUS),
        kv("LOCATION", LOCATION),
        kv("OS", OS),
        [],
        kv("Languages.Programming", ", ".join(LANGUAGES_PROG) or "—"),
        kv("Languages.Spoken", ", ".join(LANGUAGES_SPOKEN) or "—"),
        kv("Hobbies", HOBBIES or "—"),
        kv("IDE/Tools", ", ".join(IDE_TOOLS) or "—"),
        [],
        rule("Contact"),
        kv("Email", EMAIL or "—"),
        kv("LinkedIn", LINKEDIN or "—"),
        [],
        rule("GitHub Stats"),
        kv2("Repos", STATS["repos"], "Stars", STATS["stars"]),
        kv2("Commits", STATS["commits"], "Followers", STATS["followers"]),
        kv2("Following", STATS["following"], "Member since", STATS["since"]),
    ]


def html_escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(mode):
    p = PALETTES[mode]
    lines = ART.strip("\n").split("\n")
    info = build_info_lines()

    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="840" height="560" viewBox="0 0 840 560" '
        f'font-family="Consolas, Menlo, monospace" font-size="13px">',
        f'<rect x="0.5" y="0.5" width="839" height="559" rx="10" fill="{p["bg"]}" stroke="{p["border"]}"/>',
    ]
    for i, line in enumerate(lines):
        out.append(
            f'<text x="25" y="{40 + i * 15}" fill="{p["art"]}" xml:space="preserve">'
            f"{html_escape(line)}</text>"
        )
    for i, segs in enumerate(info):
        if not segs:
            continue
        spans = "".join(
            f'<tspan fill="{p[c]}">{html_escape(t)}</tspan>' for t, c in segs
        )
        out.append(f'<text x="390" y="{45 + i * 21}" xml:space="preserve">{spans}</text>')
    out.append("</svg>")
    return "\n".join(out)


def main():
    for mode in PALETTES:
        svg = render(mode)
        fname = f"{mode}_mode.svg"
        with open(fname, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"wrote {fname} ({len(svg)} bytes)")
    print("Done.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
███████╗███╗   ███╗ █████╗ ██████╗      ██████╗██╗   ██╗██████╗ ███████╗██████╗
██╔════╝████╗ ████║██╔══██╗██╔══██╗    ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║  ██║    ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║  ██║    ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██████╔╝    ╚██████╗    ██║   ██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝      ╚═════╝    ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝
                      EMAD CYBER  ::  TikTok OSINT  ::  v2.0
                              Developer: @49mu
"""

import requests
import os
import sys
import time
import random
import shutil
from datetime import datetime

try:
    import pycountry
except ImportError:
    print("[!] Missing dependency: pycountry. Install with: pip install -r requirements.txt")
    sys.exit(1)

# ═══════════════════════════ COLOR PALETTE ═══════════════════════════
class C:
    R   = "\033[0m"
    B   = "\033[1m"
    DIM = "\033[2m"
    BLINK = "\033[5m"

    # Neon palette
    NEON_GREEN  = "\033[38;5;46m"
    NEON_CYAN   = "\033[38;5;51m"
    NEON_PINK   = "\033[38;5;198m"
    NEON_PURPLE = "\033[38;5;141m"
    NEON_YELLOW = "\033[38;5;226m"
    NEON_ORANGE = "\033[38;5;208m"
    NEON_RED    = "\033[38;5;196m"
    NEON_BLUE   = "\033[38;5;39m"
    WHITE       = "\033[38;5;255m"
    GRAY        = "\033[38;5;245m"
    DARK        = "\033[38;5;238m"

    # Backgrounds
    BG_DARK     = "\033[48;5;236m"
    BG_GREEN    = "\033[48;5;22m"


# ═══════════════════════════ TERMINAL UTILS ═══════════════════════════
def term_width():
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 80

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def center(text, width=None):
    if width is None:
        width = term_width()
    pad = max(0, (width - len(strip_ansi(text))) // 2)
    return " " * pad + text

def strip_ansi(s):
    import re
    return re.sub(r'\033\[[0-9;]*m', '', s)

def slow_print(text, delay=0.003, color=""):
    for ch in text:
        sys.stdout.write(color + ch + C.R)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def gradient_line(text, start_color=C.NEON_CYAN, end_color=C.NEON_PINK):
    # simple two-tone "gradient"
    half = len(text) // 2
    return start_color + text[:half] + end_color + text[half:] + C.R


# ═══════════════════════════ MATRIX RAIN INTRO ═══════════════════════════
def matrix_rain(duration=1.2):
    cols = term_width()
    chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノ#$%&@*+="
    end = time.time() + duration
    rows = 8
    while time.time() < end:
        line = ""
        for _ in range(cols - 1):
            if random.random() < 0.5:
                line += C.NEON_GREEN + random.choice(chars)
            else:
                line += " "
        sys.stdout.write("\r" + line + C.R)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\r" + " " * (cols - 1) + "\r")
    sys.stdout.flush()


# ═══════════════════════════ BANNER ═══════════════════════════
BANNER = r"""
   ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████ ████████▄          ▄████████ ▄██   ▄    ▀█████████▄     ▄████████    ▄████████
  ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███   ▀███        ███    ███ ███   ██▄    ███    ███   ███    ███   ███    ███
  ███    █▀  ███   ███   ███   ███    ███ ███    ███        ███    █▀  ███▄▄▄███    ███    ███   ███    █▀    ███    ███
 ▄███▄▄▄     ███   ███   ███   ███    ███ ███    ███        ███        ▀▀▀▀▀▀███   ▄███▄▄▄██▀   ▄███▄▄▄      ▄███▄▄▄▄██▀
▀▀███▀▀▀     ███   ███   ███ ▀███████████ ███    ███      ▀███████████ ▄██   ███  ▀▀███▀▀▀██▄  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
  ███    █▄  ███   ███   ███   ███    ███ ███    ███               ███ ███   ███    ███    ██▄   ███    █▄  ▀███████████
  ███    ███ ███   ███   ███   ███    ███ ███   ▄███         ▄█    ███ ███   ███    ███    ███   ███    ███   ███    ███
  ██████████  ▀█   ███   █▀    ███    █▀  ████████▀        ▄████████▀   ▀█████▀   ▄█████████▀    ██████████   ███    ███
                                                                                                              ███    ███
"""

SMALL_BANNER = r"""
 ╔═╗╔╦╗╔═╗╔╦╗   ╔═╗╦ ╦╔╗ ╔═╗╦═╗   ╔╦╗╦╦╔═╔╦╗╔═╗╦╔═
 ║╣ ║║║╠═╣ ║║   ║  ╚╦╝╠╩╗║╣ ╠╦╝    ║ ║╠╩╗ ║ ║ ║╠╩╗
 ╚═╝╩ ╩╩ ╩═╩╝   ╚═╝ ╩ ╚═╝╚═╝╩╚═    ╩ ╩╩ ╩ ╩ ╚═╝╩ ╩
"""

def print_banner():
    width = term_width()
    banner_lines = BANNER.splitlines() if width >= 110 else SMALL_BANNER.splitlines()
    palette = [C.NEON_PINK, C.NEON_PURPLE, C.NEON_BLUE, C.NEON_CYAN, C.NEON_GREEN]
    for i, line in enumerate(banner_lines):
        color = palette[i % len(palette)]
        print(color + C.B + line + C.R)

    # subtitle box
    print()
    sub = f" TikTok OSINT Recon Tool  ::  v2.0  ::  by {C.NEON_YELLOW}@49mu{C.NEON_CYAN} "
    print(C.NEON_CYAN + center(sub) + C.R)

    sep = "═" * min(78, width - 2)
    print(C.NEON_PURPLE + center(sep) + C.R)


# ═══════════════════════════ SPINNER / LOADER ═══════════════════════════
def hacker_loader(message="Initializing", duration=1.0):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r{C.NEON_GREEN}[{frames[i % len(frames)]}]{C.R} {C.GRAY}{message}...{C.R}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f"\r{C.NEON_GREEN}[✔]{C.R} {C.WHITE}{message}... {C.NEON_GREEN}DONE{C.R}{' '*20}\n")


def progress_bar(label, duration=0.8):
    width = 36
    print(f"{C.NEON_CYAN}┌─[{C.NEON_YELLOW}{label}{C.NEON_CYAN}]{C.R}")
    sys.stdout.write(f"{C.NEON_CYAN}└─▶ {C.R}[")
    sys.stdout.flush()
    for i in range(width):
        time.sleep(duration / width)
        sys.stdout.write(f"{C.NEON_GREEN}█{C.R}")
        sys.stdout.flush()
    print(f"] {C.NEON_GREEN}100%{C.R}")


# ═══════════════════════════ BOX RENDERER ═══════════════════════════
def render_box(title, rows, color=C.NEON_CYAN, value_color=C.WHITE):
    """rows = list of (label, value) tuples"""
    label_w = max(len(strip_ansi(r[0])) for r in rows) if rows else 10
    val_w   = max(len(strip_ansi(str(r[1]))) for r in rows) if rows else 10
    inner = max(60, label_w + val_w + 7)

    # top border with title
    title_str = f" {title} "
    top = "╔" + "═" * 3 + title_str + "═" * (inner - 3 - len(title_str)) + "╗"
    print(color + C.B + top + C.R)

    for label, value in rows:
        pad = inner - len(strip_ansi(label)) - len(strip_ansi(str(value))) - 6
        line = (f"{color}║{C.R}  "
                f"{C.NEON_YELLOW}▸{C.R} {C.NEON_GREEN}{label:<{label_w}}{C.R} "
                f"{C.DARK}│{C.R} {value_color}{value}{C.R}"
                + " " * max(1, pad) +
                f"{color}║{C.R}")
        print(line)

    bottom = "╚" + "═" * inner + "╝"
    print(color + C.B + bottom + C.R)


# ═══════════════════════════ TIKTOK FETCHER ═══════════════════════════
def fetch_user(username):
    headers = {
        "Host": "www.tiktok.com",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "sec-fetch-site": "none",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "accept-language": "en-US,en;q=0.9",
    }
    url = f'https://www.tiktok.com/@{username}'
    resp = requests.get(url, headers=headers, timeout=15)
    return resp.text


def safe_split(text, after, before):
    try:
        return text.split(after)[1].split(before)[0]
    except Exception:
        return ""


def parse_user(html):
    block = safe_split(html, 'webapp.user-detail"', '"RecommendUserList"')
    if not block:
        return None

    data = {
        "id":        safe_split(block, 'id":"', '",'),
        "name":      safe_split(block, 'nickname":"', '",'),
        "bio":       safe_split(block, 'signature":"', '",'),
        "country":   safe_split(block, 'region":"', '",'),
        "private":   safe_split(block, 'privateAccount":', ',"'),
        "verified":  safe_split(block, 'verified":', ',"'),
        "followers": safe_split(block, 'followerCount":', ',"'),
        "following": safe_split(block, 'followingCount":', ',"'),
        "likes":     safe_split(block, 'heart":', ',"'),
        "videos":    safe_split(block, 'videoCount":', ',"'),
        "friends":   safe_split(block, 'friendCount":', ',"'),
        "secid":     safe_split(block, 'secUid":"', '"'),
        "avatar":    safe_split(block, 'avatarLarger":"', '",'),
    }
    return data


def format_int(s):
    try:
        n = int(s)
        return f"{n:,}"
    except Exception:
        return s or "—"


def country_info(code):
    if not code:
        return "Unknown", ""
    try:
        c = pycountry.countries.get(alpha_2=code)
        if not c:
            return code, ""
        name = getattr(c, "name", code)
        flag = getattr(c, "flag", "")
        return name, flag
    except Exception:
        return code, ""


def creation_date_from_id(uid):
    try:
        binary = "{0:b}".format(int(uid))
        bits = binary[:31]
        ts = int(bits, 2)
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return "—"


# ═══════════════════════════ DISPLAY RESULT ═══════════════════════════
def show_result(username, data):
    cname, cflag = country_info(data["country"])
    created = creation_date_from_id(data["id"])

    private_str = (f"{C.NEON_RED}● YES{C.R}" if data["private"] == "true"
                   else f"{C.NEON_GREEN}● NO{C.R}")
    verified_str = (f"{C.NEON_CYAN}✔ Verified{C.R}" if data["verified"] == "true"
                    else f"{C.GRAY}✗ Not Verified{C.R}")

    # Profile box
    profile_rows = [
        ("USERNAME    ", f"@{username}"),
        ("NICKNAME    ", data["name"] or "—"),
        ("USER ID     ", data["id"] or "—"),
        ("SEC UID     ", (data["secid"][:42] + "…") if len(data["secid"]) > 42 else (data["secid"] or "—")),
        ("CREATED ON  ", created),
        ("REGION      ", f"{cname} {cflag}"),
        ("PRIVATE     ", private_str),
        ("STATUS      ", verified_str),
    ]
    render_box("[⚡] PROFILE INTEL", profile_rows, color=C.NEON_CYAN)

    print()

    # Stats box
    stats_rows = [
        ("FOLLOWERS   ", f"{C.NEON_PINK}{format_int(data['followers'])}{C.R}"),
        ("FOLLOWING   ", f"{C.NEON_YELLOW}{format_int(data['following'])}{C.R}"),
        ("FRIENDS     ", f"{C.NEON_BLUE}{format_int(data['friends'])}{C.R}"),
        ("TOTAL LIKES ", f"{C.NEON_RED}{format_int(data['likes'])}{C.R}"),
        ("VIDEOS      ", f"{C.NEON_GREEN}{format_int(data['videos'])}{C.R}"),
    ]
    render_box("[#] SOCIAL METRICS", stats_rows, color=C.NEON_PURPLE, value_color=C.WHITE)

    print()

    # Bio
    bio = data["bio"].encode().decode('unicode_escape', errors="ignore") if data["bio"] else "(empty)"
    print(f"{C.NEON_CYAN}╔═══[ {C.NEON_YELLOW}[~] BIO{C.NEON_CYAN} ]" + "═" * 50 + "╗" + C.R)
    print(f"{C.NEON_CYAN}║{C.R}  {C.WHITE}{bio}{C.R}")
    print(f"{C.NEON_CYAN}╚" + "═" * 60 + "╝" + C.R)

    print()

    # Profile URL
    print(f"{C.NEON_GREEN}[+]{C.R} {C.WHITE}Profile URL :{C.R} {C.NEON_CYAN}https://www.tiktok.com/@{username}{C.R}")
    if data["avatar"]:
        avatar_url = data["avatar"].replace("\\u002F", "/").replace("\\/", "/")
        print(f"{C.NEON_GREEN}[+]{C.R} {C.WHITE}Avatar URL  :{C.R} {C.NEON_CYAN}{avatar_url}{C.R}")


# ═══════════════════════════ FOOTER ═══════════════════════════
def footer():
    width = term_width()
    print()
    print(C.NEON_PURPLE + "═" * min(78, width - 2) + C.R)
    sig = f"  {C.NEON_PINK}♦{C.R} {C.B}{C.NEON_CYAN}EMAD CYBER{C.R} {C.DARK}|{C.R} " \
          f"{C.NEON_YELLOW}TikTok :: @49mu{C.R} {C.DARK}|{C.R} " \
          f"{C.NEON_GREEN}GitHub :: e419x{C.R} {C.NEON_PINK}♦{C.R}"
    print(center(sig))
    print(C.NEON_PURPLE + "═" * min(78, width - 2) + C.R)


# ═══════════════════════════ MAIN ═══════════════════════════
def main():
    clear()
    matrix_rain(0.8)
    print_banner()
    print()

    hacker_loader("Loading recon modules", 0.6)
    hacker_loader("Establishing secure socket", 0.5)
    print()

    try:
        prompt = (f"{C.NEON_GREEN}┌──({C.NEON_PINK}49mu{C.NEON_GREEN}㉿{C.NEON_CYAN}emad-cyber{C.NEON_GREEN})\n"
                  f"└─▶ {C.NEON_YELLOW}Enter TikTok username:{C.R} {C.WHITE}")
        username = input(prompt).strip().lstrip("@")
        print(C.R, end="")
    except (KeyboardInterrupt, EOFError):
        print(f"\n{C.NEON_RED}[!] Aborted by user.{C.R}")
        sys.exit(0)

    if not username:
        print(f"{C.NEON_RED}[!] Empty username. Exiting.{C.R}")
        sys.exit(1)

    print()
    progress_bar(f"Scanning @{username}", 0.9)
    print()

    try:
        html = fetch_user(username)
    except requests.RequestException as e:
        print(f"{C.NEON_RED}[!] Network error: {e}{C.R}")
        sys.exit(1)

    data = parse_user(html)
    if not data or not data["id"]:
        print(f"{C.NEON_RED}╔══════════════════════════════════════════════════╗{C.R}")
        print(f"{C.NEON_RED}║  [!] Target not found or profile is unreachable. ║{C.R}")
        print(f"{C.NEON_RED}║      Username : @{username:<32}║{C.R}")
        print(f"{C.NEON_RED}╚══════════════════════════════════════════════════╝{C.R}")
        sys.exit(1)

    show_result(username, data)
    footer()


if __name__ == "__main__":
    main()

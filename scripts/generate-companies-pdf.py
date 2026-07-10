#!/usr/bin/env python3
"""Generate PDF directory from companies.html"""

from fpdf import FPDF
from html import unescape
from urllib.parse import quote
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "companies.html"
PDF_PATH = ROOT / "docs" / "sahiwal-it-companies-directory.pdf"


def clean(text: str) -> str:
    if not text:
        return ""
    text = unescape(text)
    text = text.replace("\u2014", "-").replace("\u2013", "-")
    text = text.replace("\u2605", "*").replace("\u2606", "*")
    text = re.sub(r"\s+", " ", text).strip()
    return text.encode("latin-1", "replace").decode("latin-1")


def parse_companies(html: str) -> list[dict]:
    card_pattern = re.compile(
        r'<div class="stc__company-card"[^>]*data-category="([^"]*)"[^>]*data-map-query="([^"]*)"[^>]*>(.*?)</div>\s*</div>\s*</div>',
        re.DOTALL,
    )
    companies = []

    for m in card_pattern.finditer(html):
        category, map_query, body = m.group(1), m.group(2), m.group(3)

        def extract(pattern):
            x = re.search(pattern, body, re.DOTALL)
            return clean(x.group(1)) if x else ""

        badge = extract(r'stc__company-badge[^>]*>([^<]+)')
        name = extract(r'stc__company-name">([^<]+)')
        description = extract(r'stc__company-description">\s*([^<]+(?:\s*[^<]+)*)')

        address = phone = email = website = highlight = ""
        info_match = re.search(
            r'stc__company-info">(.*?)(?:</div>\s*<div class="stc__company-actions"|</div>\s*</div>\s*$)',
            body,
            re.DOTALL,
        )
        info = info_match.group(1) if info_match else body

        for item in re.finditer(r'<div class="stc__info-item[^"]*">(.*?)</div>', info, re.DOTALL):
            chunk = item.group(1)
            text = clean(re.sub(r"<[^>]+>", "", chunk))
            if "fa-location-dot" in chunk:
                address = text
            elif "fa-phone" in chunk:
                phone = text
            elif "fa-envelope" in chunk:
                email = text
            elif "fa-globe" in chunk:
                website = text
            elif "stc__info-hiring" in item.group(0):
                highlight = text

        linkedin = website_url = ""
        for link in re.finditer(r'<a href="([^"]+)"[^>]*aria-label="([^"]*)"', body):
            url, label = link.group(1), link.group(2)
            if "linkedin" in url.lower():
                linkedin = url
            elif "website" in label.lower():
                website_url = url

        if website and not website_url:
            w = website.strip()
            website_url = w if w.startswith("http") else f"https://{w}"

        map_url = "https://www.google.com/maps/search/?api=1&query=" + quote(map_query)

        companies.append(
            {
                "category": category,
                "badge": badge,
                "name": name,
                "description": description,
                "address": address,
                "phone": phone,
                "email": email,
                "website": website,
                "website_url": website_url,
                "linkedin": linkedin,
                "highlight": highlight,
                "map_url": map_url,
            }
        )

    return companies


class DirectoryPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(26, 46, 34)
        self.cell(0, 8, "Sahiwal Tech Community - IT Companies Directory", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(45, 158, 71)
        self.set_line_width(0.4)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}} | Sahiwal Tech Community", align="C")

    def label_line(self, label, value):
        if not value:
            return
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(60, 60, 60)
        self.write(5, f"{label}: ")
        self.set_font("Helvetica", "", 9)
        self.set_text_color(28, 46, 34)
        self.multi_cell(0, 5, value)
        self.ln(1)

    def link_line(self, label, text, url):
        if not text or not url:
            return
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(60, 60, 60)
        self.write(5, f"{label}: ")
        self.set_font("Helvetica", "U", 9)
        self.set_text_color(0, 102, 204)
        self.write(5, text, link=url)
        self.ln(6)

    def add_company(self, idx, company):
        if self.get_y() > 250:
            self.add_page()

        self.set_fill_color(232, 245, 236)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(14, 31, 20)
        self.cell(0, 8, f"{idx}. {company['name']}", new_x="LMARGIN", new_y="NEXT", fill=True)
        self.ln(1)

        meta = f"{company['badge']} | Category: {company['category'].replace('-', ' ').title()}"
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(90, 90, 90)
        self.multi_cell(0, 5, meta)
        self.ln(1)

        self.set_font("Helvetica", "", 9)
        self.set_text_color(28, 46, 34)
        self.multi_cell(0, 5, company["description"])
        self.ln(2)

        self.label_line("Address", company["address"])
        self.label_line("Phone", company["phone"])
        if company["email"]:
            self.link_line("Email", company["email"], f"mailto:{company['email']}")
        if company["website"] and company["website_url"]:
            self.link_line("Website", company["website"], company["website_url"])
        elif company["website"]:
            self.label_line("Website", company["website"])
        if company["linkedin"]:
            self.link_line("LinkedIn", "View LinkedIn profile", company["linkedin"])
        if company["map_url"]:
            self.link_line("Google Maps", "Open in Google Maps", company["map_url"])
        self.label_line("Highlights", company["highlight"])

        self.ln(2)
        self.set_draw_color(220, 220, 220)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)


def main():
    html = HTML_PATH.read_text(encoding="utf-8")
    companies = parse_companies(html)

    pdf = DirectoryPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_page()

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(28, 46, 34)
    pdf.multi_cell(
        0,
        5,
        f"Verified IT companies listed on the Sahiwal Tech Community website. "
        f"Total companies: {len(companies)}. Generated July 10, 2026.",
    )
    pdf.ln(6)

    for i, company in enumerate(companies, 1):
        pdf.add_company(i, company)

    PDF_PATH.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(PDF_PATH))
    print(f"Created {PDF_PATH} ({len(companies)} companies)")


if __name__ == "__main__":
    main()

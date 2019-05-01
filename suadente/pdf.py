"""
PDF report module
"""
import json
import os
import sys

from fpdf import FPDF


class Report:
    def __init__(self, data):
        """Initialize the Report object."""
        self.pdf = FPDF("P", "mm", "A4")
        self.id = data["id"]
        self.data = data

    def render(self):
        self.pdf.add_page()
        self.draw_shapes()
        self.draw_title()
        self.draw_heading()
        self.draw_inventory()
        return self.pdf.output("report_%s.pdf" % self.data["id"])

    def draw_shapes(self):
        """Draw the report edge."""
        self.pdf.set_line_width(4)
        self.pdf.rect(10, 10, 190, 277)
        self.pdf.set_line_width(2)
        self.pdf.rect(15, 15, 180, 267)
        self.pdf.set_draw_color(192, 192, 192)
        self.pdf.set_line_width(1)
        self.pdf.rect(16, 16, 178, 265)

    def draw_inventory(self):
        """Draw the inventory paragraph the report."""
        self.pdf.set_y(100)
        self.pdf.set_font("Arial", "", 18)
        self.pdf.cell(170, 7, "Inventory", 0, ln=2, align="C")

        self.pdf.set_font("Arial", "", 12)
        for inventory in self.data["inventory"]:
            text = "%s: %s" % (inventory["name"], inventory["price"])
            self.pdf.cell(150, 7, text, 0, ln=2, align="C")

    def draw_title(self):
        """Draw the report title."""
        title = self.data["organization"] + " report"
        self.pdf.set_font("Arial", "B", 20)
        w = self.pdf.get_string_width(title)
        x = 210 - w / 2
        self.pdf.cell(x, 50, title, 0, 1, "C")

    def draw_heading(self):
        """Draw the report heading."""
        self.pdf.set_font("Arial", "", 12)
        self.pdf.set_x(0)
        org_text = "Organization: %s " % self.data["organization"]
        self.pdf.cell(170, 7, org_text, 0, ln=2, align="R")
        reported_text = "Reported: %s " % self.data["reported_at"]
        self.pdf.cell(170, 7, reported_text, 0, ln=2, align="R")
        created_text = "Created: %s " % self.data["created_at"]
        self.pdf.cell(170, 7, created_text, 0, ln=2, align="R")


if __name__ == "__main__":
    data = json.load(open("data.json", "r"))
    report = Report(data)
    report.render()

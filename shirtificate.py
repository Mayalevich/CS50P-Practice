from fpdf import FPDF

class ShirtificatePDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.name = name

def create_shirtificate(name):
    pdf = ShirtificatePDF(name)
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 50, "CS50 Shirtificate", ln=True, align="C")

    pdf.image("shirtificate.png", x=35, y=80, w=140)

    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 160)
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 10, name, align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    name = input("Name: ")
    create_shirtificate(name)

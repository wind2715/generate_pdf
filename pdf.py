from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="a4")
pdf.set_auto_page_break(auto=False, margin=0)
datas = pd.read_csv("topics.csv")

for item, row in datas.iterrows():
    #tao trang đầu
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    pdf.line(11, 20, 199, 20)
    #tạo dòng kẻ
    for i in range(30, 287, 10):
        pdf.line(11, i, 199, i)
    #tạo footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R")
    #tạo số trang
    for index in range(row['Pages'] - 1):
        pdf.add_page()
        #tạo dòng kẻ
        for i in range(10, 287, 10):
            pdf.line(11, i, 199, i)
        #tạo footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")
pdf.output("output.pdf")

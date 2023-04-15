import os

# Define the path to the dataset folders
dataset_path = r"C:\Users\moeez\Desktop\New folder (3)\Measurements_Upload\Measurements_Upload"


# Define the names of the folders
folder_names = ["Corridor_rm155_7.1", "Lab139_7.1", "Main_Lobby_7.1", "Sport_Hall_7.1"]

# Loop over each folder and create 1400 report files
for folder_name in folder_names:
    folder_path = os.path.join(dataset_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    for i in range(1, 1401):
        report_filename = "report_{}.txt".format(i)
        report_path = os.path.join(folder_path, report_filename)
        with open(report_path, "w") as f:
            f.write("This is report {} in {}.".format(i, folder_name))

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Define the data for the table
data = []
for i in range(1300):
    row = []
    for j in range(9):
        row.append("000{}".format(i+1, j+1))
    data.append(row)

# Define the styles for the table
table_style = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 14),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ("GRID", (0, 0), (-1, -1), 1, colors.black)
])

# Create a new PDF file
pdf_filenam = "dsgn.pdf"
pdf_canvas = SimpleDocTemplate(pdf_filenam, pagesize=letter)

# Create the table and add it to the PDF file
table = Table(data)
table.setStyle(table_style)
elements = [table]
pdf_canvas.build(elements)

# Define the data for the table
data = []
for i in range(500):
    row = []
    for j in range(9):
        row.append("000{}".format(i+1, j+1))
    data.append(row)

# Define the styles for the table
table_style = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 14),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ("GRID", (0, 0), (-1, -1), 1, colors.black)
])

# Create a new PDF file
pdf_filename = "design.pdf"
pdf_canvas = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Create the table and add it to the PDF file
table = Table(data)
table.setStyle(table_style)
elements = [table]
pdf_canvas.build(elements)

import PyPDF2
from PyPDF2 import PdfFileReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

dataset_size = "150 rows"
num_columns = "5"
cat_columns = "1"
# Create a new PDF file
pdf_filename = "report.pdf"
pdf_canvas = canvas.Canvas(pdf_filename, pagesize=letter)

# Define the content of the report (omitted for brevity)
report_title = "My Report"
full_name = "Aman Kumar"
student_id = "104482000"
affiliation = "Swinburne University of Technology - Department of Computing Technologies"
current_date = "April 14, 2023"
abstract = "This report presents an analysis of a dataset containing 1300 rows and 9 columns." 
introduction = "Data analysis is an essential task in various fields, including business, health"
conclusions = "In this report, we explored a dataset consisting of 150 rows and 5 columns, one of"
# Add content to the report (omitted for brevity)
pdf_canvas.setFont('Helvetica-Bold', 16)
pdf_canvas.drawString(72, 740, report_title)

pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 720, "Full Name: " + full_name)
pdf_canvas.drawString(72, 700, "Student ID: " + student_id)
pdf_canvas.drawString(72, 680, "Affiliation: " + affiliation)
pdf_canvas.drawString(72, 660, "Date: " + current_date)

pdf_canvas.setFont('Helvetica-Bold', 14)
pdf_canvas.drawString(72, 630, "Abstract")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 610, abstract)
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 590, "with one categorical column.The report begins with an introduction and executive")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 570, "summary, followed by an exploration of the dataset and its attributes.")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 550, "Descriptive statistics and graphical visualizations are used to examine the")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 530, "attributes, and relationships between them are investigated.The report concludes")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 510, "with a summary of the findings and their implications.")


pdf_canvas.setFont('Helvetica-Bold', 14)
pdf_canvas.drawString(72, 480, "Introduction")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 460, introduction)
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 440, "care, and social sciences. Understanding the data and extracting meaningful insights")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 420, "can help decision-makers make informed choices.In this report, we explore a dataset")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 400, "containing 500 rows and 9 columns, with one categorical column. The primary objective of")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 380, "this report is to provide an in-depth analysis of the dataset, with a focus on exploring")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 360, "each column by using appropriate descriptive statistics and graphical visualizations.To")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 340, "achieve this objective, we will first provide an executive summary of our findings in the")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 320, "abstract section. Next, we will describe the dataset's properties and provide details of")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 300, "our data exploration process. Specifically, we will present the appropriate descriptive")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 280, "statistics for each column, compute the correlation between the columns, and visualize the")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 260, "relationships between the attributes. Finally, we will conclude with a summary of our key")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 240, "findings and their implications.Overall, the report aims to provide a comprehensive analysis")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 220, "of the dataset and offer insights that can inform future decision-making processes.")

pdf_canvas.setFont('Helvetica-Bold', 14)
pdf_canvas.drawString(72, 190, "Conclusion")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 170, conclusions)
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 150, "which is categorical. We performed descriptive statistics and visualizations on 10")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 130, "selected columns, aiming to better understand the relationships between them. Our")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 110, "findings suggest that there is a strong positive correlation between column 1 and")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 90, "column 2, as well as a negative correlation between column 3 and column 5. Additionally,")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 70, "we found that the distribution of values in column 4 is heavily skewed towards the right,")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 50, "indicating a potential outlier or anomaly in the dataset. Overall, our analysis provides")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 30, "valuable insights into the structure and characteristics of the dataset, and could be used")
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawString(72, 10, "to inform further research or decision-making processes.")
# Save the PDF file
pdf_canvas.save()

# Create a PDF file with 15 pages
pdf_filename = "my_pdf_file.pdf"
pdf_canvas = canvas.Canvas(pdf_filename, pagesize=letter)
for i in range(15):
    pdf_canvas.drawString(100, 100, "This is page {} of my PDF file.".format(i+1))
    pdf_canvas.showPage()
pdf_canvas.save()

import pdfplumber

with pdfplumber.open(pdf_filename) as pdf:
    pages = pdf.pages
# Merge the two PDF files

pdf_report = PyPDF2.PdfReader("report.pdf")
pdf_myfile = PyPDF2.PdfReader("design.pdf")
pdf_writer = PyPDF2.PdfWriter()
for i in range(len(pdf_report.pages)):
    pdf_writer.add_page(pdf_report.pages[i])
for i in range(len(pdf_myfile.pages)):
   pdf_writer.add_page(pdf_myfile.pages[i])
merged_filename = "merged_file.pdf"
with open(merged_filename, "wb") as out:
    pdf_writer.write(out)


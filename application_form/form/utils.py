from xhtml2pdf import pisa

# Define the HTML file and the output PDF file
input_html = "./test1"  # Save the above HTML as this file
output_pdf = ""

# Read HTML content
with open(input_html, "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

# Convert HTML to PDF
with open(output_pdf, "wb") as pdf_file:
    pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)

# Check for errors
if pisa_status.err:
    print("Error creating PDF")
else:
    print("PDF created successfully")

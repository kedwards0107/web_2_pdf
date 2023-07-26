import pdfkit

# Set the path to the wkhtmltopdf executable (change this if needed)
config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

# Provide the URL of the web page
url = 'https://www.google.com/search?q=buy+starbucks+decaf+verona'
output_file = 'output.pdf'

# Generate the PDF
pdfkit.from_url(url, output_file, configuration=config)

# https://www.google.com/search?q=buy+starbucks+decaf+verona
# https://www.google.com/search?q=pepperidge+farm+goldfish+crackers%2C+cheddar%2C+30+oz.+carton

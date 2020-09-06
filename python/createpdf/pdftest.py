import pandas as pd
import jinja2
import pdfkit
import datetime
import hashlib 
import uuid 



def generate_pdf(name, mentor, course, details):
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "htmltemplate.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    # m = hashlib.md5()
    # m.update(date_string)
    
    outputText = template.render(id=uuid.uuid1(),
            name=name,
            course_name=course,
            additional_course_details=details,
            date=datetime.date.today(),
            mentor=mentor)

    html_file = open('certificate.html', 'w')
    html_file.write(outputText)
    html_file.close()

    options = {
        "enable-local-file-access": None,
        "orientation": "Landscape",
        "background": None,
        'margin-top': '0',
        'margin-right': '0',
        'margin-bottom': '0',
        'margin-left': '0',
        'zoom': 0.795
    }
    
    pdfkit.from_file('certificate.html', 'certificate.pdf', options=options)

generate_pdf("Bhavik Doe", "Tim Hargreaves", "Intro to Python", "Python for data science")
# 

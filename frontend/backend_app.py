
from sklearn.externals.joblib import load
from jinja2 import Environment, FileSystemLoader
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import pdfkit
import numpy as np
import time
import subprocess
from termcolor import colored


MODEL_INPPUT_PATH = 'signals.txt'
MODEL_PATH = 'finalized_model.sav'
PDF_REPORTS_PATH = 'reports'
HTML_TEMPLATE_PATH = 'template.html'

def process(data):
    # RUN THE MODEL
    print('\n' * 1)
    print(colored("""
                ################################
                # RUNNING MACHINE LEARNING MODEL
                ################################
              """, 'green'))
    predicted_symbols = predict()

    # GET SUMMARIES FOR SYMBOLS
    print('\n' * 1)
    print(colored("""
                ###############################
                # GETTING SUMMARIES FOR SYMBOLS
                ###############################
              """, 'green'))
    summaries = {}
    for i in range(int(data['no_of_instruments'])):
        summaries[predicted_symbols[i]] = get_summary(predicted_symbols[i])

    # CREATE REPORT #
    # Loading the html template "template.html" to jinja
    print('\n' * 1)
    print(colored("""
                #############################
                # CREATING THE SUMMARY REPORT
                #############################
              """, 'green'))
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(HTML_TEMPLATE_PATH)

    # Populating a dictionary of values to be passed to the html file
    template_dict = {"user_selection":data,
                    "predicted_symbols":predicted_symbols,
                    "summaries":summaries}

    # Rendering the template to html passing the dictionary of values to it 
    html_out = template.render(template_dict)

    # Write the html to a file
    with open("out.html", "w") as fh:
        fh.write(html_out)

    # Creating a pdf file from the saved output html file
    out_pdf_name = time.strftime('%m-%d-%Y-%H-%M') + "-portfolio-analysis.pdf"
    out_pdf_path = PDF_REPORTS_PATH + "\\" + out_pdf_name
    pdfkit.from_file('out.html', out_pdf_path)

    subprocess.Popen([out_pdf_path], shell=True)


def predict():
    # Load the model and make the predictions from the x test dataset
    tickers = ['MSFT','AAPL','V','MA','INTC','CSCO','ADBE','CRM','NVDA',
                'ACN','AVGO','PYPL','ORCL','IBM','TXN','QCOM','FIS','ADP',
                'INTU','FISV','GPN','AMAT','MU','NOW','ADI','AMD','ADSK',
                'LRCX','CTSH','APH','TEL','HPQ','PAYX','MSI','FLT','KLAC',
                'MCHP','XLNX','GLW','ANSS','HPE','SNPS','VRSN','CDW','KEYS',
                'CDNS','SWKS','MXIM','FTNT','NLOK','NTAP','WDC','IT','AKAM',
                'BR','CTXS','STX','QRVO','LDOS','JKHY','WU','ANET','DXC',
                'JNPR','FFIV','FLIR','XRX','IPGP','ADS']
    with open(MODEL_PATH, 'rb') as pickle_file:
        model = load(pickle_file)
    X = np.loadtxt(MODEL_INPPUT_PATH, dtype=float)
    predictions = model.predict(X)
    tickers_arr = np.array(tickers)
    predicted_symbols = tickers_arr[np.where(predictions == 1.)[0]]
    return predicted_symbols


def get_summary(ticker):
    url = 'https://finance.yahoo.com/quote/{}'.format(ticker)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    summary = soup.find("div", {"id": "quote-summary"})
    return summary

![Company logo](images/company-logo.jpg)

# Stock Selector (SS)
![Python](https://camo.githubusercontent.com/de59e8e9b410aa0b9479b114040c06468ef33cfc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d76332e362b2d626c75652e737667)  ![Build Status](https://travis-ci.org/anfederico/Clairvoyant.svg?branch=master)  ![Dependecies](https://camo.githubusercontent.com/6266857d1c53194119edf1d9aafae7a4b301fa16/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646570656e64656e636965732d7570253230746f253230646174652d627269676874677265656e2e737667) ![Contributions Welcome](https://camo.githubusercontent.com/72f84692f9f89555c176bb9e0eca9cf08d97fec9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d6f72616e67652e737667)

## Stock Selector uses machine learning algorithms to suggest stocks that have a higher probability of beating the sector index
* SS suggests stocks based on sector, risk profile, index, and number of instruments (e.g. Stocks)
* Calculations includes ~8 years of historical stock data
* One can input any different combinations of number of instruments and run   the Stock Selector to get suggestions on stocks within the reports folder
* Below is a screenshot of the user interface:

![User interface](images/user_interface.png)


## How it works
1. Clone the repo to your local drive.
2. From your terminal locate the [\frontend](/frontend) folder within the repo and in the terminal type ```python main.py``` and Hit Run.
3. Once you hit Run the SS pops up. Select Sector, market cap, index (Sector ETF), asset class (stocks), and no of instruments.
4. Hit SELECT STOCKS once all the details are entered and the SS will run all the machine learning models and scrape stock summaries from Yahoo Finance on the backed to generate a report in the reports folder.
5. Each report is time_stamped so generate as many reports you want with different number of stocks across sectors.


## Usage
The Stock Selector can be used by analysts who want to do a quick discovery on stocks that have a higher probability of beating the index as well as investors who want to understand which stocks to invest in based on their requirements.
The Stock Selector report has the below sections:
* **User Selection**: This displays all the different inputs that were provided by an individual.
* **Stock Summaries**: Suggests different stocks to invest in based on your inputs. The number of summaries are based on the number of stocks one selected within the input screen.    


## Requirements and Configuration
* All requirements and dependencies are in the build-requirements folder.
* The only other configuration is to run the wkhtmltox-0.12.5-1.msvc2015-win64.exe file in the frontend/archives folder.
* Once the config is run the user needs to add the path to their System - path variable. Below is an image of where one could find that:

![Environment variable config](images/add_to_path_variable.png)
![Environment variable config](images/add_to_path_variable2.png)



Have fun with the Stock Selector! :+1:

## Disclaimer
Developers of the SS are not registered as a securities broker-dealer or an investment adviser either with the U.S. Securities and Exchange Commission (the “SEC”) or with any state securities regulatory authority. We are not licensed to provide investment advice. Use SS suggestions at your own discretion.
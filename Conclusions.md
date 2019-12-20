# Project Analysis and Conclusions

In this project, we explored stock selection using machine learning techniques with fundamental data analysis. 

We focused on stocks in four SPDR ETF sectors: 
- XLY (Consumer Discretionary)
- XLK (Technology)
- XLP (Consumer Staples)
- XLV (Health Care)

For the company specific fundamental data we used SimFin, an open-source, platform-agnostic, free database of fundamental data for ~2,600 publicly listed companies. And for the machine learning libraries we used `SKLearn` and `Keras`. 

## Train/Test Data Preparation 

The feature data consisted of three fundamental buckets that incorporated income statement, balance sheet, and cash flow statement information for each stock on an annual basis. The SimFin Fundamental Signal data forward filled to calendar year end with end of year price data. The Train dataset was between 2011 – 2018 data, and the Test dataset was on 2019. 

<img src="/images/fund_signals.png" width="500" height="225">
<br/>

<img src="/images/xly_signals.png" width="700" height="325">
<br/>

The target data was determined by the stocks' annual returns relative to its sector, with a win defined as >= 5% out performance of the index.

<img src="/images/annual_returns_win_xly.png" width="400" height="200">

<br/>
<br/>



## Classification Models and Results 
```
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
```

![CD_chart](images/XLY_algo.png)  
<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="/images/xly_class.png" width="300" height="175">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    <img src="/images/cm_cd.png" width="225" height="150">

<br/>

![CD_chart](images/cd_relative_chart.png)    ![CD_chart](images/XLY_value_chart.png) 

<br/>

![CD_chart](images/XLK_algo.png)

<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="/images/xlk_class.png" width="300" height="175">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <img src="/images/cm_tech.png" width="225" height="150">
<br/>

![CD_chart](images/tech_relative_chart.png)    ![CD_chart](images/XLK_value_chart.png) 
<br/>
![CD_chart](images/XLP_algo.png)
<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="/images/xlp_class.png" width="300" height="175">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <img src="/images/cm_xlp.png" width="225" height="150">
<br/>
![CD_chart](images/cs_relative_chart.png)    ![CD_chart](images/XLP_value_chart.png) 
<br/>
<br/>
![CD_chart](images/XLV_algo.png) 
<br/>
<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="/images/xlv_class.png" width="300" height="175">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <img src="/images/cm_hc.png" width="225" height="150">
<br/>
 <br/>
![CD_chart](images/hc_relative_chart.png)    ![CD_chart](images/XLV_value_chart.png) 

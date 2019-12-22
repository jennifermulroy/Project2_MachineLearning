# Project Analysis and Conclusions

In this project, we explored sector specific stock selection using machine learning techniques with fundamental data analysis. 

We focused on stocks in four SPDR ETF sectors:  
- XLY (Consumer Discretionary)
- XLK (Technology)
- XLP (Consumer Staples)
- XLV (Health Care)

For the company specific fundamental data we used SimFin, an open-source, platform-agnostic, free database of fundamental data for ~2,600 publicly listed companies. And for the machine learning libraries we used `SKLearn` and `Keras`. For the stock price data we used `yahoo finance`. 

## Train/Test Data Preparation 

The feature data consisted of three fundamental buckets that incorporated income statement, balance sheet, and cash flow statement information for each stock on an annual basis. The SimFin Fundamental Signal data forward filled to calendar year end with end of year price data. The Train dataset was between 2011 – 2018, and the Test dataset was on 2019. 

<img src="/images/fund_signals.png" width="500" height="225">
<br/>

<img src="/images/xly_signals.png" width="700" height="325">
<br/>

The target data was determined by the stocks' annual returns relative to its sector, with a win defined as >= 5% out performance of the index.

<img src="/images/annual_returns_win_xly.png" width="400" height="200">

<br/>
<br/>


## Classification Models and Results

Given the limitation in historical fundamental data available on SimFim, we ran a k-fold cross validation and compared the accuracy scores generated to select the optimal classifier model. 

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

The `KNeighborsClassifier' had the best cross validation score and was used to predict with the test data for XLY. The accuracy score on the test data was 56% and a false positive rate of 50%. From the stocks selected by the model, we constructed an equally weighted portfolio and compared performance relative to the sector benchmark. AS per the chart below, the portfolio over the 2019 period has slightly outperformed the benchmark by 4%. 


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="/images/xly_class.png" width="300" height="175">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    <img src="/images/cm_cd.png" width="225" height="150">

<br/>


| Performance                              |                             |
|:---:                                     | :---:                       |
|![CD_chart](images/cd_relative_chart.png) |   ![CD_chart](images/XLY_value_chart.png) |


<br/>

![CD_chart](images/XLK_algo.png)

`GaussianNB` had the best cross validation score and was used to predict with the test data for XLK.  The accuracy score on the test data was low at 38% but a low false positive rate of approximately 20%. The equally weighted portfolio of stocks selected from the model initially outperformed the sector benchmark but outperformance declined as the year progressed. AS per the chart below, the portfolio over the 2019 period is slightly inline with the performance of the benchmark. 

<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="/images/xlk_class.png" width="300" height="175">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <img src="/images/cm_tech.png" width="225" height="150">
<br/>

| Performance                               |                             |
|:---:                                      | :---:                       |
|![CD_chart](images/tech_relative_chart.png)| ![CD_chart](images/XLK_value_chart.png) |



<br/>

![CD_chart](images/XLP_algo.png)

`SVC` had the best cross validation score and was used to predict with the test data for XLP. The accuracy score on the test data was low at 45% and a false positive rate of 100%. The model generated results that suggested selecting all of the stocks in the benchmark, expect ticker PEP.  As expected, the annual performance was inline with the benchmark.

<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="/images/xlp_class.png" width="300" height="175">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <img src="/images/cm_xlp.png" width="225" height="150">
<br/>

| Performance                               |                             |
|:---:                                      | :---:                       |
|![CD_chart](images/cs_relative_chart.png)  | ![CD_chart](images/XLP_value_chart.png)| 

<br/>

<br/>

![CD_chart](images/XLV_algo.png)

`LogisticRegression` had the best cross validation score and was used to predict with the test data for XLV. The accuracy score on the test data was high at 67% but also a high false positive rate of approximately 90%. The equally weighted portfolio of stocks selected from the model has shown strong outperformance to the Health Care sector benchmark but given the high false positive rate the model is robust. 

<br/>
<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="/images/xlv_class.png" width="300" height="175">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <img src="/images/cm_hc.png" width="225" height="150">
<br/>
 <br/>
 
| Performance                               |                             |
|:---:                                      | :---:                       |
|![CD_chart](images/hc_relative_chart.png)  | ![CD_chart](images/XLV_value_chart.png) |


In conclusion, fundamental data appears to have some predictability patterns identified by machine learning but is not sufficient to generate sustainable outsized returns. 

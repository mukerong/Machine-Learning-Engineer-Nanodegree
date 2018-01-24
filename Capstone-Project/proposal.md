# Machine Learning Engineer Nanodegree
## Capstone Proposal
Guanrong Fu

January 23, 2018

## Proposal

### Domain Background
After the tax reform recently, articles and analysis about tax are everywhere. Working as a tax analyst, I conduct data analysis over financial data every day for tax purposes, but I still find it is a pain to fill out my own individual tax return every year. You might think we can use Turbo tax or other tax preparation software to get them done, but were you ever curious about the amount you paid compared to others. Did you pay more than others or less? How’s the tax payment distribution amount US like? There are also people who have income other than salary need to figure out how much estimated tax they should pay by the end of the year to avoid fines and penalties. 

US has a very complicated tax system that not everyone has time to fully understand. Errors might happen when people type in or write down the wrong amount, and no one wants to be audited or get penalties from IRS. There is no benchmark for people to estimate their tax, other than their previous year return. What should we do if this is the first year return? What should we do if our income structure changes completely? How to minimize the potential errors? IRS has the database of the tax information in US for the past several years. If we have a model that can predict roughly about how much tax we owe each year, we will be able to understand if we need to pay estimate tax or if there might be some potential errors. 

### Problem Statement
As discussed above, it is hard for each individual to understand how much tax they need to pay each year. People are vulnerable if they do not know if they need to pay an estimate tax or if they have paid the right amount. How to avoid these situations? The potential solution is to build up a model to estimate how much tax they should pay. In this way, there will be a benchmark for people to compare to so that they know if there are abnormal amount caused by errors or other factors.

### Datasets and Inputs
IRS provided the historical tax data in its website. Kaggle also has cleaned version of the database, but only for a couple of years. In the project, I plan to use tax data for the past 10 years. The raw data from IRS is very messy and uncleaned. It includes almost all the details within a tax return. IRS used a lot of symbols, which are not consistent each year. The dataset needs to be cleaned up before combing all the year together.

Since many factors are related, I will pick up the most important factors to do some explanatory data analysis to understand the data, such as the filling status, salary and capital gain/loss. These are important factors when calculating the actual tax, so the model needs to get some base knowledge before actually training the model. When building up the model, I will only use the accessible features because people will not try the model if the input for it is as hard as that for actual tax return.

### Solution Statement
As discussed above, the potential solution is to estimate a tax amount before actually filling the return to get a benchmark. The model I will train will take into some basic information, such as salary and investment, to predict how much return people should pay this year. The model will be trained by the historical tax data from IRS, and we can measure how accurate the model is by comparing to actual number.

### Benchmark Model
There are many simple free models online, such as [smart assets]( https://smartasset.com/taxes/income-taxes), that can be used as a benchmark. However, since similar models only take salary into account, the amount my model calculated could be different from them. In this case, we can use the data from the historical data and compare again the real amount. The accuracy of my model will be the percentage difference from the real amount. 

### Evaluation Metrics
We can use the real data from IRS to test the free model online and my model. The less difference between calculated amount and the real amount, the better the model is. This is more a regression model other than a classification model, so the percentage of differences can be a good measure.

### Project Design
The first step of this project will be data cleaning, and extracting the most important features for later analysis. To extract features, I will use both my domain knowledge and models like decision tree.

The second step will be explanatory data analysis, where we can gain some insights about the data structure, destructions and other related information. There will be some data visualization and data analysis in this step. For example, there will be histogram of the tax paid in US in certain year, and the trends of the total tax paid each year.

The next step will be feature transformation and selection, which is needed for the model. Categorical data needs to be transferred to numerical, and the feature selected from step 1 will be used here. 

The next step will be actually training the data, evaluating it based on the metrics mentioned above and test the model. I will use KNN, linear regression and decision tree regression analysis. If it will not take too long, I will try svm as well.

The above steps will be go through for several times to get the best model.


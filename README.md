# Hospital_Treatment_Cost_Prediction

The project aims to develop a predictive model approach to identify key factors that drive the total cost of treatment.

> ## Table of Content

[Overview](#Overview)  
[AIM](#AIM)  
[Approach](#Approach)  
[Technical Aspect](#Technical_Aspect) 
[Conclusion](#Conclusion)

## Overview
Mission Hospital is considering the adoption of fixed package pricing to make its pricing policies more transparent while providing the best care available to its patients. Thereby satisfying the needs of both patients and hospitals. Currently the hospital is facing challenges in estimating the pricing package to be given to patients at the time of admission. Hospital is required to build a model to help the hospital determine the approximate cost associated with the patient’s treatment which is calculated based on the patient's clinical and non-clinical information available at the time of admission so that the Hospital can charge the patient accordingly.

## AIM
The project aims to build a model approach to identify the key factors which are responsible for the total cost of treatment.

## Approach'
Following the CRISP-DM approach to building a linear regression model. 
*  Business Understanding. 
*  Data Understanding. 
*  Data Preparation. 
*  Modeling. 
*  Evaluation. 

## Technical Aspect
Find Significant Variables - using correlation matrix![Correlation Heatmap](https://user-images.githubusercontent.com/70143009/106358027-b539aa00-632f-11eb-8aa3-b1bd46f2f390.png)

Developed **forward Multiple Regression Model**
Model Performance Metric - **Adjusted R2 - 0.84**
Check linear Regression Assumption - Homoscedasticity

## Conclusion


* The Regression equations for the above mentioned four models are as follows:
*  Model:
* Total cost to hospital = 7161 + 335.4*(Body Height) + 4680*(Total length of stay) + 22940*(Length of stay in ICU) + 1.73*(cost of implant)

*. With the accuracy of 84% of the model, the significant variables which are a key factor to drive the total cost of the hospital are total length of stay, length of stay in ICU, and cost of the implant. with these variables, any one of the following variables can be used: Age, height, or weight.

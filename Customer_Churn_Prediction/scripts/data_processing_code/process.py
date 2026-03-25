import pandas  as pd


#initialize pandas dataset
telco_data = pd.read_csv("D:\Customer_Churn_Prediction\data\unprocessed_data\telco_customer_data_v2.csv")


#1) Importants features of the dataset,i judge it is the most importants features
def Data_cleaning_processing(df):
    df_clean = df[["tenure","Contract","MonthlyCharges","TotalCharges","InternetService","PaymentMethod","TechSupport","OnlineSecurity"]]

   
    #2)Unifier value with same meaning in all columns

        #Churn,Payments,Contract,OnlineSecurity,TechSupport
    df_clean["Churn"] = df_clean["Churn"].replace({
            "NO CHURN": "NO",
            "N" :"NO",
            "No":"NO",
            "Yes":"YES",
            "CHURNED":"YES",
            "Y":"YES"
        })

    df_clean["PaymentMethod"] = df_clean["PaymentMethod"].replace({
    "BANK TRANSFER":"Bank transfer (automatic)"

        })
 
    df_clean["Contract"] = df_clean["Contract"].replace({
    "M-M":"Month-to-month"
        })
    
    df_clean["OnlineSecurity"] = df_clean["OnlineSecurity"].replace({

    "No internet service":"No",
    "True":"Yes",
    "Y":"Yes"
})

    df_clean["TechSupport"] = df_clean["TechSupport"].replace({
 
    "No internet service":"No",
    "True":"Yes",
    "Y":"Yes"
    })
    

    #3)Fixing total charge and tenure regularities
    
    return df_clean



        
    

    
 
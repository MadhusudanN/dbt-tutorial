

def model(dbt, session):
    dbt.config(materialized = "table",packages= ["pandas"])
    
    df_cust = dbt.ref("stg_customers")
    #df_ord = dbt.ref("stg_orders")
    #df_pay = dbt.ref("stg_payments")
     
    return df_cust
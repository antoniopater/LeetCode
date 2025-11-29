import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df_merge = pd.merge(sales,product,on="product_id")
    return df_merge[['product_name','year','price']]
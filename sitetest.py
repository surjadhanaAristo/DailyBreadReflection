import streamlit as st
import pandas as pd
from datetime import datetime
today = datetime.today()
url = "https://github.com/surjadhanaAristo/DailyBreadReflection/blob/main/new.csv?raw=true"
df = pd.read_csv(url, index_col=0)
apidate = today.strftime("%Y-%m-%d")
new_date = df[apidate][0]
print(new_date)
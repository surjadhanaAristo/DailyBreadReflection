import streamlit as st
import pandas as pd
from datetime import datetime
today = datetime.today()
url = "https://github.com/surjadhanaAristo/DailyBreadReflection/blob/main/newcsv.csv"
df = pd.read_csv(url, index_col=0)
apidate = today.strftime("%Y-%m-%d")
new_date = df[0]
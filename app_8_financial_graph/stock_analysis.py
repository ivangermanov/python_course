
# coding: utf-8

# In[1]:


import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from bokeh.plotting import figure, show, output_file, output_notebook
from pandas_datareader import data as pdr
import datetime
import fix_yahoo_finance as yf

start=datetime.datetime(2015,11,1)
end=datetime.datetime(2016,3,10)
yf.pdr_override()
df=pdr.get_data_yahoo(tickers="GOOG", start=start, end=end)

df=df.drop(columns=["Adj Close", 'Volume'])

def inc_dec(close, open):
    if close>open:
        return "Increase"
    elif close<open:
        return "Decrease"
    else:
        return "Equal"

df["Status"]=[inc_dec(c, o) for c, o in zip(df.Close,df.Open)]
df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Open-df.Close)

p=figure(x_axis_type='datetime', width=1000, height=300, sizing_mode="scale_width")
p.title.text="Candlestick Chart"
p.grid.grid_line_alpha=0.3

hours_12=12*60*60*1000

p.segment(df.index, df.High, df.index, df.Low, line_color="black")
p.rect(df.index[df.Status=="Increase"], df.Middle[df.Status=="Increase"], hours_12, df.Height[df.Status=="Increase"], fill_color="#CCFFFF", line_color="black")
p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"], hours_12, df.Height[df.Status=="Decrease"], fill_color="#FF3333", line_color="black")

output_file("CS.html")
show(p)


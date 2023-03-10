import streamlit as st
import pandas as pd

st.header('๐ ๋ฐ์ดํฐ ํ์ด๋ธ ๋ง๋ค๊ธฐ')

st.subheader("1. ๋ฐ์ดํฐ ๋ถ๋ฌ์ค๊ธฐ")
st.markdown("๋ฐ์ดํฐ๋ฅผ ๋ถ๋ฌ์์ ๋ฐ์ดํฐํ๋ ์์ ์ ์ฅํฉ๋๋ค.")
st.markdown("> ๋ฐ์ดํฐ๋ฅผ ๋ถ๋ฌ์ฌ ๋๋ :green['pandas'] ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ์ฌ์ฉํฉ๋๋ค. \n \n  "
            "> ์ค์ต์ kaggle์ด ์ ๊ณตํ๋ **'S&P 500 Stocks (daily updated)'** ๋ฐ์ดํฐ ์(CC0)์์,\n\n"
            "> ***'์์ 10๊ฐ ๊ธฐ์'***, ***'2022๋'*** ์ฃผ๊ฐ๋ง ์ถ์ถํ ๋ฐ์ดํฐ๋ฅผ ์ฌ์ฉํฉ๋๋ค.\n")

st.code("import pandas as pd\n\n"
        "stocks_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_stocks_2022.csv'\n"
        "index_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_index_2022.csv'\n"
        "df_stocks = pd.read_csv(stocks_file)\n"
        "df_index = pd.read_csv(index_file)")

df_stocks = pd.read_csv("./data/sp500_stocks_2022.csv")
df_index = pd.read_csv("./data/sp500_index_2022.csv")
st.markdown("---")
st.subheader("2. ๋ฐ์ดํฐ ํ๋ ์ ์ถ๋ ฅํ๊ธฐ")
st.markdown("๋ถ๋ฌ์จ ๋ฐ์ดํฐ๋ฅผ ๋ฐ์ดํฐ ํ๋ ์ ํํ๋ก ์ถ๋ ฅ์ด ๊ฐ๋ฅํฉ๋๋ค.")

st.markdown("- #### ๊ธฐ๋ณธ ๋ฐ์ดํฐ ํ๋ ์ ์ถ๋ ฅํ๊ธฐ")
st.code("st.dataframe(df_stocks)")
st.dataframe(df_stocks)

st.markdown("- #### Pandas ์คํ์ผ๋ง ์ ์ฉํ๊ธฐ(ex.Highlight)")
st.code("st.dataframe(df_index.style.highlight_max(axis=0))")
st.dataframe(df_index.style.highlight_max(axis=0))
st.markdown("---")

st.subheader("3. ์กฐ๊ฑด์ ์ ํํ์ฌ ๋ฐ์ดํฐ ์ถ๋ ฅํ๊ธฐ")
st.markdown("SelectBox, MultiSelectBox ๋ฑ ๋ค์ํ Input ์์ ฏ์ ์ฌ์ฉํ๋ฉด ์ํ๋ ์กฐ๊ฑด์ ๋ฐ์ดํฐ๋ง ์ถ๋ ฅํ  ์ ์์ต๋๋ค.")

st.markdown("- #### Select Box ์ฌ์ฉํ๊ธฐ")
st.markdown("> st.selectbox(label, options)\n"
            "> - label์ Select Box๋ฅผ ์ค๋ชํ๋ ๋ฌธ๊ตฌ\n"
            "> - options์ Select ์ ์๋ ๋ชฉ๋ก")
st.code("symbol = st.selectbox('๊ฒ์ํ๊ณ ์ ํ๋ ๊ธฐ์์ ์ ํํ์ธ์.', (df_stocks['Symbol'].unique()))\n"
        "st.dataframe(df_stocks[df_stocks['Symbol'] == symbol])\n")
symbol = st.selectbox('๊ฒ์ํ๊ณ ์ ํ๋ ๊ธฐ์์ ์ ํํ์ธ์.', (df_stocks['Symbol'].unique()))
st.dataframe(df_stocks[df_stocks['Symbol'] == symbol])

st.markdown("- #### Multi Select Box ์ฌ์ฉํ๊ธฐ")
st.markdown("> st.multiselect(label, options)\n"
            "> - label : Multi Select Box๋ฅผ ์ค๋ชํ๋ ๋ฌธ๊ตฌ\n"
            "> - options : Select ํ  ์ ์๋ ๋ชฉ๋ก"
            "> - default : ๊ธฐ๋ณธ์ผ๋ก Select ๋์ด ์๋ ๊ฐ")
st.code("symbol_list = st.multiselect('๊ฒ์ํ๊ณ ์ ํ๋ ๊ธฐ์์ ์ ํํ์ธ์.', (df_stocks['Symbol'].unique()), default='AAPL', key='df')\n"
        "st.dataframe(df_stocks[df_stocks['Symbol'].isin(symbol_list)])")

symbol_list = st.multiselect('๊ฒ์ํ๊ณ ์ ํ๋ ๊ธฐ์์ ์ ํํ์ธ์.', (df_stocks['Symbol'].unique()), default='AAPL', key='df')
st.dataframe(df_stocks[df_stocks['Symbol'].isin(symbol_list)])


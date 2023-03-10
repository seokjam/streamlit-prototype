import streamlit as st
import pandas as pd
import datetime

st.header("๐ ์ฐจํธ ๊ทธ๋ฆฌ๊ธฐ")

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

st.subheader("2. Line Chart ์ถ๋ ฅํ๊ธฐ")
st.markdown("๋ถ๋ฌ์จ ๋ฐ์ดํฐ๋ฅผ Line Chart๋ก ์ถ๋ ฅํฉ๋๋ค.")
st.markdown("- #### ๋จ์ผ ๋ฐ์ดํฐ ์ถ๋ ฅํ๊ธฐ")
st.code("st.line_chart(df_index, x='Date')")
st.line_chart(df_index, x='Date')

st.markdown("- #### ์ฌ๋ฌ ๋ฐ์ดํฐ ์ถ๋ ฅํ๊ธฐ")
st.markdown("> ๋ณต์์ ๋ฐ์ดํฐ๋ฅผ ์ฐจํธ๋ก ๊ทธ๋ฆฌ๊ธฐ ์ํด์๋ ๋ฐ์ดํฐ ์์ ์ด ํ์ํฉ๋๋ค.")
df_chart = pd.DataFrame(columns=['Date'])
df_chart['Date'] = df_stocks['Date'].unique()
for symbol in df_stocks['Symbol'].unique():
    df_chart[symbol] = df_stocks[df_stocks['Symbol'] == symbol]['Close'].reset_index(drop=True)
st.dataframe(df_chart.head())

st.code("df_chart = pd.DataFrame(columns=['Date'])\n"
        "df_chart['Date'] = df_stocks['Date'].unique()\n"
        "\n"
        "for symbol in df_stocks['Symbol'].unique():\n"
        "\tdf_chart[symbol] = df_stocks[df_stocks['Symbol'] == symbol]['Close'].reset_index(drop=True)\n"
        "\n"
        "st.line_chart(df_chart, x='Date')")

st.line_chart(df_chart, x='Date')
st.markdown("---")

st.subheader("3. Bar Chart ์ถ๋ ฅํ๊ธฐ")
st.markdown("๋ถ๋ฌ์จ ๋ฐ์ดํฐ๋ฅผ bar Chart๋ก ์ถ๋ ฅํฉ๋๋ค.")
st.code("df_index.tail(21), x='Data')")
st.bar_chart(df_index.tail(21), x='Date')
st.markdown("---")

st.subheader("4. ์กฐ๊ฑด์ ์ ํํ์ฌ ์ฐจํธ ์ถ๋ ฅํ๊ธฐ")
st.markdown("SelectBox, MultiSelectBox ๋ฑ ๋ค์ํ Input ์์ ฏ์ ์ฌ์ฉํ๋ฉด ์ํ๋ ์กฐ๊ฑด์ ๋ฐ์ดํฐ๋ง ์ถ๋ ฅํ  ์ ์์ต๋๋ค.")

st.markdown("- #### Multi Select Box ์ฌ์ฉํ๊ธฐ")
st.markdown("> st.multiselect(label, options)\n"
            "> - label : Multi Select Box๋ฅผ ์ค๋ชํ๋ ๋ฌธ๊ตฌ\n"
            "> - options : Select ํ  ์ ์๋ ๋ชฉ๋ก\n"
            "> - default : ๊ธฐ๋ณธ์ผ๋ก Select ๋์ด ์๋ ๊ฐ")
st.code("symbol_list = st.multiselect('๊ฒ์ํ๊ณ ์ ํ๋ ๊ธฐ์์ ์ ํํ์ธ์.', (df_stocks['Symbol'].unique()), default='AAPL', key='chart')\n"
        "symbol_list.insert(0, 'Date')\n\n"
        "st.line_chart(df_chart[symbol_list], x='Date')")
symbol_list = st.multiselect('๊ฒ์ํ๊ณ ์ ํ๋ ๊ธฐ์์ ์ ํํ์ธ์.', (df_stocks['Symbol'].unique()), default='AAPL', key='chart')
symbol_list.insert(0, 'Date')
st.line_chart(df_chart[symbol_list], x='Date')

st.markdown("- #### ๊ฒ์ ๊ธฐ๊ฐ์ ์ ํํ์ฌ ์ฐจํธ ๋ง๋ค๊ธฐ")

st.code("import datetime\n\n"
        "st.write('๊ฒ์ ๊ธฐ๊ฐ์ ์ค์ ํด ์ฃผ์ธ์.')\n"
        "start_day = st.date_input(\n"
        "\t '์์ ์ผ์,'\n"
        "\t datetime.date(2022, 1, 1))\n\n"
        "end_day = st.date_input(\n"
        "\t '์ข๋ฃ ์ผ์',\n"
        "\t datetime.date(2022, 12, 31))\n\n"
        "st.write(f'๊ฒ์ ๊ธฐ๊ฐ : {start_day} ~ {end_day}')\n"
        "st.line_chart(df_index[(df_index['Date'] >= str(start_day)) & (df_index['Date'] <= str(end_day))], x='Date')")

st.write("๊ฒ์ ๊ธฐ๊ฐ์ ์ค์ ํด ์ฃผ์ธ์.")
start_day = st.date_input(
    '์์ ์ผ์',
    datetime.date(2022, 9, 1))

end_day = st.date_input(
    '์ข๋ฃ ์ผ์',
    datetime.date(2022, 12, 31))
st.write(f'๊ฒ์ ๊ธฐ๊ฐ : {start_day} ~ {end_day}')
st.line_chart(df_index[(df_index['Date'] >= str(start_day)) & (df_index['Date'] <= str(end_day))], x='Date')

import streamlit as st

st.header("๐ ํ์คํธ ์ถ๋ ฅํ๊ธฐ")
st.markdown("Streamlit์ ๋ค์ํ ํํ๋ก ํ์ค๋ฅผ ์๋ ฅํ  ์ ์์ต๋๋ค.")

st.subheader("1. Title ์ถ๋ ฅํ๊ธฐ")
st.markdown("์ ๋ชฉ ํ์์ ํ์คํธ๋ฅผ ํ์ํฉ๋๋ค.")
st.code("st.title('๐Title์ ์๋ ฅํ์ธ์.')\n")
st.title("๐Title์ ์๋ ฅํ์ธ์.")
st.markdown("---")

st.subheader("2. Header, Subheader ์ถ๋ ฅํ๊ธฐ")
st.markdown("ํค๋(๋จธ๋ฆฌ๊ธ)๊ณผ ์ธ๋ถ ํค๋ ํญ๋ชฉ์ผ๋ก ํ์คํธ๋ฅผ ํ์ํฉ๋๋ค.")

st.code("st.header('Header(๋จธ๋ฆฌ๊ธ)์ ์๋ ฅํ์ธ์.')\n"
        "st.subheader('Subheader(์ธ๋ถ ๋จธ๋ฆฌ๊ธ)์ ์๋ ฅํ์ธ์.')")
st.header("Header(๋จธ๋ฆฌ๊ธ)์ ์๋ ฅํ์ธ์.")
st.subheader("Subheader(์ธ๋ถ ๋จธ๋ฆฌ๊ธ)์ ์๋ ฅํ์ธ์.")
st.markdown("---")

st.subheader("3. Markdown ์ถ๋ ฅํ๊ธฐ")
st.markdown("๋งํฌ๋ค์ด ํฌ๋งท์ผ๋ก ์ถ๋ ฅ์ด ๊ฐ๋ฅํฉ๋๋ค.")
st.markdown("- ํค๋(Headers) ๊ฐ์ฅ ***ํฐ ์ ๋ชฉ(H1)*** ๋ถํฐ ๊ฐ์ฅ ***์์ ์ ๋ชฉ(H6)*** ๊น๋ 6๋จ๊ณ๋ก ์ฌ์ฉ ๊ฐ๋ฅํฉ๋๋ค.  ")

st.code("st.markdown('# H1 #')\n"
        "st.markdown('## H2 ##')\n"
        "st.markdown('### H3 ###')\n"
        "st.markdown('#### H4 ####')\n"
        "st.markdown('##### H5 #####')\n"
        "st.markdown('###### H6 ######')\n")
st.markdown('# H1 #')
st.markdown('## H2 ##')
st.markdown('### H3 ###')
st.markdown('#### H4 ####')
st.markdown('##### H5 #####')
st.markdown('###### H6 ######')
st.markdown("- ๋ชฉ๋ก์ผ๋ก ๊ธ์ ์์ฑํ  ์ ์์ต๋๋ค.\n")

st.code("# ์์๊ฐ ์๋ ๋ชฉ๋ก(์ซ์+์ '.' ์ฌ์ฉ)\n"
        "st.markdown('1. ํ๋)\n"
        "st.markdown('2. ๋)\n"
        "st.markdown('3. ์)\n"
        "# ์์๊ฐ ์๋ ๋ชฉ๋ก(๊ธ ๋จธ๋ฆฌ ๊ธฐํธ '*, +, -' ์ฌ์ฉ\n"
        "st.markdown('* ํ๋')\n"
        "st.markdown('* ๋')\n"
        "st.markdown('* ์')\n")
st.markdown('1. ํ๋')
st.markdown('2. ๋')
st.markdown('3. ์')
st.markdown('* ํ๋')
st.markdown('* ๋')
st.markdown('* ์')
st.markdown("---")

st.subheader("4. Caption ์ถ๋ ฅํ๊ธฐ")
st.markdown("Caption์ ์บก์, ์ฌ๋ฐฑ, ๊ฐ์ฃผ ๋ฐ ๊ธฐํ ์ค๋ช ํ์คํธ๋ก ์ถ๋ ฅ ์ ์ฌ์ฉํฉ๋๋ค.")

st.code("st.caption('์ด๊ฒ์ Caption ์๋๋ค.')\n")
st.markdown("---")

st.subheader("5. ๊ทธ ์ธ Text ํ์ ์ถ๋ ฅํ๊ธฐ")

st.code("st.text('๊ธฐ๋ณธ ํ์คํธ๋ฅผ ์๋ ฅํฉ๋๋ค.')\n"
        "st.code('์ฝ๋ ๋ธ๋ก ํ์๊ฐ ๊ฐ๋ฅํฉ๋๋ค.')")
st.text('๊ธฐ๋ณธ ํ์คํธ๋ฅผ ์๋ ฅํฉ๋๋ค.')
st.code('์ฝ๋ ๋ธ๋ก ํ์๊ฐ ๊ฐ๋ฅํฉ๋๋ค.')


import streamlit as st

st.header("π₯ λ°°ν¬νκΈ°")

st.subheader("1. Github Repository μμ±νκΈ°")
st.markdown("#### β  Pycharm λ©λ΄μμ 'VCS > Create Git Repository' μ ν \n")
st.image("./image/5-1.Create Git Repository.jpg")

st.markdown("#### β‘ Git Repositoryλ₯Ό μμ±νκ³ μ νλ νλ‘μ νΈ λλ ν λ¦¬ μ ν \n")
st.image("./image/5-2.Select directory.jpg")

st.markdown("- λλ ν λ¦¬ μ ν ν μ°μΈ‘ μλ¨μ Git Menu μμ± νμΈ [**:blue[β(Pull)]**, :green[β(Commit)], **:green[β(Push)]]**")
st.image("./image/5-4.Git Menu Button.jpg")

st.markdown("#### β’ Git :green[β(Commit)] νκΈ°\n")
st.markdown("- Unversioned Files μ²΄ν¬ λ°μ€λ₯Ό μ²΄ν¬νμ¬ νλ‘μ νΈμ νμΌλ€μ μΆκ° ν νλ¨μ 'Commit' ν΄λ¦­")
st.image("./image/5-3.Git Commit.jpg")

st.markdown("#### β£ Pycharm λ©λ΄μμ 'Git > GitHub > Share Project GitHub' μ ννμ¬ Repository μμ±κ³Ό :green[β(Push)] μλ£νκΈ°\n")
st.image("./image/5-4.Share Project On GitHub.jpg")
st.markdown("- GitHub μ¬μ΄νΈμ μ μνμ¬ Repository μμ±μ΄ μλ£λ κ²μ νμΈ")
st.image("./image/5-5.GitHub Push.jpg")
st.markdown("---")

st.subheader("2. Streamlit νμ κ°μνκΈ°")
st.markdown("#### β  [Streamlit(https://streamlit.io/)](https://streamlit.io/) μ¬μ΄νΈ μ μνκΈ°\n")
st.markdown("μ°μΈ‘ μλ¨ ***:red['Sign up']*** λ²νΌ ν΄λ¦­")
st.image("./image/0-4.Streamlit Site.jpg")
st.markdown("#### β‘ 'Continue with Google' λλ 'Continue with GitHub'μ μ ννμ¬ νμ κ°μ μλ£νκΈ°\n")
st.image("./image/0-5.Streamlit Sign up.jpg")
st.caption(" **Streamlit Cloud λ°°ν¬λ₯Ό μν΄μ  :green[GitHub] μμ΄λκ° νμν©λλ€. κ°κΈμ  :green[GitHub] μμ΄λλ‘ νμ κ°μμ μΆμ² λλ¦½λλ€.**")
st.markdown("---")

st.subheader("3. Streamlit Cloudμ New App μΆκ°νκΈ°")
st.markdown("#### β  κ³μ μ λ‘κ·ΈμΈ ν νλ©΄μμ 'New app' λ²νΌ ν΄λ¦­ν©λλ€.\n")
st.image("./image/5-6.New App.jpg")
st.markdown("#### β‘ Deploy an app νλ©΄μμ GitHub Repository κ΄λ ¨ μ λ³΄λ₯Ό μλ ₯νκ³  Deploy λ²νΌμ ν΄λ¦­ν©λλ€.\n"
            "> - Repository : Github Repository URL(https://github.com/ λ€μ μ£Όμ)\n"
            "> - Branch : master (λλ Main Branch μ€μ  κ°)\n"
            "> - Main file path : Main.py")
st.image("./image/5-7.Deploy an app.jpg")
st.markdown("- 'Your app is in the oven' μ΄λΌλ λ©μμ§κ° λ¬ ν λͺ λΆμ΄ μ§λ ν,\n"
            " 'localhos:8501'μ λ¨λ μΉ νμ΄μ§κ° νμΈλλ€λ©΄ λ°°ν¬κ° μλ£λ κ²μλλ€.")

st.markdown("---")
st.subheader("[Tip] λ³λμ ν¨ν€μ§(λλ νΉμ  λ²μ )λ₯Ό μ€μΉν κ²½μ°")
st.markdown("PythonμΌλ‘ νλ‘μ νΈλ₯Ό μ§ννκ² λλ©΄ pipλ‘ μ¬λ¬ ν¨ν€μ§λ₯Ό μ€μΉνλ κ²½μ°κ° λ°μν©λλ€.\n"
            "κ·Έλ° κ²½μ° λ°°ν¬λλ μλ²μλ λμΌν ν¨ν€μ§λ€μ΄ μ€μΉλμ΄ μμ΄μΌ ν©λλ€.\n"
            "μ΄ λ, pipλ‘ μ€μΉλ ν¨ν€μ§ λ¦¬μ€νΈλ₯Ό 'requirements.txt'λ‘ μ μ₯ν΄ λλ©΄ Streamlit Coloudμμ μλμΌλ‘ μ€μΉκ° μ§νλ©λλ€.\n")
st.markdown("- ν°λ―Έλ μ°½μμ λ€μ λͺλ Ήμ΄λ₯Ό μ€ννλ©΄ μ€μΉλ ν¨ν€μ§ λ¦¬μ€νΈλ₯Ό νμΈν  μ μμ΅λλ€.")
st.code("pip list")
st.markdown("- ν°λ―Έλ μ°½μμ λ€μ λͺλ Ήμ΄λ₯Ό μ€ννμ¬ ν¨ν€μ§ λͺ©λ‘μ μ μ₯ν 'requirements.txt' νμΌμ μμ±ν©λλ€.")
st.code("pip list --format=freeze > requirements.txt")
st.markdown("- μμ±λ 'requirements.txt' :green[β(Commit)], **:green[β(Push)]]** νμ¬ μλ£ν©λλ€.\n")

st.markdown("---")
st.markdown("## μΆν λλ¦½λλ€.πππππ\n")
st.markdown("#### μ΄μ  μ΄λμλ  λκ΅¬λ μ μ κ°λ₯ν μ¬λ¬λΆμ μΉ νμ΄μ§λ₯Ό λ§λμ¨μ΅λλ€.\n")
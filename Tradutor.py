
import streamlit as st
import google.generativeai as gen_ai

api_keey = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_keey)

model = genai.GenerativeModel("gemini-1.5-pro")

st.title("Gemini FIPP Translator")

idiomas = [
    "Inglês", "Espanhol", "Francês", "Alemão", "Italiano", "Português", 
    "Russo", "Japonês", "Chinês", "Coreano", "Árabe", "Hindi", "Turco"]

texto_idioma_entrada = st.selectbox("Escolha o aqui o idioma de entrada:",idiomas)
texto_idioma_saida = st.selectbox("Escolha o aqui o idioma de saída:",idiomas)

input_text = st.text_area("Digite aqui o texto que deseja traduzir:", height=180)
st.caption("Digite o texto corretamente utilizando o mesmo idioma selecionado para evitar erros.")

system_instructions = (
    "você é um assistente de tradução. Sempre traduza o texto para o idioma que o usuario selecionou (texto do idioma de entrada traduzido para o idioma de saida)\n"
    "mostre apenas a linha traduzida\n"
    "se o texto de entrada não for o mesmo que o idioma de entrada selecionado, informe o usuário com uma mensagem de erro."
    "caso os dois idiomas selecionados tanto de entrada e de saida forem os mesmos, informe uma mensagem de erro no idioma selecionado"
)


if st.button("traduzir"):
    if input_text:
        st.write("Tradução:")
        with st.spinner('Traduzindo...'):
            prompt = "Siga essas instruçoes: " + system_instructions + "\nIdioma de entrada: " + texto_idioma_entrada + "\nTexto de entrada: " + '"'+input_text+'"' + "\nIdioma de saida: " + texto_idioma_saida
            response = model.generate_content(prompt)
            st.write(response.text)

    else:
        st.write("por favor, digite um texto para traduzir.")

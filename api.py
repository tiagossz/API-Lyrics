import streamlit as st
import requests

def buscar_letra(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    letra = response.json()['lyrics']  if response.status_code == 200 else ""
    return letra

st.image("https://img.freepik.com/vetores-gratis/notas-de-musica-arco-iris-colorido-com-disco-de-vinil-em-fundo-branco_1308-93455.jpg?semt=ais_rp_progressive&w=740&q=80")
st.title("Letras de Músicas")

banda = st.text_input("Digite o nome do Cantor(a)", key='banda')
musica = st.text_input("Digite o nome da música", key='musica')
pesquisar = st.button("Pesquisar")

if pesquisar:
    letra = buscar_letra(banda, musica)
    if letra:
        st.success("Encontramos a letra da música:")
        st.text(letra)
    else:
        st.error("Não foi possivel encontrar o conteúdo")
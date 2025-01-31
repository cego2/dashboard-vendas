import streamlit as st
import time

def main():
    st.title('Aprendendo Streamlit')
    st.write('Aprender python é muito legal :) ')

    st.header('Input texto')
    input_text = st.text_input('Digite aqui por gentileza')
    if input_text:
        st.write('Você digitou:', input_text)

    st.header('Slider')
    slider_value = st.slider('Escola um valor', 0, 100, 50)
    st.write('Opção Escolhiada:', slider_value)

    st.header('Seleção')
    selected_option = st.selectbox('Selecione uma opção',[
                                   'Opção 1', 'Opção 2', 'Opção 3'])
    if selected_option:
        st.write('Opção selecionada:', selected_option)

    st.header('Checkbox')
    checkbox_state = st.checkbox('Marque para ativar')
    st.write('Checkbox ativado:', checkbox_state)

    st.header('Botão')
    if st.button('Clique aqui'):
        st.write('Você clicou no botão!')

    st.header('Loading')
    with st.spinner('Carregando...'):
        time.sleep(3)
    st.success('Carregado com sucesso!')

    st.header('Upload de arquivo')
    upload_file = st.file_uploader('Escolha um arquivo', type=['pdf', 'xlsx', 'csv'])
    if upload_file:
        st.write('Nome do Arquivo:', upload_file)

    st.header('Gráfico')
    data = {'x': [1,2,3,4,5], 'y':[10, 20, 15, 22, 30]}
    st.line_chart(data)

main()
import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    # Carregar os dados
    data = pd.read_excel('Base.xlsx', sheet_name='Base')
    #Titulo
    title = "Dashboard de Vendas"
    st.set_page_config(page_title=title, layout="wide")
    st.title(title)

    # Criar filtros
    anos = data['Ano'].unique()
    paises = data['País'].unique()

    filtro_ano = st.sidebar.selectbox("Selecione o Ano:", options=["Todos"] + sorted(anos), index=0)
    filtro_pais = st.sidebar.selectbox("Selecione o País:", options=["Todos"] + sorted(paises), index=0)

    # Criar uma cópia para aplicar os filtros
    data_filtrada = data
    if filtro_ano != "Todos":
        data_filtrada = data_filtrada[data_filtrada['Ano'] == filtro_ano]
    if filtro_pais != "Todos":
        data_filtrada = data_filtrada[data_filtrada['País'] == filtro_pais]

    # Gráfico 1: Lucro por Segmento
    grafico_lucro_segmento = px.bar(
        data_filtrada.groupby('Segmento')["Lucro"].sum().reset.index(),
        x='Segmento', y='Lucro',
        title="Lucro por Segmento",
        color='Segmento',
        text_auto=True
    )
    grafico_lucro_segmento.update_layout(showlegend=False)

    # Gráfico 2: Vendas Brutas ao longo do tempo
    grafico_vendas_tempo = px.line(
        data_filtrada.groupby(['Data'])["Vendas Brutas"].sum().reset_index(),
        x='Data', y='Vendas Brutas',
        title="Vendas Brutas ao Longo do Tempo",
        markers=True
    )
    # Gráfico 3: Distribuição de Produtos Vendidos
    grafico_distribuicao_produtos = px.pie(
        data_filtrada.groupby('Produto')["Unidades Vendidas"].sum().reset_index(),
        values='Unidades Vendidas', names='Produto',
        title="Distribuição de Produtos Vendidos"
    )
    # Gráfico 4: Relação entre Custo e Lucro
    custo_lucro_data = data_filtrada.groupby(['Segmento'])[['COGS', 'Lucro']].sum().reset_index().melt(
        id_vars='Segmento', value_vars=['COGS', 'Lucro'])
    custo_lucro_data['value_formatado'] = custo_lucro_data['value'].apply(lambda x: f"R$ {x:,.2f}")

    grafico_custo_lucro = px.bar(
        custo_lucro_data,
        x='Segmento', y='value',
        title="Relação entre Custo e Lucro",
        color='variable',
        barmode='group',
        text='value_formatado'
    )

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col1.plotly_chart(grafico_lucro_segmento, use_container_width=True)
    col2.plotly_chart(grafico_vendas_tempo, use_container_width=True)
    col3.plotly_chart(grafico_distribuicao_produtos, use_container_width=True)
    col4.plotly_chart(grafico_custo_lucro, use_container_width=True)

main()


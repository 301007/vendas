import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo a Base de Dados:
df = pd.read_excel('Vendas.xlsx')

#Criando a coluna Loja:
import pandas as pd
import string

df2 = pd.DataFrame({'LojaID': [1520, 1522, 1521, 1523, 1037, 1034, 1035, 1036,  981,  983,  980, 982]})

# Lista de letras (pode expandir se tiver mais de 26 lojas)
letras = list(string.ascii_uppercase)

# Criar mapeamento dos IDs para letras
ids_unicos = df['LojaID'].unique()
mapa = {loja: letras[i] for i, loja in enumerate(ids_unicos)}

# Criar nova coluna com a letra correspondente
df['Loja'] = df['LojaID'].map(mapa)

# Agrupamentos:
df['Ano'] = df['Ano'].astype(str)
vendas_ano = df.groupby('Ano', as_index=False)['Receita'].sum()
vendas_cidade = df.groupby('Cidade')['Receita'].sum().reset_index().sort_values(by='Receita')
vendas_loja = df.groupby('Loja')['Receita'].sum().reset_index().sort_values(by='Receita')
qtde_vendas_loja = df.groupby('Loja')['Qtde'].sum().reset_index().sort_values(by='Qtde')

#criando uma função:
def main():
    st.title('Vendas entre 2018 à 2019')
    st.image('vendas.png')

    #Cálculos:
    total_receita = df['Receita'].sum()

    #Criando o Cartão:
    col1 =st.columns(1)[0]
    col1.metric('Receita Total', f"R$ {total_receita:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

    #Criando os Gráficos:
    col1, col2 = st.columns(2)

    vendas_ano['Ano'] = vendas_ano['Ano'].astype(str)
    fig1 = px.bar(vendas_ano, x='Ano', y='Receita', title='Receita x Ano', text='Receita', color='Ano',
                  width=450, height=400)
    col1.plotly_chart(fig1)
    
    fig2= px.bar(vendas_cidade, x='Receita', y='Cidade', orientation='h', color='Receita', color_continuous_scale='Blues',
                 title='Vendas x Cidade', text='Receita', width=450, height=400)
    col2.plotly_chart(fig2)

    col3, col4 = st.columns(2)

    fig3 = px.bar(vendas_loja, x='Receita', y='Loja', orientation='h', title='Total de Vendas x Loja', color='Receita', color_continuous_scale='Blues', text='Receita',
                  width=600, height=450)
    col3.plotly_chart(fig3)

    fig4 = px.bar(qtde_vendas_loja, x='Qtde', y='Loja', orientation='h', title='Quantidade de Vendas x Loja', color='Qtde', color_continuous_scale='Blues', text='Qtde',
                  width=600, height=450)
    col4.plotly_chart(fig4)


if __name__ == '__main__':
    main()
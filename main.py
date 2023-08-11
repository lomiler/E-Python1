# pandas
# openpyxl -> Python x Excel
# twilio -> Python x SMS

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "zz"
# Your Auth Token from twilio.com/console
auth_token  = "zz"
client = Client(account_sid, auth_token)


# Abrir os arquivos em Excel
lista_meses = ['janeiro','fevereiro']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx',engine='openpyxl')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas {vendas}')
        message = client.messages.create(
        to="+55zz", 
        from_="+12zz",
        body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas {vendas}')

        print(message.sid)

# Para cada Arquivo:
# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
# Se for maior do que 55.000 -> Enviar um SMS com o Nome, o mês e as vendas do vendedor
# Caso não seja maior que 55.000 não quero faer nada
# Solicita ao usuário o número de diárias e armazena na variável 'dias'
dias = int(input("Quantas diárias? "))

# Solicita ao usuário o nome da cidade e armazena na variável 'cidade'
cidade = input("Qual a cidade? [Salvador, Fortaleza, Natal ou Aracaju]: ")

# Define uma lista com as distâncias de Recife para as cidades especificadas
distancias = [850, 800, 300, 550]

# Define uma lista com os custos dos passeios diários para as cidades especificadas
passeio = [200, 400, 250, 300]

# Define o consumo de combustível do carro (km por litro)
km_l = 14

# Define o custo do litro de gasolina em reais
gasolina = 5

# Função para calcular o gasto com hotel, com base no número de diárias
def gasto_hotel(dias):
    return 150 * dias

# Função para calcular o gasto com gasolina, com base na cidade de destino
def gasto_gasolina(cidade):
    if cidade == "Salvador":
        return (2 * distancias[0] * gasolina) / km_l  # Ida e volta
    elif cidade == "Fortaleza":
        return (2 * distancias[1] * gasolina) / km_l  # Ida e volta
    elif cidade == "Natal":
        return (2 * distancias[2] * gasolina) / km_l  # Ida e volta
    elif cidade == "Aracaju":
        return (2 * distancias[3] * gasolina) / km_l  # Ida e volta

# Função para calcular o gasto com passeios, com base na cidade de destino e no número de dias
def gasto_passeio(cidade, dias):
    if cidade == "Salvador":
        return passeio[0] * dias
    elif cidade == "Fortaleza":
        return passeio[1] * dias
    elif cidade == "Natal":
        return passeio[2] * dias 
    elif cidade == "Aracaju":
        return passeio[3] * dias 

# Calcula o gasto total somando os gastos com hotel, gasolina e passeios
gastos = gasto_hotel(dias) + gasto_gasolina(cidade) + gasto_passeio(cidade, dias)

# Imprime o custo total da viagem formatado com duas casas decimais
print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {round(gastos, 2)} reais")

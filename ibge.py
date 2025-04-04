import requests

def listar_cidades_por_estado(uf):
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
    response = requests.get(url)

    if response.status_code == 200:
        municipios = response.json()
        for municipio in municipios:
            print(municipio['nome'])
    else:
        print("Erro ao acessar a API:", response.status_code)

listar_cidades_por_estado('PB')

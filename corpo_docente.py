# Importação das bibliotecas necessárias
import pandas as pd  # Manipulação de dados em formato tabular
import requests  # Requisições HTTP
from bs4 import BeautifulSoup  # Parsear e extrair dados do HTML

def extrair_dados_docentes():
    url = "https://www.ifpb.edu.br/ppgti/programa/corpo-docente"
    response = requests.get(url)
    
    # Verificando se a requisição foi bem sucedida (código 200) e definindo o objeto BeautifulSoup para parsear o HTML
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        docentes = []
        
        # Encontra a div principal que contém os dados dos docentes
        conteudo = soup.find('div', id='parent-fieldname-text')
        if conteudo:
            # Realizando busca sobre todos os elementos h4 que contêm as informações dos docentes
            for h4 in conteudo.find_all('h4'):
                nome = h4.text.strip()
                if nome and not nome.startswith('Docentes'):  
                    p = h4.find_next('p')
                    if p:
                        linha_pesquisa = ''
                        if 'Linha de Pesquisa:' in p.text:
                            # Extrai o texto da linha de pesquisa usando separador <br>
                            texto = p.get_text(separator='<br>', strip=True)
                            partes = texto.split('Linha de Pesquisa:')
                            if len(partes) > 1:
                                linha_pesquisa = partes[1].split('<br>')[0].strip()
                        
                        lattes = ''
                        lattes_link = p.find('a', href=lambda x: x and 'lattes.cnpq.br' in x)
                        if lattes_link:
                            lattes = lattes_link['href']
                        
                        email = ''
                        email_link = p.find('a', href=lambda x: x and 'mailto:' in x)
                        if email_link:
                            email = email_link['href'].replace('mailto:', '')
                        else:
                            email_text = p.text.split('E-mail:')
                            if len(email_text) > 1:
                                email = email_text[1].strip()
                        
                        proximo_p = p.find_next('p')
                        if proximo_p and 'E-mail:' in proximo_p.text:
                            email = proximo_p.text.split('E-mail:')[1].strip()
                        
                        # Adiciona os dados do docente à lista
                        docentes.append({
                            'Nome': nome,
                            'Linha de Pesquisa': linha_pesquisa,
                            'URL Lattes': lattes,
                            'E-mail': email
                        })
        
        # Converte a lista de docentes em um DataFrame do pandas
        df = pd.DataFrame(docentes)
        
        # Exibe os dados extraídos
        print("\nDados dos Docentes:")
        print(df)
        
        # Criação de arquivo CSV com codificação UTF-8
        df.to_csv('docentes_ppgti.csv', index=False, encoding='utf-8-sig')
        print("\nDados salvos em 'docentes_ppgti.csv'")
    else:
        print("Erro ao acessar a página:", response.status_code)

extrair_dados_docentes()
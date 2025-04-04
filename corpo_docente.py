import pandas as pd
import requests
from bs4 import BeautifulSoup


def extrair_dados_docentes():
    url = "https://www.ifpb.edu.br/ppgti/programa/corpo-docente"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        docentes = []
        
        conteudo = soup.find('div', id='parent-fieldname-text')
        if conteudo:
        
            for h4 in conteudo.find_all('h4'):
                nome = h4.text.strip()
                if nome and not nome.startswith('Docentes'):  

                    p = h4.find_next('p')
                    if p:

                        linha_pesquisa = ''
                        if 'Linha de Pesquisa:' in p.text:
                            linha_pesquisa = p.text.split('Linha de Pesquisa:')[1].split('<br>')[0].strip()
                        
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
                        
                        docentes.append({
                            'Nome': nome,
                            'Linha de Pesquisa': linha_pesquisa,
                            'URL Lattes': lattes,
                            'E-mail': email
                        })
        
       
        df = pd.DataFrame(docentes)
        
        
        print("\nDados dos Docentes:")
        print(df)
        
        df.to_csv('docentes_ppgti.csv', index=False, encoding='utf-8')
        print("\nDados salvos em 'docentes_ppgti.csv'")
    else:
        print("Erro ao acessar a página:", response.status_code)

extrair_dados_docentes()
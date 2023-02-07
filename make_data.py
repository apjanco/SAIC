import srsly
import spacy
from spacy.matcher import PhraseMatcher
import pandas as pd 
from tqdm import tqdm 

data = srsly.read_json("all_the_data.json")
nlp = spacy.blank("pt")
matcher = PhraseMatcher(nlp.vocab)
terms = [
    "ORIGEM",
    "DATA",
    "FORMUL",
    "DV",
    "TIPO",
    "NOME",
    "ENDEREÇO",
    "MUNICIPIO",
    "UF",
    "CEP",
    "SEXO",
    "MORADOR",
    "INSTRUÇÃO",
    "ESTADO CIVIL",
    "FAIXA ETÁRIA",
    "FAIXA RENDA",
    "ATIVIDADE",
    "DESTINATÁRIO",
    "CATÁLOGO",
    "INDEXAÇÃO",
    "SUGESTÃO"
]
# Only run nlp.make_doc to speed things up
patterns = [nlp.make_doc(text) for text in terms]
matcher.add("TerminologyList", patterns)
df_data = []
errors = []
for person in tqdm(data.keys(), total=len(list(data.keys()))):
    row = {}
    doc = nlp(data[person])
    matches = matcher(doc)
    for match_id, start, end in matches:
        if doc[start:end].text == "ORIGEM":
            ORIGEM = (start, end)
        if doc[start:end].text == "DATA":
            DATA = (start, end)
        if doc[start:end].text == "FORMUL":
            FORMUL = (start, end)
        if doc[start:end].text == "DV":
            DV = (start, end)
        if doc[start:end].text == "TIPO":
            TIPO = (start, end)
        if doc[start:end].text == "NOME":
            NOME = (start, end)
        if doc[start:end].text == "ENDEREÇO":
            ENDEREÇO = (start, end)
        if doc[start:end].text == "MUNICIPIO":
            MUNICIPIO = (start, end)
        if doc[start:end].text == "UF":
            UF = (start, end)
        if doc[start:end].text == "CEP":
            CEP = (start, end)
        if doc[start:end].text == "SEXO":
            SEXO = (start, end)    
        if doc[start:end].text == "MORADOR":
            MORADOR = (start, end)
        if doc[start:end].text == "INSTRUÇÃO":
            INSTRUÇÃO = (start, end)
        if doc[start:end].text == "ESTADO CIVIL":
            ESTADO_CIVIL = (start, end)
        if doc[start:end].text == "FAIXA ETÁRIA":
            FAIXA_ETÁRIA = (start, end)
        if doc[start:end].text == "FAIXA RENDA":
            FAIXA_RENDA = (start, end)
        if doc[start:end].text == "ATIVIDADE":
            ATIVIDADE = (start, end)
            DESTINATÁRIO = ATIVIDADE
        if doc[start:end].text == "DESTINATÁRIO":
            DESTINATÁRIO = (start, end)
        if doc[start:end].text == "CATÁLOGO":
            CATÁLOGO = (start, end)
        if doc[start:end].text == "INDEXAÇÃO":
            INDEXAÇÃO = (start, end)
        if doc[start:end].text == "SUGESTÃO":
            SUGESTÃO = (start, end)
    
    if not any(word in doc[ORIGEM[1]+1:DATA[0]].text.strip() for word in terms):
        row['ORIGEM'] = doc[ORIGEM[1]+1:DATA[0]].text.strip()
    if not any(word in doc[DATA[1]+1:FORMUL[0]].text.strip() for word in terms):
        row['DATA'] = doc[DATA[1]+1:FORMUL[0]].text.strip()
    if not any(word in doc[FORMUL[1]+1:DV[0]].text.strip() for word in terms):
        row['FORMUL'] = doc[FORMUL[1]+1:DV[0]].text.strip()
    if not any(word in doc[DV[1]+1:TIPO[0]].text.strip() for word in terms):
        row['DV'] = doc[DV[1]+1:TIPO[0]].text.strip()
    if not any(word in doc[TIPO[1]+1:NOME[0]].text.replace('\n','').strip() for word in terms):
        row['TIPO'] = doc[TIPO[1]+1:NOME[0]].text.replace('\n','').strip()
    if not any(word in doc[NOME[1]+1:ENDEREÇO[0]].text.replace('\n','').strip() for word in terms):
        row['NOME'] = doc[NOME[1]+1:ENDEREÇO[0]].text.replace('\n','').strip()
    if not any(word in doc[ENDEREÇO[1]+1:MUNICIPIO[0]].text.replace('\n','').strip() for word in terms):
        row['ENDEREÇO'] = doc[ENDEREÇO[1]+1:MUNICIPIO[0]].text.replace('\n','').replace('LOCALIZAÇÃO','').strip()
    if not any(word in doc[MUNICIPIO[1]+1:UF[0]].text.replace('\n','').strip() for word in terms):
        row['MUNICIPIO'] = doc[MUNICIPIO[1]+1:UF[0]].text.replace('\n','').strip()
    if not any(word in doc[UF[1]+1:CEP[0]].text.replace('\n','').strip() for word in terms):
        row['UF'] = doc[UF[1]+1:CEP[0]].text.replace('\n','').strip()
    if not any(word in doc[CEP[1]+1:SEXO[0]].text.replace('\n','').strip() for word in terms):
        row['CEP'] = doc[CEP[1]+1:SEXO[0]].text.replace('\n','').replace('DADOS PESSOAIS','').strip()
    if not any(word in doc[SEXO[1]+1:MORADOR[0]].text.replace('\n','').strip() for word in terms):
        row['SEXO'] = doc[SEXO[1]+1:MORADOR[0]].text.replace('\n','').replace(':','').strip()
    if not any(word in doc[MORADOR[1]+1:INSTRUÇÃO[0]].text.replace('\n','').strip() for word in terms):
        row['MORADOR'] = doc[MORADOR[1]+1:INSTRUÇÃO[0]].text.replace('\n','').replace(':','').strip()
    if not any(word in doc[INSTRUÇÃO[1]+1:ESTADO_CIVIL[0]].text.replace('\n','').strip() for word in terms):
        row['INSTRUÇÃO'] = doc[INSTRUÇÃO[1]+1:ESTADO_CIVIL[0]].text.replace('\n','').replace(':','').strip()
    if not any(word in doc[ESTADO_CIVIL[1]+1:FAIXA_ETÁRIA[0]].text.replace('\n','').strip() for word in terms):
        row['ESTADO_CIVIL'] = doc[ESTADO_CIVIL[1]+1:FAIXA_ETÁRIA[0]].text.replace('\n','').strip()
    if not any(word in doc[FAIXA_ETÁRIA[1]+1:FAIXA_RENDA[0]].text.replace('\n','').strip() for word in terms):
        row['FAIXA_ETÁRIA'] = doc[FAIXA_ETÁRIA[1]+1:FAIXA_RENDA[0]].text.replace('\n','').strip()
    if not any(word in doc[FAIXA_RENDA[1]+1:ATIVIDADE[0]].text.replace('\n','').strip() for word in terms):
        row['FAIXA_RENDA'] = doc[FAIXA_RENDA[1]+1:ATIVIDADE[0]].text.replace('\n','').strip()
    if not any(word in doc[ATIVIDADE[1]+1:DESTINATÁRIO[0]].text.replace('\n','').strip() for word in terms):
        row['ATIVIDADE'] = doc[ATIVIDADE[1]+1:DESTINATÁRIO[0]].text.replace('\n','').replace(':','').strip()
    if not any(word in doc[DESTINATÁRIO[1]+1:CATÁLOGO[0]].text.replace('\n','').strip() for word in terms):
        row['DESTINATÁRIO'] = doc[DESTINATÁRIO[1]+1:CATÁLOGO[0]].text.replace('\n','').replace(':','').strip()
    if not any(word in doc[CATÁLOGO[1]+1:INDEXAÇÃO[0]].text.replace('\n','').strip() for word in terms):
        row['CATÁLOGO'] = doc[CATÁLOGO[1]+1:INDEXAÇÃO[0]].text.replace('\n','').strip()
    if not any(word in doc[INDEXAÇÃO[1]+1:SUGESTÃO[0]].text.replace('\n','').strip() for word in terms):
        row['INDEXAÇÃO'] = doc[INDEXAÇÃO[1]+1:SUGESTÃO[0]].text.replace('\n','').strip()
    if not any(word in doc[SUGESTÃO[1]+1:].text.replace('\n','').strip() for word in terms):
        row['SUGESTÃO'] = doc[SUGESTÃO[1]+1:].text.replace('\n','').strip()
    else:
        errors.append(person)
    df_data.append(row)
df = pd.DataFrame(df_data)
df.to_csv('SAIC.tsv',sep='\t')
print(len(errors),' errors')
srsly.write_jsonl('errors.txt',errors)
## Notes 

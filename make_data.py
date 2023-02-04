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
        if doc[start:end].text == "DESTINATÁRIO":
            DESTINATÁRIO = (start, end)
        if doc[start:end].text == "CATÁLOGO":
            CATÁLOGO = (start, end)
        if doc[start:end].text == "INDEXAÇÃO":
            INDEXAÇÃO = (start, end)
        if doc[start:end].text == "SUGESTÃO":
            SUGESTÃO = (start, end)
    
    row['ORIGEM'] = doc[ORIGEM[1]+1:DATA[0]].text.strip()
    row['DATA'] = doc[DATA[1]+1:FORMUL[0]].text.strip()
    row['FORMUL'] = doc[FORMUL[1]+1:DV[0]].text.strip()
    row['DV'] = doc[DV[1]+1:TIPO[0]].text.strip()
    row['TIPO'] = doc[TIPO[1]+1:NOME[0]].text.replace('\n','').strip()
    row['NOME'] = doc[NOME[1]+1:ENDEREÇO[0]].text.replace('\n','').strip()
    row['ENDEREÇO'] = doc[ENDEREÇO[1]+1:MUNICIPIO[0]].text.replace('\n','').strip()
    row['MUNICIPIO'] = doc[MUNICIPIO[1]+1:UF[0]].text.replace('\n','').strip()
    row['UF'] = doc[UF[1]+1:CEP[0]].text.replace('\n','').strip()
    row['CEP'] = doc[CEP[1]+1:SEXO[0]].text.replace('\n','').strip()
    row['SEXO'] = doc[SEXO[1]+1:MORADOR[0]].text.replace('\n','').strip()
    row['MORADOR'] = doc[MORADOR[1]+1:INSTRUÇÃO[0]].text.replace('\n','').strip()
    row['INSTRUÇÃO'] = doc[INSTRUÇÃO[1]+1:ESTADO_CIVIL[0]].text.replace('\n','').strip()
    row['ESTADO_CIVIL'] = doc[ESTADO_CIVIL[1]+1:FAIXA_ETÁRIA[0]].text.replace('\n','').strip()
    row['FAIXA_ETÁRIA'] = doc[FAIXA_ETÁRIA[1]+1:FAIXA_RENDA[0]].text.replace('\n','').strip()
    row['FAIXA_RENDA'] = doc[FAIXA_RENDA[1]+1:ATIVIDADE[0]].text.replace('\n','').strip()
    try:
        row['ATIVIDADE'] = doc[ATIVIDADE[1]+1:DESTINATÁRIO[0]].text.replace('\n','').strip()
        row['DESTINATÁRIO'] = doc[DESTINATÁRIO[1]+1:CATÁLOGO[0]].text.replace('\n','').strip()
    except NameError:
        pass
    row['CATÁLOGO'] = doc[CATÁLOGO[1]+1:INDEXAÇÃO[0]].text.replace('\n','').strip()
    row['INDEXAÇÃO'] = doc[INDEXAÇÃO[1]+1:SUGESTÃO[0]].text.replace('\n','').strip()
    row['SUGESTÃO'] = doc[SUGESTÃO[1]+1:].text.replace('\n','').strip()
    df_data.append(row)
df = pd.DataFrame(df_data)
print(df.head())
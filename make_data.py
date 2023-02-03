import srsly
import spacy
from spacy.matcher import PhraseMatcher

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

for person in data.keys():
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
    
    row['origem'] = doc[ORIGEM[1]+1:DATA[0]].text
    row['data'] = doc[DATA[1]+1:FORMUL[0]].text
    row['formul'] = doc[FORMUL[1]+1:DV[0]].text
    row['dv'] = doc[DV[1]+1:TIPO[0]].text
    row['tipo'] = doc[TIPO[1]+1:NOME[0]].text.replace('\n','')
    row['nome'] = doc[NOME[1]+1:ENDEREÇO[0]].text.replace('\n','')
    print(row)  

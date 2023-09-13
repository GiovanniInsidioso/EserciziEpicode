 #abbiamo una lista di codici prodotto. Per ognuno estrarre la parte finale
# trattino incluso e memorizzarlo in una variabile

codici = ["knt-61", "cha-69", "qtr-78"]
cod1=codici[0][-3:]
cod2=codici[1][-3:]
cod3=codici[2][-3:]
print(cod1, " ",cod2, " ",cod3)

#le prime quadre fanno riferimento alla posizione nella liste
#le seconde gli diciamo prendi ultime 3 lettere

#Abbiamo un insieme (set) di titoli di azioni "growth" 
#(cioè che hanno una crescita dei
#ricavi maggiore della media):
growth = {"Tesla", "Shopify", "Block", "Etsy", "MercadoLibre",
"Netflix", "Amazon", "Meta Platforms", "Salesforce", "Alphabet"}

#Abbiamo un insieme di titoli "value" (cioè titoli 
#che offrono agli investitori un elevato
#ritorno sull’investimento, garantendo al contempo stabilità e sicurezza):
value = {"Pfizer", "Johnson & Johnson", "JPMorgan Chase & Co.",
"Wells Fargo & Co.", "Verizon Communications", "BP PLC",
"LyondellBasell Industries", "MetLife", "Interactive Brokers Group",
"Intel"}

#Abbiamo insieme di titoli di aziende ad alta tecnologia:
tech = {"Apple", "Microsoft", "Alphabet", "Amazon", "NVIDIA", "Meta Platforms", "Tesla", "Alibaba", "Salesforce", "Advanced Micro"
"Devices", "Intel", "PayPal", "Activision Blizzard", "Electronic Arts", "The Trade Desk", "Zillow Group", "Match Group", "Yelp"}

#Abbiamo un insieme di titoli di aziende nell'healthcare:
healthcare = {"UnitedHealth Group", "Johnson & Johnson", "Eli Lilly & Co.", "Novo Nordisk", "Merck & Co.", "Roche Holding", "Pfizer",
"Thermo Fisher Scientific", "Abbott Laboratories"}

#Un investitore vuole sapere:
#se vuole diversificare l'investimento, investendo in aziende growth e value,
#quali sono le aziende?

#devo fare un unione dei due insieme, quindi le prenderà tutto

prima_unione = growth|value
# print(prima_unione)

# oppure: 
# growth.union(value)


#quali sono le aziende tecnologiche growth?
#devo fare intersezione, quindi prenderà solo le anziende sia in growth che in tech

print(growth & tech)

#oppure
growth.intersection(tech)

#se vuole investire sia in aziende tecnologiche che value, quali deve considerare?

value.intersection(tech)

#quali sono i titoli healthcare che non sono value?
healthcare-value
healthcare.difference(value)
#ci sono aziende sia tech che healthcare?

tech.intersection(healthcare)

#in quali deve investire se vuole azioni tech 
#ma solo se siano growth o value

#unione con growth e value, poi intersezione con tech
print((growth | value) & tech)







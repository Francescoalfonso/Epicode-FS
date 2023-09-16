growth={"Tesla","Shopify","Block","Etsy","MercadoLibre","Netflix","Amazon","Meta Platforms","Salesforce","Alphabet"}
value={"Pfizer","Johnson & Johnson","JPMorgan & Co.","Wells Fargo & Co.","Verizon Communications","BP PLC","LyondellBaseball Industries","MetLife","Interactive Brokers Group","Intel"}
tech={"Apple","Microsoft","Alphabet","Amazon","NVIDIA","Meta Platforms","Tesla","Alibaba","Salesforce","Advanced Micro Devices","Intel","PayPal","Activision Blizzard","Electronic Arts","The Trade Desk", "Zillow Group", "Match Group","Yelp"}
healtacare={"UnitedHealth Group","Johnson & Johnson","Eli Lilly & Co.","Novo Nordisk","Merck & Co.","Roche Holding","Pfizer","Thermo Fisher Scientific","Abbot Laboratories"}
# Volendo diversificare investendo su growth e values uniamo i due ste in modo tale che si possa vedere in un'ica stampa le aziende che ne fanno parte  
quesito_1=growth|value
print('quesito 1 : ',quesito_1)
# Per vedere quali sono le aziende tech che fanno parte di growth facciamo l'intersezione tra i due insiemi
quesito_2=growth&tech
print('quesito 2 : ',quesito_2)
# # Per vedere quali sono le aziende tech che fanno parte di value facciamo l'intersezione tra i due insiemi
quesito_3=value&tech
print('quesito 3 : ',quesito_3)
# Se vogliamo vedere i titoli healthcare non presenti in value andiamo a fare la differenza tra i due ste
quesito_4=healtacare-value
print('quesito 4 : ',quesito_4)
# Per vedere se ci sono sia aziende tech che healthcare andiamo ad intersecare i due insiemi
quesito_5=healtacare&tech
print('quesito 5 : ',quesito_5)
# Se si vuole investire solo in azioni tech ma solo se fanno parte di growth o value, andiamo ad unire  i set growth e values e poi il tutto lo intersechiamo con il set tech
intermedio=growth|value
quesito_6=intermedio&tech
print('quesito 6 : ',quesito_6)
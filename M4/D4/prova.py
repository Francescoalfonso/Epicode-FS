studenti=['Alex','Bob','Cindy','Dan','emma','Faith','Grace']
corsi=['Cybersecurity','Data Analyst','Backend','Frontend','Data Analyst','Backend','Frontend','Cybersecurity']
edizioni=[1,2,3,2,2,1,3,3]
for studente,corso,edizione in zip(studenti,corsi,edizioni):
    if edizione==1:
        print(studente,corso,edizione) # se dovessi stampare solo gli studenti allora basta togliere corso ed edizione dalla print
         
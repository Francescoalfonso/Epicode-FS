CREATE TABLE STUDENTE (
    Matricola INT PRIMARY KEY,
    NomeStudente VARCHAR(255),
    AnnoLaurea INT,
    TitoloStudio VARCHAR(255),
    VotoLaurea DECIMAL(5, 2)
);
CREATE TABLE DIPARTIMENTO (
    CodiceDipartimento INT PRIMARY KEY,
    NomeDipartimento VARCHAR(255),
    SettoreScientifico VARCHAR(255),
    NumDocenti INT
);
CREATE TABLE CONCORSOMASTER (
    CodiceMaster INT PRIMARY KEY,
    CodiceDipartimento INT,
    DataPubblicazione DATE,
    DataScadenza DATE,
    NumPostiDisponibili INT
);
CREATE TABLE PARTECIPACONCORSOMASTER (
    CodiceDipartimento INT,
    CodiceMaster INT,
    MatricolaStudente INT,
    DataInvioDomanda DATE
);

ALTER TABLE CONCORSOMASTER
ADD FOREIGN KEY (CodiceDipartimento) REFERENCES DIPARTIMENTO(CodiceDipartimento);

ALTER TABLE PARTECIPACONCORSOMASTER
ADD FOREIGN KEY (CodiceMaster) REFERENCES CONCORSOMASTER(CodiceMaster),
ADD FOREIGN KEY (CodiceDipartimento) REFERENCES DIPARTIMENTO(CodiceDipartimento),
ADD FOREIGN KEY (MatricolaStudente) REFERENCES STUDENTE(Matricola);



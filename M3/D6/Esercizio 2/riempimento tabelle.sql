INSERT INTO STUDENTE (Matricola, NomeStudente, AnnoLaurea, TitoloStudio, VotoLaurea)
VALUES
    (1, 'Mario Rossi', 2021, 'Laurea in Informatica', 110.00),
    (2, 'Luca Bianchi', 2020, 'Laurea in Economia', 108.50),
    (3, 'Anna Verdi', 2021, 'Laurea in Fisica', 112.00),
    (4, 'Giovanna Marrone', 2019, 'Laurea in Medicina', 115.00),
    (5, 'Paolo Giallo', 2020, 'Laurea in Ingegneria', 105.00);

INSERT INTO DIPARTIMENTO (CodiceDipartimento, NomeDipartimento, SettoreScientifico, NumDocenti)
VALUES
    (101, 'Dipartimento di Informatica', 'Scienze Informatiche', 20),
    (102, 'Dipartimento di Economia', 'Scienze Economiche', 15),
    (103, 'Dipartimento di Fisica', 'Scienze Fisiche', 18);

INSERT INTO CONCORSOMASTER (CodiceMaster, CodiceDipartimento, DataPubblicazione, DataScadenza, NumPostiDisponibili)
VALUES
    (1, 101, '2023-01-10', '2023-02-15', 10),
    (2, 101, '2023-01-10', '2023-03-20', 5),
    (3, 102, '2023-01-20', '2023-02-28', 8),
    (4, 103, '2023-02-10', '2023-03-15', 15),
    (5, 103, '2023-02-10', '2023-03-15', 8);
INSERT INTO PARTECIPACONCORSOMASTER (CodiceDipartimento, CodiceMaster, MatricolaStudente, DataInvioDomanda)
VALUES
    (101, 1, 1, '2023-01-15'),
    (101, 1, 2, '2023-01-16'),
    (101, 2, 1, '2023-02-08'),
    (101, 2, 3, '2023-02-10'),
    (102, 3, 4, '2023-01-25'),
    (103, 4, 5, '2023-02-12');

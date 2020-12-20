USE BLG317;

INSERT INTO 
	paramedic(TCKN,name,surname,hospital,filiation_team)
VALUES
	(1,'Doktor1Name','Doktor1Surname',16001,1),
	(2,'Doktor1Name','Doktor2Surname',16002,NULL),
    (3,'Doktor3Name','Doktor3Surname',16001,1),
    (4,'Doktor4Name','Doktor5Surname',16003,2),
    (5,'Doktor5Name','Doktor5Surname',16004,NULL),
    (6,'Doktor6Name','Doktor7Surname',16005,1),
    (7,'Doktor7Name','Doktor7Surname',16003,3);

SELECT * FROM paramedic;
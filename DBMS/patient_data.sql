USE BLG317;

INSERT INTO 
	patient(TCKN,name,surname,age,gender,phone,adress,illness)
VALUES
	(12345678901,'Barış','İncesu',21,'m',05054241122,'Bünyan',1),
	(34561237890,'Meriç','İncesu',13,'f',05361234455,'Konya',2),
    (90871234567,'Oya','İncesu',47,'f',055543216677,'Seydişehir',6),
    (12347651212,'Emrullah','İncesu',48,'m',05349871234,'Büyüktuzhisar',3),
    (15017009210,'Barış','İncesucu',21,'m',05054241122,'Lüleburgaz',NULL),
    (15017000912,'Samet','Çobanlı',21,'m',05061239900,'Kayseri Sivas Cd. Erkilet',NULL),
    (15017000113,'İnci','Paşa',21,'f',05431234567,NULL,NULL),
    (15017002414,'Berdan','Çağlar',21,'m',05433218765,'Mudanya Cd.',4);

SELECT * FROM patient;
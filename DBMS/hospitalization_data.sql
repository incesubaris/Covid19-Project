USE BLG317;

INSERT INTO 
	hospitalization (patient,hospital,paramedic,start_date,end_date,status)
VALUES
	(12345678901,16001,1,'2020-12-20','2020-12-26','taburcu'),
	(12347651212,16001,1,'2020-12-20','2020-12-26','entübe'),
    (90871234567,16001,1,'2020-12-18',NULL,'taburcu'),
    (15017002414,16001,1,'2020-12-20','2020-12-26','taburcu'),
    (15017009210,16001,1,'2020-12-19',NULL,'taburcu'),
    (34561237890,16001,1,'2020-12-20','2020-12-26','taburcu'),
    (15017000912,16001,1,'2020-12-20','2020-12-26','yoğun bakım');

SELECT * FROM hospitalization;
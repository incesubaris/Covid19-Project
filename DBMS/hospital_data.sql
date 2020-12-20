USE BLG317;

INSERT INTO 
	hospital(name,paramedic_count,capacity)
VALUES
	('Mudanya Devlet Hastanesi',100,200),
	('Çekirge Devlet Hastanesi',75,125),
    ('Bursa Şehir Hastanesi',1000,4000),
    ('Özel Uludağ Hastanesi',30,60),
    ('Özel Erikli Hastanesi',15,50),
    ('Uludağ Üniversitesi Hastanesi',500,3000);

SELECT * FROM hospital;
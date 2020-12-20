/* Data Definition Language */
DROP DATABASE BLG317;
CREATE DATABASE BLG317;
USE BLG317;

CREATE TABLE chronic_illness(
    id INT AUTO_INCREMENT,
    illness VARCHAR(20) NOT NULL UNIQUE,
    PRIMARY KEY(id)
);

CREATE TABLE patient(
    TCKN BIGINT(11),
    name VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    age TINYINT NOT NULL,
    gender CHAR(1),
    phone BIGINT(11),
    adress VARCHAR(50),
    illness INT DEFAULT 000,
    PRIMARY KEY(TCKN),
    FOREIGN KEY (illness) REFERENCES chronic_illness(id)
);

CREATE TABLE hospital(
    id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    paramedic_count INT DEFAULT 0,
    capacity INT DEFAULT 0,
    PRIMARY KEY(id)
);

CREATE TABLE test(
    id INT AUTO_INCREMENT,
    patient BIGINT NOT NULL,
    hospital INT NOT NULL,
    test_date DATE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (patient) REFERENCES patient(TCKN),
    FOREIGN KEY (hospital) REFERENCES hospital(id)
);

CREATE TABLE filiation(
    id INT,
    religion VARCHAR(50) NOT NULL,
    member_count INT NOT NULL DEFAULT 0,
    capacity INT NOT NULL DEFAULT 0,
    PRIMARY KEY(id)
);

CREATE TABLE paramedic(
    TCKN BIGINT(11),
    filiation_team INT,
    hospital INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    capacity INT DEFAULT 0,
    PRIMARY KEY(TCKN),
    FOREIGN KEY(filiation_team) REFERENCES filiation(id),
    FOREIGN KEY(hospital) REFERENCES hospital(id)
);

CREATE TABLE hospitalization(
    id INT AUTO_INCREMENT,
    patient BIGINT(11) NOT NULL,
    hospital INT NOT NULL,
    paramedic BIGINT(11) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status VARCHAR(50),
    PRIMARY KEY(id),
    FOREIGN KEY(patient) REFERENCES patient(TCKN),
    FOREIGN KEY(hospital) REFERENCES hospital(id),
    FOREIGN KEY(paramedic) REFERENCES paramedic(TCKN)
);

CREATE TABLE homecare(
    id INT AUTO_INCREMENT,
    patient BIGINT(11) NOT NULL,
    filiation_team INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    PRIMARY KEY(id),
    FOREIGN KEY(patient) REFERENCES patient(TCKN),
    FOREIGN KEY(filiation_team) REFERENCES filiation(id)
);
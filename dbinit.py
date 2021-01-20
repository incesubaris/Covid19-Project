import os
import sys

import psycopg2 as dbapi2

INIT_STATEMENTS = [
    """CREATE SCHEMA IF NOT EXISTS PUBLIC;""",
    """CREATE TABLE IF NOT EXISTS PUBLIC.patient (
    	"tckn" VARCHAR(11),
        "name" VARCHAR(20) NOT NULL,
        "surname" VARCHAR(20) NOT NULL,
        "age" INT NOT NULL,
        "gender" CHAR(1) NOT NULL,
        "phone" VARCHAR(11),
        "adress" VARCHAR(50),
        "password" VARCHAR(255),
        PRIMARY KEY("TCKN")
        );""",
    """CREATE TABLE IF NOT EXISTS PUBLIC.hospital (
        "id" SERIAL,
        "name" VARCHAR(50) NOT NULL,
        "paramedic_count" INT DEFAULT 0,
        "capacity" INT DEFAULT 0,
        PRIMARY KEY(id)
        );""",
    """CREATE TABLE IF NOT EXISTS PUBLIC.test (
        "id" SERIAL,
        "patient" VARCHAR(11) NOT NULL,
        "hospital" INT NOT NULL,
        "test_date" DATE NOT NULL,
		"result" CHAR(1) NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (patient) REFERENCES patient(TCKN),
        FOREIGN KEY (hospital) REFERENCES hospital(id)
        );""",
]
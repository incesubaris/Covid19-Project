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
        PRIMARY KEY("tckn")
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
        FOREIGN KEY (patient) REFERENCES patient(tckn),
        FOREIGN KEY (hospital) REFERENCES hospital(id)
        );""",
]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = "postgres://cmwnxxaaygjldp:31b8a72313d52d8366f032b9ad669f7e91cef2aa3290866caf09345f84c562f1@ec2-52-2-6-71.compute-1.amazonaws.com:5432/d37b6b1t8t884a"
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
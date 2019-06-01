Local
=====================

DATABASE used: POSTGRES :-
___________________________


sudo su - postgres
psql


DROP DATABASE datapeace_db;
CREATE DATABASE datapeace_db;

CREATE USER datapeace_user WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE datapeace_db TO datapeace_user;

_____________________________________________________________________

To download all requirements:
-----------------------------

pip install -r requirements.txt
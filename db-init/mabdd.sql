CREATE SCHEMA IF NOT EXISTS mabdd;
USE mabdd;

CREATE TABLE utilisateur (
    id INT PRIMARY KEY,
    nom VARCHAR(30) NOT NULL,
    prenom VARCHAR(30) NOT NULL
);

INSERT INTO utilisateur VALUES('1','Machin','Martin');
INSERT INTO utilisateur VALUES('2','Truc','Marcel');
INSERT INTO utilisateur VALUES('3','Bidule','Joséphine');
INSERT INTO utilisateur VALUES('4','Chose','Albert');
drop database if exists Cadastro;
create database Cadastro;
use Cadastro;

create table Cadastro (
	Nome varchar(50), 
    Sobrenome varchar(50),
    Idade int(50),
    Sexo varchar(50)
);

INSERT INTO Cadastro (Nome, Sobrenome, Idade, Sexo) VALUES ('Lucas', 'Chambi', 18, 'masculino');

Select * from Cadastro
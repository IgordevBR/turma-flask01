create database 'escola_db';

create table 'tb_alunos'(
    id bigint auto_increment primary key,
    nome varchar(150) not null,
    email varchar(50) not null unique,
    senha varchar(19) not null,
    telefone varchar(15) not null
);
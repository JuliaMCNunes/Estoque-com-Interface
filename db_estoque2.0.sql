create database estoque2;
use estoque2;

create table Fabricantes (
codigo int auto_increment,
nome varchar(60),
cnpj varchar(60),
razao_social varchar(60),
primary key (codigo));

create table Produtos (
cod int auto_increment,
descricao varchar(100),
valor float,
quantidade int, 
codigo_fabricante int not null, 
primary key (cod, codigo_fabricante));

alter table Produtos add foreign key (codigo_fabricante) references Fabricantes(codigo);

create table Entrada (
cod int auto_increment,
primary key (cod));

alter table Entrada add column observacoes varchar(400);

create table Entrada_Produtos (
cod_entrada int,
cod_produtos int,
primary key (cod_entrada, cod_produtos),
foreign key (cod_entrada) references Entrada (cod),
foreign key (cod_produtos) references Produtos (cod));

alter table Entrada_Produtos add column dataEntrada timestamp;

create table Saida (
cod int auto_increment,
primary key (cod));

alter table Saida add column observacoes varchar(400);

create table Saida_Produtos (
cod_saida int,
cod_produtos int,
primary key (cod_saida, cod_produtos),
foreign key (cod_saida) references Saida (cod),
foreign key (cod_produtos) references Produtos (cod));

alter table Saida_Produtos add column dataEntrada timestamp;

select * from Produtos;
select * from Fabricantes;
select * from Entrada;
select * from Entrada_Produtos;
select * from Saida;
select * from Saida_Produtos;

update Produtos set quantidade = 0 where cod = 3;

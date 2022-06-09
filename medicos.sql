create database consultas;
show databases;
use consultas;
show tables;
create table medicos(
	id int primary key auto_increment,
	nome varchar(255),
    email varchar(255)
    
);
create table especialidades(
	id int primary key auto_increment,
	nome varchar(255)
);

create table medicos_tem_especialidades(
	id_medico int,
	id_especialidade int,
    primary key(id_medico, id_especialidade),
    foreign key(id_medico) references medicos(id),
    foreign key(id_especialidade) references especialidades(id)
);
drop table especialidades.
select*from medicos;
insert into medicos(nome,email) values('Jose Alencar Barroso','josealencar@humb')
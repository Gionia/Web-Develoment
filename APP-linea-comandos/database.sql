create database if not exists master_python;
use master_python;

create table usuarios(
    id          int(25) auto_increment not null,
    nombre      varchar(100),
    apellidos   varchar(100),
    email       varchar(255) not null,
    password    varchar(255) not null,
    fecha       date not null,
    sexo        varchar(255),
    constraint pk_usuarios primary key(id),
    constraint uq_email UNIQUE(email)
)engine=InnoDb;

create table notas(
    id          int(25) auto_increment not null,
    usuario_id  int(25) not null,
    titulo      varchar(255) not null,
    descripcion mediumtext,
    fecha       date not null,
    constraint pk_notas primary key(id),
    constraint fk_nota_usuario Foreign key(usuario_id) references usuarios(id)
)engine=InnoDb;
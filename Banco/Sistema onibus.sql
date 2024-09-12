-- Database: Sistema onibus

-- DROP DATABASE IF EXISTS "Sistema onibus";

CREATE DATABASE "Sistema onibus"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;



CREATE TABLE Administrador(
    Admin_id INT PRIMARY KEY,
    Nome VARCHAR(50),
    Senha VARCHAR(50)
);

CREATE TABLE Cidade(
    Nome VARCHAR(50) PRIMARY KEY,
    Num_habitantes INT
);

CREATE TABLE Empresa (
    Nome VARCHAR(50) PRIMARY KEY,
    Contato VARCHAR(14)
);

CREATE TABLE Garagem(
    Nome VARCHAR(50) PRIMARY KEY,
    Num_vagas INT,
    Empresa_id VARCHAR(50),
    CONSTRAINT garagem_empresa_id_fkey FOREIGN KEY (empresa_id)
        REFERENCES public.empresa (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);

CREATE TABLE Horario(
    Horario_id INT PRIMARY KEY,
    Duracao VARCHAR(25),
    Dia_semana VARCHAR(50)
);

CREATE TABLE Linha(
    Nome VARCHAR(3) PRIMARY KEY,
    Modelo VARCHAR(50),
    Empresa_id VARCHAR(50),
    Garagem_id VARCHAR(50),
    CONSTRAINT linha_empresa_id_fkey FOREIGN KEY (empresa_id)
        REFERENCES public.empresa (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT linha_garagem_id_fkey FOREIGN KEY (garagem_id)
        REFERENCES public.garagem (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);

CREATE TABLE Motorista(
    Motorista_id INT PRIMARY KEY, -- chave primaria tem que mudar no desenho que está como PK o nome o que não corresponde com o banco
	Nome VARCHAR(50),
    Telefone VARCHAR(15),
    Foto BYTEA,
	Linha_id VARCHAR(3),
	Empresa_id VARCHAR(50),
    CONSTRAINT motorista_empresa_id_fkey FOREIGN KEY (empresa_id)
        REFERENCES public.empresa (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT motorista_linha_id_fkey FOREIGN KEY (linha_id)
        REFERENCES public.linha (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);

CREATE TABLE Terminal(
    Nome VARCHAR(50) PRIMARY KEY,
    Cidade_id VARCHAR(50),
    CONSTRAINT terminal_cidade_id_fkey FOREIGN KEY (cidade_id)
      REFERENCES public.cidade (nome) MATCH SIMPLE
      ON UPDATE NO ACTION
      ON DELETE CASCADE
);

CREATE TABLE Trajeto(
    Linha_id VARCHAR(3),
    Origem_id VARCHAR(50),
    Destino_id VARCHAR(50),
    PRIMARY KEY (Linha_id, Origem_id, Destino_id),
    CONSTRAINT trajeto_destino_id_fkey FOREIGN KEY (destino_id)
        REFERENCES public.terminal (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT trajeto_linha_id_fkey FOREIGN KEY (linha_id)
        REFERENCES public.linha (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT trajeto_origem_id_fkey FOREIGN KEY (origem_id)
        REFERENCES public.terminal (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);

CREATE TABLE Parada(
    Nome VARCHAR(6) PRIMARY KEY,
    Cidade_id VARCHAR(50),
    CONSTRAINT parada_cidade_id_fkey FOREIGN KEY (cidade_id)
        REFERENCES public.cidade (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);

CREATE TABLE Trajeto_Parada(
    Linha_id VARCHAR(3),
    Parada_1 VARCHAR(6),
    Parada_2 VARCHAR(6),
    Parada_3 VARCHAR(6),
    Parada_4 VARCHAR(6),
    Parada_5 VARCHAR(6),
    PRIMARY KEY (Linha_id),
	CONSTRAINT trajeto_parada_linha_id_fkey FOREIGN KEY (linha_id)
        REFERENCES public.linha (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT trajeto_parada_parada_1_fkey FOREIGN KEY (parada_1)
        REFERENCES public.parada (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT trajeto_parada_parada_2_fkey FOREIGN KEY (parada_2)
        REFERENCES public.parada (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT trajeto_parada_parada_3_fkey FOREIGN KEY (parada_3)
        REFERENCES public.parada (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT trajeto_parada_parada_4_fkey FOREIGN KEY (parada_4)
        REFERENCES public.parada (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT trajeto_parada_parada_5_fkey FOREIGN KEY (parada_5)
        REFERENCES public.parada (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);

CREATE TABLE Horario_Linha(
    Linha_id VARCHAR(3),
    Horario_1 INT,
    Horario_2 INT,
    Horario_3 INT,
    Horario_4 INT,
    Horario_5 INT,
    PRIMARY KEY (Linha_id),
    CONSTRAINT horario_linha_horario_1_fkey FOREIGN KEY (horario_1)
        REFERENCES public.horario (horario_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT horario_linha_horario_2_fkey FOREIGN KEY (horario_2)
        REFERENCES public.horario (horario_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT horario_linha_horario_3_fkey FOREIGN KEY (horario_3)
        REFERENCES public.horario (horario_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT horario_linha_horario_4_fkey FOREIGN KEY (horario_4)
        REFERENCES public.horario (horario_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT horario_linha_horario_5_fkey FOREIGN KEY (horario_5)
        REFERENCES public.horario (horario_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT horario_linha_linha_id_fkey FOREIGN KEY (linha_id)
        REFERENCES public.linha (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);

-- INSERÇÃO DE ADMINISTRADORES --
INSERT INTO Administrador (admin_id, nome, senha)
VALUES
    (1, 'Maristela Holanda', 'Banco_Dados24.1'),
    (2, 'Gabriel Faustino', 'Banco_Dados24.1'),
    (3, 'Bianca Carvalho', 'Banco_Dados24.1'),
    (4, 'Kethlen Ângela', 'Banco_Dados24.1'),
    (5, 'Luana Ferreira', 'Banco_Dados24.1');


	SELECT * FROM Administrador;


	-- INSERÇÃO DE CIDADES --
INSERT INTO Cidade (nome, num_habitantes)
VALUES
    ('Nova Esperança', 287000),
    ('Vale do Sol', 135000),
    ('Orquídea Azul', 458000),
    ('Verdemontes', 76000),
    ('Aurora do Vale', 213000);


	SELECT * FROM Cidade;


	-- INSERÇÃO DE EMPRESAS --
INSERT INTO Empresa (nome, contato)
VALUES
    ('TransVia Express', '(61) 3445-7766'),
    ('Rota Brasil', '(61) 3892-1433'),
    ('Expresso Horizonte', '(61) 3567-9822'),
    ('Viação Estrela Azul', '(61) 3728-5544'),
    ('RotaSul Transportes', '(61) 3998-2233');

-- CONSULTA PARA VERIFICAR A INSERÇÃO --
SELECT * FROM Empresa;

-- INSERÇÃO DE GARAGENS --
INSERT INTO Garagem (nome, num_vagas, empresa_id)
VALUES
    ('Garagem_TE', 6, 'TransVia Express'),
    ('Garagem_RB', 6, 'Rota Brasil'),
    ('Garagem_EH', 6, 'Expresso Horizonte'),
    ('Garagem_VEA', 6, 'Viação Estrela Azul'),
    ('Garagem_RST', 8, 'RotaSul Transportes');

-- CONSULTA PARA VERIFICAR A INSERÇÃO --
SELECT * FROM Garagem;

-- INSERÇÃO DE HORÁRIOS --
INSERT INTO horario (horario_id, duracao, dia_semana)
VALUES 
    (1, '06:00-08:00', 'Segunda à Domingo'),
    (2, '08:00-10:00', 'Segunda à Domingo'),
    (3, '10:00-12:00', 'Segunda à Domingo'),
    (4, '12:00-14:00', 'Segunda à Domingo'),
    (5, '14:00-16:00', 'Segunda à Domingo'),
    (6, '16:00-18:00', 'Segunda à Domingo'),
    (7, '18:00-20:00', 'Segunda à Domingo'),
    (8, '20:00-22:00', 'Segunda à Domingo'),
    (9, '06:00-08:00', 'Segunda à Sexta'),
    (10, '18:00-20:00', 'Segunda à Sexta');

-- CONSULTAS PARA VERIFICAÇÃO --
SELECT * FROM horario;


-- INSERÇÃO DE TERMINAIS  --
INSERT INTO Terminal (Nome, Cidade_id)
VALUES
    ('Terminal Arara Azul', 'Nova Esperança'),
    ('Terminal Patas Pintadas', 'Vale do Sol'),
    ('Terminal Anta Careca', 'Orquídea Azul'),
    ('Terminal Vales Vermelhos', 'Verdemontes'),
    ('Terminal Capim Dourado', 'Aurora do Vale');

-- CONSULTA PARA VERIFICAÇÃO --
SELECT * FROM Terminal;


-- INSERÇÃO DE PARADAS --
INSERT INTO Parada (nome, cidade_id)
VALUES
    ('P1OA', 'Orquídea Azul'),
    ('P2OA', 'Orquídea Azul'),
    ('P3OA', 'Orquídea Azul'),
    ('P4OA', 'Orquídea Azul'),
    ('P5OA', 'Orquídea Azul'),
    ('P6OA', 'Orquídea Azul'),
    ('P7OA', 'Orquídea Azul'),
    ('P8OA', 'Orquídea Azul'),
    ('P9OA', 'Orquídea Azul'),
    ('P10OA', 'Orquídea Azul'),
    ('P11OA', 'Orquídea Azul'),
    ('P12OA', 'Orquídea Azul'),
    ('P1NE', 'Nova Esperança'),
    ('P2NE', 'Nova Esperança'),
    ('P3NE', 'Nova Esperança'),
    ('P4NE', 'Nova Esperança'),
    ('P5NE', 'Nova Esperança'),
    ('P6NE', 'Nova Esperança'),
    ('P7NE', 'Nova Esperança'),
    ('P8NE', 'Nova Esperança'),
    ('P1AV', 'Aurora do Vale'),
    ('P2AV', 'Aurora do Vale'),
    ('P3AV', 'Aurora do Vale'),
    ('P4AV', 'Aurora do Vale'),
    ('P5AV', 'Aurora do Vale'),
    ('P6AV', 'Aurora do Vale'),
    ('P7AV', 'Aurora do Vale'),
    ('P8AV', 'Aurora do Vale'),
    ('P1VS', 'Vale do Sol'),
    ('P2VS', 'Vale do Sol'),
    ('P3VS', 'Vale do Sol'),
    ('P4VS', 'Vale do Sol'),
    ('P5VS', 'Vale do Sol'),
    ('P1V', 'Verdemontes'),
    ('P2V', 'Verdemontes'),
    ('P3V', 'Verdemontes');


-- CONSULTA PARA VERIFICAÇÃO --
SELECT * FROM Parada;

-- INSERÇÃO DE LINHAS  --
INSERT INTO Linha (nome, modelo, empresa_id, garagem_id)
VALUES
    ('665', 'Micro Ônibus', 'TransVia Express', 'Garagem_TE'),
    ('557', 'Ônibus Urbano Padrão', 'TransVia Express', 'Garagem_TE'),
    ('755', 'Ônibus Urbano Padrão', 'TransVia Express', 'Garagem_TE'),
    ('494', 'Ônibus Urbano Sanfonado', 'TransVia Express', 'Garagem_TE'),
    ('821', 'Ônibus Interestadual', 'TransVia Express', 'Garagem_TE'),
    ('566', 'Ônibus Interestadual', 'TransVia Express', 'Garagem_TE'),
    ('242', 'Micro Ônibus', 'Rota Brasil', 'Garagem_RB'),
    ('859', 'Ônibus Urbano Padrão', 'Rota Brasil', 'Garagem_RB'),
    ('485', 'Ônibus Urbano Padrão', 'Rota Brasil', 'Garagem_RB'),
    ('748', 'Ônibus Urbano Sanfonado', 'Rota Brasil', 'Garagem_RB'),
    ('905', 'Ônibus Interestadual', 'Rota Brasil', 'Garagem_RB'),
    ('833', 'Ônibus Interestadual', 'Rota Brasil', 'Garagem_RB'),
    ('355', 'Micro Ônibus', 'Expresso Horizonte', 'Garagem_EH'),
    ('161', 'Ônibus Urbano Padrão', 'Expresso Horizonte', 'Garagem_EH'),
    ('167', 'Ônibus Urbano Padrão', 'Expresso Horizonte', 'Garagem_EH'),
    ('131', 'Ônibus Urbano Sanfonado', 'Expresso Horizonte', 'Garagem_EH'),
    ('586', 'Ônibus Interestadual', 'Expresso Horizonte', 'Garagem_EH'),
    ('797', 'Ônibus Interestadual', 'Expresso Horizonte', 'Garagem_EH'),
    ('234', 'Micro Ônibus', 'Viação Estrela Azul', 'Garagem_VEA'),
    ('284', 'Ônibus Urbano Padrão', 'Viação Estrela Azul', 'Garagem_VEA'),
    ('928', 'Ônibus Urbano Padrão', 'Viação Estrela Azul', 'Garagem_VEA'),
    ('750', 'Ônibus Urbano Sanfonado', 'Viação Estrela Azul', 'Garagem_VEA'),
    ('913', 'Ônibus Interestadual', 'Viação Estrela Azul', 'Garagem_VEA'),
    ('784', 'Ônibus Interestadual', 'Viação Estrela Azul', 'Garagem_VEA'),
    ('341', 'Micro Ônibus', 'RotaSul Transportes', 'Garagem_RST'),
    ('893', 'Micro Ônibus', 'RotaSul Transportes', 'Garagem_RST'),
    ('870', 'Ônibus Urbano Padrão', 'RotaSul Transportes', 'Garagem_RST'),
    ('458', 'Ônibus Urbano Padrão', 'RotaSul Transportes', 'Garagem_RST'),
    ('342', 'Ônibus Urbano Padrão', 'RotaSul Transportes', 'Garagem_RST'),
    ('747', 'Ônibus Urbano Sanfonado', 'RotaSul Transportes', 'Garagem_RST'),
    ('263', 'Ônibus Urbano Sanfonado', 'RotaSul Transportes', 'Garagem_RST'),
    ('988', 'Ônibus Urbano Sanfonado', 'RotaSul Transportes', 'Garagem_RST');

-- CONSULTA PARA VERIFICAÇÃO --
SELECT * FROM Linha;

-- INSERÇÃO DE TRAJETOS  --
INSERT INTO Trajeto (Linha_id, Origem_id, Destino_id)
VALUES
    ('821', 'Terminal Arara Azul', 'Terminal Anta Careca'),
    ('566', 'Terminal Arara Azul', 'Terminal Vales Vermelhos'),
    ('905', 'Terminal Vales Vermelhos', 'Terminal Capim Dourado'),
    ('784', 'Terminal Vales Vermelhos', 'Terminal Anta Careca'),
    ('833', 'Terminal Capim Dourado', 'Terminal Anta Careca'),
    ('586', 'Terminal Capim Dourado', 'Terminal Patas Pintadas'),
    ('797', 'Terminal Patas Pintadas', 'Terminal Anta Careca'),
    ('913', 'Terminal Patas Pintadas', 'Terminal Arara Azul'),
    ('821', 'Terminal Anta Careca', 'Terminal Arara Azul'),
    ('566', 'Terminal Vales Vermelhos', 'Terminal Arara Azul'),
    ('905', 'Terminal Capim Dourado', 'Terminal Vales Vermelhos'),
    ('784', 'Terminal Anta Careca', 'Terminal Vales Vermelhos'),
    ('833', 'Terminal Anta Careca', 'Terminal Capim Dourado'),
    ('586', 'Terminal Patas Pintadas', 'Terminal Capim Dourado'),
    ('797', 'Terminal Anta Careca', 'Terminal Patas Pintadas'),
    ('913', 'Terminal Arara Azul', 'Terminal Patas Pintadas'),
    ('665', 'Terminal Arara Azul', 'Terminal Arara Azul'),
    ('557', 'Terminal Arara Azul', 'Terminal Arara Azul'),
    ('755', 'Terminal Arara Azul', 'Terminal Arara Azul'),
    ('494', 'Terminal Arara Azul', 'Terminal Arara Azul'),
    ('242', 'Terminal Patas Pintadas', 'Terminal Patas Pintadas'),
    ('859', 'Terminal Patas Pintadas', 'Terminal Patas Pintadas'),
    ('485', 'Terminal Patas Pintadas', 'Terminal Patas Pintadas'),
    ('748', 'Terminal Patas Pintadas', 'Terminal Patas Pintadas'),
    ('355', 'Terminal Capim Dourado', 'Terminal Capim Dourado'),
    ('161', 'Terminal Capim Dourado', 'Terminal Capim Dourado'),
    ('167', 'Terminal Capim Dourado', 'Terminal Capim Dourado'),
    ('131', 'Terminal Capim Dourado', 'Terminal Capim Dourado'),
    ('234', 'Terminal Vales Vermelhos', 'Terminal Vales Vermelhos'),
    ('284', 'Terminal Vales Vermelhos', 'Terminal Vales Vermelhos'),
    ('928', 'Terminal Vales Vermelhos', 'Terminal Vales Vermelhos'),
    ('750', 'Terminal Vales Vermelhos', 'Terminal Vales Vermelhos'),
    ('341', 'Terminal Anta Careca', 'Terminal Anta Careca'),
    ('893', 'Terminal Anta Careca', 'Terminal Anta Careca'),
    ('870', 'Terminal Anta Careca', 'Terminal Anta Careca'),
    ('458', 'Terminal Anta Careca', 'Terminal Anta Careca'),
    ('342', 'Terminal Anta Careca', 'Terminal Anta Careca'),
    ('747', 'Terminal Anta Careca', 'Terminal Anta Careca'),
    ('263', 'Terminal Anta Careca', 'Terminal Anta Careca'),
    ('988', 'Terminal Anta Careca', 'Terminal Anta Careca');

-- CONSULTA PARA VERIFICAÇÃO --
SELECT * FROM Trajeto;

-- INSERÇÃO DE MOTORISTA  --

INSERT INTO Motorista(telefone, linha_id, empresa_id, nome, motorista_id) VALUES
('(61) 96013-8821', '665', 'TransVia Express', 'Lucas', 1),
('(61) 93396-8782', '557', 'TransVia Express', 'Mateus', 2),
('(61) 98307-8258', '755', 'TransVia Express', 'Gabriel ', 3),
('(61) 95797-6886', '494', 'TransVia Express', 'Rafael', 4),
('(61) 99271-8670', '821', 'TransVia Express', 'Gustavo', 5),
('(61) 96206-4900', '566', 'TransVia Express', 'Pedro', 6),
('(61) 96562-9019', '242', 'Rota Brasil', 'Thiago', 7),
('(61) 92261-2079', '859', 'Rota Brasil', 'Felipe', 8),
('(61) 91592-2363', '485', 'Rota Brasil', 'João', 9),
('(61) 97881-4855', '748', 'Rota Brasil', 'Bruno', 10),
('(61) 96902-3184', '905', 'Rota Brasil', 'Vinícius', 11),
('(61) 92071-6998', '833', 'Rota Brasil', 'Carlos', 12),
('(61) 92628-3021', '355', 'Expresso Horizonte', 'Ricardo', 13),
('(61) 96548-1500', '161', 'Expresso Horizonte', 'Fernando', 14),
('(61) 92503-9565', '167', 'Expresso Horizonte', 'André', 15),
('(61) 95878-4937', '131', 'Expresso Horizonte', 'Marcelo', 16),
('(61) 95681-9326', '586', 'Expresso Horizonte', 'Ana', 17),
('(61) 92640-3918', '797', 'Expresso Horizonte', 'Beatriz', 18),
('(61) 99451-4522', '234', 'Viação Estrela Azul', 'Carla', 19),
('(61) 94339-1495', '284', 'Viação Estrela Azul', 'Diana', 20),
('(61) 95232-3169', '928', 'Viação Estrela Azul', 'Elisa', 21),
('(61) 97734-2893', '750', 'Viação Estrela Azul', 'Fernanda', 22),
('(61) 95088-9602', '913', 'Viação Estrela Azul', 'Gabriela', 23),
('(61) 91276-9366', '784', 'Expresso Horizonte', 'Helena', 24),
('(61) 97956-8952', '341', 'RotaSul Transportes', 'Isabela', 25),
('(61) 98522-5702', '893', 'RotaSul Transportes', 'Juliana', 26),
('(61) 95944-7918', '870', 'RotaSul Transportes', 'Karina', 27),
('(61) 96067-1382', '458', 'RotaSul Transportes', 'Laura', 28),
('(61) 97511-1807', '342', 'RotaSul Transportes', 'Mariana', 29),
('(61) 95003-3995', '747', 'RotaSul Transportes', 'Natália', 30),
('(61) 91481-4672', '263', 'RotaSul Transportes', 'Olivia', 31),
('(61) 95336-8570', '988', 'RotaSul Transportes', 'Patrícia', 32);

-- CONSULTA PARA VERIFICAÇÃO --
SELECT * FROM Motorista;


-- INSERÇÃO DE Horario_Linha  --


INSERT INTO Horario_Linha(Linha_id, Horario_1, Horario_2, Horario_3, Horario_4, Horario_5) VALUES
('665', 1, 3, 5, 7, NULL),
('242', 1, 3, 5, 7, NULL),
('355', 1, 3, 5, 7, NULL),
('234', 1, 3, 5, 7, NULL),
('341', 1, 3, 5, 7, NULL),
('893', 1, 3, 5, 7, NULL),
('557', 1, 2, 4, 6, 8),
('755', 1, 2, 4, 6, 8),
('859', 1, 2, 4, 6, 8),
('485', 1, 2, 4, 6, 8),
('161', 1, 2, 4, 6, 8),
('167', 1, 2, 4, 6, 8),
('284', 1, 2, 4, 6, 8),
('928', 1, 2, 4, 6, 8),
('870', 1, 2, 4, 6, 8),
('458', 1, 2, 4, 6, 8),
('342', 1, 2, 4, 6, 8),
('494', 2, 3, 6, 7, 8),
('748', 2, 3, 6, 7, 8),
('131', 2, 3, 6, 7, 8),
('750', 2, 3, 6, 7, 8),
('747', 2, 3, 6, 7, 8),
('263', 2, 3, 6, 7, 8),
('988', 2, 3, 6, 7, 8),
('566', 9, 10, NULL, NULL, NULL),
('905', 9, 10, NULL, NULL, NULL),
('833', 9, 10, NULL, NULL, NULL),
('586', 9, 10, NULL, NULL, NULL),
('797', 9, 10, NULL, NULL, NULL),
('913', 9, 10, NULL, NULL, NULL),
('784', 9, 10, NULL, NULL, NULL);


-- CONSULTA PARA VERIFICAÇÃO --
SELECT * FROM Horario_Linha;

-- INSERÇÃO DE Trajeto_Parada --
INSERT INTO Trajeto_Parada(Linha_id,Parada_1, Parada_2, Parada_3, Parada_4, Parada_5) VALUES
('665', 'P1NE', 'P4NE', 'P7NE', 'P2NE', NULL),
('242', 'P1VS', 'P4VS', 'P5VS', 'P2VS', NULL),
('355', 'P1AV', 'P4AV', 'P7AV', 'P2AV', NULL),
('234', 'P1V', 'P2V', 'P3V', NULL, NULL),
('341', 'P1OA', 'P2OA', 'P3OA', 'P4OA','P5OA'),
('893', 'P5OA', 'P6OA', 'P7OA', 'P8OA', 'P9OA'),
('557', 'P2NE', 'P4NE', 'P6NE', 'P8NE', 'P1NE'),
('755', 'P1NE', 'P3NE', 'P5NE', 'P7NE', 'P2NE'),
('859', 'P2VS', 'P4VS', 'P5VS', 'P3VS', 'P1VS'),
('485', 'P1VS', 'P3VS', 'P5VS', 'P4VS', 'P2VS'),
('161', 'P2AV', 'P4AV', 'P6AV', 'P8AV', 'P1AV'),
('167', 'P1AV', 'P3AV', 'P5AV', 'P7AV', 'P2AV'),
('284', 'P3V', 'P2V', 'P1V', NULL, NULL),
('928', 'P2V', 'P3V', 'P1V', NULL, NULL),
('870', 'P12OA', 'P11OA', 'P10OA', 'P9OA', 'P8OA'),
('458', 'P7OA', 'P6OA', 'P5OA', 'P4OA', 'P3OA'),
('342', 'P1OA', 'P6OA', 'P8OA', 'P12OA', 'P3OA'),
('494', 'P5NE', 'P4NE', 'P3NE', 'P2NE', 'P1NE'),
('748', 'P5VS', 'P4VS', 'P3VS', 'P2VS', 'P1VS'),
('131', 'P5AV', 'P4AV', 'P3AV', 'P2AV', 'P1AV'),
('750', 'P3V', 'P2V', 'P1V', NULL, NULL),
('747', 'P12OA', 'P3OA', 'P6OA', 'P1OA', 'P7OA'),
('263', 'P10OA', 'P4OA', 'P7OA', 'P8OA', 'P11OA'),
('988', 'P11OA', 'P7OA', 'P5OA', 'P10OA', 'P2OA');

-- CONSULTA PARA VERIFICAÇÃO --
SELECT * FROM Trajeto_Parada;

-- CRIAÇÃO DA VIEW PAINEL GERAL METROPOLITANO --
CREATE VIEW Painel_Geral_Metropolitano AS
SELECT motorista.nome, 
		foto,
		Horario_Linha.Linha_id, 
      	Linha.modelo,
		Linha.empresa_id,
      	Horario.Duracao, 
      	Horario.Dia_semana,
		Terminal.cidade_id,
      	Trajeto.origem_id, 
      	Trajeto.destino_id, 
    	Trajeto_Parada.Parada_1, 
      	Trajeto_Parada.Parada_2, 
      	Trajeto_Parada.Parada_3, 
      	Trajeto_Parada.Parada_4, 
      	Trajeto_Parada.Parada_5
FROM Motorista
INNER JOIN Horario_linha ON motorista.linha_id = horario_linha.linha_id
INNER JOIN Horario ON Horario.horario_id = Horario_Linha.horario_1 OR horario_2 = horario_id OR horario_3 = horario_id OR horario_4 = horario_id OR horario_5 = horario_id
INNER JOIN Linha ON Horario_Linha.linha_id = Linha.nome
INNER JOIN Trajeto ON Trajeto.linha_id = Linha.nome
INNER JOIN Terminal ON Terminal.nome = Trajeto.origem_id
INNER JOIN Trajeto_Parada ON Trajeto.Linha_id = Trajeto_Parada.Linha_id;

-- CONSULTA PARA VERIFICAÇÃO --
SELECT * FROM Painel_Geral_Metropolitano;

-- CRIAÇÃO DA VIEW PAINEL GERAL INTERESTADUAL --
CREATE VIEW Painel_Geral_Interestadual AS
SELECT 
		motorista.nome, 
		foto,
		Horario_Linha.Linha_id,
		modelo,
        Linha.empresa_id, 
		Duracao, 
		Dia_semana,
		origem_id, 
		destino_id 
FROM Motorista
INNER JOIN Horario_linha ON motorista.linha_id = horario_linha.linha_id
INNER JOIN Horario ON horario_1 = horario_id OR horario_2 = horario_id OR horario_3 = horario_id OR horario_4 = horario_id OR horario_5 = horario_id 
INNER JOIN Linha ON Horario_Linha.linha_id = Linha.nome 
INNER JOIN Trajeto ON Trajeto.linha_id = Linha.nome
WHERE modelo = 'Ônibus Interestadual';

-- CONSULTA PARA VERIFICAÇÃO --
SELECT * FROM Painel_Geral_Interestadual;

-- CRIAÇÃO FUNÇÃO BUSCAR ORIGEM DESTINO INTERESTADUAL --

CREATE OR REPLACE FUNCTION buscar_por_origem_destino_interestadual(
    p_origem_id character varying,
    p_destino_id character varying
)
RETURNS TABLE (
    nome_motorista character varying,
    foto bytea,
    linha_id character varying,
    modelo character varying,
    empresa_id character varying,
    duracao character varying,
    dia_semana character varying,
    origem_id character varying,
    destino_id character varying
) AS
$$
BEGIN
    RETURN QUERY
    SELECT Painel_Geral_Interestadual.nome, Painel_Geral_Interestadual.foto, 
	Painel_Geral_Interestadual.Linha_id, Painel_Geral_Interestadual.modelo, 
	Painel_Geral_Interestadual.empresa_id, Painel_Geral_Interestadual.Duracao, 
	Painel_Geral_Interestadual.Dia_semana, 
	Painel_Geral_Interestadual.origem_id, Painel_Geral_Interestadual.destino_id
    FROM Painel_Geral_Interestadual
    WHERE Painel_Geral_Interestadual.origem_id = p_origem_id
    AND Painel_Geral_Interestadual.destino_id = p_destino_id;

    IF NOT FOUND THEN
        RAISE NOTICE 'Nenhuma linha encontrada com origem na origem e destino informados';
    END IF;
END;
$$
LANGUAGE plpgsql;

-- CHAMAMENTO DA FUNÇÃO BUSCAR ORIGEM DESTINO INTERESTADUAL -- 
SELECT * FROM buscar_por_origem_destino_interestadual('Terminal Anta Careca', 'Terminal Patas Pintadas');

-- CRIAÇÃO PROCEDURE INSERIR MOTORISTA --
CREATE OR REPLACE PROCEDURE InserirMotorista(
    p_motorista_id INT,
    p_nome VARCHAR(50),
    p_telefone VARCHAR(15),
    p_foto BYTEA,
    p_linha_id VARCHAR(3),
    p_empresa_id VARCHAR(50)
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Linha WHERE nome = p_linha_id) THEN
        RAISE EXCEPTION 'A linha % não existe.', p_linha_id;
    END IF;

    IF NOT EXISTS (SELECT 1 FROM Empresa WHERE nome = p_empresa_id) THEN
        RAISE EXCEPTION 'A empresa % não existe.', p_empresa_id;
    END IF;

    INSERT INTO Motorista(motorista_id, nome, telefone, foto, linha_id, empresa_id)
    VALUES (p_motorista_id, p_nome, p_telefone, p_foto, p_linha_id, p_empresa_id);

    RAISE NOTICE 'Motorista % inserido com sucesso.', p_nome;
END;
$$;

-- CHAMAMENTO DA PROCEDURE INSERIR MOTORISTA --
CALL InserirMotorista(69, 'João Silva', '(61) 91234-5678', NULL, '665', 'TransVia Express');

-- FUNÇÃO LINHAS ATUAIS --
CREATE OR REPLACE FUNCTION LinhasAtuais()
RETURNS TABLE(linha_nome VARCHAR(3), modelo VARCHAR(50), empresa_nome VARCHAR(50), horario_duracao VARCHAR(25)) AS
$$
DECLARE
    dia_atual_num INT;
    hora_atual TIME;
    dia_texto VARCHAR;
BEGIN
    dia_atual_num := EXTRACT(DOW FROM NOW()); -- 0 = Domingo, 1 = Segunda, ..., 6 = Sábado
    hora_atual := NOW()::time;
	
    CASE dia_atual_num
        WHEN 0 THEN dia_texto := 'Domingo';
        WHEN 1 THEN dia_texto := 'Segunda';
        WHEN 2 THEN dia_texto := 'Terça';
        WHEN 3 THEN dia_texto := 'Quarta';
        WHEN 4 THEN dia_texto := 'Quinta';
        WHEN 5 THEN dia_texto := 'Sexta';
        WHEN 6 THEN dia_texto := 'Sábado';
    END CASE;

    RETURN QUERY
    SELECT
        pgm.linha_id,
        pgm.modelo,
        pgm.empresa_id,
        pgm.duracao
    FROM
        Painel_Geral_Metropolitano pgm
    WHERE
        pgm.duracao IS NOT NULL 
        AND POSITION('-' IN pgm.duracao) > 0 
        AND SPLIT_PART(pgm.duracao, '-', 1) <> '' AND SPLIT_PART(pgm.duracao, '-', 2) <> ''
        AND hora_atual BETWEEN SPLIT_PART(pgm.duracao, '-', 1)::time AND SPLIT_PART(pgm.duracao, '-', 2)::time
        AND (
            (pgm.dia_semana ILIKE '%Segunda à Sexta%' AND dia_atual_num BETWEEN 1 AND 5) OR
            (pgm.dia_semana ILIKE '%Segunda à Sábado%' AND dia_atual_num BETWEEN 1 AND 6) OR
            (pgm.dia_semana ILIKE '%Segunda à Domingo%' AND dia_atual_num BETWEEN 1 AND 7) OR
            (pgm.dia_semana ILIKE '%' || dia_texto || '%') 
        );
END;
$$ LANGUAGE plpgsql;

-- CONSULTA A FUNÇÃO LINHAS ATUAIS --
SELECT * FROM LinhasAtuais();

-- PROCEDURE LIXEIRA -- 
CREATE OR REPLACE PROCEDURE Lixeira()
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM linha
    WHERE nome NOT IN (
        SELECT DISTINCT linha_id
        FROM trajeto
    );
    
    RAISE NOTICE 'Linhas sem trajetos foram deletadas.';
END;
$$;

-- CHAMAMENTO DA PROCEURE LIXEIRA --
CALL Lixeira();


-- UPDATE MOTORISTA PARA INSERIR FOTO  --

	UPDATE Motorista
SET Foto = pg_read_binary_file('C:\Users\mllbi\Documents\Projeto BD\gabriel.jpg')
WHERE Nome = 'Gabriel';


	-- QUERY MOTORISTA PARA BUSCAR FOTO  --
SELECT Foto
FROM Motorista
WHERE Nome = 'Gabriel';

-- 1. Criando a sequência
CREATE SEQUENCE motorista_id_seq;

-- 2. Definindo a coluna para usar a sequência
ALTER TABLE Motorista
ALTER COLUMN Motorista_id SET DEFAULT nextval('motorista_id_seq');

-- 3. Ajustando a sequência com base no valor máximo existente
SELECT setval('motorista_id_seq', COALESCE((SELECT MAX(Motorista_id) FROM Motorista), 0) + 1);

-- Alterando nome de lucas --
UPDATE Motorista
SET nome = 'Lucas.Souza'
WHERE motorista_id = 1;


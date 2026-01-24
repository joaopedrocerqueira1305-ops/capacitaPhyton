CREATE TABLE aluno (
    id_aluno INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT
);

CREATE TABLE curso (
    id_curso INTEGER PRIMARY KEY,
    nome TEXT,
    carga_horaria INTEGER
);

CREATE TABLE matricula (
    id_matricula INTEGER PRIMARY KEY,
    id_aluno INTEGER,
    id_curso INTEGER,
    data_matricula DATE,
    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno),
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
);


/* =========================
   INSERÇÃO DE DADOS
   ========================= */

/* Alunos */
INSERT INTO aluno VALUES
(1, 'Ana Silva', 'ana@email.com'),
(2, 'Bruno Costa', 'bruno@email.com'),
(3, 'Carlos Lima', 'carlos@email.com'),
(4, 'Daniela Rocha', 'daniela@email.com');

/* Cursos */
INSERT INTO curso VALUES
(1, 'Banco de Dados', 60),
(2, 'Programação em Python', 80),
(3, 'Redes de Computadores', 40);

/* Matrículas */
INSERT INTO matricula VALUES
(1, 1, 1, '2025-01-10'),
(2, 1, 2, '2025-01-12'),
(3, 2, 2, '2025-01-15'),
(4, 3, 1, '2025-01-20');

SELECT * from curso;
SELECT * from matricula;
SELECT * from aluno;

SELECT aluno.nome,curso.nome
from aluno inner join matricula
	on aluno.id_aluno = matricula.id_aluno
  INNER JOIN curso
  	on curso.id_curso = matricula.id_curso;

SELECT aluno.nome,curso.nome
from aluno RIGHT join matricula
	on aluno.id_aluno = matricula.id_aluno
  RIGHT JOIN curso
  	on curso.id_curso = matricula.id_curso;
    
SELECT aluno.nome,curso.nome
from aluno LEFT join matricula
	on aluno.id_aluno = matricula.id_aluno
  LEFT JOIN curso
  	on curso.id_curso = matricula.id_curso WHERE matricula.id_aluno is NULL;
    
/*Exercicio 5 */
SELECT aluno.nome,curso.nome
from aluno RIGHT join matricula
	on aluno.id_aluno = matricula.id_aluno
  right JOIN curso
  	on curso.id_curso = matricula.id_curso WHERE matricula.id_curso is NULL;
    
/* Exercicio 6 */
SELECT curso.nome as curso,
COUNT(matricula.id_aluno) as total_alunos 
from curso LEFT join matricula
	on curso.id_curso = matricula.id_curso
 GROUP by curso.nome; 

/* Exercicio 7 */
SELECT aluno.nome ,
COUNT(matricula.id_curso) as total_cursos 
from aluno INNER join matricula
	on aluno.id_aluno = matricula.id_aluno
GROUP by aluno.nome
HAVING COUNT(matricula.id_curso) > 1;

CREATE TABLE produtos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    categoria VARCHAR(50)
);

CREATE TABLE vendas (
    id INT PRIMARY KEY,
    produto_id INT,
    valor_venda DECIMAL(10,2),
    data_venda DATE,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

INSERT INTO produtos (id, nome, categoria) VALUES
(1, 'Notebook Dell', 'Informática'),
(2, 'Mouse Logitech', 'Informática'),
(3, 'Teclado Mecânico', 'Informática'),
(4, 'Monitor 27"', 'Informática'),

(5, 'Geladeira Brastemp', 'Eletrodomésticos'),
(6, 'Micro-ondas LG', 'Eletrodomésticos'),
(7, 'Liquidificador Philips', 'Eletrodomésticos'),

(8, 'Sofá 3 lugares', 'Móveis'),
(9, 'Mesa de Jantar', 'Móveis'),
(10, 'Cadeira Escritório', 'Móveis'),

(11, 'Camiseta', 'Vestuário'),
(12, 'Calça Jeans', 'Vestuário'),
(13, 'Tênis Esportivo', 'Vestuário');


INSERT INTO vendas (id, produto_id, valor_venda, data_venda) VALUES
(1, 1, 4500.00, '2024-01-10'),
(2, 1, 4500.00, '2024-01-15'),
(3, 2, 150.00, '2024-01-12'),
(4, 3, 600.00, '2024-01-18'),
(5, 4, 1800.00, '2024-01-20'),

(6, 5, 3200.00, '2024-01-08'),
(7, 6, 900.00, '2024-01-09'),
(8, 7, 400.00, '2024-01-22'),

(9, 8, 2500.00, '2024-01-11'),
(10, 9, 1800.00, '2024-01-14'),
(11, 10, 950.00, '2024-01-19'),

(12, 11, 120.00, '2024-01-05'),
(13, 12, 220.00, '2024-01-06'),
(14, 13, 480.00, '2024-01-07'),
(15, 13, 480.00, '2024-01-21');


SELECT produtos.id, produtos.nome,
sum(valor_venda) as valor_total_vendas_em_reais,
avg(valor_venda) as media_vendas_em_reais

FROM produtos
LEFT join vendas
on produtos.id =  vendas.produto_id
GROUP by produtos.id;
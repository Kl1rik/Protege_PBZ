
# 1 задание вариант 23

SELECT * FROM db_connector;
SELECT * FROM subject;
SELECT * FROM teacher;
SELECT * FROM student_group;
SELECT DISTINCT group_id AS Номера_групп
    FROM db_connector
        WHERE subject_id IN (

SELECT subject_id 

    FROM subject
        WHERE speciality_subject = (

SELECT speciality_student 

    FROM student_group
        WHERE group_name  = "АС-8"
)

)
ORDER BY group_id

;
















# 2 задание вариант 23






SELECT detail_id AS Номер_детали,
detail_name AS Название,
detail_color AS Цвет,
detail_size AS Размер, 
detail_city AS Город 
FROM   details;

SELECT project_id AS Номер_проекта,
project_name AS Название,
project_city AS Город
FROM   projects;


SELECT supplier_id AS Номер_поставщика,
supplier_name AS Название,
status AS Статус,
supplier_city AS Город
FROM   suppliers;

SELECT supplier_id AS Номер_поставщика,
detail_id AS Номер_детали,
project_id AS Номер_проекта,
sum AS Количество
FROM   supplier_orders
ORDER BY project_id;


# 10+  33+ 5+  15+  20+  23+  27+  21+  9+ 29+


#10
SELECT detail_id AS Номер_детали 
FROM  supplier_orders

JOIN suppliers 
    ON  suppliers.supplier_id = supplier_orders.supplier_id
JOIN projects 
    ON  projects.project_id = supplier_orders.project_id

WHERE supplier_orders.supplier_id IN (

    SELECT supplier_id
    FROM   suppliers
    WHERE supplier_city = "Таллин"

) AND supplier_orders.project_id IN (

    SELECT project_id
    FROM   projects
    WHERE project_city = "Таллин"

)
ORDER BY detail_id;


#33
SELECT DISTINCT detail_city AS Номер_детали
FROM  details

JOIN supplier_orders 
    ON  details.detail_id = supplier_orders.detail_id
JOIN projects 
    ON  supplier_orders.project_id = supplier_orders.project_id
JOIN suppliers 
    ON  supplier_orders.supplier_id = suppliers.supplier_id

WHERE detail_city = project_city and detail_city = supplier_city;



#5
SELECT detail_color AS Цвет_детали ,detail_city AS Город_детали 
FROM  details 
ORDER BY detail_color;




#15
SELECT COUNT(project_id) AS Общее_число_проектов
FROM  supplier_orders
WHERE supplier_id = "П1";


#20
SELECT DISTINCT detail_color AS Цвет_детали
FROM  details

JOIN supplier_orders 
    ON  details.detail_id = supplier_orders.detail_id

WHERE supplier_id = "П1";

#23
SELECT DISTINCT supplier_id AS Номер_поставщика
FROM  supplier_orders
    WHERE detail_id  IN (

    SELECT detail_id FROM  details
        WHERE detail_color  = "Красный"

)
ORDER BY supplier_id;

#27
SELECT DISTINCT supplier_id AS Номер_поставщика
FROM  supplier_orders
    WHERE sum > (

    SELECT AVG(sum) 
    FROM  supplier_orders

    ) 
    AND detail_id = "Д1" 
ORDER BY supplier_id;

#21
SELECT DISTINCT detail_id AS Номер_детали
FROM  supplier_orders

    WHERE project_id IN (

    SELECT project_id FROM  projects
        WHERE project_city = "Москва"

);


#9
SELECT DISTINCT detail_id AS Номер_детали
FROM supplier_orders
    JOIN suppliers
         ON supplier_orders.supplier_id = suppliers.supplier_id
WHERE supplier_city = "Таллин"
ORDER BY detail_id;


#29
SELECT project_id AS Номер_проекта
FROM  supplier_orders

    WHERE supplier_id = (

    SELECT  supplier_id
    FROM  supplier_orders
        GROUP BY supplier_id
        HAVING COUNT(DISTINCT project_id) = 1
    ORDER BY supplier_id

);
#Поставщики: 
#( П#, ИмяП, Статус, Город ) 
#Детали: 
#( Д#, ИмяД, Цвет, Размер, Город) 
#Проекты: 
#(ПР#, ИмяПР, Город ) 
#Количество деталей, поставляемых одним поставщиком для одного проекта:#
#SPJ ( П#, Д#, ПР#, S ) 



# создание бд

-- Adminer 4.8.1 MySQL 8.1.0 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `db_connector`;
CREATE TABLE `db_connector` (
  `group_id` char(4) DEFAULT NULL,
  `subject_id` char(4) DEFAULT NULL,
  `teacher_id` char(4) DEFAULT NULL,
  `class_number` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `db_connector` (`group_id`, `subject_id`, `teacher_id`, `class_number`) VALUES
('8Г',	'12П',	'222Л',	112),
('8Г',	'14П',	'221Л',	220),
('8Г',	'17П',	'222Л',	112),
('7Г',	'14П',	'221Л',	220),
('7Г',	'17П',	'222Л',	241),
('7Г',	'18П',	'225Л',	210),
('4Г',	'12П',	'222Л',	112),
('4Г',	'18П',	'225Л',	210),
('3Г',	'12П',	'222Л',	112),
('3Г',	'17П',	'221Л',	241),
('3Г',	'18П',	'225Л',	210),
('17Г',	'12П',	'222Л',	112),
('17Г',	'22П',	'110Л',	210),
('17Г',	'34П',	'430Л',	118),
('12Г',	'12П',	'222Л',	112),
('12Г',	'22П',	'110Л',	210),
('10Г',	'12П',	'222Л',	210),
('10Г',	'22П',	'110Л',	210);

DROP TABLE IF EXISTS `details`;
CREATE TABLE `details` (
  `detail_id` char(10) DEFAULT NULL,
  `detail_name` char(255) DEFAULT NULL,
  `detail_color` char(255) DEFAULT NULL,
  `detail_size` int DEFAULT NULL,
  `detail_city` char(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `details` (`detail_id`, `detail_name`, `detail_color`, `detail_size`, `detail_city`) VALUES
('Д1',	'Болт',	'Красный',	12,	'Москва'),
('Д2',	'Гайка',	'Зеленая',	17,	'Минск'),
('Д3',	'Диск',	'Черный',	17,	'Вильнюс'),
('Д4',	'Диск',	'Черный',	14,	'Москва'),
('Д5',	'Корпус',	'Красный',	12,	'Минск'),
('Д6',	'Крышки',	'Красный',	19,	'Москва');

DROP TABLE IF EXISTS `projects`;
CREATE TABLE `projects` (
  `project_id` char(10) DEFAULT NULL,
  `project_name` char(10) DEFAULT NULL,
  `project_city` char(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `projects` (`project_id`, `project_name`, `project_city`) VALUES
('ПР1',	'ИПР1',	'Минск'),
('ПР2',	'ИПР2',	'Таллин'),
('ПР3',	'ИПР3',	'Псков'),
('ПР4',	'ИПР4',	'Псков'),
('ПР5',	'ИПР5',	'Москва'),
('ПР6',	'ИПР6',	'Саратов'),
('ПР7',	'ИПР7',	'Москва');

DROP TABLE IF EXISTS `student_group`;
CREATE TABLE `student_group` (
  `group_id` char(4) DEFAULT NULL,
  `group_name` char(6) DEFAULT NULL,
  `student_count` int DEFAULT NULL,
  `speciality_student` char(255) DEFAULT NULL,
  `name_leader` char(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `student_group` (`group_id`, `group_name`, `student_count`, `speciality_student`, `name_leader`) VALUES
('8Г',	'Э-12',	18,	'ЭВМ',	'Иванова'),
('7Г',	'Э-15',	22,	'ЭВМ',	'Сеткин'),
('4Г',	'АС-9',	24,	'АСОИ',	'Балабанов'),
('3Г',	'АС-8',	20,	'АСОИ',	'Чижов'),
('17Г',	'С-14',	29,	'СД',	'Амросов'),
('12Г',	'М-6',	16,	'Международная экономика',	'Трубин'),
('10Г',	'Б-4',	11,	'Бухучет',	'Зязюткин');

DROP TABLE IF EXISTS `subject`;
CREATE TABLE `subject` (
  `subject_id` char(4) DEFAULT NULL,
  `name_subject` char(255) DEFAULT NULL,
  `hours_subject` int DEFAULT NULL,
  `speciality_subject` char(255) DEFAULT NULL,
  `semester` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `subject` (`subject_id`, `name_subject`, `hours_subject`, `speciality_subject`, `semester`) VALUES
('12П',	'Мини ЭВМ',	36,	'ЭВМ',	1),
('14П',	'ПЭВМ',	72,	'ЭВМ',	2),
('17П',	'СУБД ПК',	48,	'АСОИ',	4),
('18П',	'ВКСС',	52,	'АСОИ',	6),
('34П',	'Физика',	30,	'СД',	6),
('22П',	'Аудит',	24,	'Бухучета',	3);

DROP TABLE IF EXISTS `supplier_orders`;
CREATE TABLE `supplier_orders` (
  `supplier_id` char(10) DEFAULT NULL,
  `detail_id` char(10) DEFAULT NULL,
  `project_id` char(10) DEFAULT NULL,
  `sum` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `supplier_orders` (`supplier_id`, `detail_id`, `project_id`, `sum`) VALUES
('П2',	'Д3',	'ПР5',	600),
('П2',	'Д3',	'ПР6',	400),
('П2',	'Д3',	'ПР7',	800),
('П2',	'Д5',	'ПР2',	100),
('П3',	'Д3',	'ПР1',	200),
('П3',	'Д4',	'ПР2',	500),
('П4',	'Д6',	'ПР3',	300),
('П5',	'Д2',	'ПР2',	300),
('П5',	'Д2',	'ПР4',	100),
('П5',	'Д5',	'ПР5',	500),
('П5',	'Д5',	'ПР7',	100),
('П5',	'Д6',	'ПР2',	200),
('П5',	'Д1',	'ПР2',	100),
('П5',	'Д3',	'ПР4',	200),
('П5',	'Д4',	'ПР4',	800),
('П5',	'Д5',	'ПР4',	400),
('П5',	'Д6',	'ПР4',	500),
('П1',	'Д1',	'ПР1',	200),
('П1',	'Д1',	'ПР2',	700),
('П2',	'Д3',	'ПР1',	400),
('П2',	'Д2',	'ПР2',	200),
('П2',	'Д3',	'ПР3',	200),
('П2',	'Д3',	'ПР4',	500);

DROP TABLE IF EXISTS `suppliers`;
CREATE TABLE `suppliers` (
  `supplier_id` char(10) DEFAULT NULL,
  `supplier_name` char(255) DEFAULT NULL,
  `status` int DEFAULT NULL,
  `supplier_city` char(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `suppliers` (`supplier_id`, `supplier_name`, `status`, `supplier_city`) VALUES
('П1',	'Петров',	20,	'Москва'),
('П2',	'Синицин',	10,	'Таллин'),
('П3',	'Федоров',	30,	'Таллин'),
('П4',	'Чаянов',	20,	'Минск'),
('П5',	'Крюков',	30,	'Киев');

DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `teacher_id` char(4) DEFAULT NULL,
  `name` char(255) DEFAULT NULL,
  `position` char(255) DEFAULT NULL,
  `department` char(255) DEFAULT NULL,
  `speciality` char(255) DEFAULT NULL,
  `telephone` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `teacher` (`teacher_id`, `name`, `position`, `department`, `speciality`, `telephone`) VALUES
('221Л',	'Фролов',	'Доцент',	'ЭВМ',	'АСОИ,ЭВМ',	487),
('222Л',	'Костин',	'Доцент',	'ЭВМ',	'ЭВМ',	543),
('225Л',	'Бойко',	'Проффесор',	'АСУ',	'АСОИ,ЭВМ',	112),
('430Л',	'Глазов',	'Ассистент',	'ТФ',	'СД',	421),
('110Л',	'Петров',	'Ассистент',	'Экономики',	'Международная экономика',	324);

-- 2023-09-07 19:06:12







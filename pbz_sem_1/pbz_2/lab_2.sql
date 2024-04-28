DROP TABLE IF EXISTS supplier_ingredient;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS way_bills;

CREATE TABLE way_bills  (
  bill_id INTEGER  PRIMARY KEY ,
  date_receipt CHAR(255),
  price INTEGER 
);

CREATE TABLE authors (
  author_id INTEGER  PRIMARY KEY,
  surname CHAR(255),
  name CHAR(255),
  country CHAR(255),
  year CHAR(255)
);
CREATE TABLE supplier_ingredient (
  supplier_id INTEGER  PRIMARY KEY,
  name CHAR(255),
  address CHAR(255)
);

CREATE TABLE recipes (
  recipe_id INTEGER  PRIMARY KEY,
  recipe_name CHAR(255),
  recipe_def CHAR(255),
  FOREIGN KEY (author_id) REFERENCES authors (author_id) ON DELETE CASCADE, 
  cooking_method CHAR(255)
);

#
CREATE TABLE ingredients (
  ingredient_id INTEGER  PRIMARY KEY,
  calories INTEGER ,
  FOREIGN KEY (bill_id) REFERENCES way_bills (bill_id) ON DELETE CASCADE , 
  FOREIGN KEY (supplier_id) REFERENCES supplier_ingredient (supplier_id) ON DELETE CASCADE 

);

CREATE TABLE products (
  product_id INTEGER  PRIMARY KEY,
  FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id) ON DELETE CASCADE ,
  FOREIGN KEY (ingredient_id) REFERENCES ingredients (ingredient_id) ON DELETE CASCADE
);




# Удаляем таблицы, если они существуют
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS ingredients;
DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS supplier_ingredient;
DROP TABLE IF EXISTS way_bills;
DROP TABLE IF EXISTS authors;

# Создаем таблицу way_bills
CREATE TABLE way_bills (
  bill_id INTEGER PRIMARY KEY,
  date_receipt CHAR(255),
  price INTEGER
);

# Создаем таблицу authors
CREATE TABLE authors (
  author_id INTEGER PRIMARY KEY,
  surname CHAR(255),
  name CHAR(255),
  country CHAR(255),
  year CHAR(255)
);

# Создаем таблицу supplier_ingredient
CREATE TABLE supplier_ingredient (
  supplier_id INTEGER PRIMARY KEY,
  name CHAR(255),
  address CHAR(255)
);
CREATE TABLE cook_method(
    method_id INTEGER PRIMARY KEY,
    cook_method CHAR(255)
);
# Создаем таблицу ingredients с внешними ключами bill_id и supplier_id
CREATE TABLE ingredients (
  ingredient_id INTEGER PRIMARY KEY,
  calories INTEGER,
  bill_id INTEGER,
  supplier_id INTEGER,
  FOREIGN KEY (bill_id) REFERENCES way_bills (bill_id) ON DELETE CASCADE,
  FOREIGN KEY (supplier_id) REFERENCES supplier_ingredient (supplier_id) ON DELETE CASCADE
);

# Создаем таблицу recipes с внешним ключом author_id, который ссылается на authors
CREATE TABLE recipes (
  recipe_id INTEGER PRIMARY KEY,
  measure INTEGER,
  recipe_name CHAR(255),
  recipe_def CHAR(255),
  author_id INTEGER,
  method_id INTEGER,
  ingredient_id INTEGER,
  FOREIGN KEY (ingredient_id) REFERENCES ingredients (ingredient_id) ON DELETE CASCADE,
  FOREIGN KEY (method_id) REFERENCES cook_method (method_id) ON DELETE CASCADE,
  FOREIGN KEY (author_id) REFERENCES authors (author_id) ON DELETE CASCADE
);



# Создаем таблицу products с внешними ключами recipe_id и ingredient_id
CREATE TABLE products (
  product_id INTEGER PRIMARY KEY,
  recipe_id INTEGER,
  ingredient_id INTEGER,
  FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id) ON DELETE CASCADE,
  FOREIGN KEY (ingredient_id) REFERENCES ingredients (ingredient_id) ON DELETE CASCADE
);


CREATE TABLE products_group (
    group_id INTEGER PRIMARY KEY, 
    group_name CHAR(255),
    product_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products (product_id) ON DELETE CASCADE



);









# Просмотр прайс-листа заданного поставщика на заданную дату – дата, реквизиты поставщика, название ингредиента, его стоимость за единицу.
SELECT date_receipt,supplier_ingredient.name,ingredient_def,address,price
FROM supplier_ingredient
JOIN ingredients ON supplier_ingredient.supplier_id = ingredients.supplier_id
JOIN way_bills ON ingredients.bill_id = way_bills.bill_id
WHERE date_receipt = "2023-09-14" 
;

#Просмотр списка блюд, имеющих минимальную калорийность.
SELECT recipe_name AS Рецепт ,recipe_def AS Описание
,SUM(subquerry.calories) AS Калорийность 
FROM (



SELECT   recipe_name,recipe_def,calories
  from recipes 
  JOIN ingredients
    ON recipes.ingredient_id_1 = ingredients.ingredient_id 
  
UNION
    
     

SELECT recipe_name,recipe_def,calories 
  from recipes 
  JOIN ingredients
    ON recipes.ingredient_id_2 = ingredients.ingredient_id 
      
UNION

SELECT recipe_name,recipe_def,calories 
  from recipes 
  JOIN ingredients
    ON recipes.ingredient_id_3 = ingredients.ingredient_id 
      

ORDER BY recipe_def

) as subquerry

GROUP BY subquerry.recipe_name,subquerry.recipe_def 
ORDER BY SUM(subquerry.calories)
;




# Просмотр списка блюд и названия рецептов для каждого блюда.
SELECT recipe_name AS Рецепт ,recipe_def AS Описание

FROM (



SELECT   recipe_name,recipe_def,calories
  from recipes 
  JOIN ingredients
    ON recipes.ingredient_id_1 = ingredients.ingredient_id 
  
UNION
    
     

SELECT recipe_name,recipe_def,calories 
  from recipes 
  JOIN ingredients
    ON recipes.ingredient_id_2 = ingredients.ingredient_id 
      
UNION

SELECT recipe_name,recipe_def,calories 
  from recipes 
  JOIN ingredients
    ON recipes.ingredient_id_3 = ingredients.ingredient_id 
      

ORDER BY recipe_def

) as subquerry

GROUP BY subquerry.recipe_name,subquerry.recipe_def 
ORDER BY subquerry.recipe_name

;

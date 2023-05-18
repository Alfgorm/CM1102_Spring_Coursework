-- CREATE TABLE products(
--    prod_id INTEGER PRIMARY KEY NOT NULL,
--    prod_name TEXT NOT NULL,
--    prod_price REAL NOT NULL
--);

--INSERT INTO products(prod_id,prod_name,prod_price)
--VALUES (9,"YS_Deck_Green", 59.99);

--INSERT INTO products(image)
--VALUES

--ALTER TABLE products
--ADD COLUMN image TEXT;

--UPDATE products
--SET image = 'static/built in/Images for my online Flask shop/Yardsale deck 4.webp'
--WHERE prod_id = 9;


--CREATE TABLE cart (
--   prod_id INTEGER PRIMARY KEY NOT NULL,
 --   prod_name TEXT NOT NULL,
 --   prod_price REAL NOT NULL
--);

SELECT * FROM products;

--ALTER TABLE products
--ADD COLUMN description TEXT;

--UPDATE products SET description = 'This beautifull Green yardsale deck has dimesions of width: 7.8"
--length: 31.0" making it the perfect size for smaller skaters. It is also handcrafted with sustainable materials ensuring you leave no negative impact on the environment upon purchase.' WHERE prod_id = 9;




--INSERT INTO products(prod_id,prod_name,prod_price,image,description)
--VALUES (10,"Sk8 Hut Complete Deck",125.00,"static/built in/Images for my online Flask shop/Limited edition.jpeg","This limited edition Sk8 Hut Complete Deck is definately not one that you want to miss!. It comes equiped with grizly griptape ensuring high performance tricks. Aswell as this we have thrown on some Formula Four Wheels that are made from specially developed performance urethane, that holds shape, has fewer flat spots and a controllable grip. As well as this the machinery used to create these wheels runs off of 100% sustainable energy.Also included in the package are our very own branded Trucks made from recycled metal as well as our own specially developed bearings that will ensure you get further with each push!");
-- prepara un servidor sql.


-- crea una base de datos si no existe.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- crea un usuario si no existe.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
--otorgando privilegios.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
--otorgando un solo privilegio.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- recargando los privilegios.
FLUSH PRIVILEGES;


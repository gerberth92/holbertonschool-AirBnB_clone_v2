-- Este modulo prepara un servidor sql.


-- crea una base de datos si no existe.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- crea un usuario si no existe.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- otorga privilegios a un usuario.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- otorga un privilegio.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- recarga los privilegios.
FLUSH PRIVILEGES;


""" Este modulo prepara un servidor sql. """

-- crea una base de datos si no existe.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd";
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";
GRANT SELECT ON performance_schema.* TO "hbnb_dev"@"localhost";
FLUSH PRIVILEGES;


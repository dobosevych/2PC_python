DROP DATABASE IF EXISTS fly;
DROP DATABASE IF EXISTS hotel;
DROP DATABASE IF EXISTS account;

CREATE DATABASE fly;
CREATE DATABASE hotel;
CREATE DATABASE account;

\c fly;

DROP TABLE IF EXISTS booking;

CREATE TABLE booking (
   booking_id VARCHAR(10) PRIMARY KEY,
   client_name VARCHAR(255),
   fly_number VARCHAR(255),
   "from" VARCHAR(255),
   "to" VARCHAR(255),
   date TIMESTAMP
);

INSERT INTO booking(booking_id, client_name, fly_number, "from", "to", date) VALUES ('XXX', 'Nik', 'KLM 1382', 'KBP', 'AMS', '01/05/2015');


\c hotel;

DROP TABLE IF EXISTS booking;

CREATE TABLE booking (
   booking_id VARCHAR(10) PRIMARY KEY,
   client_name VARCHAR(255),
   hotel_name VARCHAR(255),
   arrival TIMESTAMP,
   departure TIMESTAMP
);

INSERT INTO booking(booking_id, client_name, hotel_name, arrival, departure) VALUES ('YYY', 'Nik', 'Hilton', '01/05/2015', '07/05/2015');

\c account;

DROP TABLE IF EXISTS account;

CREATE TABLE account (
   account_id VARCHAR(50) PRIMARY KEY,
   client_name VARCHAR(255),
   amount FLOAT CHECK (amount >= 0)
);

INSERT INTO account(account_id, client_name, amount) VALUES ('YYY', 'Nik', 200);
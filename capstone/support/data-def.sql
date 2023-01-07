CREATE DATABASE capstone;

\c capstone; # Re-enter password

CREATE TABLE address (
    ID SERIAL PRIMARY KEY,
    Address CHAR(50),
    City CHAR(25),
    State CHAR(25),
    ZipCode CHAR(5)
);

CREATE TABLE customer (
    ID SERIAL PRIMARY KEY,
    FirstName CHAR(25),
    LastName CHAR(25),
    AddressID INT REFERENCES address(ID),
    Email CHAR(50)
);

CREATE TABLE account (
    ID SERIAL PRIMARY KEY,
    AccountNumber CHAR(10),
    CustomerID INT REFERENCES customer(ID),
    CurrentBalance INT
);
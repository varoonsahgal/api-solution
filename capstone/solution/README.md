This runs the postgres database locally (for testing before moving to ec2)

`docker run --name postgres -e POSTGRES_PASSWORD=<your password here> -p 5432:5432 -d postgres`


## EC2 migration

This creates the Docker image for your python application - you can run this in EC2 if you have your source code present otherwise run it locally:

`docker build -t accounts_app .` (from solution root)


This will run your python application and also connect to your  RDS  postgres instance:

`docker run --name accounts_app_cont -p 8100:8100 -e PGHOST=<host name> -e PGDATABASE=<database name> PGUSER=<user name> PGPASSWORD=<your password here> -d accounts_app`

Use scripts in `support/data-def.sql` to create database and tables.

# swagger-dialect
SQLAlchemy Swagger definition reflection 

*Swagger_DBAPI* : DBAPI compatible class that returns Swagger model definitions as:
* Tables
* Columns
* Foreign key relationships

Very important to Note, currently a primary key identity column `id` is added to each extracted table definition

*SwaggerDialect* : SQLAlchemy dialect which can translate the schema extraction via Sawgger_DBAPI into valid SQLAlchemy MetaData


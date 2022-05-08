# swagger-dialect
SQLAlchemy Swagger definition reflection 

*Swagger_DBAPI* : DBAPI compatible class that returns Swagger model definitions as:
* Tables
* Columns
* Foreign key relationships

Very important to Note, currently a primary key identity column `id` is added to each extracted table definition

*SwaggerDialect* : SQLAlchemy dialect which can translate the schema extraction via Swagger_DBAPI into valid SQLAlchemy MetaData

Python 10 support only as use is made of the new match statement syntax

Here is an example where Python code is generated for SQLAlchemy from the Swagger definitions. (sqlacodegen>=3.0rc1)

```python
import logging
import argparse
import sys
from contextlib import ExitStack
from typing import TextIO
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import MetaData
from sqlacodegen.generators import DeclarativeGenerator

from swagger_dialect import register_swagger_dialect

LOGGING_FORMAT = "[%(levelname)1.1s %(asctime)s.%(msecs)03d %(process)d %(module)s:%(lineno)d %(name)s] %(message)s"

register_swagger_dialect()


def get_args():
    parser = argparse.ArgumentParser(
        description="Generates SQLAlchemy model code from an existing database."
    )
    parser.add_argument(
        "--option", nargs="*", help="options passed to the generator class"
    )
    parser.add_argument(
        "--version", action="store_true", help="print the version number and exit"
    )
    parser.add_argument(
        "--schemas", help="load tables from the given schemas (comma separated)"
    )
    parser.add_argument(
        "--tables", help="tables to process (comma-separated, default: all)"
    )
    parser.add_argument("--noviews", action="store_true", help="ignore views")
    parser.add_argument("--outfile", help="file to write output to (default: stdout)")
    return parser.parse_args()


def run_reflection(url, model_file_name=None):

    # Use reflection to fill in the metadata
    engine = create_engine(url)
    metadata = MetaData()
    tables = None
    incl_views = False
    schemas = [None]
    for schema in schemas:
        metadata.reflect(engine, schema, incl_views, tables)

    args = get_args()
    generator = DeclarativeGenerator(metadata, engine, set(args.option or ()))

    # Open the target file (if given)
    with ExitStack() as stack:
        outfile: TextIO
        if model_file_name:
            outfile = open(model_file_name, "w", encoding="utf-8")
            stack.enter_context(outfile)
        else:
            outfile = sys.stdout
        outfile.write(generator.generate())


if __name__ == "__main__":
    run_reflection(url='swagger://MyAppSwagger.yaml', model_file_name="generated_model.py")

```
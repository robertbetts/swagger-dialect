import pkg_resources
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import MetaData
from sqlacodegen.generators import DeclarativeGenerator

from swagger_dialect import register_swagger_dialect

swagger_yaml = sample_file = pkg_resources.resource_filename(__name__, "sample_swagger.yaml")

def test_connection():
    register_swagger_dialect()
    from sqlalchemy import create_engine
    engine = create_engine(f'swagger:///{swagger_yaml}')

    with engine.connect() as connection:
        swagger_connection = connection.connection.dbapi_connection
        swagger_version = swagger_connection.get_swagger_version()
        assert swagger_version == "2.0"
        swagger_connection.close()
        swagger_connection.commit()

        assert connection.dialect.has_table(swagger_connection, "Order")
        assert [] == connection.dialect.get_schema_names(swagger_connection)




def test_reflection():
    register_swagger_dialect()

    # Use reflection to fill in the metadata
    swagger_engine = create_engine(f'swagger:///{swagger_yaml}')
    metadata = MetaData()
    tables = None
    incl_views = False
    schemas = [None]
    for schema in schemas:
        metadata.reflect(swagger_engine, schema, incl_views, tables)

    sqlite_engine = create_engine("sqlite:///:memory:")
    metadata.create_all(sqlite_engine)

    generator = DeclarativeGenerator(metadata, swagger_engine, set(()))

    code = generator.generate()
    print (code)



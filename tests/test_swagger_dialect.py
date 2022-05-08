import pkg_resources
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import MetaData

from swagger_dialect import register_swagger_dialect

swagger_yaml = sample_file = pkg_resources.resource_filename(__name__, "sample_swagger.yaml")

def test_connection():
    register_swagger_dialect()
    from sqlalchemy import create_engine
    engine = create_engine(f'swagger:///{swagger_yaml}')


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



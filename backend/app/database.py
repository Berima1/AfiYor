from databases import Database
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from .core.config import settings

# databases supports async db access
DATABASE_URL = str(settings.DATABASE_URL)
database = Database(DATABASE_URL)
metadata = MetaData()

# For synchronous operations (alembic, migrations) engine:
engine = create_engine(DATABASE_URL.replace("+asyncpg", ""), future=True)
SessionLocal = sessionmaker(bind=engine)

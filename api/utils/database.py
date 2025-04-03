# utils/database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DATABASE URL for MySQL (replace credentials if necessary)
DATABASE_URL = "mysql+asyncmy://root:@localhost:3306/kgw_db"

# Set `echo=True` for debugging SQL queries
engine = create_async_engine(DATABASE_URL, echo=True)

# Define an asynchronous session
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

# Dependency: Get Async DB session
async def get_db():
    """Provides a new database session per request."""
    async with AsyncSessionLocal() as session:
        yield session

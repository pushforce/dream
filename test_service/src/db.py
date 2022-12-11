from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from settings import PG_URL

_async_session = None

Base = declarative_base()

async def init():
    engine = create_async_engine(PG_URL, echo=True)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    global _async_session
    _async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session():
    global _async_session

    if _async_session is None:
        await init()
    
    async with _async_session() as session:
        yield session
    
    await session.close()


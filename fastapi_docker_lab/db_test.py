import asyncpg
import asyncio
import os

DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_NAME = os.getenv("POSTGRES_DB", "fastapi_db")
DB_HOST = os.getenv("POSTGRES_HOST", "db")

async def test_connection():
    try:
        conn = await asyncpg.connect(
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            host=DB_HOST
        )
        print("✅ Connection successful!")
        await conn.close()
    except Exception as e:
        print("❌ Connection failed:", e)

if __name__ == "__main__":
    asyncio.run(test_connection())


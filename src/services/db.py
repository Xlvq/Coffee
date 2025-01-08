import aiosqlite

DB_PATH = "loyalty.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS loyalty (
            user_id INTEGER PRIMARY KEY,
            points INTEGER DEFAULT 0
        )
        """)
        await db.commit()


async def get_user_points(user_id: int) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT points FROM loyalty WHERE user_id = ?", (user_id,))
        row = await cursor.fetchone()
        return row[0] if row else 0

# Начисление баллов пользователю
async def add_user_points(user_id: int, points: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
        INSERT INTO loyalty (user_id, points) 
        VALUES (?, ?) 
        ON CONFLICT(user_id) 
        DO UPDATE SET points = points + excluded.points
        """, (user_id, points))
        await db.commit()

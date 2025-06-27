import aiosqlite

DB_PATH = "loyalty.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS loyalty (
                user_id INTEGER PRIMARY KEY,
                points INTEGER DEFAULT 0
            )
            """
        )
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                coffee TEXT,
                volume TEXT,
                milk TEXT,
                syrup TEXT,
                additions TEXT,
                dessert TEXT,
                promo_code TEXT,
                status TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        await db.commit()

async def get_user_points(user_id: int) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT points FROM loyalty WHERE user_id = ?", (user_id,))
        row = await cursor.fetchone()
        return row[0] if row else 0

async def add_user_points(user_id: int, points: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            INSERT INTO loyalty (user_id, points)
            VALUES (?, ?)
            ON CONFLICT(user_id)
            DO UPDATE SET points = points + excluded.points
            """,
            (user_id, points),
        )
        await db.commit()

async def add_order(user_id: int, coffee: str, volume: str | None, milk: str | None,
                    syrup: str | None, additions: list | None, dessert: str | None,
                    promo_code: str | None, status: str = "Создан") -> int:
    additions_str = ",".join(additions) if additions else None
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            """
            INSERT INTO orders (user_id, coffee, volume, milk, syrup, additions, dessert, promo_code, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (user_id, coffee, volume, milk, syrup, additions_str, dessert, promo_code, status),
        )
        await db.commit()
        return cursor.lastrowid

async def update_order_status(order_id: int, status: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
        await db.commit()

async def get_user_orders(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT id, coffee, status, created_at FROM orders WHERE user_id = ? ORDER BY created_at DESC",
            (user_id,),
        )
        return await cursor.fetchall()


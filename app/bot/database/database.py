import aiosqlite


async def add_user(user_id, full_name, username):
    connect = await aiosqlite.connect('app/bot/database/db.db')
    cursor = await connect.cursor()
    check_user = await cursor.execute("SELECT * FROM users WHERE (user_id) = ?", (user_id,))
    check_user = await check_user.fetchone()
    if check_user is None:
        await cursor.execute("INSERT INTO users (user_id, full_name, username) VALUES (?, ?, ?)",
                             (user_id, full_name, username))
        await connect.commit()
    await cursor.close()
    await connect.close()

async def add_password(user_id, title, login, password):
    async with aiosqlite.connect('app/bot/database/db.db') as db:
        async with db.execute('INSERT INTO passwords (user_id, title, login, password) '
                              'VALUES (?, ?, ?, ?)',
                              (user_id, title, login, password)) as cursor:
            await db.commit()
            return await cursor.fetchone()
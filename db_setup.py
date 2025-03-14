from tortoise import Tortoise


async def setup_db():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3", modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()



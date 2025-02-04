"""Создание БД SQLite, подключение, сохранение данных."""
from sqlalchemy import create_engine

engine = create_engine("sqlite:///movies.db")


def save_to_database(df):
    """Сохраняет DataFrame в базу данных SQLite."""
    df.to_sql("movies", engine, if_exists="replace", index=False)
    print("Данные успешно сохранены в базу данных!")

"""Создание DataFrame и удаление дубликатов."""
import pandas as pd


def create_dataframe(movies):
    """Создает DataFrame и выполняет предобработку."""
    df = pd.DataFrame(movies, columns=["title", "year", "rating IMDb"])
    df.drop_duplicates(inplace=True)
    return df

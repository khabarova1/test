"""Точка входа приложения."""
from dataframes.dataframe import create_dataframe
from parsing.html_request import fetch_html
from parsing.parsing import parse_movies


def main():
    """Функция для запуска всех этапов обработки данных."""
    URL = "https://www.film.ru/a-z"
    html = fetch_html(URL)

    if html:
        movies = parse_movies(html)
        df = create_dataframe(movies)
        # Средний рейтинг по годам
        avg_rating = round(df.groupby("year")["rating IMDb"].mean(), 1)
        print(avg_rating)
    else:
        print("Ошибка загрузки страницы.")


if __name__ == "__main__":
    main()
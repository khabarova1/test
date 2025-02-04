"""Парсинг данных с сайта film.ru."""
from bs4 import BeautifulSoup


def parse_movies(html):
    """Парсит HTML и извлекает данные о фильмах."""
    soup = BeautifulSoup(html, "html.parser")
    movies = []

    for movie in soup.find_all("div", class_="redesign_afisha_movie_main"):
        title = movie.find("strong").text.strip()
        year = movie.find("div", class_="redesign_afisha_movie_main_subtitle")
        year = (year.contents[2].strip())[:4]
        rating = movie.find("div", class_="redesign_afisha_movie_main_rating")
        rating = float(rating.find_all("span")[2].text)
        movies.append([title, year, rating])

    try:
        return movies
    except AttributeError as e:
        print(f"Ошибка при парсинге фильма: {e}")

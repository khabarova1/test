"""Get-запрос на получение URL сайта фильмов."""
import requests


def fetch_html(url):
    """Получает HTML-код страницы."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return (f"Ошибка при получении HTML: {e}")

import requests


def get_weather(location, lang):
    url_template = "https://wttr.in/{}?nTQm&lang={}"
    try:
        url = url_template.format(location, lang)
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Ошибка при запросе для {location}: {e}"


def main():
    locations = [
        "Лондон",
        "аэропорт Шереметьево",
        "Череповец",
    ]
    lang = "ru"

    for loc in locations:
        weather = get_weather(loc, lang)
        print(weather)


if __name__ == "__main__":
    main()

import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(url)
        data = response.json()

        joke = f"{data['setup']}\n\n{data['punchline']}"
        return joke

    except Exception as e:
        return f"Error: {e}"
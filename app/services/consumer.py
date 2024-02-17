import requests

def request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json(), 200
    except requests.exceptions.RequestException as e:
        return {"error": f"No se pudieron obtener los datos: {str(e)}"}, 500

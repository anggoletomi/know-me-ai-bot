import requests

SERVICE_URL = "https://know-me-ai-bot.onrender.com/"

def keep_alive():
    try:
        response = requests.get(SERVICE_URL)
        print(f"Keep-alive ping successful: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Keep-alive ping failed: {e}")

if __name__ == "__main__":
    keep_alive()
import requests

def fetch_username():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"

    response = requests.get(url)

    data = response.json()

    if data["success"] and "data" in data:
        print("authors: ",data["data"]["author"])
        print("content: ",data["data"]["content"])
    else:
        raise Exception("failed to fetch user data")

def main():
    try:
        fetch_username()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
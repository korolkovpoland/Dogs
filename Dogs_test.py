import requests
import webbrowser

def image():
    
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")

        if response.status_code == 200:
            data = response.json()

            if data["status"] == "success":
                image_url = data["message"]
                print(f"Dog image URL: {image_url}")
                webbrowser.open(image_url)

            else:
                print(f"Error: {data['message']}")
        else:
            print(f"Error: {response.status_code}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

image()
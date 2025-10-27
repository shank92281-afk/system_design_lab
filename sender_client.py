import requests
import json
import time

def send_data():
    url = "http://127.0.0.1:9000/data"   # Receiver API endpoint

    payload = {
        "message": "Hello Receiver!",
        "from": "Sender Client",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        print("🚀 Sending data to receiver...")
        response = requests.post(url, json=payload)

        # Check if request was successful
        if response.status_code == 200:
            print("✅ Success:", response.json())
        else:
            print(f"⚠️ Failed with status code {response.status_code}")
            print("Response:", response.text)

    except requests.exceptions.ConnectionError:
        print("❌ Connection error — is the receiver running on port 9000?")
    except requests.exceptions.RequestException as e:
        print("❌ Request failed:", e)
    except json.JSONDecodeError:
        print("⚠️ Could not decode JSON response")

if __name__ == "__main__":
    send_data()

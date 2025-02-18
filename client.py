import pyautogui
import requests
import platform
import datetime
import time

# List of images to look for
images_to_detect = ["youtube.png", "twitch.png", "steam1.png", "steam2.png", "steam3.png", "steam4.png", "modrinth.png"]  # Replace with your image filenames

# Flask server URL
server_url = "http://127.0.0.1:5000/report"  # Replace with your server's URL

def get_device_name():
    """Get the device's name."""
    return platform.node()

def send_to_server(image_name):
    """Send detected image info to the server."""
    data = {
        "image": image_name,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "device": get_device_name()
    }
    try:
        response = requests.post(server_url, json=data)
        print(f"Sent to server: {response.status_code}")
    except Exception as e:
        print(f"Failed to send data: {e}")

def main():
    print("Starting image detection...")
    while True:
        for image in images_to_detect:
            try:
                location = pyautogui.locateOnScreen(image, confidence=0.6)  # Adjust confidence as needed
                if location:
                    print(f"Detected {image} at {datetime.datetime.now()}")
                    send_to_server(image)
                    time.sleep(1)  # To avoid spamming the server
            except pyautogui.ImageNotFoundException:
                print(f"Image {image} not found.")
        time.sleep(2)  # Small delay to avoid high CPU usage
        print("\n Looping... \n")

if __name__ == "__main__":
    main()

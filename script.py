import pyscreenshot as Imagegrab
import os
import time
from datetime import datetime

INTERVAL = 120
SAVE_FOLDER = "captures"

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

def capture_screenshot():
    """Prend une capture d'écran et l'enregistre avec un horodatage."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(SAVE_FOLDER, f"screenshot_{timestamp}.jpg")

    screenshot = Imagegrab.grab()
    screenshot.save(filename, "JPEG")

    print(f"[*] Capture d'écran enregistrée : {filename}")

def main():
    """Boucle infinie pour capturer des écrans à intervalle régulier."""
    while True:
        capture_screenshot()
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()

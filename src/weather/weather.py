import fire
from PIL import Image
from io import BytesIO
import requests

def weather (city = "London"):
	response = requests.get(f"https://wttr.in/{city}.png")
	img = Image.open(BytesIO(response.content))
	img.show()

if __name__ == '__main__':
	fire.Fire(weather)
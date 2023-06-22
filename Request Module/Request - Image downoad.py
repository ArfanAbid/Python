import requests
from PIL import Image
from io import BytesIO
r= requests.get("https://assets.telegraphindia.com/telegraph/2022/Mar/1647575151_resized-pic23.jpg")
i=Image.open(BytesIO(r.content))
fp= open("Img.jpg","wb")
i.save(fp)
fp.close
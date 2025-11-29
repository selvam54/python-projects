import qrcode

link="https://www.youtube.com/"

img=qrcode.make(link)
img.save("youtube.png")

print("qrcode is created")
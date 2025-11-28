# qr code project

# qr code project

import qrcode

text = """Two hearts met in the most unexpected way.
What began as small jokes and playful teasing slowly turned into something deeper.
Every time their eyes met, the world around them felt a little quieter… a little softer.

One would pretend to be calm, but secretly enjoyed every moment of attention.
The other knew exactly how to make them blush — a smile here, a wink there,
just enough to make their heart race.

One evening, while walking side by side, their hands brushed for a second.
Neither pulled away. The air felt warm, the moment felt right.
A gentle breeze passed, and suddenly fingers intertwined naturally,
as if they had always belonged together.

‘I think you make my life a little sweeter,’ one whispered.
The other smiled back, eyes shining.
‘Good… because you make mine a little brighter every day.’

And just like that, without loud declarations or grand gestures,
a soft, magical, flirty love began — built from tiny moments,
quiet smiles, and the feeling of being exactly where they belong.
"""

img = qrcode.make(text)
img.save("love_story.png")

print("QR code saved successfully!")

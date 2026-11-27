from PIL import Image, ImageDraw

S = 1024
c1 = (23, 219, 165)
c2 = (5, 110, 80)
img = Image.new('RGB', (S, S))
d = ImageDraw.Draw(img)
for y in range(S):
    t = (y / (S - 1)) ** 0.85
    col = (int(c1[0] + (c2[0]-c1[0])*t), int(c1[1] + (c2[1]-c1[1])*t), int(c1[2] + (c2[2]-c1[2])*t))
    d.line([(0, y), (S, y)], fill=col)

sheen = Image.new('L', (S, S), 0)
sd = ImageDraw.Draw(sheen)
for i in range(90):
    a = int(26 * (1 - i/90))
    sd.polygon([(0, 0), (S*0.95 - i*6, 0), (0, S*0.95 - i*6)], fill=a)
img = Image.composite(Image.new('RGB', (S, S), (255, 255, 255)), img, sheen)
d = ImageDraw.Draw(img)

white = (255, 255, 255)

def rounded_line(draw, p1, p2, width, fill):
    draw.line([p1, p2], fill=fill, width=width)
    r = width / 2
    for (x, y) in (p1, p2):
        draw.ellipse([x-r, y-r, x+r, y+r], fill=fill)

top_y, bot_y, half = 350, 740, 190
rounded_line(d, (512-half, top_y), (512+half, top_y), 58, white)
rounded_line(d, (512, top_y), (512, bot_y), 58, white)

def star(cx, cy, R, r, fill):
    d.polygon([(cx, cy-R), (cx+r, cy-r), (cx+R, cy), (cx+r, cy+r),
               (cx, cy+R), (cx-r, cy+r), (cx-R, cy), (cx-r, cy-r)], fill=fill)

star(774, 246, 72, 20, white)
star(866, 138, 38, 11, white)

img = img.resize((512, 512), Image.LANCZOS)
img.save('icon-512.png', optimize=True)
img.resize((192, 192), Image.LANCZOS).save('icon-192.png', optimize=True)
img.resize((180, 180), Image.LANCZOS).save('icon-180.png', optimize=True)
print('ok')

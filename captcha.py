import random
from scipy import ndimage

from PIL import Image, ImageDraw, ImageFont, ImageFilter


def draw_lines(draw, size):
    for i in range(random.randint(3, 10)):
        start = random.randint(0, size[0]), random.randint(0, size[1])
        end = random.randint(0, size[0]), random.randint(0, size[1])
        draw.line([start, end], fill=(random.randint(128, 255), random.randint(128, 255), random.randint(128, 255)),
         width=random.randint(2, 6))


def create_captcha(size):
    bg = Image.new("RGBA", size, (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255)))
    draw = ImageDraw.Draw(bg)
    draw_lines(draw, (600, 150))

    chars = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str = ''
    ran = random.randint(3, 4)
    u, v = 0, 0
    if ran == 3:
        u = random.randint(0, 150)
    else:
        u = random.randint(0, 40)

    for i in range(ran):
        ind = random.randint(0, 25)
        str += chars[ind]
        fg = Image.open('ref_img/'+chars[ind]+'_e.png')
        
        datas = fg.getdata()

        boun_col = (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))
        inside_col = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            
            elif item[0] ==255 and item[1] == 174 and item[2] == 201:
                newData.append(inside_col)
            else:
                newData.append(boun_col)

        fg.putdata(newData)

        fg = fg.rotate(10*random.randint(-3, 3))
        
        bg.paste(fg, (u, v), fg)

        u += 140

    return bg, str

for i in range(2000):
    img, name = create_captcha((600, 150))
    img = img.convert('RGB')
    name = 'test_samples/'+name+'.png'
    img.save(name, 'png')
    

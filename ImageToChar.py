from PIL import Image

#灰度与字符的映射
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

WIDTH=int(input("请输入你想输出的宽度："))
HEIGHT=int(input("请输入你想输出的高度："))
INPUT=r'D:\Download\psb.jpg'
OUTPUT=r'D:\Download\output.txt'

def get_char(r,g,b,alpha=256):
    if alpha==0:
        return ' '
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
    length=len(ascii_char)
    unit=(256+1)/length
    return ascii_char[int(gray/unit)]

im=Image.open(INPUT)
im=im.resize((WIDTH,HEIGHT),Image.NEAREST)

txt=''

for i in range(HEIGHT):
    for j in range(WIDTH):
        txt += get_char(*im.getpixel((j,i)))
    txt += '\n'

with open(OUTPUT,'w') as f:
    f.write(txt)

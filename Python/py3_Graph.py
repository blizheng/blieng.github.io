from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    if alpha ==0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

#argparse 使用
# 创建 ArgumentParser() 对象
parser = argparse.ArgumentParser()
# 调用 add_argument() 方法添加参数

parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--height',type = int, default = 80)
parser.add_argument('--width',type = int, default = 80)

args = parser.parse_args()# 使用 parse_args() #解析添加的参数

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

if __name__ == '__main__':
    im = Image.open(IMG)#打开图片文件
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)#改变图像的大小：

    txt = " "

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))获取某个像素位置的值：
    print(txt)
    if OUTPUT:#如果OUTPUT不为空
        with open(OUTPUT, 'w') as f:#将txt中内容写入OUTPUT
            f.write(txt)
    else:#如果OUTPUT为空
        with open("output.txt", 'w') as f: #将txt中的内容写入到output.txt
            f.write(txt)

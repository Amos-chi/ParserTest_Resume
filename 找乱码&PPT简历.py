import os
import fitz


def checkCHAR(file):
    try:
        doc = fitz.Document(file)
        page = doc[0]
        garbled_count = len([x for x in page.get_text() if ord(x) > 65500])
        if garbled_count > len(page.get_text()) * 0.5:
            print(f'{file} 乱码 ..............................')

        width, height = page.rect[2], page.rect[3]
        if width > 1.2 * height:
            print(f'ppt {file}.................')
    except:
        pass


dir = r'E:\中英文简历总\resume en'
files = os.listdir(dir)
for file in files:
    checkCHAR(os.path.join(dir,file))
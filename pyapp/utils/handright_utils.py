from PIL import Image, ImageFont

from handright import Template, handwrite
import os

def get_handwrite(text, fontPath, outputPath):
    if outputPath == '' or outputPath is None:
        outputPath = os.path.join(os.path.expanduser("~"), 'Desktop')
    
    # text = "我能吞下玻璃而不伤身体。"
    template = Template(
        background=Image.new(mode="1", size=(1024, 2048), color=1),
        font=ImageFont.truetype(fontPath, size=100),
    )
    images = handwrite(text, template)

    img_out_path = outputPath + "/{}.webp".format(text[0:10])
    for im in images:
        assert isinstance(im, Image.Image)
        im.save(img_out_path)
        break
    
    return img_out_path
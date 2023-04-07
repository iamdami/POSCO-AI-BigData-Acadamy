import os

image_dir = "Pytorch_Retinaface/faceCroped/croped_JH"
txt_dir = "Pytorch_Retinaface/faceLabelCroped/labelCroped_JH"
if not os.path.isdir(txt_dir):
    os.mkdir(txt_dir)

txt_files = [os.path.join(txt_dir, f) for f in os.listdir(txt_dir) if f.endswith('.txt') and os.path.getsize(os.path.join(txt_dir, f)) == 0]

for f in os.listdir(image_dir):
    if f.endswith('.jpg'):
        img_name = os.path.splitext(f)[0]
        txt_name = img_name + '.txt'
        txt_path = os.path.join(txt_dir, txt_name)
        with open(txt_path, 'w') as file:
            file.write('')

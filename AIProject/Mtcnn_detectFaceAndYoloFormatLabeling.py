import cv2, os
from mtcnn.core.detect import create_mtcnn_net, MtcnnDetector

pnet, rnet, onet = create_mtcnn_net(p_model_path="./original_model/pnet_epoch.pt", r_model_path="./original_model/rnet_epoch.pt", o_model_path="./original_model/onet_epoch.pt", use_cuda=False)
mtcnn_detector = MtcnnDetector(pnet=pnet, rnet=rnet, onet=onet, min_face_size=24)

oriFaceImgDir = "data_set/SB"
txtDir = "new_SB"
if not os.path.isdir(txtDir):
    os.mkdir(txtDir)

for f in os.listdir(oriFaceImgDir):
    img_name = os.path.splitext(f)[0]
    txt_name = img_name + '.txt'
    img_path = os.path.join(oriFaceImgDir, f)
    txt_path = os.path.join(txtDir, txt_name)

    img = cv2.imread("data_set/SB/IMG_0045.JPG")
    height, width, _ = img.shape
    bboxes, landmarks = mtcnn_detector.detect_face(img)

    with open(txt_path, 'w') as file:
        for bbox in bboxes:
            x, y, w, h = bbox[0:4].astype(int)
            centerX = x + w/2
            centerY = y + h/2
            imgWidth, imgHeight = img.shape[1], img.shape[0]
            centerX /= imgWidth
            centerY /= imgHeight
            bboxWidth = w / imgWidth
            bboxHeight = h / imgHeight

            yoloBboxStr = f"0 {centerX:.6f} {centerY:.6f} {bboxWidth:.6f} {bboxHeight:.6f}"
            file.write(yoloBboxStr + '\n')

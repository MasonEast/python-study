import cv2

def oil_painting_effect(image_path, output_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 转换颜色通道，OpenCV读取图片是BGR, 需要转换为RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 使用油画效果（油画滤波器）
    oil_painted_image = cv2.xphoto.oilPainting(image_rgb, 7, 1)

    # 保存处理后的图像
    cv2.imwrite(output_path, cv2.cvtColor(oil_painted_image, cv2.COLOR_RGB2BGR))

# 替换为你的图像路径
input_image_path = '../static/test.jpeg'
output_image_path = 'output_oil_painting.jpg'
oil_painting_effect(input_image_path, output_image_path)
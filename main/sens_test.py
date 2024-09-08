import cv2
import numpy as np
import mainGenarator as gen

format = "111001011110011"

data2 = "0010000000111001110011010100010101000111001101001111000011101100000100011110110000010001111011000001000111101100000100011110110000010001111011000001000110011010010110111001010000010101100100001110100000101010"
data = "0213404321430432043214304302013040302430200103402104032104032043204030204301204032004203040020430030210321431043014034321032014032104032040320301403020103024030210403201032031040302140340302001020304030210203"


def decoderCV2(image):
    qrCodeDetector = cv2.QRCodeDetector()
    decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
    if points is not None:
        points = points[0]  # Reshape points array if necessary
        return True, points
    return False, []

def doScan():
    sens = 50
    dectedqr = False
    qrtries = 0
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read() 
    
        dectedqr, point = decoderCV2(frame)
        if dectedqr == True and qrtries == sens:
            p1 = [point[0][0], point[0][1]]
            p3 = [point[1][0], point[1][1]]
            p4 = [point[2][0], point[2][1]]
            p2 = [point[3][0], point[3][1]]

            width = 210
            height = 210

            input_points = np.float32([p1, p2, p3, p4])
            converted_points = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            matrix = cv2.getPerspectiveTransform(input_points, converted_points)
            img_output = cv2.warpPerspective(frame, matrix, (width, height))
            cv2.destroyAllWindows()       
            break
        if dectedqr == True:
            qrtries += 1
        cv2.imshow("cam", frame)
        code = cv2.waitKey(10)
        if code == ord('q'):
            break
    return img_output

def sharpen_and_enhance_colors(image, sharpening_intensity=0.5, color_enhance_method='none'):
    # Convert image to float32 for more precise operations
    image = image.astype(np.float32) / 255.0
    
    # Sharpening kernel
    kernel = np.array([[-1, -1, -1],
                       [-1, 9 + sharpening_intensity, -1],
                       [-1, -1, -1]])
    
    # Apply the sharpening filter
    sharpened_image = cv2.filter2D(image, -1, kernel)
    
    # Clip values to [0, 1] and convert back to uint8
    sharpened_image = np.clip(sharpened_image * 255, 0, 255).astype(np.uint8)
    
    # Color enhancement
    if color_enhance_method == 'clahe':
        # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to each channel
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        channels = cv2.split(sharpened_image)
        enhanced_channels = [clahe.apply(channel) for channel in channels]
        enhanced_image = cv2.merge(enhanced_channels)
    else:
        # Apply histogram equalization to each channel
        channels = cv2.split(sharpened_image)
        enhanced_channels = [cv2.equalizeHist(channel) for channel in channels]
        enhanced_image = cv2.merge(enhanced_channels)
    
    return enhanced_image

def increase_contrast(image, alpha=1.5, beta=0):
    # Increase contrast using convertScaleAbs
    contrast_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return contrast_image

def quantize_image(image, qr_code_colors):

    # Load the image to be filtered
    image_to_filter = image
    
    # Convert colors to HSV or another color space as needed
    qr_code_colors_hsv = [cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)[0][0] for color in qr_code_colors]

    # Create a mask to filter colors
    mask = np.zeros(image_to_filter.shape[:2], dtype=np.uint8)

    for color in qr_code_colors_hsv:
        lower_bound = np.array(color) - np.array([100, 100, 100])  # Adjust bounds as needed
        upper_bound = np.array(color) + np.array([255, 255, 255])  # Adjust bounds as needed
        color_mask = cv2.inRange(cv2.cvtColor(image_to_filter, cv2.COLOR_BGR2HSV), lower_bound, upper_bound)
        mask = cv2.bitwise_or(mask, color_mask)

    # Apply the mask to the image
    filtered_image = cv2.bitwise_and(image_to_filter, image_to_filter, mask=mask)
    
    return filtered_image

def find_closest_color(image, roi_start, roi_size, color_list):
    x_start, y_start = roi_start
    width, height = roi_size

    roi = image[y_start:y_start + height, x_start:x_start + width]
    avg_color = cv2.mean(roi)[:3]
    avg_color = np.array(avg_color)

    min_dist = float('inf')
    closest_color = None
    second_closest_color = None

    for color in color_list:
        color_np = np.array(color)
        dist = np.linalg.norm(avg_color - color_np)
        if dist < min_dist:
            min_dist = dist
            second_closest_color = closest_color
            closest_color = color

    if second_closest_color is not None:
        mixed_color = np.mean([closest_color, second_closest_color], axis=0)
        mixed_dist = np.linalg.norm(avg_color - mixed_color)
        if mixed_dist < min_dist:
            return tuple(mixed_color.astype(int))
    
    return closest_color

def extract_colors(image, colors):
    Matrix = [[0 for x in range(21)] for y in range(21)]
    size = (10, 10)
    for y in range(21):
        for x in range(21):
            Matrix[x][y] = find_closest_color(image, (x*10,y*10), size, colors)
    return Matrix

def display_matrix(Matrix, scaling = 10, windowsSize = [21, 21]):
    img = np.zeros((windowsSize[0]*scaling, windowsSize[1]*scaling, 3), np.uint8)
    for y in range(21):
        for x, i in enumerate(Matrix[y]):
            if i == [255, 255, 255]:
                img[y*scaling:y*scaling+scaling, x*scaling:x*scaling+scaling] = (255, 255, 255)
            elif i == [0, 0, 0]:
                img[y*scaling:y*scaling+scaling, x*scaling:x*scaling+scaling] = (0, 0, 0)
            elif i == [255, 0, 0]:
                img[y*scaling:y*scaling+scaling, x*scaling:x*scaling+scaling] = (255, 0, 0)
            elif i == [0, 255, 0]:
                img[y*scaling:y*scaling+scaling, x*scaling:x*scaling+scaling] = (0, 255, 0)
            elif i == [0, 0, 255]:
                img[y*scaling:y*scaling+scaling, x*scaling:x*scaling+scaling] = (0, 0, 255)
    return img

def compare_accuracy(array1, array2):
    correct = sum(1 for i in range(len(array1)) for j in range(len(array1[0])) if array1[i][j] == array2[i][j])
    total = len(array1) * len(array1[0])
    accuracy = (correct / total) * 100
    return round(accuracy, 1), f"{correct}/{total}"

colors = [
    [0, 255, 0],  # Green
    [255, 0, 0],  # Blue
    [0, 0, 255],  # Red
    [255, 255, 255],  # White
    [0, 0, 0],   # Black
    [255, 0, 255], #pink
    [255, 255, 0], #Yellow
    [0, 255, 255] #purple
]

img_output = doScan()
img_filter = quantize_image(img_output, colors)

cv2.imshow("filter", img_filter)
cv2.waitKey(10)

cv2.imshow("sharp", sharpen_and_enhance_colors(img_filter))
cv2.waitKey(10)

img = display_matrix(extract_colors(img_filter, colors))

cv2.imshow("out", img)
cv2.waitKey(0)
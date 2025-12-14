import cv2
import numpy as np

def combine_images(image1_path, image2_path, output_path):
    # Load the two images
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # Check if images are loaded properly
    if img1 is None or img2 is None:
        raise ValueError("One of the images could not be loaded. Check the file paths.")

    # Resize images to the same height
    height = min(img1.shape[0], img2.shape[0])
    img1_resized = cv2.resize(img1, (int(img1.shape[1] * height / img1.shape[0]), height))
    img2_resized = cv2.resize(img2, (int(img2.shape[1] * height / img2.shape[0]), height))

    # Combine images side by side
    combined_image = np.hstack((img1_resized, img2_resized))

    # Save the combined image
    cv2.imwrite(output_path, combined_image, [int(cv2.IMWRITE_JPEG_QUALITY), 60])

# Example usage
combine_images('max-power-transfer.png', 'maksimum_guc_transferi.png', 'power-transfer.jpg')
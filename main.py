# Image Encryption using Pixel Manipluiation
# Here the pixel of an image is permutated randomly
# the randomness is depended on key provided by the user


# Defining Library
import cv2 as img  # OpenCV(Open Computer Vision) Library
import numpy as np  # NumPy for calculation
import random  # random for randomness

# Defining functions


def execution(uploaded_image, process):
    # verifying if the image has been uploaded or not
    '''
        If the image is not found then 
        print the error message and 
        exit
    '''
    if (uploaded_image is None):
        print("IMAGE NOT FOUND")
        return 0

    keyFlag = False  # setting the initial value of keyFlag for key input
    '''
        Loop until key is not provided
    '''
    while (not keyFlag):
        key = input("Enter Key:\n")
        if (key != ''):
            keyFlag = True
        else:
            print("Please Enter Key to continue...\n")
    # End of loop

    if (process == 'encrypt'):
        return encryption(uploaded_image, key)
    else:
        return decryption(uploaded_image, key)


def encryption(image, key):
    encrypted_image = np.zeros_like(image)
    random.seed(key)
    height, width, _ = image.shape

    permutation = list(range(height * width))

    random.shuffle(permutation)
    for i in range(height):
        for j in range(width):
            index = permutation[i*width + j]
            encrypted_image[i, j] = image[index // width, index % width]

    return encrypted_image


def decryption(image, key):
    decrypted_image = np.zeros_like(image)
    random.seed(key)
    height, width, _ = image.shape

    permutation = list(range(height * width))
    random.shuffle(permutation)

    for i in range(height):
        for j in range(width):
            index = permutation[i * width + j]
            decrypted_image[index // width, index % width] = image[i, j]

    return decrypted_image
# End of custom functions


# Load the image
image_path = "example_image.jpg"
encrypted_path = "encrypted_image.jpg"

# user input process
processKey = True
while (processKey):
    process = input(
        "'encrypt' for Encryption, 'decrypt' for Decryption and 'q' for quit...\n").lower()

    if (process == 'q'):
        processKey = False
        print("Exiting....")
    elif (process == 'encrypt' or process == 'decrypt'):
        # image = execution(original_image, process)
        # img.imwrite("encrypted_image.jpg", image)
        if (process == 'encrypt'):
            image = execution(img.imread(image_path), process)
            img.imwrite("encrypted_image.jpg", image)
            img.imshow("Encrypted Image", image)
        else:
            image = execution(img.imread(image_path), process)
            # img.imwrite("encrypted_image.jpg", image)
            img.imshow("Decrypted Image", image)

        img.waitKey(0)
        img.destroyAllWindows()
    else:
        print("Invalid Input.\nPlease try again")

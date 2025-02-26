import cv2

img = cv2.imread("encryptedImage.png")

# Try to read the passcode from the file
try:
    with open("pass.txt", "r") as f:
        correct_pass = f.read().strip()
except FileNotFoundError:
    print("Password file is missing!")
    exit()

# Input the passcode
password = input("Enter the passcode: ")
if password != correct_pass:
    print("Access denied!")
    exit()

# Extract the hidden message from the image
msg_bytes = bytearray()
for n in range(img.shape[0]):
    for m in range(img.shape[1]):
        for z in range(3):
            byte = img[n, m, z]
            if byte == 0:  # Stop at the NULL byte
                break
            msg_bytes.append(byte)
        if byte == 0:
            break
    if byte == 0:
        break

# Decode and print the secret message
msg = msg_bytes.decode("utf-8")
print("The secret message is:", msg)

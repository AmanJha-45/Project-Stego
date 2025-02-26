import cv2

# Read the image
img = cv2.imread("mypic.jpg")

msg = input("Enter the secret message: ")
password = input("Enter a passcode: ")

# Save the passcode to a file
with open("pass.txt", "w") as f:
    f.write(password)
msg += "\0"
msg_bytes = msg.encode("utf-8")

# Check if the message fits within the image
if len(msg_bytes) > img.size:
    print("The message is too long to be hidden in this image.")
    exit()
index = 0
for n in range(img.shape[0]):
    for m in range(img.shape[1]):
        for z in range(3):
            if index < len(msg_bytes):
                img[n, m, z] = msg_bytes[index]
                index += 1
            else:
                break
        if index >= len(msg_bytes):
            break
    if index >= len(msg_bytes):
        break

# Save the encrypted image
cv2.imwrite("encryptedImage.png", img)
print("Encryption completed. The image is saved as 'encryptedImage.png'.")

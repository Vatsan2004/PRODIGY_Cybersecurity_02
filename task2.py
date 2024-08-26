from PIL import Image
import random

def encrypt_image(image_path, output_path):
    try:
        image = Image.open(image_path)
        pixels = image.load()
        width, height = image.size

        # Apply a simple pixel shift for encryption
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                # Simple transformation: shift RGB values
                r = (r + 50) % 256
                g = (g + 100) % 256
                b = (b + 150) % 256
                pixels[i, j] = (r, g, b)

        image.save(output_path)
        print(f"Image encrypted and saved as {output_path}")

    except FileNotFoundError:
        print(f"File not found: {image_path}. Please check the file path and try again.")

def decrypt_image(encrypted_path, output_path):
    try:
        image = Image.open(encrypted_path)
        pixels = image.load()
        width, height = image.size

        # Reverse the simple pixel shift for decryption
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                r = (r - 50) % 256
                g = (g - 100) % 256
                b = (b - 150) % 256
                pixels[i, j] = (r, g, b)

        image.save(output_path)
        print(f"Image decrypted and saved as {output_path}")

    except FileNotFoundError:
        print(f"File not found: {encrypted_path}. Please check the file path and try again.")

# Use paths for testing
image_path = r'C:\Users\welcome\Downloads\images.jpg'
encrypted_image_path = r'C:\Users\welcome\Downloads\encrypted_image.png'
decrypted_image_path = r'C:\Users\welcome\Downloads\decrypted_image.png'

# Encrypt and decrypt the image
encrypt_image(image_path, encrypted_image_path)
decrypt_image(encrypted_image_path, decrypted_image_path)

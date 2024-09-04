# PRODIGY_CS_02
<h1>Image Encryption and Decryption</h1>
<p>This Python script provides functionality for encrypting and decrypting images using simple pixel manipulation techniques. It uses the PIL (Pillow) library for image processing and numpy for array operations. The script currently supports both RGB and grayscale images.</p>

<h2>Encryption</h2>
<p>th Function encrypt(path, value, save_path) Encrypts an image by shuffling its pixels based on a given key.</p>
<h3>Process:</h3>
<p>The image is opened through the given path and converted into a NumPy array.
For each pixel, new coordinates are computed using a combination of mathematical operations and bitwise XOR operations.
The pixels are swapped based on the new coordinates.
The modified array is converted back into an image and saved in the given path.</p>
<h2>Decryption</h2>
the function decrypt(path, value, save_path) decrypts an image that was previously encrypted using the same key.
<h3>Process:</h3>
<p>The encrypted image is opened and converted into a NumPy array.
For each pixel, new coordinates are computed in reverse of the encryption process.
The pixels are restored to their original positions based on the computed coordinates.
The modified array is converted back into an image and saved.</p>
<h2>User Input</h2>
<p>The script interacts with the user via the command line to:
<h3>Input the Image Path:</h3> The path to the image file to be encrypted or decrypted.
<h3>Input the Key:</h3> An integer value used for encryption or decryption.
<h3>Input Save Path:</h3> The path where the resulting image (encrypted or decrypted) will be saved.
<h3>Choose Operation:</h3> Specify whether to encrypt (enter 1) or decrypt (enter 2).</p>
<h2>usage exampel:</h2>
encrypting the image cats.jpg with the key 55 and decrypting it back

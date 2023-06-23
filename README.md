# qr-generator

This Python project generates QR codes using the QR code generator library. It allows you to create QR codes with your desired qr and background color. It also allows you to create qr codes for various purposes, such as sharing URLs, contact information, or text messages.


## Installation
To use this QR code generator, you need to have Python installed on your machine. You can download Python from the official website: python.org

Additionally, you need to install the required dependencies. Open your terminal or command prompt and run the following command:

```
 pip install qrcode
```
And Also install Pillow Library :
``` pip install Pillow ```

## Usage
1. Import the qrcode module into your Python script:
   
   ```python
   import qrcode
   ```

2.Import the Image module from PIL library into your Python script:

  ```python
  from PIL import Image
  ```

3. Create a QR code instance and specify the data you want to encode:
   
   ```python
   qr = qrcode.QRCode(version=1,
               error_correction=qrcode.constants.ERROR_CORRECT_H,
               box_size=10, border=4,
                     )
                     
    user = input("Enter your Link: ")
    color = "black"
    bgColor = "white"
    color = input("Enter your qr color: ")
    bgColor = input("Enter your Baclkground color: ")

     qr.add_data(user)
     qr.make(fit=True)
     ```

4. Generate the QR code image:
   
   ```python
   img = qr.make_image(fill_color=color, back_color=bgColor)
   ```

5. Save the QR code image to a file:

   ```python
   img.save("Qrcode.png")
   ```

6. Run your Python script, and it will generate a QR code image named qrcode.png in the current directory.

 Feel free to modify the code according to your specific requirements.


## Contributing
If you would like to contribute to this project, you are welcome to submit pull requests. Please ensure that your contributions adhere to the coding standards and follow the project's guidelines.


## Acknowledgments
The QR code generation functionality is powered by the qrcode library (https://pypi.org/project/qrcode/).
Thanks to the open-source community for their contributions and continuous support.

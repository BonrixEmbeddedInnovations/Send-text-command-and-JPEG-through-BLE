# Send-text-command-through-BLE-to-Dynamic-QR-code-Scanner-Display-DQR-111
This repository contains two python scripts for for send text command to display different screens and send jpeg image in chunks through BLE.

**1.  Script Name: sendtextcommand.py**

Description:
This Python script is designed to interface with a 3.5-inch 320x480 pixel display over Bluetooth Low Energy (BLE). It allows users to send text commands to the display to switch between different screens. This functionality is useful for applications where multiple display states or screens are required.

Key Features:

•	Establishes a BLE connection to the display.

•	Sends text commands to switch between different screens.

•	Can be easily modified to include additional commands as needed.

Usage:

•	Ensure the display is powered on and in BLE mode.

•	Run the script and follow the prompts to send text commands.

•	Observe the display change screens according to the sent commands.

Dependencies:

•	bleak (BLE library for Python)


# Send-JPEG-Image-File-through-BLE-to-Dynamic-QR-code-Scanner-Display-DQR-111

*2. 	Script Name: sendjpeg.py*


Description:

This Python script enables users to send JPEG images in chunks via Bluetooth Low Energy (BLE). The script handles the process of splitting the image into manageable chunks and transmitting them sequentially to the display. This is ideal for applications requiring dynamic image updates on the display.

Key Features:

•	Establishes a BLE connection to the device.

•	Splits JPEG images into chunks and sends them sequentially.

•	Ensures proper reassembly and display of the image on the screen.

Usage:

•	Ensure the display is powered on and in BLE mode.

•	Run the script with the path to the JPEG image you wish to send.

•	The script will handle the rest, and the image will be displayed once the transfer is complete.

Dependencies:

•	bleak (BLE library for Python)


import asyncio
from bleak import BleakClient, BleakScanner

# Define the UUIDs for the BLE service and characteristic
SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"  # Replace with your service UUID
CHARACTERISTIC_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"  # Replace with your characteristic UUID

# Define the BLE device name
DEVICE_NAME = "BLE device name"  # Replace with your BLE device name

commands = {
    '1': "welcome",
    '2': "final",
    '3': "to_pay",
    '4': "success",
    '5': "fail",
    '6': "cancel",
    '0': "exit"
}

messages = {
    'welcome': "WelcomeScreen**7418529631@icici",
    'final': "DisplayTotalScreen**2390.32**50**50*2390.32",
    'to_pay': "DisplayQRCodeScreen**upi://pay?pa=63270083167.payswiff@indus&pn=Bonrix&cu=INR&am=10&pn=Bonrix%20Software%20Systems**10**7418529631@icici",
    'success': "DisplaySuccessQRCodeScreen**1234567890**ORD10594565**29-03-2023",
    'fail': "DisplayFailQRCodeScreen**1234567890**ORD10594565**29-03-2023",
    'cancel': "DisplayCancelQRCodeScreen**1234567890**ORD10594565**29-03-2023"
}

async def find_device_by_name(name):
    devices = await BleakScanner.discover()
    for device in devices:
        if device.name == name:
            return device
    return None

async def send_command(client, command):
    await client.write_gatt_char(CHARACTERISTIC_UUID, command.encode())

async def main():
    print("Press '1' for Welcome Message.")
    print("Press '2' for Final Invoice Message.")
    print("Press '3' for To Pay QR.")
    print("Press '4' for Payment Success Message.")
    print("Press '5' for Payment Fail Message.")
    print("Press '6' for Payment Cancel Message.")
    print("Press '0' to Exit.")

    # Find the BLE device by name
    device = await find_device_by_name(DEVICE_NAME)
    if device is None:
        print(f"Device with name '{DEVICE_NAME}' not found.")
        return

    # Get the device address
    address = device.address
    print(f"Found device '{DEVICE_NAME}' with address: {address}")

    async with BleakClient(address) as client:
        while True:
            # Get user input
            choice = input("Enter command number (1-6): ")

            # Validate user input
            if choice in commands:
                # Get the command key based on user choice
                command_key = commands[choice]

                if command_key == 'exit':
                    break
                else:
                    # Get the command message based on the command key
                    command = messages[command_key]
                    await send_command(client, command)
                    print(f"Sent: {command}")
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

# Run the main function
asyncio.run(main())

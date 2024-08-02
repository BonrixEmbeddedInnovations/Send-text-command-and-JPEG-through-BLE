import asyncio
from bleak import BleakClient, BleakScanner

# Define the BLE device name and characteristic UUIDs
device_name = "BLE device name"  # Replace with your BLE device name
write_characteristic_uuid = "87654321-4321-4321-4321-cba987654321" # Replace with your write characteristic UUID
notify_characteristic_uuid = "98765432-1234-1234-1234-123456789abc" # Replace with your notify characteristic UUID

# Path to the image file
image_path = r"path\\to\\your\\image.jpeg" #replace with your JPEG image path

# Event to signal that the "OK" notification has been received
ok_received_event = asyncio.Event()

def notification_handler(sender, data):
    message = data.decode()
    print(f"Notification received: {message}")
    if message == "OK":
        ok_received_event.set()

async def find_device_by_name(name):
    devices = await BleakScanner.discover()
    for device in devices:
        if device.name == name:
            return device
    return None

async def send_image_data():
    try:
        # Find the BLE device by name
        device = await find_device_by_name(device_name)
        if device is None:
            print(f"Device with name '{device_name}' not found.")
            return

        # Get the device address
        address = device.address
        print(f"Found device '{device_name}' with address: {address}")

        client = BleakClient(address)
        await client.connect()

        # Set a reasonable chunk size
        chunk_size = 512

        print(f"Connected to BLE device. Using chunk size: {chunk_size} bytes.")

        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            file_size = len(image_data)

            # Send the startsendingfile command
            command = f"startsendingfile success.jpg {file_size}\n"
            print("Sent command to start sending file.")
            await client.start_notify(notify_characteristic_uuid, notification_handler)
            await client.write_gatt_char(write_characteristic_uuid, command.encode())
            
            # # Wait for the "OK" notification
            # print("Waiting for 'OK' notification...")
            # await ok_received_event.wait()

            # Send image data in chunks
            for i in range(0, file_size, chunk_size):
                chunk = image_data[i:i+chunk_size]
                await client.write_gatt_char(write_characteristic_uuid, chunk)
                print(f"Sent chunk: {i // chunk_size + 1}")

                await asyncio.sleep(0.01)  # Short delay to prevent overflow

        await client.disconnect()
        print("Disconnected from BLE device.")

    except Exception as e:
        print(f"An error occurred: {e}")

asyncio.run(send_image_data())

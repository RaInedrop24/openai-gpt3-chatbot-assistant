
import pyaudio

# Create a PyAudio object
p = pyaudio.PyAudio()

# Get a list of input devices
input_devices = p.get_device_info_by_host_api_device_index(1, 1)
print("Input devices:")
print(input_devices)
print("Index: " + str(input_devices['index']))
print("Name: " + input_devices['name'])

p.terminate()

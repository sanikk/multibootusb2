from udev.udev import get_all_block_devices
from fs_utils.runners import gather_device_info, gather_block_info

# from usb_utils.usb_utils import find_mass_storage

devs = get_all_block_devices()
for addr, fs_type in devs:
    print(f"{addr} {fs_type}")
g = gather_device_info(devs)
print(f"{g=}")
print("*" * 12)
b = gather_block_info(devs)
print(f"{b=}")
# m = find_mass_storage()
# print(f"{m=}")

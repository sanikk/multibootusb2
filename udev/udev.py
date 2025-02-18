import pyudev


def get_all_block_devices():
    context = pyudev.Context()
    usb_devices = [
        (device.device_node, device.get("ID_FS_TYPE"))
        for device in context.list_devices(subsystem="block", DEVTYPE="disk")
        if device.get("ID_BUS") == "usb"
    ]
    return usb_devices


# monitor example. monitor for inserted devices.
# https://pyudev.readthedocs.io/en/latest/guide.html

if __name__ == "__main__":
    print(get_all_block_devices())

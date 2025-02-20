import usb.core
import usb.util


def check_interfaces(device):
    for config in device:
        for interface in config:
            if interface.bInterfaceClass == 0x08:
                return True
    return False


def find_mass_storage():
    all_devices = usb.core.find(find_all=True, bDeviceClass=0)
    # all_devices = usb.core.find(find_all=True)
    if all_devices:
        mass_storage_devices = [dev for dev in all_devices if check_interfaces(dev)]
        if mass_storage_devices:
            return mass_storage_devices
    raise Exception("No USB mass storage devices found")


if __name__ == "__main__":
    devs = find_mass_storage()
    for dev in devs:
        print(dev)

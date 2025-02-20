import sys
import parted
import json


def get_device_info(device_path):
    device = parted.getDevice(device_path)
    disk = parted.newDisk(device)

    info = {
        "device": device_path,
        "capacity": f"{device.getSize() / (1024 * 1024):.2f} MB",
        "free_space": [(g.start, g.length) for g in disk.getFreeSpaceRegions()],
        "partitions": [
            {
                "number": p.number,
                "size": f"{p.getSize():.2f} MB",
                "start": p.geometry.start,
                "length": p.geometry.length,
            }
            for p in disk.partitions
        ],
    }
    return info


if __name__ == "__main__":
    devices = sys.argv[1:]
    device_infos = [get_device_info(dev) for dev in devices]
    print(json.dumps(device_infos, indent=4))

from tables.partition_types import translate_partition_type
import subprocess
import sys
import json

vpython = ""
try:
    vpython = subprocess.run(
        ["which", "python3"], capture_output=True, text=True
    ).stdout.strip()
except Exception as e:
    print("Something went wrong trying to find a python3 with which.")
    print(e)
if not vpython:
    print("No local python3 found. Exiting with extreme prejudice.")
    sys.exit(1)


def run_subprocess_with_sudo(command, arguments: list, error_type, error_message: str):
    try:
        return subprocess.run(
            ["sudo", vpython, command, *arguments],
            capture_output=True,
            text=True,
        )
    except error_type:
        print(error_message)
        return None


def gather_device_info(devs):
    print("We need sudo to collect device info with PyParted.")
    print("This is a read-only op.")
    ret = run_subprocess_with_sudo(
        "fs_utils/gather_device_info.py",
        devs,
        ModuleNotFoundError,
        "Module PyParted not found. We should probably be running in a virtual environment with pyparted installed.",
    )
    if ret and ret.returncode == 0:
        device_infos = json.loads(ret.stdout)
        return device_infos
    else:
        if not ret:
            print("Error: no return value from gathering device info")
        else:
            print("Error:", ret.stderr)
        return None


def gather_block_info(devs):
    ret = subprocess.run(
        [
            "lsblk",
            "-J",
            "-o",
            "NAME,PHY-SeC,LOG-Sec,SIZE,label,model,vendor,fstype,PARTTYPE",
            *devs,
        ],
        capture_output=True,
        text=True,
    )
    if ret and ret.returncode == 0:
        block_infos = json.loads(ret.stdout)
        for dev in block_infos["blockdevices"]:
            if "parttype" in dev and dev["parttype"]:
                dev["partname"] = translate_partition_type(dev["parttype"])
            if "children" in dev and dev["children"]:
                for child in dev["children"]:
                    if "parttype" in child and child["parttype"]:
                        child["partname"] = translate_partition_type(child["parttype"])
        return block_infos
    if not ret:
        print("Error: no return value from gathering block info")
    else:
        print("Error:", ret.stderr)
    return None

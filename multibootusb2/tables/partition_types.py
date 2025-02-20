def translate_partition_type(code):
    PARTITION_TYPES = {
        "0x00": "Empty",
        "0x01": "FAT12",
        "0x04": "FAT16 <32M",
        "0x05": "Extended",
        "0x06": "FAT16",
        "0x07": "NTFS",
        "0x0b": "FAT32",
        "0x0c": "FAT32 LBA",
        "0x0e": "FAT16 LBA",
        "0x0f": "Extended LBA",
        "0x82": "Linux swap",
        "0x83": "Linux",
        "0x8e": "Linux LVM",
        "0xef": "EFI System",
        "0xfd": "Linux RAID",
    }
    return PARTITION_TYPES.get(code, "Unknown Partition Type")

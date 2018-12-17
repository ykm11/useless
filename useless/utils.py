import struct
import binascii


def le_4_num2bytes(x):
    return struct.pack("<I", x)

def le_4_bytes2num(data):
    return struct.unpack("<I", data)[0]

def be_4_num2bytes(x):
    return struct.pack(">I", x)

def be_4_bytes2num(data):
    return struct.unpack(">I", data)[0]

def le_8_num2bytes(x):
    return struct.pack("<Q", x)

def le_8_bytes2num(data):
    return struct.unpack("<Q", data)[0]

def be_8_num2bytes(x):
    return struct.pack(">Q", x)

def be_8_bytes2num(data):
    return struct.unpack(">Q", data)[0]


def le_num2bytes(x):
    hex_x = hex(x)[2:]
    if len(hex_x) % 2 != 0:
        hex_x = '0' + hex_x
    return binascii.unhexlify(hex_x)[::-1]

def le_bytes2num(data):
    return int(binascii.hexlify(data[::-1]), 16)

def num2bytes(x):
    hex_x = hex(x)[2:]
    if len(hex_x) % 2 != 0:
        hex_x = '0' + hex_x
    return binascii.unhexlify(hex_x)

def bytes2num(data):
    return int(binascii.hexlify(data), 16)



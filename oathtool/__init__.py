import base64
import hashlib
import string
import struct
import sys
import time

trans_5C = bytes(x ^ 0x5C for x in range(256))
trans_36 = bytes(x ^ 0x36 for x in range(256))

# https://tools.ietf.org/html/rfc3548.html#page-6
b32_lookup = {letter: ord(letter) - ord('A') for letter in string.ascii_uppercase}

b32_lookup.update((str(number), number + 24) for number in range(2, 8))


def hmac(key, msg):
    # https://www.ietf.org/rfc/rfc2104.txt - sha1, 64 block
    outer = hashlib.sha1()
    inner = hashlib.sha1()
    if len(key) > 64:
        key = hashlib.sha1(key).digest()
    key = key + b'\x00' * (64 - len(key))
    outer.update(key.translate(trans_5C))
    inner.update(key.translate(trans_36))
    inner.update(msg)
    outer.update(inner.digest())
    return outer.digest()


def pad(input, size=8):
    """
    >>> pad('foo')
    'foo====='
    >>> pad('MZXW6YTBOJUWU23MNU')
    'MZXW6YTBOJUWU23MNU======'
    """
    quanta, remainder = divmod(len(input), size)
    padding = '=' * ((size - remainder) % size)
    return input + padding


def clean(input):
    return input.replace(' ', '')


def generate_otp(key, hotp_value=None):
    """
    >>> generate_otp('MZXW6YTBOJUWU23MNU', 52276810)
    '487656'
    >>> generate_otp('MZXW6YTBOJUWU23MNU'*10, 52276810)
    '295635'
    """
    # convert HOTP to bytes
    # https://tools.ietf.org/rfc/rfc6238.txt
    # http://opensource.apple.com//source/python/python-3/python/Modules/structmodule.c
    hotp_value = struct.pack('>q', hotp_value or int(time.time() / 30))
    # convert base32 key to bytes
    key = base64.b32decode(pad(clean(key)), casefold=True)
    # generate HMAC-SHA1 from HOTP based on key
    HMAC = hmac(key, hotp_value)
    # compute hash truncation
    cut = HMAC[-1] & 0x0F
    # encode into smaller number of digits
    return '%06d' % (
        (struct.unpack('>L', HMAC[cut : cut + 4])[0] & 0x7FFFFFFF) % 1000000
    )


def _one(items):
    (item,) = items
    return item


def get_key_arg():
    return _one(sys.argv[1:])


def get_key_stdin():
    return not sys.stdin.isatty() and sys.stdin.read().strip()


def main():
    try:
        key = get_key_stdin() or get_key_arg()
    except ValueError:
        print('provide secret key as only arg or via stdin')
        sys.exit(1)
    print(generate_otp(key))

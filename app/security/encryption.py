import base64
import codecs

from urllib.parse import quote, unquote

def encode_base64(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def decode_base64(text):
    return base64.b64decode(text.encode('utf-8')).decode('utf-8')

def encode_base32(text):
    return base64.b32encode(text.encode('utf-8')).decode('utf-8')

def decode_base32(text):
    return base64.b32decode(text.encode('utf-8')).decode('utf-8')

def encode_hex(text):
    return text.encode('utf-8').hex()

def decode_hex(text):
    return bytes.fromhex(text).decode('utf-8')

def encode_url(text):
    return quote(text.encode('utf-8'))

def decode_url(text):
    return unquote(text)

import hashlib

def create_key(host):
    h = hashlib.new('sha256')
    h.update()

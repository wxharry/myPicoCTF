# a simple script to decode
# you need to separate strings base on 16 mannully by adding space

def decode(base, secret):
    return ''.join([chr(int(x, base])) for x in secret.split(' ')])



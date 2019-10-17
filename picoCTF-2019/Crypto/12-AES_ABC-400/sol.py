#!/usr/bin/env python

from Crypto.Cipher import AES
# from key import KEY
import os
import math

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))


def to_bytes(n):
    s = hex(n)
    s_n = s[2:]
    if 'L' in s_n:
        s_n = s_n.replace('L', '')
    if len(s_n) % 2 != 0:
        s_n = '0' + s_n
    decoded = s_n.decode('hex')

    pad = (len(decoded) % BLOCK_SIZE)
    if pad != 0: 
        decoded = "\0" * (BLOCK_SIZE - pad) + decoded
    return decoded


def remove_line(s):
    # returns the header line, and the rest of the file
    return s[:s.index('\n') + 1], s[s.index('\n')+1:]


def parse_header_ppm(f):
    data = f.read()

    header = ""

    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i

    return header, data
        

def pad(pt):
    padding = BLOCK_SIZE - len(pt) % BLOCK_SIZE
    return pt + (chr(padding) * padding)


def aes_abc_encrypt(pt):
    cipher = AES.new(KEY, AES.MODE_ECB)
    ct = cipher.encrypt(pad(pt))

    blocks = [ct[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(ct) / BLOCK_SIZE)]
    iv = os.urandom(16)
    blocks.insert(0, iv)
    
    for i in range(len(blocks) - 1):
        prev_blk = int(blocks[i].encode('hex'), 16)
        curr_blk = int(blocks[i+1].encode('hex'), 16)

        n_curr_blk = (prev_blk + curr_blk) % UMAX
        blocks[i+1] = to_bytes(n_curr_blk)

    ct_abc = "".join(blocks)
 
    return iv, ct_abc, ct

def from_bytes(b):
    decoded = b.replace("\0", "")
    s_n = decoded.encode('hex')
    n = int(s_n, 16)

    return n

def aes_abc_decrypt(c_img):
    blocks = [c_img[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(c_img) / BLOCK_SIZE)]

    for i in range(len(blocks) - 2, -1, -1):
        n_curr_blk = from_bytes(blocks[i+1])
        n_prev_blk = from_bytes(blocks[i])

        curr_blk = (n_curr_blk - n_prev_blk) % UMAX

        blocks[i+1] = to_bytes(curr_blk)

    ct = ''.join(blocks[1:])
    
    print len(blocks)
    print len(set(blocks))

    return ct
    # print blocks

if __name__=="__main__":
    with open('body.enc.ppm', 'rb') as f:
        header, c_img = parse_header_ppm(f)
    
    ct = aes_abc_decrypt(c_img)

    # for d in data:
        # print len(d), type(d), d
    # iv, c_img, ct = aes_abc_encrypt(data)

    with open('flag.ppm', 'wb') as fw:
        fw.write(header)
        fw.write(ct)
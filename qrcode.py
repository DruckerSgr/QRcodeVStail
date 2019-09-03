#! /user/bin/python
# -*- coding: UTF-8-*-
# -*- coding: mbcs -*-
"""
Created on Tue Sep  3 11:20:31 2019

@author: Rico
"""

import qrcode
import os
def getQRcode(strs, name):
    qr = qrcode.QRCode(version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10, border=2,)
    print (strs)
    qr.add_data(strs)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert("RGBA")  # RGBA
    img.save(name)
    return img
def read(name):
    file = open(name)
    code_list = []
    for item in file.readlines():
        line = item.strip('\n')
        code_list.append(line)
    file.close()
    return code_list

if __name__ == '__main__':
    for item in os.listdir('.'):
        if item.endswith('.png'):
            os.remove(item)
    http = read('http.txt')
    mycodes = read('mycodes.txt')
    count = 0
    for i in http:
        for j in mycodes:
            count += 1
            strs = i + j
            name = str(count) + '.png'
            getQRcode(strs, name)

import qrcode
import os
def make(link):
	img = qrcode.make(link)
	name='qrcode.png'
	img.save(name)
	return name
def dele(na):
	os.remove(na)
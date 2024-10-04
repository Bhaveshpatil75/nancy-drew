import instaloader
import os
def download(id):
	a=instaloader.Instaloader()
	try:
		prof=instaloader.Profile.from_username(a.context,id)
		a.download_profile(prof,profile_pic_only=True)
	except:
		return '''Invalid Instagram ID.
		if the ID is valid please contact admin-@bhaveshpatil_75'''
	try:
		os.chdir(id)
		for file in os.listdir():
			if '.jpg' in file:
				return file
	except:
		return '''an unexpected error occured.please try again later or contact-@bhaveshpatil-75'''

def delete():
	try:
		for i in os.listdir():
			os.remove(i)
	except:
		return ''
x=input('Enter ID : ')
download(x)
#delete()
import instaloader
def function(PROFILE):
	a=instaloader.Instaloader()
	USER='nancy_drew_bot'
#	PASSWORD='basilisk'
	# try:
	# 	a.login(USER,PASSWORD)
#	a.load_session_from_file(USER)
	a.interactive_login(USER)
	# except:
	# 	return '''There is a problem with instagram servers.please try again later or contact admin-@bhaveshpatil_75'''
	try:
		profile=instaloader.Profile.from_username(a.context,PROFILE)
		wers=profile.get_followers()
		wing=profile.get_followees()
		followers=[]
		following=[]
		for i in wers:
			followers.append(i)
		for i in wing:
			following.append(i)
		out=[]
		if followers==[] and following==[]:
			return '''Private Account.
			Try setting your account as public or just follow https://instagram.com/nancy_drew_bot?igshid=ZDdkNTZiNTM= and send the command again.
			
			Note: You can set your account back to private or you can unfollow above account after your work is done
			
			contact @bhaveshpatil_75 to report an error.'''
		for i in following:
			if i not in followers:
				out.append(i.username)
		return out
	except:
		return '''Invalid Instagram ID.
		if the ID is valid please contact admin-@bhaveshpatil_75'''
print(function('bhaveshpatil_75'))
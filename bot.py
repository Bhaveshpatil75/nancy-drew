import telebot
from insta1234 import function
from profilepic import download,delete
from lovebot import love
from qrcodemaker import make,dele
import private

bot=telebot.TeleBot(private.token)

@bot.message_handler(['start'])
def start(message):
	hlw='''Hello there, I am Nancy Drew a bot coded by Bhavesh Patil.
	To see how to use me type /help'''
	bot.send_message(message.chat.id,hlw)
	
@bot.message_handler(['help'])
def help(message):
	hlp='''Currently I can perform 4 operations.
	Use following commands to access them--
	
	1. /pro_pic <Insta ID>
	   at the place of <Insta ID> enter any Instagram ID(also private) to get its profile picture.
	ex- /pro_pic bhaveshpatil_75
	
	2. /unfollowers <Insta ID>
	    at the place of <Insta ID> enter your Instagram ID to find those accounts which you're following but they aren't following you back.
	ex- /unfollowers bhaveshpatil_75
	
	3. /lovers <your name>,<lovers name>
	    shows love percentage...
	    Note : dont forget the comma.
	 ex- /lovers vision,wanda
	    
	4. /qrcode <link>
	    creates qrcode....
	 ex- /qrcode www.google.com
	  
	contact @bhaveshpatil_75 to report an issue.'''
	bot.send_message(message.chat.id,hlp)
@bot.message_handler(regexp='^/qrcode')
def qr(message):
	link=message.text[7:].strip()
	a='Fine be patient it can take few seconds.....'
	bot.send_message(message.chat.id,a)
	fu=make(link)
	bot.send_photo(message.chat.id,open(fu,'rb'))
	dele(fu)
	
@bot.message_handler(regexp='^/unfollowers')
def bitch(message):
	pa='Fine,Be patient it can take few minutes.....'
	bot.send_message(message.chat.id,pa)
	txt=message.text[12:].strip()
	final=function(txt)
	try:
		final.isalnum()
		bot.reply_to(message,final)
	except:
		total='Total no of accounts = '+str(len(final))
		bot.reply_to(message,total)
		for i in final:
			bot.send_message(message.chat.id,i)

@bot.message_handler(regexp='^/pro_pic')
def xyz(message):
	pa='Fine,Be patient it can take few seconds.....'
	bot.send_message(message.chat.id,pa)
	id=message.text[8:].strip()
	fun=download(id)
	if '.jpg' in fun:
		bot.send_photo(message.chat.id,open(fun,'rb'))
		delete()
	else:
		bot.send_message(message.chat.id,fun)
		
@bot.message_handler(regexp='^/lovers')
def lov(message):
	m=message.text[7:].strip()
	c=m.split(',')
	per=love(c[0],c[1])
	bot.reply_to(message,per)
	
@bot.message_handler(func=lambda message:True)
def inv(message):
	inval='''Invalid Input.
	type /help to know valid commands'''
	bot.send_message(message.chat.id,inval)
	
bot.polling()
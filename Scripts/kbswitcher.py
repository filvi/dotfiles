import os


# python da 256 come valore di return se non presente
if (os.system('setxkbmap -query | grep layout | grep it')):
	os.system('setxkbmap -layout it')
	os.system("notify-send 'switching to IT'")


# python da 256 come valore di return se non presente
elif (os.system('setxkbmap -query | grep layout | grep us')):
	os.system('setxkbmap -layout us')
	os.system("notify-send 'switching to US'")


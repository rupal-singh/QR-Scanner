from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB', (1100,1000), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)
import random
import os
import datetime
import qrcode


d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t ID CARD Generator\t\t\t  %I:%M:%S %p")
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print (reg_format_date)
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
 
# starting position of the message
name1= "All Fields are Mandatory"
print(name1.upper()) 
name2= "Avoid any kind of Spelling Mistakes"
print(name2.upper())
name3= "Write Everything in uppercase letters"
print(name3.upper())

(x, y) = (50, 50)
message = input('\nEnter Your Company Name: ')
company=message
color = 'rgb(0, 0, 0)' #black colour
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((x, y), message.upper(), fill=color, font=font)


# adding an unique id number. You can manually take it from user
(x, y) = (600, 80)
idno=random.randint(10000000,90000000)
message = str('ID '+str(idno))
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message.upper(), fill=color, font=font)




(x, y) = (50, 250)
message = input('Enter Your Full Name: ')
name= message
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), message.upper(), fill=color, font=font)



(x, y) = (50, 350)
message = input('Enter Your Gender: ')
gender=message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message.upper(), fill=color, font=font)


(x, y) = (250, 350)
message = input('Enter Your Age: ')
age=message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message.upper(), fill=color, font=font)



(x, y) = (50, 450)
message = input('Enter Your Date Of Birth: ')
dob=message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message.upper(), fill=color, font=font)



(x, y) = (50, 550)
message = input('Enter Your Blood Group: ')
bg=message
color = 'rgb(255, 0, 0)' # red color 
draw.text((x, y), message.upper(), fill=color, font=font)



(x, y) = (50, 650)
message = input('Enter Your Mobile Number: ')
temp=message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message.upper(), fill=color, font=font)




(x, y) = (50, 750)
message = input('Enter Your Address: ')
add=message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message.upper(), fill=color, font=font)




# save the edited image
 
image.save(str(name)+'.png')



img = qrcode.make(str(company)+str(idno)+"\n"+str(name)+"\n"+str(gender)+"\n"+str(age)+"\n"+str(dob)+"\n"+str(bg)+"\n"+str(temp)+"\n"+str(add))   # this info. is added in QR code, also add other things
img.save(str(idno)+'.bmp')


til = Image.open(name+'.png')
im = Image.open(str(idno)+'.bmp') #25x25
til.paste(im,(600,350))
til.save(name+'.png')

print(('\n\n\nYour ID Card Successfully created in a PNG file '+name+'.png'))
exit()
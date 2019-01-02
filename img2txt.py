from PIL import Image
import sys
#int values for ascii characters
a = [33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255]

def convert(imageName):
	try:
		#open image and convert to black and white
		im = Image.open(imageName).convert('LA')
		#create new txt file to write to
		f = open(imageName.split('.')[0] + ".txt","w+")
		#hold the height and width of the image
		width, height = im.size
		#loop though each pixel in image
		for x in range(height):
			for y in range(width):
				#get the bightness value for pixel
				r,b = im.getpixel((x,y))
				#check if pixel is black to avoid devide by 0
				if(r != 0):
					#check that the devision of brightness is less than length of 'a'
					if(int(255/int(r) < len(a))):
						#convert int value to hex and then decode to char and write to text file
						f.write(hex(a[int(255/int(r))])[2:].decode('hex'))
					else:
						#convert int value to hex and then decode to char and write to text file
						f.write(hex(a[len(a)-1])[2:].decode('hex'))
				else:
					#convert int value to hex and then decode to char and write to text file
					f.write(hex(a[len(a) - 1])[2:].decode('hex'))
			#write new line
			f.write('\n')
		#save and close text file
		f.close()
	except IOError:
		print imageName + " does not exsist"

if __name__ == '__main__':
	try:
		convert(sys.argv[1])
	except IndexError:
		print "no file name given"

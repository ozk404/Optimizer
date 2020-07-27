import os #For Windows OS Tools
import os.path as pt 
import click #For command line options
import tinify #TinyPNG module
import requests #For donwload the image
from random import randint #To assing random name to temp images

"""
---[
Author: Oscar Morales
Version: 1.0 - 2020
]----

-- This software uses the API of TinyPNG https://tinypng.com --
-- This software is used under the Apache 2.0 license - https://www.apache.org/licenses/LICENSE-2.0 --

"""

textini = """
   ____          _    _             _                 
  / __ \        | |  (_)           (_)                
 | |  | | _ __  | |_  _  _ __ ___   _  ____ ___  _ __ 
 | |  | || '_ \ | __|| || '_ ` _ \ | ||_  // _ \| '__|
 | |__| || |_) || |_ | || | | | | || | / /|  __/| |   
  \____/ | .__/  \__||_||_| |_| |_||_|/___|\___||_|   v1.0
         | |                                          
         |_|                                          
"""

tinify.key = "HERE-HERE-HERE"		# API KEY DEVELOPER TINYPNG

def HeaderPro(): ### Header Style, you can delete this
	os.system('cls')
	print ("\n*********************************************************************")
	print (textini)
	print ("*********************************************************************\n")

def PathCompress(path, width): ## This function compress a directory
	if not pt.isdir(path):
		print ("Please enter a valid folder")
		return
	else: 
		try:
			fromFilePath = path 			
			toFilePath = pt.dirname(pt.abspath(__file__)) +"/Tiny" 	#Create a new folder on the current script directory
			print ("Current Directory:: " +  fromFilePath)
			print ("Compress Directory: " + toFilePath)

			for root, dirs, files in os.walk(fromFilePath):
				print ("File list: ", files)
				print ("Total files: ",len(files))
				for name in files:
					fileName, fileSuffix = pt.splitext(name)
					if fileSuffix.lower() == '.png' or fileSuffix.lower()  == '.jpg' or fileSuffi.lower()  == '.jpeg': 
						toFullPath = toFilePath + root[len(fromFilePath):]
						toFullName = toFullPath + '/' + name
						if pt.isdir(toFullPath):
							pass
						else:
							os.mkdir(toFullPath)
						ImagenCompress(root + '/' + name, toFullName, width)
				break
		except:
			print("Something wrong, please try again")	# If something goes wrong						

def FileCompress(inputFile, width): ## This function compress only a selected image
	if not pt.isfile(inputFile):
		print ("Invalid image!")
		return
	try:	
		print ("Archivo: ", inputFile)
		dirname  = pt.dirname(inputFile)
		basename = pt.basename(inputFile)
		fileName, fileSuffix = pt.splitext(basename)
		if fileSuffix.lower()  == '.png' or fileSuffix.lower()  == '.jpg' or fileSuffix.lower()  == '.jpeg':
			ImagenCompress(inputFile, pt.dirname(pt.abspath(__file__))+"/tiny_"+basename, width)
		else:
			print ("The file is not supported")
	except:
		print("Something wrong, please try again")	# If something goes wrong	
		
def URLCompress(imgurl, width):  ## Download and compress a image from URL
	ext = imgurl.split(".")[-1].lower() 
	if ext == 'jpg' or ext == 'png' or ext == 'jpeg' :
		try:
			img_data = requests.get(imgurl).content
			tempname = "itemp"+str(randint(0,1000))+"."+ext
			with open(tempname, 'wb') as handler:
				handler.write(img_data)
			FileCompress(tempname, width)	# Compress from the directory where it was downloaded
			os.remove(tempname) ## Delete downloaded image, delete this line of code if you want to keep the downloaded image
		except:
			print("An error occurred with the selected URL")
	
def ImagenCompress(inputFile, outputFile, img_width): ## This function compress every image
	source = tinify.from_file(inputFile)
	if img_width is not -1:
		resized = source.resize(method = "scale", width  = img_width)
		resized.to_file(outputFile)
	else:
		source.to_file(outputFile)
		print("Image successfully compressed into: "+ outputFile)
		

def MenuP():
		### Menu to run if there is no start command
		print('Please select one of the following options:')
		print("1) Compress only one image")
		print('2) Compress an entire folder')
		print('3) Compress image from URL ')
		print('Any other number will come out of the program')
		print("")
		try:
			op = int(input('Option:  '))  
			if op == 1:
				HeaderPro()
				print('Compress only one image:')
				print("Enter the directory / path of the image:")
				filez = input("Path: ")
				FileCompress(filez,width)	
			elif op == 2:
				HeaderPro()
				print('Compress an entire folder:')
				print("Enter the directory / path you want to compress:")
				filez = input("Path: ")
				PathCompress(filez,width)	
			elif op == 3:
				HeaderPro()
				print('Compress image from URL:')
				print("Enter the URL you want to compress:")
				print("Important: Make sure the url ends in '.jpg', '.png' or '.jpeg'")
				filez = input("Image URL: ")
				URLCompress(filez,-1)
			else:
				return
		except:
			return

######## Console command line
@click.command()
@click.option('-i', "--imagen",  type=str,  default=None,  help="Compress only one image")
@click.option('-d', "--dir",   type=str,  default=None,  help="Compress entire selected directory")
@click.option('-u', "--url", type=str,  default=None,    help="Compress an image from a URL")
@click.option('-w', "--width", type=int,  default=-1,    help="Image width, this value can be default, no matter")

def optimizer(imagen, dir, url, width):
	HeaderPro()
	if imagen is not None:
		FileCompress(imagen, width)			
	elif dir is not None:
		PathCompress(dir, width)			
	elif url is not None:
		URLCompress(url, width)				
	else:
		print(' * * * You did not enter a valid start option, if you need help use --help\n')
		MenuP()

	print ("The program has ended!")

if __name__ == "__main__":
    optimizer()

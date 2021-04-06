#Firstly import liberies
import json
import os
import time
import cv2
import numpy as np
#Start Timer
start=time.time()

#At there I am assuming that the file's location is in Desktop
#If you want you can change the path of input from here
path="C:\\Users\\User\\Desktop"
img_path="C:\\Users\\User\\Desktop"

#Starting of the loop
while True:
    print("Menu for labels' folder")
    print("Current directory is -"+ path+"-")

#Showing a list of folders and etc. to choose one of them
    for index,files in enumerate(os.listdir(path)):
        print( str(index+1) + ". " + files )

    print("\n\n\n")

#Start of a try-except block

    try:

        entry = int(input("Choose a directory: "))

        #Updating the path with the entry that had been gotten from user.
        path = path + "\\" + os.listdir(path)[entry-1]

        #Controlling if the file doesn't exit or not
        if os.path.isfile(path) == True:
            continue

        #If not exits
        else:
            print("------------------------------------------------\n"+
            path+" Directory doesn't exit. Please try again.\n"
                   "------------------------------------------------\n")

        #Updating the interface by the progress

            last_list=path.split("\\")[:-1]

            number=0

            for numbers in path.split("\\")[:-1]:
                number+=1

            new_path=""

            for index in range(0,number):
                new_path=new_path+last_list[index]+"\\"

            for index, files in enumerate(os.listdir(new_path)):
                print(str(index + 1) + ". " + files)

    #It breaks the loop whenever user press a word instead of a number
    except ValueError:
            break

print("Files has been gotten from "+path+"\n")





#Same loop for images' folder
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
while True:
    print("Menu for images' folder")
    print("Current directory is -"+ img_path+"-")

#Showing a list of folders and etc. to choose one of them
    for index,files in enumerate(os.listdir(img_path)):
        print( str(index+1) + ". " + files )

    print("\n\n\n")

#Start of a try-except block

    try:

        entry = int(input("Choose a directory: "))

        #Updating the path with the entry that had been gotten from user.
        img_path = img_path + "\\" + os.listdir(img_path)[entry-1]

        #Controlling if the file doesn't exit or not
        if os.path.isfile(img_path) == True:
            continue

        #If not exits
        else:
            print("------------------------------------------------\n"+
            img_path+" Directory doesn't exit. Please try again.\n"
                   "------------------------------------------------\n")

        #Updating the interface by the progress

            last_list=img_path.split("\\")[:-1]

            number=0

            for numbers in img_path.split("\\")[:-1]:
                number+=1

            new_img_path=""

            for index in range(0,number):
                new_img_path=new_img_path+last_list[index]+"\\"

            for index, files in enumerate(os.listdir(new_img_path)):
                print(str(index + 1) + ". " + files)

    #It breaks the loop whenever user press a word instead of a number
    except ValueError:
            break
print("Images has been gotten from "+img_path+"\n")



#Location for new directory
out_loc_file=""
for each in path.split("\\")[:-1]:
    out_loc_file=out_loc_file+each+"\\"

#Name of the new folder
name_of_the_folder=path.split("\\")[-1]+" YOLO"

#Creating the new folder
if os.getcwd()!=out_loc_file:
    os.chdir(out_loc_file)
os.mkdir(name_of_the_folder)

#Location for exctracting new json files
out_loc=""
for each in path.split("\\")[:-1]:
    out_loc=out_loc+each+"\\"
out_loc=out_loc+name_of_the_folder

print("New folder has been created at "+out_loc+"\n")

vehicle_type=int(input("0:Tank\n1:Helicopter: "))
print("Files are being converted. Please do not turn off the program...")

for files in os.listdir(path):
    line_count = 0
    purified_files = files[:len(files) - 4]
    for images in os.listdir(img_path):
        purified_images=images[:len(images)-4]
        if purified_images==purified_files:

            img=cv2.imread(img_path+"\\"+images)

            height, width, depth=img.shape

            with open(path+"\\"+files) as file:
                for lines in file:

                    lines=lines[:-1]
                    lines.strip(" ")

                    lst = lines.split(" ")

                    x1 = (float(lst[1]))
                    x2 = (float(lst[3]))
                    y1 = (float(lst[2]))
                    y2 = (float(lst[4]))
                    center_x=(x1+x2)/(2*width)
                    centre_y=(y1+y2)/(2*height)

                    boundingBox_width=(x2-x1)/width
                    boundingBox_height=(y2-y1)/height


                    out_file = open(out_loc + "\\" + purified_files + ".txt" ,"a+")
                    out_file.write(str(vehicle_type)+" "+str(center_x)+" "+str(centre_y)+" "+str(boundingBox_width)+" "+str(boundingBox_height)+"\n")




                    out_file.close()


#End of the timer
finish=time.time()
timer=finish-start
minutes=int(round(timer/60))
seconds=timer%60
print("All the files has been converted perfectly.")
print("This converting took {} minutes and {} seconds".format(minutes, seconds))

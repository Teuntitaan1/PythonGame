from Imports import *
PhotosDir = os.listdir("Photos")

Photos = {}

# Takes all the photos out of the Photos directory and puts them in a list
for i in PhotosDir:
    extension = os.path.splitext(i)
    if extension[1] == '.png':
        print("Found " + i + " in directory")
        Photos[i] = pygame.image.load("Photos" + "\\" + i).convert()

print("loaded all photos")


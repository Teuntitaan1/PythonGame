from Imports import *
PhotosDir = os.listdir("Photos")

Photos = {}

# Takes all the photos out of the Photos directory and puts them in a list
for i in PhotosDir:
    print("Found " + i + " in directory")
    Photos[i] = pygame.image.load("Photos" + "\\" + i)

print("loaded all photos")

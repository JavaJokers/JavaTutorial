from util import *
import replit
from time import sleep
from util import *

print(dim + red + "Welcome to..." + reset)
sleep(0.5)
replit.clear()
print(red + "Welcome to..." + reset)
sleep(0.5)
replit.clear()
print(dim + red + "Welcome to..." + reset)
sleep(0.5)
replit.clear()

sleep(2)
slowPrint(flash + green + "An " + blue + "@HENRYMARTIN4 and @elipie " + green +
          "Production" + reset)
sleep(0.5)
replit.clear()
print(flash + green + dim + "An " + blue + "@HENRYMARTIN4 and @elipie " +
      green + "Production" + reset)
sleep(0.5)
replit.clear()
sleep(0.5)

slowPrint(blue + "The official " + red + "Java Jokers" + green +
          " Java Tutorial!" + reset)

print("\n")

slowPrint("Lesson 1 - A basic Java App"+reset)
slowerPrint(
    "Any Java app will begin with a CLASS. A class is an object. When you create a Java file, you must name it. The name of the file will be the class's name.  ")

slowPrint("Sample Code(remember this!):")
print(green)
slowerprintfromfile("snippets/basicclass.java")
print(green)
input("Press enter to continue")
print(reset)
slowerPrint("Next, inside the file, we need to declare a function called \"Main\", with one parameter, for the command line parameters. This is the code that is run when you run your file. So far, our code looks like this(our file name is Main):") 

print(blue)
slowerprintfromfile("snippets/basicclass.java")
print(reset)

slowerPrint("The last two curly brackets (curly brackets are: " + blue + "{" +reset + " or " + blue + "}" + reset +") are defining the end of our function and our class.")
print(green)
input("Press enter to continue  ")
print(reset)

while True:
    inp = input("")

    if inp == "class Main{}":
        print(green+"Correct!"+reset)
        break
    else:
        print(red+"Incorrect. The correct answer was: ")
        print(blue+"class Main{}"+reset)

slowPrint("____________________________________________________")
sleep(0.5)

slowerPrint("Lesson 2 - Printing text to the console")
slowerPrint("To start, follow lesson 1 to create a new class. Then, in the middle, in place of the comment placed earlier, we place a function call for the function \"System.out.println\".\nThen, you can pass in the text that you would like to print. The result code looks like this:\n")
print(green)
input("Are you ready to continue(enter if yes)")
print(reset)
print(blue)
slowerprintfromfile("snippets/helloworld.java")
print(reset)
input("Press enter if you are ready to continue.")

slowerprintfromfile("snippets/vartutorial.txt")

# Henrys if tutorial
slowerprintfromfile("snippets/iftutorial.txt")
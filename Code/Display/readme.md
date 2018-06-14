# Display Operation
The display on the dragonboard is a 20x4 Sunfounder LCD. <br/><br/>
In order to use the board, we first need to level shift the 1.8V i2c on the dragonboard to the 5V of the display.<br/><br/>
To do so we use an off the shelf level shifter. <br/><br/>
After doing so, we can drive the i2c pins using the libmraa and upm libraries. After installing such dependencies, (see list of dependencies in project), the code used to run the display is located in display.cpp and compiled to display.o<br/><br/>
As our previous Stock ticker was coded in python, it would be more ideal to have this code drive the screen in python, however, there was difficulty in getting python to recognize the library files for libmraa. <br/><br/>
As such we simply call display.o from our python code and give it a string to display on the screen. Having implemented this feature, whenever we wish to print to the display we simply import the showDisplay.py class and call its printDisplay(string) to display our message in python.<br/><br/>
There are a few more nuances to the way we implemented the code. Instead of printing individually to each line. Since we have to call the C-code from python we decided to simplify and only pass 1 string, using a mod function to divide it between rows. ScrollText takes in a list of 4 strings (1 per row) and truncates them to 20 characters and prints 1 on each row. <br/><br/>
testTick.py displays an example where we now scroll through a string that is longer than 20 characters (autoscroll was not working in our upm library) and refreshes the display giving a pseudo scroll method.

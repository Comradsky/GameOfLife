# GameOfLife
I've been focusing on C# for the past couple years, this project is to help me get in the Python Groove using both synchronous and asynchronous(concurrent) strategies to print GameOfLife
Note to self:  I will come back to polish this more in the future but for now I'm moving on to bigger projects



# Before Starting:
Packages needed for this project:
	Only need the standard Libraries that come with Python3

This project will not be updated to Use PyGame or another visualization framework(at least not as of now, need to spend time in other proejcts), so to get the best results from printing to the terminal console:

	1.   Make sure you have logging turned off, this program prints out every state of the grid (don't want to spam your logs)
	2.   Try Alacritty terminal for faster printing, (Hint: It's pretty awesome! GameOfLife looks even cooler)

# Instructions:
	1.   Navigate to the projects directory, you should see 'BaseClasses/', 'Logic/', 'Program.py', etc.
	2.   Run Program.py --help and the instructions should be self explanatory
               - Don't forget to zoome out after running to see the big grid
               - Example of what I like to run: 'Program.py 200 3 --sleepTime 0 --verbose'




# FYI, stuff I'm coming back to do after other projects:
	1.   prevent poor input, do error checking and more handling and try catches, validate input etc.
	2.   handle ctrl+c on async, signal handler
	3.   handle --verbose : fix verbose (make it pring out the original seed, make sure it works for async version as well)   




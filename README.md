                                                   # JUNK FILE Organiser #

### Introduction: 
		           Arranging files on your computer is just like arranging anything else. Say you want to organize your clothes. 
                    You might arrange each type of clothes into separate stacks or you could throw everything into one place and 
                    hope you can find the right pair of clothes when you need it and that's how we typically treat our files: 
                    we save files randomly to our Desktop and Documents folders, then waste time searching for files every day.
                    This is very useful for Lazy programmer who keeps bunch of files and folders at one location and sometimes 
                    he is in lot of confusion about which files are present. It is very boring task to manually arrange all the 
                    files into one folder.So This a python programm to organise everything in the single go in a blink of an eye.


### Built using:
                 1. Python language
                 2. The code is built according to the standard pep8/flake8 rules and regulations.
                 3. The code is built in conjunctions with the princliples of OOPs concepts.
                 4. The code is extensible and can be understood easily.


### Prerequisites:
                 - python 3.9 (Install this from the  official website https://www.python.org/)
                 - Basic knowledge of how to use command prompt, how to copy and paste files ..


### Requirements:
             - usage of os module
		 - usage of shutil module
		 - usage of tkinter module
		 - usage of time module
		 - File handling in python
		 - recursion


### How to run:
		 - run the junk_file_organizer.exe : The GUI window will ask you for the path of the directory which you want
    				    		to organise as per the selected method i.e. (extension, size, last modified,
				  		     recently used, etc.

		 - run the command_prompt.py script : It works as a command line parser and will organise the file based on the 
				   		      parsed arguments. The commands are listed below:


### Commands:
   		  1) python command_prompt.py -d "path" -o "extension"

   		  2) python command_prompt.py -d "path" -o "size"

   		  3) python command_prompt.py -d "path" -o "last_modified"

  		  4) python command_prompt.py -d "path" -o "recently_used"



### Approach:
		1. Create different folders based on type of files according to size/modified date/extension 
 		   we are going to segregate into different folders using dictionaries.
		2. Create the map of file types into their respective folders.
		3. Create a function to filter file types into their respective folders.
		4. Use os module of python to recursively list out all the files that are present in the folders 
		   with their relative and absolute path. 
		5. Using Shutil module of python, move all the folders into a newly created folders depending on 
		   keywords and extantion.
		6. After running the above setup in the required destination, the output will be something iike 
 		   as shown in the above image.
 

### Features:
		1. This script can organize the files according to given specific extension in the command line
  		   or in the GUI window.
		2. This script can organize the files of according to the substring of the file name.
		3. The executable file can be given to anyone as a single file package which can be used to do 
 		   all the organise your junk in many ways.



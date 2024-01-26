#Week 6
#now that everything is complete, now i want to see if i can make this into a Tkinter GUI quiz
#copy paste this into python shell to install Tkinter (pip install tk)
#Quick note: if you're wondering how on 111 did I get the actual division "÷" symbol, press "alt+/"(works only on Macontish OSX)

#Week 7
#Still working on Tkinter, learning the scrollbar function, and how to make it proccess an answer
#Double check IDLE version to ensure nothing is wrong with that incase the TKinter version is unsuccessful

#Week 8
#Put the answering tools and questions on seperate windows, now I'm trying to make the command check the answer
#Double check IDLE version to ensure nothing is wrong with that incase the TKinter version is unsuccessful
#Make sure the ASCII art is the correct font - Done it using Pyfiglet

#importations---------
import time
#------------------

#title screen--------------------------------------------------------------------------------------------------------------------------
def title_screen():
    print("""
----------------------------------------------------------------------------------------------------------------------------
Welcome to the Python 3 Quiz! This quiz will test your knowledge within Python 3 and educate you to become a
Python 3 Master. You will begin with a basics quiz and if you get 100%, you can move onto the advanced quiz and if you
get all questions right on that as well, you'll be about ready to use Python 3 in the real world in IT environments.
To give you a background on Python 3, the first version of Python 3 - Python 3.0 (also called "Python 3000" or "Py3K") 
was released on December 3 2008 by Guido van Rossum. It was designed to rectify fundamental design flaws in the 
language, the changes required could not be implemented while retaining full backwards compatibility with the 2.x 
series, which necessitated a new major version number. Please type your answer for multi-choice questions in capitals
and type sentences without capitalizing letters or commas, but still include full stops and type 'True' or 'False' to answer
True/False Questions. DO NOT ADD SPACES IN YOUR ANSWERS BECAUSE THE CODE WILL COUNT YOU AS INCORRECT AND DON'T TYPE
ANYTHING OR PRESS ENTER WHILE YOUR RESULTS ARE BEING DISPLAYED!!
----------------------------------------------------------------------------------------------------------------------------""")
    name = str(input('Please enter your full name: '))
    delayed_printing3("""----------------------------------------------------------------
Welcome to the Python 3 Basics Quiz, """, name + "! Get ready!", 
"""\n-------------------------------------------------------------------------
    ____        __  __                   _____    ____             _          
   / __ \__  __/ /_/ /_  ____  ____     |__  /   / __ )____ ______(_)_________
  / /_/ / / / / __/ __ \/ __ \/ __ \     /_ <   / __  / __ `/ ___/ / ___/ ___/
 / ____/ /_/ / /_/ / / / /_/ / / / /   ___/ /  / /_/ / /_/ (__  ) / /__(__  ) 
/_/    \__, /\__/_/ /_/\____/_/ /_/   /____/  /_____/\__,_/____/_/\___/____/  
      /____/                                                                                                                      
""")
#------------------------------------------------------------------------------------------------------------------------------------

#basics quiz-------------------------------------------------------------------------------------------------------------------
basics_quiz = [
["""
-------------------------------------------------------------------------
What do you need to type in order for Python 3 to print a string literal?
(A) Print('')
(B) print()
(C) print('')
(D) print''
-------------------------------------------------------------------------\n""", "C"
, 
"""\n
--------------------------------------------------------------------------------
B will print nothing, A will give you a syntax Error, D's format is for Python 2
--------------------------------------------------------------------------------
"""
],

["""
-------------------------------------------------------------------------- 
Difference between Ctrl + D / Ctrl + C?
(A) Ctrl + C stops a process but not the prompt, Ctrl + D quits the prompt
(B) Ctrl + C quits the prompt, Ctrl + D stops a process but not the prompt
stops a process but not the prompt
(C) Nothing
--------------------------------------------------------------------------\n""", "A", 
"""\n
------------------------------------------------------------------------
There is a difference and if you answered B, it's the opposite way round
------------------------------------------------------------------------
"""],

["""
---------------------------------------------------------------------------------------------------------------
True/False: The 4 basic data types in Python are 'strings', 'floats', 'integers', and 'Boolean(True/False)'
---------------------------------------------------------------------------------------------------------------\n""", "True", 
"""\n
--------------------------------------
Great try. You'll get it next time! :)
--------------------------------------
"""],

["""
------------------------------------------------------------------------------------------------------------
True/False: If you set this variable: current_time = 12, and then type under it: print(current_Time) it will
print the number 12
------------------------------------------------------------------------------------------------------------\n""", "False", 
"""\n
-------------------------------------------------------------------------------------------------------------------------
It will give you an error saying current_Time is not defined because it's not, but great try. You'll get it next time! :)
-------------------------------------------------------------------------------------------------------------------------
"""],
["""
------------------------------------------------
What does this symbol do? '+'
(A) Literally adds 2 things together
(B) Literally subtracts one thing from the other
(C) Literally multiplys 2 things together
(D) Literally divides one thing from the other
------------------------------------------------
""", "A", 
"""\n
-------------------
Did you fail maths?
-------------------
"""

],

[
"""
------------------------------------------------
What does this symbol do? '/'
(A) Literally adds 2 things together
(B) Literally subtracts one thing from the other
(C) Literally multiplys 2 things together
(D) Literally divides one thing from the other
------------------------------------------------
""", "D", 
"""\n
------------------------------------
'/' replaces the division symbol '÷'
------------------------------------
"""
],

[
"""
------------------------------------------------
What does this symbol do? '*'
(A) Literally adds 2 things together
(B) Literally subtracts one thing from the other
(C) Literally multiplys 2 things together
(D) Literally divides one thing from the other
------------------------------------------------
""", "C", 
"""\n
------------------------------------
'*' replaces the multiply symbol "x"
------------------------------------
"""
],

[
"""
------------------------------------------------
What does this symbol do? '-'
(A) Literally adds 2 things together
(B) Literally subtracts one thing from the other
(C) Literally multiplys 2 things together
(D) Literally divides one thing from the other
------------------------------------------------
""", "B", 
"""\n
-------------------
Did you fail maths?
-------------------
"""
],

[
"""
----------------------------------------------
What does this symbol do? '**'
(A) Literally adds 2 things together
(B) 'To the power of'
(C) Literally multiplys 2 things together
(D) Literally divides one thing from the other
----------------------------------------------
""", "B", 
"""\n
----------------------------------
'x ** y' means x to the power of y
----------------------------------
"""
],

[
"""
----------------------------------------------------------
True/False: There's no difference between lists and tuples
----------------------------------------------------------
""", "False", """\n
-----------------------------------
Lists are mutable but tuples aren't
-----------------------------------
"""
],

[
"""
------------------------------------------------
True/False: Is there another way to write this?:
print("What is your name?")
name = input()
print(name)
------------------------------------------------
""", "True", 
"""\n
---------------------------------
name = input("What is your name?)
print(name)
---------------------------------
"""
],

[
"""
------------------------------------------------------------------------------------------------
What's the difference between "==" and "="?
(A) Nothing
(B) "==" is not a valid syntax in python language
(C) "=" assigns values into a variable while "==" check to see if something is equal to another
(D) "=" check to see if something is equal to another  "==" assigns values into a variable while
------------------------------------------------------------------------------------------------
""", "C", """\n
------------------------------------------------------------------------
"=="" is a valid syntax and if you picked D, it's the opposite way round
------------------------------------------------------------------------
"""
],

[
"""
-----------------------------------------------------------------------------
What will happen when the code below is ran?
lists = ()
tuples = []
lists.insert(0, "Hi")
print(tuples)
---------------------
(A) "tuples" will be printed
(B) An error will occur since tuples are immutable
(C) "Hi" will be added into "lists" as the first index and then printed
(D) "Hi" will be added into "tuples" as the first index due to the list index
-----------------------------------------------------------------------------
""", "B",
"""
--------------------------------------------------------------------------------------------------------------
Did you not notice "lists" waas enclosed with round parentheses meaning the list type has been set as a tuple?
--------------------------------------------------------------------------------------------------------------
"""
],

[
"""
---------------------------------------------------------------------------------------------------------------------------
What is a "for" loop?
(A) A control flow statement that's used to execute statements as long as the conditions are met that's also known as an it
(B) Nothing
(C) A control flow statement that's used to exeute statements even if the statements are not met
---------------------------------------------------------------------------------------------------------------------------
""", "A", """\n
----------------------
It's the opposite of C
----------------------
"""
],

[
"""
------------------------------------------------------------------------------------------------
What is a "while" loop?
(A) Does the same as a for loop
(B) A control flow statement that's used to exeute statements even if the statements are not met
(C) Nothing
------------------------------------------------------------------------------------------------
""", "A", """\n
---------------------------------------------------------------------------------------------------------------------
The only difference a while loop has with a for loop is that a for loop is used on things like tuples and lists while
a while loop doesn't to be directly used on something, it can just be something like while True:
---------------------------------------------------------------------------------------------------------------------
"""
],

[
"""
------------------------------------------------------------------------------
What do you need to name a Python file for the device to recognise it as that?
(A) File.xlsx
(B) File.js
(C) File.pdf
(D) File.py
------------------------------------------------------------------------------
""", "D", 
"""\n
------------------------------------------------------------------------------------------------------------------
File.xlsx is Excel, ".js" is JavaScript, if you're stupid enough to not know, ".pdf" is a Portable Document Format
------------------------------------------------------------------------------------------------------------------
"""
],

[
"""
--------------------------------------------------------------------------------------------
Fill in the blank: You need to type a __ on the very beginning of a line to create a comment
--------------------------------------------------------------------------------------------
""", "#",
"""\n
---------------------------------------------------
Hint: What symbol do you get when you type Shift+3?
---------------------------------------------------
"""
],
[
"""
------------------------------------------------------------------
Fill in the blank: To create a new line in a string, you type ___.
------------------------------------------------------------------
""", "\\n",
"""\n
------------------------------------------------------------------------
Hint: The opposite of frontslash and 15th letter in the English alphabet
------------------------------------------------------------------------
"""
],

[
"""
--------------------------------------------
Fill in the blank: "___" means not equals to
--------------------------------------------
""", "!=",
"""\n
---------------------
!= mean not equals to
---------------------
"""
],

[
"""
-------------------------------------------------------------------------------------------------
What are the 3 arrows ">>>" that apppear in the Python shell? Type the answer using all lowercase
-------------------------------------------------------------------------------------------------
""", "prompt",
"""\n
----------------------
It's called the prompt
----------------------
"""
],

[
"""
--------------------------------------------------------------------------
True/False: Python will check for spelling errors in strings and variables
--------------------------------------------------------------------------
""", "False",
"""\n
-----------------------------------------------------------------------------------------------------------------------------------------
Unlike applications like Word, Excel and Powerpoint, Python couldn't care less unless you make a spelling error on a keyword like "print"
-----------------------------------------------------------------------------------------------------------------------------------------
"""
]
]
#------------------------------------------------------------------------------------------------------------------------------------

#advanced quiz----------------------------------------------------------------------------------------------------------------
advanced_quiz = [
[
"""
-----------------------------------------------------------------------------------------------------------
What is a dictionary?
(A) A collection of key-value pairs, all of them must be unique and not duplicated and are enclosed with {}
(B) A collection of key-value pairs, all of them can be duplicated and are enclosed with {}
(C) A collection of key-value pairs, all of them must be unique and not duplicated and are enclosed with ()
(D) A collection of key-value pairs, all of them can be duplicated and are enclosed with []
-----------------------------------------------------------------------------------------------------------
""", "A",
"""\n
----------------------------------------------------------
They can't be duplicate and [] are lists and () are tuples
----------------------------------------------------------
"""
],
[
"""
----------------------------------------------------------------------------------------------------------------
What is  class?
(A) A code template for creating objects. Objects have member variables and have behaviour associated with them.
(B) A function that can (doesn't have to include a parameter)
(C) Nothing
----------------------------------------------------------------------------------------------------------------
""", "A",
"""\n
------------------------------------------
It is a real Python keyword but it's not B
------------------------------------------
"""
],

[
"""
-------------------------------------------------------------
What does "del()" do?
(A) Not a keyword
(B) Defines a function
(C) Anything typed into the parenthathese will be deleted
(D) Can delete anything but a tuple since they're untouchable
-------------------------------------------------------------
""", "C",
"""\n
-----------------------------------------------------------------------------------------------------------------------------------------
It's a keyword. "def()" defines functions, although tuples can't be changed, "del()" can and will delete anything typed into the brackets
-----------------------------------------------------------------------------------------------------------------------------------------
"""
],

[
"""
-------------------------------------------------------------------------------------------------------
Define "try and except"?
(A) Same as if/else
(B) Nothing
(C) The try block lets you test a block of code for errors. The except block lets you handle the error.
-------------------------------------------------------------------------------------------------------
""", "C", 
"""\n
------------------------------------------------------------------------------------------------------
They both are keywords in Python and they're not the same as if/else despite them doing the same thing
------------------------------------------------------------------------------------------------------
"""
],

[
"""
---------------------------------------------------------------------
True/False: If you type "While False" nothing will occur in the shell
---------------------------------------------------------------------
""", "False",
"""\n
---------------------------------------------------------------------------------------------------------------------------------
Did you not notice the "W" in "while" was capitalized? That will give you a syntax error dummy! But yes, if you set the condition 
as "False", it will not do anything
---------------------------------------------------------------------------------------------------------------------------------
"""
],

[
"""
--------------------------------------------------------------------------------------------------------------------------------
Fill in the blank: You need to type import _______ to get access to math functions like square roots, HCF, LCM and Trigonometric
Functions
--------------------------------------------------------------------------------------------------------------------------------
""", "math",
"""\n
------------------------------------------------------------------------------------------------------------------------------
Here's a hint: what kind of science study does not include the Nobel prize? The reason for is Alfred Bernhard Nobel hated that
------------------------------------------------------------------------------------------------------------------------------
"""
],

[
"""
----------------------------------------------------------------------------------------------------
True/False: If you try to execute a function without the "()" at the end, the function won't execute
----------------------------------------------------------------------------------------------------
""", "True",
"""\n
--------------------------------------------------------------
You must include the "()" in order for the function to execute
--------------------------------------------------------------
"""
],

[
"""
-----------------------------------------------------------------------------------------------
True/False: You must include spaces when using things like maths symbols and commas in the code
-----------------------------------------------------------------------------------------------
""", "False",
"""\n
------------------------------------------------
You don't, but it will make it easier to read :)
------------------------------------------------
"""
],

[
"""
------------------------------------------------------------------------------------------------------------------
True/False: Order of operations is not in Python meaning it will literally do math calculations from left to right
------------------------------------------------------------------------------------------------------------------
""", "False",
"""\n
--------------------------------------------------------------------------------------------------------------------------
All languages that most people know of respect order of operation, except the ones where the order of operations is always 
explicit such as Lisp, Forth or Assembly.
--------------------------------------------------------------------------------------------------------------------------
"""
],

[
"""
------------------------------------------------------------------------------
True/False: 3 examples and big GUIs of Python are Tkinter, wxPython and Pygame
------------------------------------------------------------------------------
""", "True",
"""\n
-----------------------------------------------------------------
Not only are they well known but also all of them are Python GUIs
-----------------------------------------------------------------
"""
],

[
"""
----------------------------------------------------------------------------------------------------------------------------
What will hapen if you type "import file as f"?
(A) Nothing
(B) It will allow you to access whatever is in that file
(C) It enables you to write things like "f.init()" instead of "file.init()" temporarily in the designated file it's typed in
(D) It enables you to write things like "f.init()" instead of "file.init()" everywhere as long as you keep it
----------------------------------------------------------------------------------------------------------------------------
""", "C",
"""\n
-------------------------------------------------------------------------------------------------------------------------
Things like string literals, variables and functions can only be used in the file it's in since it has been defined there
-------------------------------------------------------------------------------------------------------------------------
"""
],

[
"""
---------------------------------------------------------------------------------------------------
Fill in the blank: open("File.txt", "__") will allow you to write something into that specific file
(A) r
(B) w
(C) a
(D) r+
---------------------------------------------------------------------------------------------------
""", "B", 
"""\n
-----------------------------------------------
Hint: the answer is the first letter in "write"
-----------------------------------------------
"""
],

[
"""
------------------------------------------------------------
True/False: If you type int(2/3), it will print the number 0
------------------------------------------------------------
""", "True",
"""\n
--------------------------------------------------------------------------------------------------------------------------
Python will round numbers to the nearest whole number when set into an integer regardless of the tenths place in the float 
--------------------------------------------------------------------------------------------------------------------------
"""
],

[
"""
------------------------------------------------------------------------------
Which of the following statements is true about IDLE?
(A) It can run other languages aside from Python
(B) The shortcut to run a file is f5 on OSX, Windows and Linux
(C) The shortcut to run a file is f5 on only Windows and Linux
(D) You don't need to name you files with ".py" at the end to run them on IDLE
------------------------------------------------------------------------------
""", "B", 
"""\n
---------------------------------------------------------------------------------------------------------------------------------------------------
The f5 shortcut works on all the systems mentioned in the question, it only runs Python and you still need to name your files with ".py" at the end
---------------------------------------------------------------------------------------------------------------------------------------------------
"""
],

[
"""
--------------------------------------------------------------------------------------------
True/False: If an error in a code while it's running a GUI, the GUI applictation won't crash
--------------------------------------------------------------------------------------------
""", "False",
"""\n
------------------------------------------------------------------------------------
Sometimes it will, but you certainly can fix that with the help of try and except :)
------------------------------------------------------------------------------------
"""
],

[
"""
--------------------------------------------------------------------------
True/False: You can write and run python code directly in the shell script
--------------------------------------------------------------------------
""", "True",
"""\n
----------------------------------------
You can but it might be pretty confusing
----------------------------------------
"""
],

[
"""
-------------------------------------------------------------------------------
In the code below, what will be printed once ran?
if 7>6 and not 5<4:
        print(True)
    else:
       print(False)
-------------------------------------------------------------------------------
""", "True",
"""\n
-------------------------------------------------------------------------
Since 7 is bigger than 6 and 4 is not bigger than 5, it will print "True"
-------------------------------------------------------------------------
"""
],

[
"""
----------------------------------------------------------------------------------------------------------------
Fill in the blank: "import _____" allowes you to get access to funcitons related to time like delays in the code
----------------------------------------------------------------------------------------------------------------
""", "time",
"""
--------------------
The answer is "time"
--------------------
"""
],

[
"""
----------------------------------------------------------------------------------------------------------------------------------
Fill in the blank: "import _______" loads the random module, which contains a number of random number generation-related functions
----------------------------------------------------------------------------------------------------------------------------------
""", "random", 
"""
----------------------
The answer is "random"
----------------------
"""
],

[
"""
-------------------------------------------------------------------------------------
True/False: Different Python 3 versions have differences regarding things like syntax
-------------------------------------------------------------------------------------
""", "True",
"""
-------
They do
-------
"""
]
]
#-----------------------------------------------------------------------------------------------------------------------------

# only used to check question count------------------------
print(len(basics_quiz))
print(len(advanced_quiz))
#----------------------------------------------------------

#Fancy way of printing----------------------------------------------------------------
def delayed_printing3(str1, str2, str3):
    for letter in str1:
        print(letter, end = "")
        time.sleep(0.0001)
    for letter in str2:
        print(letter, end = "")
        time.sleep(0.0001)
    for letter in str3:
        print(letter, end = "")
        time.sleep(0.0001)

def delayed_printing(str6):
    for letter in str6:
        print(letter, end = "")
        time.sleep(0.0001)
#----------------------------------------------------------------

#Main code--------------------------------------------------------------------------------------------------------------------
def run_quizzes():
    score = 0
    score2 = 0
    title_screen()
    time.sleep(4)
    for x in basics_quiz:
        answer = input(x[0])
        if answer == x[1]:
            delayed_printing("""\n
   ______                          __  __   _       __     ____   ____                   __
  / ____/___  _____________  _____/ /_/ /  | |     / /__  / / /  / __ \____  ____  ___  / /
 / /   / __ \/ ___/ ___/ _ \/ ___/ __/ /   | | /| / / _ \/ / /  / / / / __ \/ __ \/ _ \/ / 
/ /___/ /_/ / /  / /  /  __/ /__/ /_/_/    | |/ |/ /  __/ / /  / /_/ / /_/ / / / /  __/_/  
\____/\____/_/  /_/   \___/\___/\__(_)     |__/|__/\___/_/_/  /_____/\____/_/ /_/\___(_)   
                                                                                           
""")
            time.sleep(1.5)
            score+=1
        else:
            print(x[2])
            time.sleep(3.5)
    if score == len(basics_quiz):
        yes_or_no = input("""
---------------------------------------------------------------------------------------------------
Congrats! You got 100 percent! Would you like to move onto the advanced quiz? please type Yes or No
---------------------------------------------------------------------------------------------------

""")
        if yes_or_no == "Yes":
            delayed_printing("""
------------------------------------------------------------------------------------------------
Get ready for a real challenge!
    ____        __  __                   _____    ___       __                                __
   / __ \__  __/ /_/ /_  ____  ____     |__  /   /   | ____/ /   ______ _____  ________  ____/ /
  / /_/ / / / / __/ __ \/ __ \/ __ \     /_ <   / /| |/ __  / | / / __ `/ __ \/ ___/ _ \/ __  / 
 / ____/ /_/ / /_/ / / / /_/ / / / /   ___/ /  / ___ / /_/ /| |/ / /_/ / / / / /__/  __/ /_/ /  
/_/    \__, /\__/_/ /_/\____/_/ /_/   /____/  /_/  |_\__,_/ |___/\__,_/_/ /_/\___/\___/\__,_/   
      /____/                                                                                    
------------------------------------------------------------------------------------------------
""")
            time.sleep(4)
            for y in advanced_quiz:
                answer2 = input(y[0])
                if answer2 == (y[1]):
                    delayed_printing("""\n
   ______                          __  __   _       __     ____   ____                   __
  / ____/___  _____________  _____/ /_/ /  | |     / /__  / / /  / __ \____  ____  ___  / /
 / /   / __ \/ ___/ ___/ _ \/ ___/ __/ /   | | /| / / _ \/ / /  / / / / __ \/ __ \/ _ \/ / 
/ /___/ /_/ / /  / /  /  __/ /__/ /_/_/    | |/ |/ /  __/ / /  / /_/ / /_/ / / / /  __/_/  
\____/\____/_/  /_/   \___/\___/\__(_)     |__/|__/\___/_/_/  /_____/\____/_/ /_/\___(_)   
                                                                                           
""")
                    time.sleep(1.5)
                    score2 += 1
                else:
                    print(y[2])
                    time.sleep(3.5)
            if score2 == len(advanced_quiz):
                name = input("""
---------------------------------------------------------------------------------------------------------------------------------------------
Well done!! You got 100%! Congrats, you've done well! now please enter your full name again to confirm it on the certificate: 
---------------------------------------------------------------------------------------------------------------------------------------------\n
""")
                delayed_printing("""
--------------------------------------------------------------------
""" +
name + """
--------------------------------------------------------------------
    ____        __  __                   _____    ____        _    
   / __ \__  __/ /_/ /_  ____  ____     |__  /   / __ \__  __(_)___
  / /_/ / / / / __/ __ \/ __ \/ __ \     /_ <   / / / / / / / /_  /
 / ____/ /_/ / /_/ / / / /_/ / / / /   ___/ /  / /_/ / /_/ / / / /_
/_/    \__, /\__/_/ /_/\____/_/ /_/   /____/   \___\_\__,_/_/ /___/
      /____/                                                       
Basics: 100%
Advanced: 100%
--------------------------------------------------------------------
""")
            else:
                print("""
---------------------------------------------------------------------------------------------------------------------
Aw that's too bad. You didn't get 100%. You got """, score2 / len(advanced_quiz) * 100, "%.", """ 
Oh well, there's always hope. Good luck next time but you've done great by making it to this quiz in the first place!
---------------------------------------------------------------------------------------------------------------------
""")
        else:
            print("""
-----------------------------------------------------------------------
Ok. Well again, thankyou and congrats again on getting 100%, well done!
-----------------------------------------------------------------------           
""")
            time.sleep(2)
    else:
        print("""
----------------------------------------------------------------------------------
Looks like you didn't get 100%. You got """, score / len(basics_quiz) * 100, "%.", """ 
Oh well, there's always hope. Good luck next time!
----------------------------------------------------------------------------------
""")
        time.sleep(2)
run_quizzes()
#-------------------------------------------------------------------------------------------------------------------------------
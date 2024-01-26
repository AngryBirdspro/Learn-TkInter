from tkinter import *
r = Tk()
r.geometry("1200x800")

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
-----------------------------------------------
True/False: Is there another way to write this:
print("What is your name?")
name = input()
print(name)
-----------------------------------------------
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
What's the difference between "==" and "="
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

for x in basics_quiz:
    global questions
    questions = Label(text=x[0], font = "Aptos 20").grid(sticky=W+E, columnspan=7)
    questions

mainloop()
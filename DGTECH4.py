#Week log/pogress------------------------------------------------------------------------------------------------------------
#Week 6
#now that everything is complete, now i want to see if i can make this into a Tkinter GUI quiz
#copy paste this into python shell to install Tkinter (pip install tk)
#Quick note: if you're wondering how I got the actual division "÷" symbol, press "alt+/"(works only on Macontish OSX)

#Week 7
#Still working on Tkinter, learning the scrollbar function, and how to make it proccess an answer
#Double check IDLE version to ensure nothing is wrong with that incase the TKinter version is unsuccessful

#Week 8
#Put the answering tools and questions on seperate windows, now I'm trying to make the command check the answer
#Double check IDLE version to ensure nothing is wrong with that incase the TKinter version is unsuccessful
#Make sure the ASCII art is the correct font - DONE AND SORTED
#Figure out why at the end of the basics quiz if you get all questions riht it doesn't show the username in yes_or-no
#Copy final version from VS Code into IDLE and upload
#-----------------------------------------------------------------------------------------------------------------------------

#Additional Notes--------------------------------------------------------------------------------------------------------------
#pyfiglet install (copy/paste the following into the terminal of operating system) - pip3 install pyfiglet
#Tkinter install in case not included (copy/paste the following into the terminal of operating system) - pip3 install tk
#-----------------------------------------------------------------------------------------------------------------------------

#Importations-----------------
from tkinter import *
import pyfiglet
#---------------------------

#Main---------------------------------------------------------------------------------------------------------------------------------------
r = Tk()
r.title("Python 3 Quiz")
username = Entry(r, font="Aptos 20")
basics_quiz_score = 0
basics_quiz_question_index = 0
advanced_quiz_score = 0
advanced_quiz_question_index = 0
#---------------------------------------------------------------------------------------------------------------------------------------------------

#Quizzes----------------------------------------------------------------------------------------------------------------------------------------------------
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
"""
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
"""
------------------------------------------------------------------------
There is a difference and if you answered B, it's the opposite way round
------------------------------------------------------------------------
"""],

["""
---------------------------------------------------------------------------------------------------------------
True/False: The 4 basic data types in Python are 'strings', 'floats', 'integers', and 'Boolean(True/False)'
---------------------------------------------------------------------------------------------------------------\n""", "True", 
"""
--------------------------------------
Great try. You'll get it next time! :)
--------------------------------------
"""],

["""
------------------------------------------------------------------------------------------------------------
True/False: If you set this variable: current_time = 12, and then type under it: print(current_Time) it will
print the number 12
------------------------------------------------------------------------------------------------------------\n""", "False", 
"""
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
"""
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
"""
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
"""
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
"""
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
"""
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
""", "False", """
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
"""
-------------------------------------
name = input("What is your name?\\n)
print(name)
-------------------------------------
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
""", "C", """
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
""", "A", """
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
""", "A", """
---------------------------------------------------------------------------------------------------------------------
The only difference a while loop has with a for loop is that a for loop is used on things like tuples and lists while
a while loop doesn't to be directly used on something, it can just be something like while True:
---------------------------------------------------------------------------------------------------------------------
"""
],

[
"""
----------------------------------
What file extension is for python?
(A) File.xlsx
(B) File.js
(C) File.pdf
(D) File.py
----------------------------------
""", "D", 
"""
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
"""
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
"""
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
"""
---------------------
!= mean not equals to
---------------------
"""
],

[
"""
--------------------------------------------------------------------------------------------------------------------------------
What are the 3 arrows ">>>" that apppear in the Python shell? Type JUST and ONLY the name into the fill in the blank entry using 
all lowercase, DON'T ADD ANY DEFINITE/INDEFINITE ARTICLES OR ANY ADDITIONAL WORDS/LETTERS BEFORE/AFTER THE WORD
--------------------------------------------------------------------------------------------------------------------------------
""", "prompt",
"""
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
"""
-----------------------------------------------------------------------------------------------------------------------------------------
Unlike applications like Word, Excel and Powerpoint, Python couldn't care less unless you make a spelling error on a keyword like "print"
-----------------------------------------------------------------------------------------------------------------------------------------
"""
]
]
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
What is a class?
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
------------------------------------------------------------------------
True/False: If you type "While False" nothing will occur in the terminal
------------------------------------------------------------------------
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
#----------------------------------------------------------------------------------------------------------------------------------------------------

#Assigned results---------------------------------------------------------------------------------------------------------------
correct_label = Label(r, text=pyfiglet.figlet_format("Correct! Well Done!", font="slant"), font="Courier 14", fg="lime")
incorrect_label = Label(r, text=basics_quiz[basics_quiz_question_index][2], font="Aptos 20", fg="red")
incorrect2_label = Label(r, text=advanced_quiz[advanced_quiz_question_index][2], font="Aptos 20", fg="red")
#----------------------------------------------------------------------------------------------------------------------------------------------------

#Functions-------------------------------------------------------------------------------------------------------------------------------
def give_certificate():
    outro.grid_forget()
    print_certificate.grid_forget()
    Label(r, text=pyfiglet.figlet_format(username.get()+"""
    Python 3 Quiz
    Basics Quiz: 100%
    Advanced Quiz: 100%
    """), font="Courier 14").grid()
    Button(r, text="Quit", font="Aptos 20", command=quit_tk).grid()
def quit_tk():
    quit()
def next_basics_question():
    answering()
    if basics_quiz_question_index >= len(basics_quiz):
        if basics_quiz_score == len(basics_quiz):
            correct_label.grid_forget()
            incorrect_label.grid_forget()
            a.grid_forget()
            b.grid_forget()
            c.grid_forget()
            d.grid_forget()
            true.grid_forget()
            false.grid_forget()
            fill_in_the_blank.grid_forget()
            confirm_answer.grid_forget()
            reset_answer.grid_forget()
            basics_title.grid_forget()
            global yes_or_no
            yes_or_no = Label(r, font="Aptos 20", text="Congrats, "+username.get()+"! You got 100%! Now would you like to move onto the advanced quiz?")
            yes_or_no.grid(columnspan=2)
            yes.grid(column=0, row=0)
            no.grid(column=1, row=0)
        else:
            correct_label.grid_forget()
            incorrect_label.grid_forget()
            a.grid_forget()
            b.grid_forget()
            c.grid_forget()
            d.grid_forget()
            true.grid_forget()
            false.grid_forget()
            fill_in_the_blank.grid_forget()
            confirm_answer.grid_forget()
            reset_answer.grid_forget()
            basics_title.grid_forget()
            Label(r, font="Aptos 20", text="Aw that's too bad, "+username.get()+", you only got " + 
            str(basics_quiz_score/len(basics_quiz)*100) + "%. Oh well, maybe next time.").grid()
            Button(r, text="Quit", font="Aptos 20", command=quit_tk).grid()
    else:
        label_basics_questions()
    correct_label.grid_forget()
    incorrect_label.grid_forget()
    next_basics.grid_forget()
def next_advanced_question():
    answering2()
    if advanced_quiz_question_index >= len(advanced_quiz):
        if advanced_quiz_score == len(advanced_quiz):
            a.grid_forget()
            b.grid_forget()
            c.grid_forget()
            d.grid_forget()
            true.grid_forget()
            false.grid_forget()
            fill_in_the_blank.grid_forget()
            confirm_answer2.grid_forget()
            reset_answer.grid_forget()
            advanced_title.grid_forget()
            global outro
            global print_certificate
            outro = Label(r, text="Congrats, "+username.get()+"! You got 100% on both quizzes! It's time to claim your certificate now!", 
            font="Aptos 20")
            print_certificate = Button(r, text="Claim Certificate", font="Aptos 20", command=give_certificate)
            outro.grid()
            print_certificate.grid()
        else:
            a.grid_forget()
            b.grid_forget()
            c.grid_forget()
            d.grid_forget()
            true.grid_forget()
            false.grid_forget()
            fill_in_the_blank.grid_forget()
            confirm_answer2.grid_forget()
            reset_answer.grid_forget()
            advanced_title.grid_forget()
            Label(r, text="Aw man, "+username.get()+", you only got"+str(advanced_quiz_score/len(advanced_quiz)*100)+"%. "+
            "But again, you did great by making it here, Good luck next time! :)",
            font="Aptos 20").grid()
            Button(r, text="Quit", font="Aptos 20", command=quit_tk).grid()
    else:
        label_advanced_questions()
    correct_label.grid_forget()
    incorrect2_label.grid_forget()
    next_advanced.grid_forget()
def result():
    a.grid_forget()
    b.grid_forget()
    c.grid_forget()
    d.grid_forget()
    true.grid_forget()
    false.grid_forget()
    fill_in_the_blank.grid_forget()
    confirm_answer.grid_forget()
    reset_answer.grid_forget()
    next_basics.grid(column=0, row=0, sticky=NW)
def result2():
    a.grid_forget()
    b.grid_forget()
    c.grid_forget()
    d.grid_forget()
    true.grid_forget()
    false.grid_forget()
    fill_in_the_blank.grid_forget()
    confirm_answer2.grid_forget()
    reset_answer.grid_forget()
    next_advanced.grid(column=0, row=0, sticky=NW)
def label_basics_questions():
    global basics_questions
    basics_questions = Label(r, text=basics_quiz[basics_quiz_question_index][0], font="Aptos 16")
    basics_questions.grid(column=1, row=10, sticky=E)
def label_advanced_questions():
    global advanced_questions
    advanced_questions = Label(r, text=advanced_quiz[advanced_quiz_question_index][0], font="Aptos 16")
    advanced_questions.grid(column=1, row=10, sticky=E)
def start_basics():
    answering()
    r.title("Python 3 Basics Quiz")
    global basics_title
    basics_title = Label(r, text=pyfiglet.figlet_format("Python 3 Basics Quiz", font="slant") 
    + "Welcome to the Python 3 Basics Quiz, " + username.get() + "!", font="Courier 14", fg="lime")
    basics_title.grid(column=1, row=0, columnspan=8, rowspan=8, padx=0, sticky=(N,E,W))
    intro.destroy()
    username.grid_forget()
    confirm_username.destroy()
    label_basics_questions()
def check_answer_for_basics_quiz():
    global basics_quiz_question_index
    incorrect_label.configure(text=basics_quiz[basics_quiz_question_index][2])
    if fill_in_the_blank.get() == basics_quiz[basics_quiz_question_index][1]:
        incorrect_label.grid_forget()
        correct_label.grid(column=1, row=10, sticky=NE)
        global basics_quiz_score
        basics_quiz_score += 1
    else:
        correct_label.grid_forget()
        incorrect_label.grid(column=1, row=10, sticky=NE)
    a.deselect()
    b.deselect()
    c.deselect()
    d.deselect()
    true.deselect()
    false.deselect()
    basics_questions.destroy()
    basics_quiz_question_index = basics_quiz_question_index + 1
    fill_in_the_blank.delete(0, END)
    result()
def check_answer_for_advanced_quiz():
    global advanced_quiz_question_index
    incorrect2_label.configure(text=advanced_quiz[advanced_quiz_question_index][2])
    if fill_in_the_blank.get() == advanced_quiz[advanced_quiz_question_index][1]:
        incorrect2_label.grid_forget()
        correct_label.grid(column=1, row=10, sticky=NE)
        global advanced_quiz_score
        advanced_quiz_score += 1
    else:
        correct_label.grid_forget()
        incorrect2_label.grid(column=1, row=10, sticky=NE)
    a.deselect()
    b.deselect()
    c.deselect()
    d.deselect()
    true.deselect()
    false.deselect()
    advanced_questions.destroy()
    advanced_quiz_question_index = advanced_quiz_question_index + 1
    fill_in_the_blank.delete(0, END)
    result2()
def start_advanced():
    answering2()
    yes_or_no.grid_forget()
    yes.grid_forget()
    no.grid_forget()
    global advanced_title
    advanced_title = Label(r, text=pyfiglet.figlet_format("Python 3 Advanced Quiz!", font="slant")+
    "Get ready for a real challenge, "+username.get()+"!", font="Courier 14", fg="lime")
    advanced_title.grid(column=1, row=0, columnspan=8, rowspan=8, padx=0, sticky=(N,E,W))
    label_advanced_questions()
def fill_in_the_blank_reset():
    fill_in_the_blank.delete(0, END)
    a.deselect()
    b.deselect()
    c.deselect()
    d.deselect()
    true.deselect()
    false.deselect()
def a_selection_reset():
    b.deselect()
    c.deselect()
    d.deselect()
    true.deselect()
    false.deselect()
    fill_in_the_blank.delete(0, END)
    fill_in_the_blank.insert(0, "A")
def b_selection_reset():
    a.deselect()
    c.deselect()
    d.deselect()
    true.deselect()
    false.deselect()
    fill_in_the_blank.delete(0, END)
    fill_in_the_blank.insert(0, "B")
def c_selection_reset():
    a.deselect()
    b.deselect()
    d.deselect()
    true.deselect()
    false.deselect()
    fill_in_the_blank.delete(0, END)
    fill_in_the_blank.insert(0, "C")
def d_selection_reset():
    a.deselect()
    c.deselect()
    b.deselect()
    true.deselect()
    false.deselect()
    fill_in_the_blank.delete(0, END)
    fill_in_the_blank.insert(0, "D")
def true_selection_reset():
    a.deselect()
    c.deselect()
    d.deselect()
    b.deselect()
    false.deselect()
    fill_in_the_blank.delete(0, END)
    fill_in_the_blank.insert(0, "True")
def false_selection_reset():
    a.deselect()
    c.deselect()
    d.deselect()
    true.deselect()
    b.deselect()
    fill_in_the_blank.delete(0, END)
    fill_in_the_blank.insert(0, "False")
#-------------------------------------------------------------------------------------------------------------------------------

#Answering tools-------------------------------------------------------------------------------------------------------------------------------
yes = Button(r, text="YES", font="Aptos 20", borderwidth=5, command=start_advanced)
no = Button(r, text="NO", font="Aptos 20", borderwidth=5, command=quit_tk)
a = Checkbutton(r, text="A", font="Aptos 20", command=a_selection_reset)
b = Checkbutton(r, text="B", font="Aptos 20", command=b_selection_reset)
c = Checkbutton(r, text="C", font="Aptos 20", command=c_selection_reset)
d = Checkbutton(r, text="D", font="Aptos 20", command=d_selection_reset)
true = Checkbutton(r, text="True", font="Aptos 20", command=true_selection_reset)
false = Checkbutton(r, text="False", font="Aptos 20", command=false_selection_reset)
fill_in_the_blank = Entry(r, font="Aptos 20", width=8)
confirm_answer = Button(r, text="Confirm answer", font="Aptos 20", borderwidth=5, command=check_answer_for_basics_quiz)
confirm_answer2 = Button(r, text="Confirm answer", font="Aptos 20", borderwidth=5, command=check_answer_for_advanced_quiz)
reset_answer = Button(r, text="Reset answer", font="Aptos 20", borderwidth=5, command=fill_in_the_blank_reset)
next_basics = Button(r, text="Next", font="Aptos 20", borderwidth=5, command=next_basics_question)
next_advanced = Button(r, text="Next", font="Aptos 20", borderwidth=5, command=next_advanced_question)
intro = Label(r, font="Aptos 14", text=
"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Welcome to the Python 3 Quiz! This quiz will test your knowledge within Python 3 and educate you to become a
Python 3 Master. You will begin with a basics quiz and if you get 100%, you can move onto the advanced quiz and if you
get all questions right on that as well, you'll be about ready to use Python 3 in the real world in IT environments.
to give you a background on Python 3, the first version of Python 3 - Python 3.0 (also called "Python 3000" or "Py3K") 
was released on December 3 2008 by Guido van Rossum. It was designed to rectify fundamental design flaws in the 
language, the changes required could not be implemented while retaining full backwards compatibility with the 2.x 
series, which necessitated a new major version number. Just select the A/B/C/D and True/False buttons in the left 
corner according to if they are True/False or multiple choice and then confirm the answer by pressing
"Confirm answer", simply type your answer into the Entry box to answer fill in the blank quesiton and submit the answer
by pressing "Confirm answer". Remember: DO NOT ADD SPACES IN YOUR ANSWERS FOR THE FILL IN THE BLANK QUESIONS BECAUSE 
YOU WILL BE COUNTED AS INCORRECT.
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Please enter your full name in the box below:
----------------------------------------------
""", anchor=NW)
confirm_username = Button(r, text="Confirm name and start quiz", font="Aptos 20", command=start_basics)
#-------------------------------------------------------------------------------------------------------------------------------

#Quiz running functions-------------------------------------------------------------------------------------------------------------------------------
def title_screen():
    intro.grid()
    username.grid()
    confirm_username.grid()

def answering():
    a.grid(sticky=W, column=0, row=0, columnspan=2)
    b.grid(sticky=W, column=0, row=1)
    c.grid(sticky=W, column=0, row=2)
    d.grid(sticky=W, column=0, row=3)
    true.grid(sticky=W, column=0, row=4)
    false.grid(sticky=W, column=0, row=5)
    fill_in_the_blank.grid(sticky=W, column=0, row=6)
    confirm_answer.grid(sticky=W, column=0, row=7)
    reset_answer.grid(sticky=W, column=0, row=8)
def answering2():
    a.grid(sticky=W, column=0, row=0, columnspan=2)
    b.grid(sticky=W, column=0, row=1)
    c.grid(sticky=W, column=0, row=2)
    d.grid(sticky=W, column=0, row=3)
    true.grid(sticky=W, column=0, row=4)
    false.grid(sticky=W, column=0, row=5)
    fill_in_the_blank.grid(sticky=W, column=0, row=6)
    confirm_answer2.grid(sticky=W, column=0, row=7)
    reset_answer.grid(sticky=W, column=0, row=8)
title_screen()
mainloop()
#-------------------------------------------------------------------------------------------------------------------------------
#funckje
disp = print
nie = False
tak = True
hw = "Hello World!"
ws = "Witaj Świecie"




disp("Welcome to SherPython!")
disp("Szerwigi's very own programming language!")
disp("Instead of print use disp")
disp("Remember: nie means False and tak means True")

#cośtamy
pytanie = input("Wanna start coding? tak/nie: ")

if pytanie == True or pytanie == "tak":
    disp("So lets start!")
else:
    disp("Goodbye fpr now!")
    exit()

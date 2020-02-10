from functools import reduce

def programy():
    running = True

    print("I output the average of a list that you add files to. \nType MENU to access the menu. \n")
    listy = []
    
    while running == True:
        
        def listaverage(givenlist):
            print(sum(listy) / len(listy))

        currentnum = input("Please type a number to add to the list: ")

        
        if currentnum.isdigit():
            listy.append(int(currentnum))
            listaverage(listy)
        else:
            if str(currentnum.lower()) == "menu":
                running = False
            else:
                print("Not a number!")


active = True
while active == True:
    answer = input("Please type either: EXIT or START\n")

    if str(answer.lower()) == "start":
        print("Starting... \n")
        programy()
    if str(answer.lower()) == "exit":
        print("Now exiting...")
        active = False
    else:
        print("Not valid answer...\n")


    

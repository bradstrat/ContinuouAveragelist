from functools import reduce

def programy():
    running = True

    print("I output the average of a list that you add files to.")
    listy = []
    
    while running == True:
        def listaverage(givenlist):
            print(sum(listy) / len(listy))

        currentnum = input("Please type a number to add to the list: ")

        try:
            val = int(currentnum)
        except ValueError:
            if str(currentnum) == "MENU":
                running = False
            else:
                print("Not a number!")
                continue
   
        listy.append(int(currentnum))
        listaverage(listy)

    answer = input("Please type either: EXIT or RESTART")

    if str(answer) == "RESTART":
        running = True
    if answer == "EXIT":
        exit
    
programy()

import time

def timer(start : int , stop : int , repeat : int):
    for i in range(repeat):
        actionS = start
        if actionS >= stop:
            while actionS != stop:
                print(actionS)
                time.sleep(1)
                actionS -=1
            print(actionS)
        elif stop >= actionS:
            while stop != actionS:
                print(actionS)
                time.sleep(1)
                actionS +=1
            print(actionS)
while True:
    try:
        start = int(input("Enter start time : "))
        stop = int(input("Enter stop time : "))
        repeat = int(input("Enter number of times : "))

    except ValueError:
        print("Please enter a number")
    else:
        break

timer(start, stop, repeat)
import time
import os





def convert(t):
    return t * 60


def counttimer(t, label):
    while t:
        min, sec = divmod(t,60)
        print(f"{label}: {min:02d}:{sec:02d}", end="\r")
        time.sleep(1)
        t -= 1 


def pomodoro(work, rest): 
    # setting minutes to seconds 
    w = convert(work)
    r = convert(break_time)
    counttimer(w, "Work")
    os.system("clear||cls")
    counttimer(r, "Break_time") 
    os.system("clear||cls")




work = int(input("Enter work time, in min: ")) 
break_time = int(input("Enter break time, in min: ")) 

pomodoro(work, break_time)


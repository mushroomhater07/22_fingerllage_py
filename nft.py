
import random, os
tab = ["mayor","police","guard","priest","detective","villager","imposter1","imposter2","prisoner"]
playset = set(range(1,10))
random.shuffle(tab)
clearwindows = lambda: os.system("cls")
clearlinux = lambda: os.system("clear")
job = {"grid1" : {"alive": True, "job": tab[0], "message": False, "deadmsg": ""}, 
"grid2" : {"alive": True, "job": tab[1], "message": False, "deadmsg": ""}, 
"grid3" : {"alive": True, "job": tab[2], "message": False, "deadmsg": ""}, 
"grid4" : {"alive": True, "job": tab[3], "message": False, "deadmsg": ""}, 
"grid5" : {"alive": True, "job": tab[4], "message": False, "deadmsg": ""}, 
"grid6" : {"alive": True, "job": tab[5], "message": False, "deadmsg": ""}, 
"grid7" : {"alive": True, "job": tab[6], "message": False, "deadmsg": ""}, 
"grid8" : {"alive": True, "job": tab[7], "message": False, "deadmsg": ""}, 
"grid9" : {"alive": True, "job": tab[8], "message": False, "deadmsg": ""}}
pri = tab.index("prisoner") + 1
imp1 = tab.index("imposter1") + 1
imp2 = tab.index("imposter2") + 1
gud = tab.index("guard") + 1
winimposter = {pri,imp1,imp2}
winvillage = playset - winimposter
vote1 = 0
vote2 = 0
vote3 = 0
dead = []
guardsave = ""
msg_content =""
guardlife = 2
def Mayor():
    print("you are mayor, you can send message but not dead person")
    print(f"enter a number (1-9) you want to reach to.  {killed()} deaded")
    sd_msg = int(input("enter a number: "))     
    global msg_content
    global job
    msg_content = input("the message you want to send: ")
    match sd_msg:
        case 1:
            job["grid1"]["message"] = True
        case 2:
            job["grid2"]["message"] = True
        case 3:
            job["grid3"]["message"] = True
        case 4:
            job["grid4"]["message"] = True
        case 5:
            job["grid5"]["message"] = True
        case 6:
            job["grid6"]["message"] = True
        case 7:
            job["grid7"]["message"] = True
        case 8:
            job["grid8"]["message"] = True
        case 9:
            job["grid9"]["message"] = True
        case unknown_command:
            print("Unknown command!")
    input("Thanks, press ENTER to clear the screen and give it to next person.")
    clearwindows()
def Police():
    print("your job is a policeman! your job is to catch the prisioner into jail")
    global job
    sus = input("enter the number (1-9) you think is suspisious: ")
    if sus == pri:
        print("prisoner founded! he is in jail now!")
        match sus:
            case 1:
                job["grid1"]["alive"] = False
            case 2:
                job["grid2"]["alive"] = False
            case 3:
                job["grid3"]["alive"] = False
            case 4:
                job["grid4"]["alive"] = False
            case 5:
                job["grid5"]["alive"] = False
            case 6:
                job["grid6"]["alive"] = False
            case 7:
                job["grid7"]["alive"] = False
            case 8:
                job["grid8"]["alive"] = False
            case 9:
                job["grid9"]["alive"] = False
    else:
        print("wrong person.")
    input("Thanks, press ENTER to clear the screen and give it to next person.")
    clearwindows()
def Guard():
    global guardsave
    print("you are a guard, you can save 2 ppl life. at the third time you will die")
    print(f"you have {guardlife} life left")
    guardsave = int(input("enter a number(1-9) you would protect: ")) 
    input("Thanks, press ENTER to clear the screen and give it to next person.")
    clearwindows()
def Priest():
    print("you are a priest, you can read a dead person's message")
    if len(killed()) == 0:
        print("nobody dead")
    else:
        print("list that you can access to :"+ str(killed()))
        ppl = int(input("enter the number of the dead person: "))
        grid = "grid" + str(ppl)
        if (job[grid]["alive"] == False) and (job[grid]["deadmsg"] != ""):
            print("message from "+ grid + " : "+job[grid]["deadmsg"])
        elif job[grid]["alive"] == True:
            print("he is alive and he keep it in secret")
        elif job[grid]["deadmsg"] == "":
            print("he did wrote anything")
    input("Thanks, press ENTER to clear the screen and give it to next person.")
    clearwindows()
def Detective():
    print("you are a detective, you can see if the person is good or not")
    ppl = int(input("enter the number you want to check: "))
    grid = "grid" + str(ppl)
    findjob = job[grid]["job"]
    match findjob:
        case "mayor":
            print("good person")
        case"police":
            print("good person")
        case"guard":
            print("good person")
        case"priest":
            print("good person")
        case"detective":
            print("good person")
        case"villager":
            print("good person")
        case "imposter1":
            print("bad person")
        case"imposter2":
            print("bad person")
        case"prisoner":
            print("bad person")
    input("Thanks, press ENTER to clear the screen and give it to next person.")
    clearwindows()
def Villager(): 
    print("you are a villager, your mission is sleeping")
    print("Here is your dream: Number guessing 1-10")
    num = random.randint(1,10)
    again = True
    while again == True:
        trying = int(input("enter a number between 1-10: "))
        if trying == num:
            print("congrats, bingo")
            again = False
        elif trying > num:
            print("too large")
            again = True
        else:
            print("too small")
            again = True
    input("Thanks, press ENTER to clear the screen and give it to next person.")
    clearwindows()
def imposter1():
    print("you are a killer, you had team up with another killer and a prisoner")
    print(f"imposter1: {imp1} ,imposter2: {imp2},prisoner: {pri}, dead: {killed()}")
    global vote1
    vote2 = int(input("vote for the person you want to kill: "))
    input("Thanks, press ENTER to clear the screen and give it to next person.")
    clearwindows()
def imposter2():
    print("you are a killer, you had team up with another killer and a prisoner")
    print(f"imposter1: {imp1} ,imposter2: {imp2},prisoner: {pri}, dead: {killed()}")
    global vote2
    vote2 = int(input("vote for the person you want to kill: "))
    input("Thanks, press ENTER to clear the screen and give it to next person.")
    clearwindows()
def prisoner():
    print("you was a detective and you get into trouble, but you escape from jail")
    print("you team up with 2 killer, decide who you want to kill")
    print(f"imposter1: {imp1} ,imposter2: {imp2},prisoner: {pri}, dead: {killed()}")
    global vote3
    vote3 = int(input("vote for the person you want to kill: "))
    ppl = int(input("enter the number you want to check their job: "))
    grid = "grid" + str(ppl)
    print(job[grid]["job"])
    input("Thanks, press ENTER to clear the screen and give it to next person.")
    clearwindows()
def killed():
    global dead
    dead = []
    for i,x in enumerate(job):
        if job[x]["alive"] == False:
            dead.append(i+1)
    next
    return dead
def voting():
    global guardlife
    votelists = [vote1, vote2, vote3]
    seen = set()
    dupes = []
    for x in votelists:
        if x in seen:
            dupes.append(x)
        else:
            seen.add(x)
    if len(dupes) >=1:
        decided = dupes[0]
    else:
        choices = random.choices(votelists, k=1)
        decided = choices[0]
    ppl = "grid" + str(decided)
    guad = "grid" + str(gud)
    if (guardsave == decided) and (guardlife != 0):
        job[ppl]["alive"] = True
        guardlife -=1
    else:
        job[guad]["alive"] = False
        job[ppl]["alive"] = False
    return job[ppl]["alive"]
again = True
print("9 of you is in the same village, but 3 of them is killer")
print("each player will assign a job and each job has different super power")
while again == True:
    input("press enter to rise dark night")
    clearwindows()
    for x in playset: 
        player = x-1
        grid = "grid" + str(x)
        print(f"you are player {x}")
        getjob = tab[player]
        if job[grid]["alive"] == True:
            job[grid]["deadmsg"] = str(input("Write a message to priest in case you die: "))
            match getjob:
                case "mayor":
                    if job[grid]["message"] == True:
                        print("you receive a message from mayor: " + msg_content)
                    Mayor()
                case"police":
                    if job[grid]["message"] == True:
                        print("you receive a message from mayor: " + msg_content)
                    Police()
                case"guard":
                    if job[grid]["message"] == True:
                        print("you receive a message from mayor: " + msg_content)
                    Guard()
                case"priest":
                    if job[grid]["message"] == True:
                        print("you receive a message from mayor: " + msg_content)
                    Priest()
                case"detective":
                    if job[grid]["message"] == True:
                        print("you receive a message from mayor: " + msg_content)
                    Detective()
                case"villager":
                    if job[grid]["message"] == True:
                        print("you receive a message from mayor: " + msg_content)
                    Villager()
                case "imposter1":
                    imposter1()
                case"imposter2":
                    imposter2()
                case"prisoner":
                    prisoner()
    next
    voting()
    playset = playset -set(killed())
    print("Sunrise, ask everyone wake up and see the result")
    print("dead: " + str(killed()))
    print("list that is alive: " + str(playset))
    check_win = set(killed())
    if (check_win.issuperset(winimposter) == True) or (check_win.issuperset(winvillage) == True):
        again = False
    else:
        again = True
    
        


def distancebtw2pts(taxiPosX, taxiPosY ,posX2, posY2):

    return abs(taxiPosX - posX2) + abs(taxiPosY - posY2)

OKGREEN = '\033[92m'
WARNING = '\033[91m'
RESET = "\033[0m"

with open('/home/darkloner99/code/Hashcode/Hashcode/2018-qualif/out/results.txt') as f:
    file = [line.rstrip(' \n') for line in f]

with open('/home/darkloner99/code/Hashcode/Hashcode/2018-qualif/in/input2.in') as f:
    fileInputData = [line.rstrip('\n') for line in f]

firstLine = fileInputData[0].split(" ")
maxstepts = int(firstLine[7])
bonus = int(firstLine[4])
constantefee = int(firstLine[5])
distancefee = int(firstLine[6])

stepError = False

# Repeat for each song in the text file

scoreTotal = 0
scorefind = int(file[0])
file.pop(0)
for line in file:

    fields = line.split(" ")
    fields.pop(0)
    fields[len(fields)-1] = fields[len(fields)-1].replace('\n','')

    nbRides = fields[0]
    #if(nbRides == len(fields)) :
    taxiPosX = 0
    taxiPosY = 0

    totalTime = 0

    scoreForTaxi = 0

    for i in range(len(fields)) :
        #print("line numer =" + str(int(fields[i+1]) + 1))
        #print(fileInputData)
        #print(fields)
        inputLine = fileInputData[int(fields[i]) + 1]  # ligne de la corespondante a la course
        #print(inputLine)

        inputfields = inputLine.split(" ")

        distanceToArrive = distancebtw2pts(taxiPosX, taxiPosY, int(inputfields[0]),int(inputfields[1])) # distance entre taxi & depart ride
        delayTime = 0
        useDelay = False
        if (int(inputfields[4]) >= (distanceToArrive + totalTime)):
            delayTime = int(inputfields[4]) - distanceToArrive - totalTime
            useDelay = True
            #if(delayTime < 0):
             #   delayTime = 0
            #print(str(delayTime) + "wait")

        distanceToFinishRide = distancebtw2pts(int(inputfields[0]), int(inputfields[1]), int(inputfields[2]),int(inputfields[3]))  # distance finish ride
        taxiPosX = int(inputfields[2])
        taxiPosY = int(inputfields[3])
        totalTime += distanceToArrive + distanceToFinishRide + delayTime
        #print("start :" +str(distanceToArrive) + " finish :"+ str(distanceToFinishRide)+ " wait :"+  str(delayTime))

        scoreForTaxi += constantefee
        if (useDelay == True) and (delayTime >= 0):
            scoreForTaxi += bonus
        scoreForTaxi += (distanceToFinishRide * distancefee)
        #print("scoreForTaxi :" + str(scoreForTaxi) + "..")

    scoreTotal += scoreForTaxi
    #print("scoreTotal :" + str(scoreTotal)  + " scoreForTaxi :" + str(scoreForTaxi))

    if totalTime >= maxstepts :
        print(WARNING +"> NOK To much steps : " + str(totalTime) +RESET)
        stepError = True
    else :
        print(OKGREEN +"> OK steps :" + str(totalTime) +RESET)

if scoreTotal != scorefind:
    print(WARNING +"#### NOK score Incorrect : " + str(scoreTotal) + " difference =" + str(scoreTotal-scorefind) +RESET)
else:
    print(OKGREEN +"#### OK score " + str(scoreTotal) +RESET)
if stepError:
    print(WARNING +"#### NOK step Error found" +RESET)
else:
    print(OKGREEN +"#### OK steps "+ RESET)


# It is good practice to close the file at the end to free up resources
#file.close()


from sendmsg import send_msg
import random

#send_msg(receiver, subject, msg)

participants = [['John Doe', 'johndoe@gmail.com'], 
                ['Jake Doe', 'jakedoe@gmail.com'], 
                ['Jane Doe', 'janedoe@gmail.com']]

#comma separated list of tuples of people who can't be each other's secret santas
constraints = [['John Doe', 'Jane Doe']]

random.shuffle(participants)

#loop to check constraints
i = 0
j= 0
while(i < len(participants) and j < len(constraints)): 
            #checks if last participant and if constraint violated
            if ((i == (len(participants) - 1)) and ((constraints[j][0] == participants[i][0] or constraints[j][1] == participants[i][0]) and  (constraints[j][0] == participants[0][0] or constraints[j][1] == participants[0][0]))):
                random.shuffle(participants)
                i = 0
                j = 0
                continue 
            #last participant but current constraint not violated, move on to next constraint
            elif (i == len(participants) - 1):
                i = 0
                j = j + 1
                continue
                
            #last particiapant, but no constraint violated?
            if ((constraints[j][0] == participants[i][0] or constraints[j][1] == participants[i][0]) and (constraints[j][0] == participants[i + 1][0] or constraints[j][1] == participants[i + 1][0])):
                random.shuffle(participants)
                i = 0
                j = 0
                continue
            
            #move to next participant to check current constraint
            i+=1


for i in range(len(participants)): 
    gifter = ""
    receiver = ""
    if(i == len(participants) - 1): 
        #print(participants[i][0] + ' is ' + participants[0][0] + "'s secret santa.")
        gifter = participants[i]
        receiver = participants[0]
    else: 
        #print(participants[i][0] + ' is ' + participants[i + 1][0] + "'s secret santa.")
        gifter = participants[i]
        receiver = participants[i + 1]
    msg = """Hello, """ + gifter[0] + """. This email contains your secret santa assignment!
You will be giving a gift to """ + receiver[0] + '.' 

    send_msg(gifter[1], 'Secret Santa Assignment', msg) 


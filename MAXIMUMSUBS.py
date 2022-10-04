T=int(input())
for i in range(T):
\
    minutes=float(input())
    totalTimeInSeconds = minutes*60
    submissionInSeconds = 30
    cantSubmitInLastSeconds = 5
    
    #Actual calculation starts here
    
    allotedTimeForSubmission = totalTimeInSeconds - cantSubmitInLastSeconds
    maxSubmission = (allotedTimeForSubmission + submissionInSeconds - 1)/submissionInSeconds
    print(int(maxSubmission))
    
    """ There are many solutions available already. This particular solution aims at improving readability.
    Variable declarations should match the case. also, logically ir was not required to deduct 5 seconds to get the answer, but for customer (Problem) requirement,
    it was important to include cantSubmitInLastSeconds. Just multiplying by 2 will solve the problem, but will not address customer requirements.
    Python is known for minimal code but writing code so that others can understand the purpose of code is what makes prodcution ready code """
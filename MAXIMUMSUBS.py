T=int(input())
for i in range(T):
    minutes=float(input())
    totalTimeInSeconds = minutes*60
    submissionInSeconds = 30
    cantSubmitInLastSeconds = 5
    allotedTimeForSubmission = totalTimeInSeconds - cantSubmitInLastSeconds
    maxSubmission = (allotedTimeForSubmission + submissionInSeconds - 1)/submissionInSeconds
    print(int(maxSubmission))
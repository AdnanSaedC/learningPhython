import time

waitTimeInSeconds=1
attempt=1
maxAttempt=5

while attempt <= maxAttempt:
    print("Attempt:",attempt,"-waitTime:",waitTimeInSeconds)
    attempt+=1
    waitTimeInSeconds*=2
    time.sleep(waitTimeInSeconds)
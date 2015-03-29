# Module to find the number of correct, wrong and missed responses and the
# final score from the passed response string.
import os

CORRECT_MARKS = 3
INCORRECT_MARKS = -1

def get_result(qpset , response , questions) :
    #global correct , wrong , missed , score
    correct = wrong = missed = 0
    try:
		path = os.curdir + os.sep + 'system' + os.sep + 'data' + os.sep + 'key.txt'    
		f1 = open(path)
    except IOError:
	return 
    key = f1.readline()
    while key[0] != qpset :
        key = f1.readline()
    key = key[1:]
    i = 0
    for word in key[1:] :

		if i not in questions:    #Check question is to be evaluated
			if response[i] != ' ' :		#Check question not missed
				if response[i] == key[i] :	
					correct+=1			#Correct response
				else :
					wrong+=1			#Incorrect response
			else:
				missed += 1
		i += 1

    score = CORRECT_MARKS * correct + INCORRECT_MARKS * wrong
    f1.close()
    return correct , wrong , missed , score

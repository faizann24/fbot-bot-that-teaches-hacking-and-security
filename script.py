import pandas as pd
import numpy as np
import difflib
import sys
reload(sys)
sys.setdefaultencoding("ascii")

sm = difflib.SequenceMatcher(None)

filepath = 'E:\\Downloads\\CSV\\gooddata.csv'
data = pd.read_csv(filepath,quotechar='"',error_bad_lines=False)
data = pd.DataFrame(data)
data = np.array(data)
print len(data)

questions = []
answers = []
for i in data:
	questions.append(i[0])
	goodParagraph = i[2]
	goodParagraph = ' '.join(goodParagraph.split())
	goodParagraph = goodParagraph.replace("'", "")
	answers.append(goodParagraph)

while True:
	question = raw_input('Enter your question: ')
	sm.set_seq2(question.lower())
	similarities = []
	simDict = {}
	for i in range(0,len(questions)):
		ans = answers[i]
		i = questions[i]
		sm.set_seq1(str(i).lower())
		x = sm.ratio()
		similarities.append(x)
		simDict[x] = str(ans)
	import operator
	simDict = sorted(simDict.items(), key=operator.itemgetter(0))
	simDict.reverse() 

	if float(simDict[0][0]*100) >= 70.0:
		print 'Giving answer with probability ' + str(simDict[0][0]*100)
		print simDict[0][1]
	else:
		print 'I\'m sorry Sir, I cannot find an answer for you.'

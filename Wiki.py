import wikipedia
import sys

def search(term = '', searchCount = 25):
	if term == '':
		term = raw_input("Enter search term: ")
	results = wikipedia.search(term,searchCount)
	if len(results) == 0:
		print("No articles found for term: " + term)
		exit()
	print '\n'
	print('*~*~Article Select~*~*\n')
	articleNo = selectArticle(results)
	if articleNo == -1:
		exit()
	else:
		summary(results[articleNo])

def summary(article):
	print '\n'
	try:
		summaryText = wikipedia.summary(article)
		print "*~*~ " + "Summary: " + article.encode('utf-8') + " ~*~*\n"
		print summaryText.encode('utf-8')
	except wikipedia.exceptions.DisambiguationError, e:
		print "Disambiguation needed.  Select desired article. \n"
		articleNo = selectArticle(e.options)
		if articleNo == -1:
			exit()
		else:
			summary(e.options[articleNo])

def confirmYN(question):
	print(question + ' [y/n]')
	while True:
		response = raw_input()
		if response is 'y':
			return True
		elif response is 'n':
			return False
		else:
			print "Please enter 'y' or 'n'"

def selectArticle(articles):
	buffer = 1
	for article in articles:
		print str(buffer) + ": " + article.encode('utf-8')
		buffer += 1
	print '\n'	 
	valid = False
	articleNo = -1
	while not valid:
		response = raw_input("Enter article number for summary or exit to quit: ")
		if response == 'exit':
			valid = True
		try:
			if (int(response) - 1) in range(len(articles)):
				articleNo = int(response) - 1
				valid = True
			else:
				print ("Invalid Input.")
		except:
			print("Invalid Input")
	return articleNo

def main():
	if len(sys.argv) == 1:
		search()
	elif len(sys.argv) == 2:
		search(sys.argv[0])
	elif len(sys.argv) == 3:
		search(sys.argv[1],sys.argv[2])
	else:
		print "Too many arguments!"

if __name__ == "__main__":
    main()


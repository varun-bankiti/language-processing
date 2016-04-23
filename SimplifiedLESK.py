""" Author: Varun Kumar Reddy B
    Simplified LESK Algorithm """

from nltk.corpus import wordnet

def removeStopWords(words):
    from nltk.corpus import stopwords
    stop=stopwords.words('english')
    return [word for word in words if word not in stop]
def computeOverlap(signature,context):
    overlap=0
    overlapWords=[]
    for word in context:
        count=signature.count(word)
        if(count>0):
            overlapWords.append(word)
            overlap+=1
    return (overlap,overlapWords)
def simplifiedLESK(word,sentence,REMOVE_STOPWORDS=False):
    syns=wordnet.synsets(word)
    bestSense=syns[0]
    maxOverlap=0
    context=sentence.split()
    if(REMOVE_STOPWORDS):
        context=removeStopWords(context)
    overlaps={}
    for sense in syns:
        signature=sense.definition().split()
        examples=sense.examples()
        for example in examples:
            signature+=example.split()
        if(REMOVE_STOPWORDS):
            signature=removeStopWords(signature)
        overlap,overlapWords=computeOverlap(signature,context)
        overlaps[sense]=(overlap,overlapWords)
        if overlap>maxOverlap:
            maxOverlap=overlap
            bestSense=sense
    return (bestSense,maxOverlap,overlaps)

sentence="The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities"
word="bank"
REMOVE_STOPWORDS=True;

choosedSense,maxOverlap,overlaps=simplifiedLESK(word,sentence,REMOVE_STOPWORDS)

for sense in overlaps:
    print "Choosen Sense\t: ",sense.name()
    print "Glossy\t\t: ",sense.definition()
    print "Total Overlaps\t: ",overlaps[sense][0]
    print "Overlap Words\t: ",overlaps[sense][1]
    print "\n"

print "\n************************************************\n"
print "Choosen Sense\t: ",choosedSense.name()
print "Glossy\t\t: ",choosedSense.definition()
print "Total Overlaps\t: ",overlaps[choosedSense][0]
print "Overlap Words\t: ",overlaps[choosedSense][1]
print "\n************************************************\n"

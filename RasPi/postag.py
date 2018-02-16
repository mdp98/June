import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

def postag(userCommand):
    stop_words = set(stopwords.words('english'))
    stop_words.remove('you')
    stop_words.remove('yours')
    stop_words.remove('your')
    stop_words.remove('what')
    tokens = word_tokenize(userCommand)
    refinedTokens = [w for w in tokens if not w in stop_words]
    tagTokens = nltk.pos_tag(refinedTokens)
    return tagTokens

postag("How's the weather")
    
if __name__ == "__main__":
    main()

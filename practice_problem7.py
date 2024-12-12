
def matchingWords(sentence1, sentence2):
    score = 0
    words1 = sentence1.split(' ')
    words2 = sentence2.split(' ')

    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1

    return score


if __name__ == '__main__':

    sentences = ['This is good', 'My name is Hiral', 'Python is good language', 'Hiral Hiral is a good boy']

    queryString = input('Please enter query string\n')

    scores = [matchingWords(queryString, sentence) for sentence in sentences]
    # print(scores)

    sortedList = [sortedItem for sortedItem in sorted(zip(scores, sentences), reverse=True)]
    print(sortedList)

    for score, item in sortedList:
        print(f'"{item}": with a score of {score}')

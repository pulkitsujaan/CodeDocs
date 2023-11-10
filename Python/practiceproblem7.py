"""Search Engine"""
def matches(sent1, sent2):
    match = 0
    word1 = sent1.split(" ")
    word2 = sent2.split(" ")
    for words1 in word1:
        for words2 in word2:
            if words1.lower() == words2.lower():
                match += 1
    return match


if __name__ == "__main__":
    # print(matches("I am a Boy", "I am a girl"))
    query=input("Please enter the query string\n")
    sentences=["my name is Pulkit","I am a boy","I am a programmer","I love singing","Python hai bhaika"]
    scores=[matches(query,sentence) for sentence in sentences]
    finaldata=[data for data in sorted(zip(scores,sentences),reverse=True)]
    print(f"\n{len(scores)} results found")
    for match,item in finaldata:
        print(f"\"{item}\"-----matches found-{match}")
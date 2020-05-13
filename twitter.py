from collections import Counter

def similiary_score(user_handle, twitter_handles):
    scores = {} # keep track of a score
    # create a loop to compare letters in my_handle to letters in each twitter_handle
    for i in range(len(twitter_handles)):
        score = 0
        for letter in user_handle:
            if letter in twitter_handles[i]:
                score += 1  # if we find similar letter, +1 to score
            else:
                score -= 1
        # add twitter_handle(as key), and score(as value) to scores dictionary
        scores[twitter_handles[i]] = score
    return scores

print(similiary_score('at', ['Hat', 'coat']))

def suggestions(user_handle, twitter_handles, k):
    similarity_scores = similiary_score(user_handle, twitter_handles)
    similarity_counter = Counter(similarity_scores)
    top_suggestions = similarity_counter.most_common(k)
    return top_suggestions

print(suggestions('iLoveHats', ['iLovedHatts', 'ilovecoats', 'coat'], 2))
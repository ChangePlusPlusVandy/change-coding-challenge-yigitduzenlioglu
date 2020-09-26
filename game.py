import tweepy, random
#import csv

# Twitter Credentials
consumer_key = "ElayDpMVlojn9K13lhEgLxLjN"
consumer_secret = "AH82IoOvxpxFV2ckdxOomsXPDT67yMo9HDLr5gsMbwk6bhpX2Y"
access_key = "1309616136003051521-BAgQAPPZ64NkaklA1X6gs3eKqZDVEr"
access_secret = "2onw206tT4HPMeLLU8pdyle2yAokPGEeaK9auB5cqwIxX"

# Function to extract tweets
def get_tweets(username):


        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)

        # Calling api
        api = tweepy.API(auth)

        # 3200 tweets to be extracted
        number_of_tweets = 3200
        tweets = tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets)

        '''We could have created a file containing tweets for a faster initialization.'''
        #csvFile = open(str(username), 'a')
        #csvWriter = csv.writer(csvFile)
        #for tweet in tweets:
        #    if j.find('http') == -1 and j.find('@') == -1 :
        #        csvWriter.writerow([tweet.text.encode('utf-8')])
        #        print (tweet.text)
        #csvFile.close() 

        # Empty Array that will be appended by tweets
        tmp=[]

        # create csv array of tweet texts
        tweets_for_csv = [tweet.text for tweet in tweets]
        for j in tweets_for_csv:
            # Appending only text tweets to the empty array tmp
            if j.find('http') == -1 and j.find('@') == -1 :
                tmp.append(j)

        return tmp
        # Printing the tweets
        #print(tmp)

# Driver code
if __name__ == '__main__':

    # Arrays to contain tweets
    elon = []
    elon = get_tweets("@elonmusk")

    kanye = []
    kanye = get_tweets("@kanyewest")

    # Statistical counters
    correct = 0
    total = 0

    playtime = int(input("How many tweets do you want to view?"))

    for i in range(playtime):
        # Choosing between elon and kanye
        elon_or_kanye = random.randint(1, 2)

        #if kanye is chosen
        if elon_or_kanye % 2 == 0:
            # Select a random tweet of kanye, print it,
            # then remove it from the array
            random_kanye_tweet = random.choice(kanye)
            print(random_kanye_tweet)
            kanye.remove(random_kanye_tweet)

            # Answer input and statistical adjustment
            answer = str(input("Who do you think this tweet belongs? (k/e)"))
            total += 1
            if answer == 'k':
                correct += 1
        else:
            # Select a random tweet of elon, print it,
            # then remove it from the array
            random_elon_tweet = random.choice(elon)
            print(random_elon_tweet)
            elon.remove(random_elon_tweet)

            # Answer input and statistical adjustment
            answer = str(input("Who do you think this tweet belongs? (k/e)"))
            total += 1
            if answer == 'e':
                correct += 1

    # Display the statistics
    print('Number of correct answers:', correct)
    print('Number of Wrong answers:', total - correct)

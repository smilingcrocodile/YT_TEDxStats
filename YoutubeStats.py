import requests, csv, datetime

#Parameter
YoutubeAPIKey = #"Your YouTube API key"


#String containing up to 50 vid ID at a time (check YouTube API doc for more info). If you want to check more than 50 videos, make a list and loop the rest of the script over it.
#Here's our talks list for this year.
vidIdList = 'MJeXyPFYVEY,UlXqZsGfQII,7CAaoWcknvM,29y9bQak6-s,R9OtUn4hYpE,5TtwG_LR0iY,6cVxUNsP-Eg,HAJORjDMw5c,L934qGaEUZU,f2TCJ9XBtvM,5VexLuYzn6w'

#Make the API call
vidStatsResponse = requests.get("https://www.googleapis.com/youtube/v3/videos?key=" + YoutubeAPIKey + "&part=statistics&id=" + vidIdList)
#update the range with the number of id in your string.
a = vidStatsResponse.json()
for i in range(0,10):
    vidId = a['items'][i]['id']
    viewCount = a["items"][i]['statistics']['viewCount']
    likeCount = a["items"][i]['statistics']['likeCount']
    dislikeCount = a["items"][i]['statistics']['dislikeCount']
    favoriteCount = a["items"][i]['statistics']['favoriteCount']
    commentCount = a["items"][i]['statistics']['commentCount']
    timeStamp = datetime.datetime.utcnow()
    #Stores it in a csv file
    with open("./TEDxStats.csv", 'a', newline='', encoding="utf-8") as outputfile:
        outputwriter = csv.writer(outputfile, delimiter=';')
        outputwriter.writerow([timeStamp,vidId,viewCount,likeCount,dislikeCount,favoriteCount,commentCount])
        outputfile.close()
    timeStampHour = datetime.datetime.utcnow()
print('Filed saved at ' + str(timeStampHour))
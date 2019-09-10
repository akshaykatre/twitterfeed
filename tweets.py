from keys import auth
from tweepy import Stream, StreamListener
import json 
import pdb

file = open("Output.csv", "w")
file.write("X,Y\n")


data_list = []
count = 0

class listener(StreamListener):

    def on_data(self, data):
        global count

        #How many tweets you want to find, could change to time based
        if count <= 10:
            json_data = json.loads(data)
           # pdb.set_trace()
            try:
                coords = json_data["coordinates"]
            except KeyError:
                coords = None
            if coords is not None:
               print(coords["coordinates"])
               lon = coords["coordinates"][0]
               lat = coords["coordinates"][1]

               data_list.append(json_data)

               file.write(str(lon) + ",")
               file.write(str(lat) + "\n")

               count += 1
            return True
        else:
            file.close()
            return False

    def on_error(self, status):
        print(status)

twitterStream = Stream(auth, listener())
#What you want to search for here
twitterStream.filter(track=["#BoyWithLuv"])
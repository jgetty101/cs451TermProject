import json


def cleanStr4SQL(s):
    return s.replace("'", "`").replace("\n", " ")


def flatten_json(obj):
    ret = {}

    # recursive function
    def flatten(x, flattened_key=""):
        # we want to loop over the keys in the object
        # and flatten
        if type(x) is dict:
            for curr_key in x:
                # we are appending the nested keys to the original
                flatten(x[curr_key], curr_key + '_')
        else:
            # base case: not at a list or object or dict (i.e. at a single string)
            # meaning x will be a string, integer, etc
            # take our flattened key and add it to our return object
            ret[flattened_key[:-1]] = x

    flatten(obj)
    return ret.items()


def parseBusinessData():
    # read the JSON file
    # We assume that the Yelp data files are available in the current directory. If not, you should specify the path when you "open" the function. 
    with open('.//yelp_business.JSON', 'r') as f:
        outfile = open('.//business.txt', 'w')
        line = f.readline()
        count_line = 0
        # read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write("{} - business info : '{}' ; '{}' ; '{}' ; '{}' ; '{}' ; '{}' ; {} ; {} ; {} ; {}\n".format(
                str(count_line),  # the line count
                cleanStr4SQL(data['business_id']),
                cleanStr4SQL(data["name"]),
                cleanStr4SQL(data["address"]),
                cleanStr4SQL(data["state"]),
                cleanStr4SQL(data["city"]),
                cleanStr4SQL(data["postal_code"]),
                str(data["latitude"]),
                str(data["longitude"]),
                str(data["stars"]),
                str(data["is_open"])))

            # process business categories
            categories = data["categories"].split(', ')
            outfile.write("      categories: {}\n".format(str(categories)))

            # TO-DO : write your own code to process attributes
            # make sure to **recursively** parse all attributes at all nesting levels. You should not assume a particular nesting level.

            attributes = data["attributes"]
            outfile.write("      attributes: {}\n".format(str(flatten_json(attributes))))

            # TO-DO : write your own code to process hours data

            hours = data["hours"]
            businessHours = []
            for day in hours:
                hours_str = "('" + day + "','" + \
                             hours[day].split("-")[0] + "','" + hours[day].split("-")[1] + "')"
                businessHours.append(hours_str)
            outfile.write("      hours: {}".format(str(flatten_json(businessHours))))

            outfile.write("")

            outfile.write('\n')

            line = f.readline()
            count_line += 1
    print(count_line)
    outfile.close()
    f.close()


def parseUserData():
    # TO-DO : write code to parse yelp_user.JSON
    #read the JSON file
    # We assume that the Yelp data files are available in the current directory. If not, you should specify the path when you "open" the function.
    with open('.//yelp_user.JSON','r') as f:
        outfile =  open('.//user.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write("{} - user info : '{}' ; '{}' ; '{}' ; '{}' ; '{}' ; '{}'\n".format(
                              str(count_line), # the line count
                              cleanStr4SQL(data['user_id']),
                              cleanStr4SQL(data["name"]),
                              cleanStr4SQL(data["yelping_since"]),
                              str(data["tipcount"]),
                              str(data["fans"]),
                              str(data["average_stars"])
                              #str(data["account_reviews"])
                            )
                        )

            # TO-DO : write your own code to process friends

            friends = data["friends"]
            outfile.write("      friends: {}\n".format(str(flatten_json(friends))))

            outfile.write("")

            outfile.write('\n')

            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
    f.close()
    pass


def parseCheckinData():
    pass
    # TO-DO : write code to parse yelp_checkin.JSON
    #read the JSON file
    # We assume that the Yelp data files are available in the current directory. If not, you should specify the path when you "open" the function.
    with open('.//yelp_checkin.JSON','r') as f:
        outfile =  open('.//checkin.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write("{}- '{}': \n".format(
                              str(count_line), # the line count
                              cleanStr4SQL(data['business_id']),
                              #cleanStr4SQL(data["date"])
                            )
                        )

            # TO-DO : write your own code to process date

            friends = data["date"]
            date = friends.split(',')
            i = 0
            while i < len(date):
                outfile.write("(" + "'" + date[i][:4] + "'" + ","+ "'" + date[i][5:7] + "'" + "," + "'" + date[i][8:10] + "'" + "," + "'" + date[i][11:19] + "'" + ")")
                outfile.write("")
                i = i + 1

            outfile.write("")

            outfile.write('\n')

            line = f.readline()
            count_line +=1
    #print(count_line)
    outfile.close()
    f.close()


def parseTipData():
    # TO-DO : write code to parse yelp_tip.JSON
    with open('.//yelp_tip.JSON', 'r') as f:
        outfile = open('.//tip.txt', 'w')
        line = f.readline()
        count_line = 0
        # read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write("{} - business info : '{}' ; '{}' ; '{}' ; '{}' ; '{}'\n".format(
                str(count_line),  # the line count
                cleanStr4SQL(data['business_id']),
                cleanStr4SQL(data["date"]),
                int(data["likes"]),
                cleanStr4SQL(data["text"]),
                cleanStr4SQL(data["user_id"])))

            outfile.write("")

            outfile.write('\n')

            line = f.readline()
            count_line += 1
    print(count_line)
    outfile.close()
    f.close()


if __name__ == "__main__":
    parseBusinessData()
    parseUserData()
    parseCheckinData()
    parseTipData()

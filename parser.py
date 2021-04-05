import re

def parse_randomtweets():
    new_tab = []
    for file_number in range(2):
        with open("tweets/randomtweets"+str(file_number+1)+".txt","r") as tweets:
            string = tweets.read()
        tab = []
        #parse the data into a list
        for i in range(1000):
            elem,string = string.split('"'+str(i+1)+'"')
            tab.append(elem)
        tab.append(string)

        #Clean the sentences
        
        for line in tab:
            #remove "
            line = line.replace('"',"")
            #remove ( and ))
            line = line.replace('(',"")
            line = line.replace(')',"")
            #replace < by " <" to make it detectable sometimes
            line = line.replace('<'," <")
            #remove the first comma
            line = line[1:]
            #remove the multiple whitespaces
            line = re.sub('\s+', ' ', line)

            words = line.split(" ")
            rebuild_line=""
            for word in words:
                if word == "":
                    break
                if not (word[0]=="#" or word[0]=="@" or word[0]=="&" or word[0]=="<" or word[:2]=="[#" or word[:2]=="(@") :
                    if not word[:4]=="http":
                        rebuild_line += word
                        rebuild_line += " "
            rebuild_line = rebuild_line[:-1]
            if rebuild_line[:2]=="RT":
                rebuild_line = rebuild_line[3:]
            if not rebuild_line == "":
                new_tab.append(rebuild_line)

    with open("tweets/randomtweets_clean.txt","w") as tweets:
        for line in new_tab:
            tweets.writelines(line)
            tweets.writelines("\n")
            tweets.writelines("//FIN//")
            tweets.writelines("\n")
    print("Parsing finished")

if __name__ == "__main__":
    parse_randomtweets()

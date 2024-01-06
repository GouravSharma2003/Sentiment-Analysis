#Importing json file, so that we can add our inputted data into a file.
import json

#Creating a DataBase Class
class DataBase:
    #Creating a function from which we will get the data from the database.
    def  getData(self, name, email, password, number):
        #Opening JSON file where our data is stored.
        with open('myDATA.json', 'r') as rdF:
            #Loading our all data into "DataBase".
            db = json.load(rdF)

            #Checing if the email already exists or not, else add NAME and PASSWORD into EMIAL
            if email in db:
                return 0
            else:
                db[email] = [name, password, number]
                with open('myDATA.json', 'w') as wtF:
                    json.dump(db, wtF)
                return 1
    def search(self, email, password):
        with open("myDATA.json", 'r') as rdF:
            db = json.load(rdF)

            if email in db:
                if db[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0




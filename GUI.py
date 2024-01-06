from tkinter import *               #Importing tkinter library: used for creating GUI.
from db import DataBase           #Importing myDB a python file, which we have created to use it into our MainFile.
from tkinter import messagebox      #Importing messagebox from tkinter library: is used to generate a dialog box.
from myAPI import Api

class NLP:
    #Default constructor created using: __init__(self):
    def __init__(self):
        #Object of DataBase class from myDB.py a pythonFile, is declared
        self.dbObj = DataBase()
        self.apiObj = Api()

        #Object of tkinter is initialized/declared as self.root
        self.root = Tk()

        # It will modify my title.
        self.root.title("My GUI")

        # It will generate a logo for my window
        # Isko skip kr dena abhi ke liye... because isme image ki location manually deni padegi
        # self.root.iconbitmap(r'C:\Users\abhie\PycharmProjects\pythonProject\Resources\Home.ico')

        #It will set my windows background color.
        self.root.configure(bg='grey')

        # It will set the height and width of our window
        self.root.geometry("350x650")

        # Calling login_GUI function
        self.login_GUI()

        # It is used to hold our screen.
        self.root.mainloop()

    #Login Page Creation with this function.
    def login_GUI(self):
        #This "self.clear()" function is used to destroy/vanish/clear the previous data
        self.clear()
        self.root.geometry("350x650")

        #It will generate a heading
        heading = Label(self.root, text=' Login Page', bg='#FFFFFF', fg='black')
        #It will set my font
        heading.configure(font=('Verdana', 24, 'bold'))
        heading.pack(pady=(20,20))

        #Email Label
        email = Label(self.root, text='Email', bg='#FFFFFF', fg='black')
        email.configure(font=('Verdana', 14, 'bold'))
        email.pack(pady=(20, 20))
        # Taking input from user
        self.emailInput = Entry(self.root)
        self.emailInput.insert(0, '')
        self.emailInput.pack(pady=(5, 5))

        #Password Label
        pw = Label(self.root, text='Password', bg='#FFFFFF', fg='black')
        pw.configure(font=('Verdana', 14, 'bold'))
        pw.pack(pady=(20, 20))
        #Taking Password as input
        self.pwInput = Entry(self.root, show='*')
        self.pwInput.insert(0, '')
        self.pwInput.pack(pady=(5, 5))

        #Login Button
        login_Button = Button(self.root, text='Login', height=1, width=5, command=self.doLogin)
        login_Button.pack(pady=(20, 20))

        #Label
        notMember = Label(self.root, text='Not a member?', bg='#FFFFFF', fg='black')
        notMember.configure(font=('Verdama', 14, 'bold'))
        notMember.pack(pady=(2, 5))

        # Register Button
        reg_Button = Button(self.root, text='Register', height=1, width=7, command=self.register_GUI)
        reg_Button.pack(pady=(20, 20))

    # Register Page Creation with this function.
    def register_GUI(self):

        self.clear()    #Calling clear() function

        #It will generate a heading
        heading = Label(self.root, text='Apna Register Page', bg='#FFFFFF', fg='black')

        #It will set my font
        heading.configure(font=('Verdama', 24, 'bold'))
        heading.pack(pady=(20,20))

        # Name Label
        name = Label(self.root, text='Name', bg='#FFFFFF', fg='black')
        name.configure(font=('Verdama', 14, 'bold'))
        name.pack(pady=(20, 20))
        # Taking input from user
        self.nameInput = Entry(self.root)
        self.nameInput.insert(0, '')
        self.nameInput.pack(pady=(5, 5))

        #Email Label
        email = Label(self.root, text='Email', bg='#FFFFFF', fg='black')
        email.configure(font=('Verdama', 14, 'bold'))
        email.pack(pady=(20, 20))
        # Taking input from user
        self.emailInput = Entry(self.root)
        self.emailInput.insert(0, '')
        self.emailInput.pack(pady=(5, 5))

        #Password Label
        passd = Label(self.root, text='Create Password', bg='#FFFFFF', fg='black')
        passd.configure(font=('Verdama', 14, 'bold'))
        passd.pack(pady=(20, 20))
        #Taking Password as input
        self.pwInput = Entry(self.root, show='*')
        self.pwInput.insert(0, '')
        self.pwInput.pack(pady=(5, 5))

        #Phone Number
        phNo = Label(self.root, text='Contact Number', bg='#FFFFFF', fg='black')
        phNo.configure(font=('Verdama', 14, 'bold'))
        phNo.pack(pady=(20, 20))
        # Taking input from user
        self.phNoInput = Entry(self.root)
        self.phNoInput.insert(0, '')
        self.phNoInput.pack(pady=(5, 5))

        # Register Button
        # After clicking on RegisterButton, the backEnd will process our data which we have filled into the different labels and Do our Registration.
        reg_Button = Button(self.root, text='Register', height=1, width=7, command=self.doRegistration)
        reg_Button.pack(pady=(20, 20))

        # Label
        member = Label(self.root, text='Already a member?', bg='#FFFFFF', fg='black')
        member.configure(font=('Verdama', 14, 'bold'))
        member.pack(pady=(2, 5))

        # Login Button
        # After clicking on LoginButton, we will be directing to our LogIn Page.
        login_Button = Button(self.root, text='Login', height=1, width=5, command=self.login_GUI)
        login_Button.pack(pady=(20, 20))

    # Main Home Page, in which we can add as many as analysis features.
    # Here we have Sentimental Analyser
    def homeGUI(self):
        #CLearing the existing window
        self.clear()

        #Setting up new window size
        self.root.geometry("650x400")

        heading = Label(self.root, text='Apne Sentiments kb tk chupaoge', bg='#FFFFFF', fg='black')
        # It will set my font for heading
        heading.configure(font=('Verdana', 24, 'bold'))
        heading.pack(pady=(10, 20))

        #Creating a button for SentimentAnalysis
        # After clicking on SentimentButton, it will redirect us on SentimentGUI page.
        sentimentBTN = Button(self.root, text='Sentiment Analyser', height=1, width=15, command=self.sentimentGUI)
        sentimentBTN.pack(pady=(10, 20))

        #Creating a button for LogOut
        # After clicking on LogOut button, we will redirect to LogIn page.
        logOutBTN = Button(self.root, text='Log Out', height=1, width=10, command=self.login_GUI)
        logOutBTN.pack(pady=(30, 20))


    # Sentimental Analysis Main Window where Input and Output will be visible.
    def sentimentGUI(self):
        self.clear()
        self.root.geometry("500x400")

        # Heading
        heading = Label(self.root, text='Apne vicharo ki vykhra kijie..!', bg='#FFFFFF', fg='black')
        heading.configure(font=('Verdana', 14, 'bold'))
        heading.pack(pady=(20, 20))

        #Taking input from user.
        self.textInput = Entry(self.root, width=50)
        self.textInput.pack(pady=(10, 20), ipady=5)

        # Analyser Button
        # After clicking on the AnalyserButton, the code will send the string to "doSentimentAnalysis" function which will analyse inputted string and print the OutPut
        analyserBTN = Button(self.root, text="Analyser", height=1, width=7, command=self.doSentimentAnalysis)
        analyserBTN.pack(pady=(10, 20))

        # Creating a lable for the result of our sentiments entered.
        self.sentimentResult = Label(self.root, text='', bg='#FFFFFF', fg='black', height=5, width=60)
        self.sentimentResult.configure(font=('Verdana', 10))
        self.sentimentResult.pack(pady=(10, 20))

        # Back Button
        # After click BackButton, we will be directed on our HomePage.
        backBTN = Button(self.root, text="Back", height=1, width=7, command=self.homeGUI)
        backBTN.pack(pady=(10, 20))


    #This clear function is used to clear our last opened window.
    def clear(self):
        for i in self.root.pack_slaves():
            #Destroy() function is used to destroy/vanish everything.
            i.destroy()

    #This function is used for Save information regarding registration.
    def doRegistration(self):
        # using .get() we are taking values, which we have entered and storing into our database file.
        name = self.nameInput.get()
        email = self.emailInput.get()
        password = self.pwInput.get()
        mbNumber = self.phNoInput.get()

        #Using the object of dataBase class, we are calling the getData() function,
        #
        response = self.dbObj.getData(name, email, password, mbNumber)

        if response:
            # messagebox - is used to show a dialogbox, containing title and message respectvely.
            messagebox.showinfo("Successfully Opened..!", "Register Successful")
            self.login_GUI()
        else:
            messagebox.showerror("Invalid..!", "Invalid ID & Password")

    #This function is used Login, using existing email Id and Password
    def doLogin(self):
        # using .get() we are taking values, which we have entered and storing into our database file.
        email = self.emailInput.get()
        password = self.pwInput.get()

        # Using the object of dataBase class, we are calling the search() function,
        # To find, emailId and password contains of Valid user or not.
        response = self.dbObj.search(email, password)

        if response:
            messagebox.showinfo("Successfully Opened..!", "Login Successful")
            self.homeGUI()
        else:
            messagebox.showerror("Invalid..!", "Invalid ID & Password")

    def doSentimentAnalysis(self):
        text = self.textInput.get()
        result = self.apiObj.sentimentAnalysis(text)

        if 'sentiment' in result:
            sentiment_data = result['sentiment']
            self.sentimentResult.config(
                text=f"Sentiment Analysis Result:\nNegative: {round(sentiment_data['negative']*100, 2)} %\nNeutral: {round(sentiment_data['neutral']*100, 2)} %\nPositive: {round(sentiment_data['positive']*100, 2)} %"
            )
        else:
            self.sentimentResult.config(
                text="Error in sentiment analysis response"
            )

        #Some more methods to print our Sentimental Analysis Result.
        #self.sentimentResult.config(text=f"Sentiment Analysis Result:\n{result}")

        #self.sentimentResult.config(text=f"Sentiment Analysis Result:\nLabel: {result['label']}\nConfidence: {result['confidence']}")
        #self.sentimentResult.config(text=f"Sentiment Analysis Result:\nNegative: {result['negative']}\nNeutral: {result['neutral']}\nPositive: {result['positive']}")

        #self.sentimentResult.config(text=f"Sentiment Analysis Result:\nSentiment: {result['sentiment']}\nConfidence: {result['confidence']}")


# Create an instance of the NLP class
# Here is the main function of the whole program.
project = NLP()
GUI.py
#Displaying GUI.py.
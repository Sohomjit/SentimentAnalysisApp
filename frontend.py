from tkinter import *
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

root = Tk()
root.title("Sentiment Analyser App")

def myClick():
    name_user = e1.get()
    textForAnalysis = e2.get()
    analysis_score = sentiment_analyzer_scores(textForAnalysis)

    if analysis_score['compound'] >= 0.05:
                print("Positive")
                finalSentiment = "Positive"
                
    elif analysis_score['compound'] <= - 0.05:
                print("Negative")
                finalSentiment = "Negative"
                
    else :
        print("Neutral")
        finalSentiment = "Neutral"
    
    e3.configure(state = 'normal')
    e3.delete(0, END)
    e3.insert(0, name_user)
    e3.configure(state = 'readonly')

    e4.configure(state = 'normal')
    e4.delete(0, END)
    e4.insert(0, finalSentiment)
    e4.configure(state = 'readonly')
    

def reset():
    e1.delete(0, END)
    e1.insert(0, "Enter Your Name")
    e2.delete(0, END)
    e2.insert(0, "Enter Text for Sentiment Analysis")
    
    e3.configure(state = 'normal')
    e3.delete(0, END)
    e3.insert(0, " Your Name ")
    e3.configure(state = 'readonly')

    e4.configure(state = 'normal')
    e4.delete(0, END)
    e4.insert(0, " Result will be displayed here ")
    e4.configure(state = 'readonly')

    e5.grid_forget()
    e6.grid_forget()

def credit():
    
    e5.grid(row=0, column = 3, columnspan=2, padx = 10, pady = 10)
    e5.configure(state = 'readonly')
    e6.grid(row=1, column = 3, columnspan=2, padx = 10, pady = 10)
    e6.configure(state = 'readonly')

def clear1(event):
    e1.delete(0, END)
    
def clear2(event):
    e2.delete(0, END)


def sentiment_analyzer_scores(text):
    score = analyzer.polarity_scores(text)
    print(text)
    print(score)
    return score

def quit():
    root.quit()

l1 = Label(root, text = "Name : ")
l1.grid(row=0, column=0)

e1 = Entry(root, width = 50, bg = "lightblue", fg = "red", borderwidth = 10)
e1.insert(0, "Enter Your Name")
e1.grid(row=0, column = 1, columnspan=2, padx = 10, pady = 10)
e1.bind('<Button-1>', clear1)


l2 = Label(root, text = "Enter Text for Sentiment Analysis : ")
l2.grid(row=1, column=0)

e2 = Entry(root, width = 50, bg = "lightblue", fg = "red", borderwidth = 10)
e2.insert(1, "Enter Text for Sentiment Analysis")
e2.grid(row=1, column = 1, columnspan=2, padx = 10, pady = 10)
e2.bind('<Button-1>', clear2)

l3 = Label(root, text = "User's Name :")
l3.grid(row=2, column=0)

e3 = Entry(root, width = 50, bg = "lightblue", fg = "red", borderwidth = 10)
e3.insert(1, " Your Name ")
e3.grid(row=2, column = 1, columnspan=2, padx = 10, pady = 10)
e3.configure(state = 'readonly')

l4 = Label(root, text = "Final Analysis :")
l4.grid(row=2, column=3)


e4 = Entry(root, width = 50, bg = "lightblue", fg = "red", borderwidth = 10)
e4.insert(1, " Result will be displayed here ")
e4.grid(row=2, column = 4, columnspan=2, padx = 10, pady = 10)
e4.configure(state = 'readonly')


e5 = Entry(root, width = 50, bg = "lightblue", fg = "red", borderwidth = 10)
e5.insert(1, "Developer - Sohomjit Ganguly (INSAID - www.insaid.co)")
#e5.grid(row=0, column = 3, columnspan=2, padx = 10, pady = 10)

e6 = Entry(root, width = 50, bg = "lightblue", fg = "red", borderwidth = 10)
e6.insert(1, "Mailto - sohomjit.ganguly@gmail.com")
#e6.grid(row=1, column = 3, columnspan=2, padx = 10, pady = 10)


    
submitButton = Button(root, text="SUBMIT", padx= 50, command = myClick, fg="blue", bg="lightblue")
submitButton.grid(row=3,  column = 0, columnspan=2, padx = 20, pady = 10)


quitButton = Button(root, text="QUIT", padx= 60, command = quit, fg="blue", bg="lightblue")
quitButton.grid(row=3,  column = 1, columnspan=2, padx = 20, pady = 10)

resetButton = Button(root, text="RESET", padx= 60, command = reset, fg="blue", bg="lightblue")
resetButton.grid(row=3,  column = 2, columnspan=2, padx = 20, pady = 10)

creditButton = Button(root, text="CREDIT", padx= 60, command = credit, fg="blue", bg="lightblue")
creditButton.grid(row=3,  column = 3, columnspan=2, padx = 20, pady = 10)


root.mainloop()
 
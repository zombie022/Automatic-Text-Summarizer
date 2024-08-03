# Core Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
import time
timestr=time.strftime("%Y%m%d-%H%M%S")

# NLP Pkgs
from text_summarization import text_summarizer
from nltk_summarization import nltk_summarizer

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen

#sumy packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
     
window = Tk()
window.title("Summarizer GUI")
window.geometry("1500x900")

#style
style = ttk.Style(window)

style.configure('lefttab.TNotebook', tabposition='wn')

# TABS 
tab_control = ttk.Notebook(window,style='lefttab.TNotebook')
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text=f'{"HOME":^50s}')
tab_control.add(tab2, text=f'{"FILE":^50s}')
tab_control.add(tab3, text=f'{"URL":^50s}')
tab_control.add(tab4, text=f'{"Comparer ":^50s}')
tab_control.add(tab5, text=f'{"ABOUT ":^50s}')

#LABELS
label1 = Label(tab1, text= 'SUMMARIZER',padx=5, pady=5,font=("Times New Roman", 15, "bold"))
label1.grid(column=0, row=0)
 
label2 = Label(tab2, text= 'FILE PROCESSING',padx=5, pady=5,font=("Times New Roman", 15, "bold"))
label2.grid(column=0, row=0)

label3 = Label(tab3, text= 'URL',padx=5, pady=5,font=("Times New Roman", 15, "bold"))
label3.grid(column=0, row=0)

label4 = Label(tab4, text= 'COMPARE  SUMMARIZER\'S',padx=5, pady=5,font=("Times New Roman", 15, "bold"))
label4.grid(column=0, row=0)

label5 = Label(tab5, text= 'ABOUT',padx=5, pady=5,font=("Times New Roman", 15, "bold"))
label5.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

# Functions
def get_summary():
	raw_text = entry.get('1.0',tk.END)
	final_text = nltk_summarizer(raw_text)
	print(final_text)
	result = '\nSummary:{}'.format(final_text)
	tab1_display.insert(tk.END,result)

def save_summary():
        raw_text = entry.get('1.0',tk.END)
        final_text = nltk_summarizer(raw_text)
        file_name='YourSummary'+timestr+'.txt'
        with open(file_name,'w') as f:
                f.write(final_text)
        result = '\n\nName of File: {} ,\nSummary:{}'.format(file_name,final_text)
        tab1_display.insert(tk.END,result)

def openfiles():
	file1 = tkinter.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1).read()
	displayed_file.insert(tk.END,read_text)


def get_file_summary():
	raw_text = displayed_file.get('1.0',tk.END)
	final_text = nltk_summarizer(raw_text)
	result = '\nSummary:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)

def get_text():
	raw_text = str(url_entry.get())
	page = urlopen(raw_text)
	soup = BeautifulSoup(page,"lxml")
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	url_display.insert(tk.END,fetched_text)

def get_url_summary():
	raw_text = url_display.get('1.0',tk.END)
	final_text = nltk_summarizer(raw_text)
	result = '\nSummary:{}'.format(final_text)
	tab3_display_text.insert(tk.END,result)
       
#sumy
def sumy_summary(docx):
        parser=PlaintextParser.from_string(docx,Tokenizer("english"))
        lex_summarizer=LexRankSummarizer()
        summary=lex_summarizer(parser.document,3)
        summary_list=[str(sentence) for sentence in summary]
        result=''.join(summary_list)
        return result

#clear function
def clear_text():
	entry.delete('1.0',END)
	
def clear_display_result():
	tab1_display.delete('1.0',END)
	
def clear_text_file():
	displayed_file.delete('1.0',END)

def clear_text_result():
	tab2_display_text.delete('1.0',END)
	
def clear_url_entry():
	url_entry.delete(0,END)
	
def clear_urltext_display():
	url_display.delete('1.0',END)

def clear_url_display():
	tab3_display_text.delete('1.0',END)


def clear_compare_text():
	entry1.delete('1.0',END)

def clear_compare_display_result():
	tab4_display.delete('1.0',END)

# COMPARER FUNCTIONS
def use_spacy():
	raw_text = entry1.get('1.0',tk.END)
	final_text = text_summarizer(raw_text)
	print(final_text)
	result = '\nSpacy Summary:{}\n'.format(final_text)
	tab4_display.insert(tk.END,result)

def use_nltk():
	raw_text = entry1.get('1.0',tk.END)
	final_text = nltk_summarizer(raw_text)
	print(final_text)
	result = '\nNLTK Summary:{}\n'.format(final_text)
	tab4_display.insert(tk.END,result)

def use_sumy():
	raw_text = str(entry1.get('1.0',tk.END))
	final_text = sumy_summary(raw_text)
	print(final_text)
	result = '\nSumy Summary:{}\n'.format(final_text)
	tab4_display.insert(tk.END,result)

#-------------------------------------------------------------------------------------------------------------------------
# MAIN HOME TAB
l1=Label(tab1,text="E N T E R   T E X T   T O   S U M M A R I Z E",padx=5,pady=5,font=("Times New Roman",12,"bold"))
l1.grid(row=1,column=0)
entry=ScrolledText(tab1,height=15,width=100)
entry.grid(row=2,column=0,columnspan=2,pady=5,padx=5)


# BUTTONS
button1=Button(tab1,text="RESET",command=clear_text,width=15,bg='cornflower blue',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab1,text="SUMMARIZE",command=get_summary, width=15,bg='green3',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab1,text="CLEAR RESULT", command=clear_display_result,width=15,bg='DarkOrange2',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab1,text="SAVE",command=save_summary, width=15,bg='red3',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button4.grid(row=5,column=1,padx=10,pady=10)

#display Screen for result
tab1_display=ScrolledText(tab1,height=15,width=100)
tab1_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)

#-------------------------------------------------------------------------------------------------------------------------
#FILE PROCESSING TAB
l1=Label(tab2,text="O P E N   F I L E   T O   S U M M A R I Z E",font=("Times New Roman",12,"bold"))
l1.grid(row=1,column=1)

displayed_file = ScrolledText(tab2,height=15,width=100)# Initial was Text(tab2)
displayed_file.grid(row=2,column=0, columnspan=3,padx=5,pady=3)

# BUTTONS FOR SECOND TAB/FILE READING TAB
b0=Button(tab2,text="OPEN FILE",command=openfiles,width=15,bg='cornflower blue',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
b0.grid(row=3,column=0)

b1=Button(tab2,text="RESET",command=clear_text_file,width=15,bg='cyan4',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
b1.grid(row=3,column=2,padx=10,pady=10)

b2=Button(tab2,text="SUMMARIZE",command=get_file_summary,width=15,bg='green3',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
b2.grid(row=3,column=1,padx=10,pady=10)

b3=Button(tab2,text="CLEAR RESULT",command=clear_text_result,width=15,bg='DarkOrange2',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
b3.grid(row=5,column=0)

b4=Button(tab2,text="CLOSE",command=window.destroy,width=15,bg='red3',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
b4.grid(row=5,column=2,padx=10,pady=10)

# Display Screen
tab2_display_text = ScrolledText(tab2,height=15,width=100)
tab2_display_text.grid(row=7,column=0, columnspan=3,padx=5,pady=3)

# Allows you to edit
tab2_display_text.config(state=NORMAL)

#-------------------------------------------------------------------------------------------------------------------------
# URL TAB
l1=Label(tab3,text="E N T E R   U R L   T O   S U M M A R I Z E",font=("Times New Roman",12,"bold"))
l1.grid(row=1,column=0)

raw_entry=StringVar()
url_entry=Entry(tab3,textvariable=raw_entry,width=50)
url_entry.grid(row=1,column=1)

# BUTTONS
button1=Button(tab3,text="RESET",command=clear_url_entry, width=15,bg='cornflower blue',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button1.grid(row=5,column=0,padx=10,pady=10)

button2=Button(tab3,text="GET TEXT",command=get_text, width=15,bg='burlywood3',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button2.grid(row=5,column=1,padx=10,pady=10)

button3=Button(tab3,text="CLEAR RESULT", command=clear_url_display,width=15,bg='DarkOrange2',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button3.grid(row=6,column=0,padx=10,pady=10)

button3=Button(tab3,text="CLEAR TEXT", command=clear_urltext_display,width=15,bg='red3',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button3.grid(row=6,column=2,padx=10,pady=10)

button4=Button(tab3,text="SUMMARIZE",command=get_url_summary, width=15,bg='green3',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button4.grid(row=5,column=2,padx=10,pady=10)

# Display Screen For Result
url_display = ScrolledText(tab3,height=15,width=100)
url_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)

tab3_display_text = ScrolledText(tab3,height=15,width=100)
tab3_display_text.grid(row=10,column=0, columnspan=3,padx=5,pady=5)

#-------------------------------------------------------------------------------------------------------------------------
# COMPARER TAB
l1=Label(tab4,text="E N T E R   T E X T   T O   S U M M A R I Z E",font=("Times New Roman",12,"bold"))
l1.grid(row=2,column=0)

entry1=ScrolledText(tab4,height=15,width=100)
entry1.grid(row=3,column=0,columnspan=3,padx=5,pady=3)

# BUTTONS
button1=Button(tab4,text="RESET",command=clear_compare_text, width=15,bg='cornflower blue',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab4,text="SPACY",command=use_spacy, width=15,bg='burlywood3',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab4,text="CLEAR RESULT", command=clear_compare_display_result,width=15,bg='DarkOrange2',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab4,text="NLTK",command=use_nltk,width=15,bg='green3',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button4.grid(row=4,column=2,padx=10,pady=10)

button4=Button(tab4,text="SUMY",command=use_sumy, width=15,bg='steelblue1',fg='#fff',height=2,font=("Times New Roman",10,"bold"),foreground='ghost white')
button4.grid(row=5,column=2,padx=10,pady=10)

# Display Screen For Result
tab4_display = ScrolledText(tab4,height=15,width=100)
tab4_display.grid(row=7,column=0, columnspan=3,padx=5,pady=3)

#-------------------------------------------------------------------------------------------------------------------------
# About TAB
about_label = Label(tab5,text="S U M M A R I Z E R   G U I",pady=5,padx=5,font=("Times New Roman",12,"bold"),anchor="center")
about_label.grid(column=0,row=2)

about_label = Label(tab5,text="A text summarizer is a tool that shortens long texts,like articles or documents,\ninto shorter summaries. It does this by finding the main points and key ideas in the text.\nThis helps people get the gist of the content quickly withoutreading the whole thing.\nText summarizers are handy for saving time and making information easier to understand.",pady=5,padx=5,font=("Times New Roman",15),anchor="center")
about_label.grid(column=0,row=3)

window.mainloop()
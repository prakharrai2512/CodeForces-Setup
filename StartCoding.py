import os
from datetime import date
import string
from shutil import copyfile
from bs4 import BeautifulSoup
import requests
import sys

from logging import root
from tkinter import Button, Checkbutton, Label, Tk, Variable,messagebox,StringVar,Entry


from requests.sessions import default_headers

win = Tk()
win.title("Setup CP")
win.after(1, lambda: win.focus_force())
contest_var= StringVar()


def makeSetup(something = 0):
    win.destroy()
    default_url = "https://codeforces.com/"

    today = date.today()
    d4 = today.strftime("%d %b %Y")

    cwd = os.getcwd()  

    # contest = sys.argv[1]
    # contest = "1551"
    contest = contest_var.get()

    folder_name =  contest + " " + d4
    tmplate_path = os.path.join(cwd, "Template.cpp") 
    path = os.path.join(cwd, folder_name) 
    new_path = path
    

    os.mkdir(path) 
    os.chdir(path)
    main_path = os.getcwd()  

    contestURL = default_url + "contest/" + contest

    html_text  =  requests.get(contestURL).text
    # print(html_text)
    soup = BeautifulSoup(html_text,features="html.parser")
    contest_table = soup.find('table',class_="problems")
    # print(contest_table)
    contest_problems = contest_table.find_all('td',class_="id")
    for problem in contest_problems:
        problem_number = problem.text.replace(' ','').replace('\n','').replace('\r','')
        problem_path = os.path.join(main_path,problem_number)
        
        # print(problem_path)
        os.mkdir(problem_path)
        os.chdir(problem_path)
        file_path = os.path.join(problem_path, problem_number + ".cpp") 
        inp_file = open("input.txt", "w")
        out_file = open("output.txt", "w")
        copyfile(tmplate_path, file_path)
        link = problem.a['href']
        link = default_url + link
        con_text  =  requests.get(link).text

        con_soup = BeautifulSoup(con_text,features="html.parser")
        inps = con_soup.find_all('div',class_="input")
        outs = con_soup.find_all('div',class_="output")
        for inp in inps:
            inp_file.write(inp.pre.text[1:])
            if len(inps) > 1:
                inp_file.write("\n\n*********************\n\n")
        for out in outs:
            out_file.write(out.pre.text[1:])
            if len(outs) > 1:
                out_file.write("\n\n*********************\n\n")

    os.system("code " +'"' +str(new_path) +'/"' )




MyWord = Label(win , text= "Enter Contest Number", font=("Arial Bold", 14))
MyWord.grid(row=1,column=1,padx= 12,pady=10)
cnts = Entry(win,textvariable = contest_var, font=('calibre',10,'normal'))
cnts.grid(row=2,column=1)
cnts.focus_set()
win.bind('<Return>', makeSetup)
SaveButton = Button(win, text= "Save" , command= makeSetup)
SaveButton.grid(row=3,column=1,pady=10)


win.mainloop()
import os
from bs4 import BeautifulSoup

from tkinter import *

root = Tk()

frame1 = Frame(root)
frame1.pack()

label1 = Label(frame1,text = "Starting roll number")
label1.grid(row = 0,column = 0)

label2 = Label(frame1,text = "Ending roll number")
label2.grid(row = 1,column = 0,sticky = E)

entry1 = Entry(frame1)
entry1.grid(row = 0,column = 1)

entry2 = Entry(frame1)
entry2.grid(row = 1,column = 1)

frame2 = Frame(root)
frame2.pack()



def values():
    i = 1
    starting_roll = int(entry1.get())
    ending_roll = int(entry2.get())
    number_of_values = ending_roll - starting_roll

    label_roll = Label(frame2,text = "Roll Number\t")
    label_roll.grid(row = 0, column = 0)

    label_roll = Label(frame2,text = "Name\t")
    label_roll.grid(row = 0, column = 1)

    label_roll = Label(frame2,text = "Branch\t")
    label_roll.grid(row = 0, column = 2)

    label_roll = Label(frame2,text = "SGPA\t")
    label_roll.grid(row = 0, column = 3)

    label_roll = Label(frame2,text = "Cumulative Grade Points\t")
    label_roll.grid(row = 0, column = 4)

    label_roll = Label(frame2,text = "CGPA\t")
    label_roll.grid(row = 0, column = 5)

    for x in range(starting_roll,ending_roll):
        roll = "ue" + str(x)
        sem = '6'

        os.system("""curl -k -X POST https://uwp.puchd.ac.in/common/viewmarks.aspx -d "__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKLTMzMTUyNjUzMA9kFgJmD2QWAgIDD2QWBAIBDw8WAh4EVGV4dAUKVmlldyBNYXJrc2RkAgMPZBYCAgEPZBYCAhUPZBYEAg8PPCsADQBkAhEPPCsADQBkGAMFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYGBSBjdGwwMCRtaWRkbGVDb250ZW50JFJhZGlvQnV0dG9uRwUhY3RsMDAkbWlkZGxlQ29udGVudCRSYWRpb0J1dHRvbk5HBSFjdGwwMCRtaWRkbGVDb250ZW50JFJhZGlvQnV0dG9uTkcFIGN0bDAwJG1pZGRsZUNvbnRlbnQkUmFkaW9CdXR0b24xBSBjdGwwMCRtaWRkbGVDb250ZW50JFJhZGlvQnV0dG9uMgUgY3RsMDAkbWlkZGxlQ29udGVudCRSYWRpb0J1dHRvbjIFHWN0bDAwJG1pZGRsZUNvbnRlbnQkR3JpZFZpZXcyD2dkBR1jdGwwMCRtaWRkbGVDb250ZW50JEdyaWRWaWV3MQ9nZO7cAGc2QXOLUQaauey%2Bl91SR1Yi&__VIEWSTATEGENERATOR=F368589A&__EVENTVALIDATION=%2FwEWFQKStte1AQLKm%2F%2FKDwKwzYbXDQKxzYbXDQKyzYbXDQKzzYbXDQK0zYbXDQK1zYbXDQK2zYbXDQKnzYbXDQKozYbXDQKwzcbUDQLgzbrJDQKyqe3pBgLdzbrJDQKs9fOJAQKJ27%2BqBwLtmLvJDAL2wcuTDwL2wb%2B3BgKSyNCHBunfT8LihqgqsAWHKGWvkBRdcf8n&ctl00%24middleContent%24TextBox1={}&ctl00%24middleContent%24DropDownList1={}&ctl00%24middleContent%24DropDownList2=BE&ctl00%24middleContent%24type=RadioButtonG&ctl00%24middleContent%24resulttype=RadioButton1&ctl00%24middleContent%24cmdsubmit=Show Marks" > response.txt""".format(roll,sem))

        html_code = open("response.txt")
        code = html_code.read()

        page_soup = BeautifulSoup(code.strip(),"html.parser")

        try:
            result = page_soup.findAll("span",{"id" : "ctl00_middleContent_Label7"})[0].text.split(',')
            name = page_soup.findAll('span',{'id' : 'ctl00_middleContent_Label3'})[0].text
            branch = page_soup.findAll('span',{'id' : 'ctl00_middleContent_Label1'})[0].text
            sgpa = result[0][7:]
            credits = result[1][29:]
            cgpa = result[2][8:]



            label_roll = Label(frame2,text = roll + '\t')
            label_roll.grid(row = i, column = 0,sticky = W)

            label_name = Label(frame2,text = name + '\t')
            label_name.grid(row = i,column = 1,sticky = W)

            label_branch = Label(frame2,text = branch + '\t')
            label_branch.grid(row = i ,column = 2,sticky = W)

            label_sgpa = Label(frame2,text = sgpa + '\t')
            label_sgpa.grid(row = i ,column = 3,sticky = W)

            label_credits = Label(frame2,text = credits + '\t')
            label_credits.grid(row = i ,column = 4,sticky = W)

            label_cgpa = Label(frame2,text = cgpa + '\t')
            label_cgpa.grid(row = i ,column = 5,sticky = W)

            i+=1


        except Exception as e:
            print(str(e))



        print('printing',roll)






search_btn = Button(frame1, text = "Search",command = values)
search_btn.grid(columnspan = 2)




root.mainloop()

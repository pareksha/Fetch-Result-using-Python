import os
from bs4 import BeautifulSoup
import csv

csv_file = open('result.csv','w')
headings = ['Roll Number','Name','Branch','SGPA','Cumulative Earned Credits','CGPA']
writer = csv.writer(csv_file)
writer.writerow(headings)

for i in {10,30,80,40,50,90}:
    start = int('14' + str(i) + '001')
    end =  int('14' + str(i) + '121')
    for x in range(start,end):
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

            writer.writerow([roll,name,branch,sgpa,credits,cgpa])


        except Exception as e:
            print(str(e))



        print('printing',roll)

csv_file.close()

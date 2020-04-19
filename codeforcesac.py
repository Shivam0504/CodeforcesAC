from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://codeforces.com/submissions/shivamkirti71/page/1'

client = uReq(url)
page = client.read()
client.close()

done = set()

page_soup = soup(page, "html.parser")
#submissions = page_soup.findAll("tr")
total_pages = page_soup.findAll("span",{"class":"page-index"})
lastpage = total_pages[len(total_pages)-1].a.text
print(lastpage)

for i in range (1,int(lastpage)+1):
    url2 = "https://codeforces.com/submissions/shivamkirti71/page/"+ str(i)
    client = uReq(url2)
    page = client.read()
    client.close()
    page_soup = soup(page, "html.parser")
    submissions = page_soup.findAll("tr")
    for submission in submissions:
        solution_verdict = submission.find("span",{"class":"verdict-accepted"})
    
        if(solution_verdict != None):
            problem = submission.find("a",{"class":"view-source"})
            problemid= problem.text
            print(problemid)
            problemlink= problem["href"]
            print(problemlink)
            clientx = uReq("https://codeforces.com"+problemlink)
            res = clientx.read()
            clientx.close()
            res_soup = soup(res, "html.parser")
            #print(res_soup)
            #table = res_soup.find("div","datatable")
            allTd = res_soup.findAll("td")
            #print(len(allTd[0].text))
            problem_name = "//"+allTd[2].a["title"]
            #print(problem_name)
            problem_code = allTd[2].a.text
            problem_link = "//https://codeforces.com"+allTd[2].a["href"]
            il = len(done)
            done.add(problem_code)
            nl = len(done)
            if(il != nl):
                code = res_soup.find("pre").text
                print(code)
                filename=str(problem_code)+".txt"
                f= open(filename,"w+")
                f.write(problem_name+"\n")
                f.write(problem_link+"\n")
                f.write(code)
                f.close()
    


        


    

#python codeforcesac.py
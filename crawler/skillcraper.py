import bs4 as bs

def getJobs():
    jobcont = []
    soup = bs.BeautifulSoup(open('jobs.html'),'lxml')
# soup = bs.BeautifulSoup('jobs.html','html.parser')
    jobs = soup.find_all('li')

    for job in jobs:
        id = job.get('value')
        text = job.get('data-job_name')
        jobdict = {
            'id' : id,
            'text' : text
        }
        jobcont.append(jobdict)
    

    return jobcont


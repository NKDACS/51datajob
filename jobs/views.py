from django.shortcuts import render
from .models import *
import datetime
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.decorators.cache import cache_page

# Create your views here.

def paginate(request,jobs):
    paginator = Paginator(jobs,5)
    page = request.GET.get('page')
    if page is None:
        page = '1'
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
        page = '1'
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
        page = str(paginator.num_pages)
    pageNums = [str(i) for i in range(1,paginator.num_pages+1)]
    return contacts,page,pageNums

links = Link.objects.filter(isPublish=True).order_by('orderID')
announce = Announcement.objects.filter(isPublish=True).order_by('orderID')

@cache_page(60*15)
def home(request):
    jobs = Job.objects.filter(isPublish=True).order_by('pubTime').reverse()
    contacts,page,pageNums = paginate(request,jobs)
    return render(request, 'jobs/home.html', {"jobs":contacts,"page":page,"pageNums":pageNums,"pageNum":len(pageNums),'head':'数据工作站',"friendLinks":links,"Announce":announce,})

@cache_page(60*15)
def company(request,href):
    jobCompanyName = Job.objects.filter(isPublish=True,id=int(href))[0].companyName
    jobs = Job.objects.filter(isPublish=True,companyName=jobCompanyName).order_by('pubTime').reverse()
    contacts,page,pageNums = paginate(request,jobs)
    return render(request, 'jobs/home.html', {"jobs":contacts,"page":page,"pageNums":pageNums,"pageNum":len(pageNums),"head":jobCompanyName,"friendLinks":links,"Announce":announce,})

@cache_page(60*15)
def internship(request):
    jobs = Job.objects.filter(isPublish=True,isPractice=True).order_by('pubTime').reverse()
    contacts,page,pageNums = paginate(request,jobs)
    return render(request, 'jobs/home.html', {"jobs":contacts,"page":page,"pageNums":pageNums,"pageNum":len(pageNums),"head":"实习","friendLinks":links,"Announce":announce,})

@cache_page(60*15)
def fulltime(request):
    jobs = Job.objects.filter(isPublish=True,isFullTime=True).order_by('pubTime').reverse()
    contacts,page,pageNums = paginate(request,jobs)
    return render(request, 'jobs/home.html', {"jobs":contacts,"page":page,"pageNums":pageNums,"pageNum":len(pageNums),"head":"全职","friendLinks":links,"Announce":announce,})

@cache_page(60*15)
def search(request):
    try:
        word = request.POST['word']
    except:
        word = request.GET.get('word')
    title = "搜索--" + word
    jobs = []
    jobs += list(Job.objects.filter(isPublish=True,companyName__contains=word))
    jobs += list(Job.objects.filter(isPublish=True,jobName__contains=word))
    jobs += list(Job.objects.filter(isPublish=True,jobInfo__contains=word))
    jobs += list(Job.objects.filter(isPublish=True,jobNeed__contains=word))
    jobs = list(set(jobs))
    jobs.sort(key=lambda x:x.pubTime,reverse=True)
    contacts,page,pageNums = paginate(request,jobs)
    return render(request, 'jobs/search.html', {"word":word,"jobs":contacts,"page":page,"pageNums":pageNums,"pageNum":len(pageNums),"head":title,"friendLinks":links,"Announce":announce,})

@cache_page(60*15)
def content(request,href):
    job = Job.objects.filter(isPublish=True,id=int(href))[0]
    jobNeeds = job.jobNeed
    jobNeedList = jobNeeds.split(';')
    return render(request, 'jobs/content.html', {"job":job,"jobNeedList":jobNeedList,"friendLinks":links,"Announce":announce,})

@cache_page(60*15)
def status(request):
    companyName = request.POST['companyName']
    jobName = request.POST['jobName']
    jobInfo = request.POST['jobInfo']
    jobNeed = request.POST['jobNeed']
    deadline = request.POST['deadline']
    date = deadline.split('-')
    deadline = datetime.date(int(date[0]),int(date[1]),int(date[2]))
    website = request.POST['website']
    contactEmail = request.POST['contactEmail']
    publisherEmail = request.POST['publisherEmail']
    try:
        isFullTime = request.POST['isFullTime']
        isFullTime = True
    except:
        isFullTime = False
    try:
        isPractice = request.POST['isPractice']
        isPractice = True
    except:
        isPractice = False
    Job.objects.create(companyName=companyName,jobName=jobName,jobInfo=jobInfo,jobNeed=jobNeed,deadline=deadline,website=website,contactEmail=contactEmail,publisherEmail=publisherEmail,isFullTime=isFullTime,isPractice=isPractice)
    return render(request, 'jobs/status.html', {"head":"提交招聘信息","status":"提交成功!请耐心等待审核!","friendLinks":links,"Announce":announce,})
    
@cache_page(60*15)
def meetingpoststatus(request):
    meetingName = request.POST['meetingName']
    startTime = request.POST['startTime']
    date =startTime.split('-')
    startTime = datetime.date(int(date[0]),int(date[1]),int(date[2]))
    endTime = request.POST['endTime']
    date = endTime.split('-')
    endTime = datetime.date(int(date[0]),int(date[1]),int(date[2]))
    place = request.POST['place']
    meetingInfo = request.POST['meetingInfo']
    website = request.POST['website']
    Meeting.objects.create(meetingName=meetingName,startTime=startTime,endTime=endTime,place=place,meetingInfo=meetingInfo,website=website)
    return render(request, 'jobs/status.html', {"head":"提交会议信息","status":"提交成功!请耐心等待审核!","friendLinks":links,"Announce":announce,})

@cache_page(60*15)
def meetingShow(request):
    meetings = Meeting.objects.filter(isPublish=True).order_by('startTime').reverse()
    contacts,page,pageNums = paginate(request,meetings)
    return render(request, 'jobs/meetings.html', {"jobs":contacts,"page":page,"pageNums":pageNums,"pageNum":len(pageNums),"friendLinks":links,"Announce":announce,})

@cache_page(60*15)
def meetingcontent(request,href):
    meeting = Meeting.objects.filter(isPublish=True,id=int(href))[0]
    return render(request, 'jobs/meetingcontent.html', {"meeting":meeting,"friendLinks":links,"Announce":announce,})

@cache_page(60*15)
def contestpoststatus(request):
    contestName = request.POST['contestName']
    contestInfo = request.POST['contestInfo']
    website = request.POST['website']
    Contest.objects.create(contestName=contestName,contestInfo=contestInfo,website=website)
    return render(request, 'jobs/status.html', {"head":"提交竞赛信息","status":"提交成功!请耐心等待审核!","friendLinks":links,"Announce":announce,})

@cache_page(60*15)
def contestShow(request):
    contests = Contest.objects.filter(isPublish=True).order_by('pubTime').reverse()
    contacts,page,pageNums = paginate(request,contests)
    return render(request, 'jobs/contests.html', {"jobs":contacts,"page":page,"pageNums":pageNums,"pageNum":len(pageNums),"friendLinks":links,"Announce":announce,})

@cache_page(60*15)
def contestcontent(request,href):
    contest = Contest.objects.filter(isPublish=True,id=int(href))[0]
    return render(request, 'jobs/contestcontent.html', {"contest":contest,"friendLinks":links,"Announce":announce,})

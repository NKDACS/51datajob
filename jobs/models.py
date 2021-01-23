from django.db import models

# Create your models here.
from django.db import models

class Job(models.Model):
    companyName = models.CharField(max_length=50,verbose_name="公司名称")
    jobName = models.CharField(max_length=50,verbose_name="职位名称")
    jobInfo = models.TextField(max_length=4000,verbose_name="职位介绍")
    jobNeed = models.TextField(max_length=4000,verbose_name="职位要求")
    pubTime = models.DateTimeField(auto_now=True,verbose_name="发布日期")
    deadline = models.DateField(verbose_name="截止日期")
    isFullTime = models.BooleanField(default=False,verbose_name="全职")
    isPractice = models.BooleanField(default=False,verbose_name="兼职")
    website = models.CharField(max_length=200,blank=True,null=True,verbose_name="网址")
    contactEmail = models.CharField(max_length=30,verbose_name="联系人邮箱")
    publisherEmail = models.CharField(max_length=30,verbose_name="发布人邮箱")
    isPublish = models.BooleanField(default=False,verbose_name="发布")

    def __str__(self):
        return self.companyName


class Meeting(models.Model):
    meetingName = models.CharField(max_length=50,verbose_name="会议名称")
    pubTime = models.DateTimeField(auto_now=True,verbose_name="发布日期")
    startTime = models.DateField(verbose_name="会议开始日期")
    endTime = models.DateField(verbose_name="会议结束日期")
    place = models.CharField(max_length=200,verbose_name="会议地点")
    meetingInfo = models.TextField(max_length=4000,verbose_name="会议信息")
    website = models.CharField(max_length=200,blank=True,null=True,verbose_name="会议网址")
    isPublish = models.BooleanField(default=False,verbose_name="发布")

    def __str__(self):
        return self.meetingName

class Contest(models.Model):
    contestName = models.CharField(max_length=50,verbose_name="竞赛名称")
    contestInfo = models.TextField(max_length=4000,verbose_name="竞赛简介")
    pubTime = models.DateTimeField(auto_now=True,verbose_name="发布日期")
    website = models.CharField(max_length=200,blank=True,null=True,verbose_name="网址")
    isPublish = models.BooleanField(default=False,verbose_name="发布")

    def __str__(self):
        return self.contestName

class Link(models.Model):
    linkName = models.CharField(max_length=20,verbose_name="链接标题")
    website = models.CharField(max_length=200,verbose_name="网址")
    orderID = models.IntegerField(verbose_name="顺序ID")
    isPublish = models.BooleanField(default=False,verbose_name="发布")

    def __str__(self):
        return self.linkName

class Announcement(models.Model):
    annTitle = models.CharField(max_length=20,verbose_name="公告标题")
    annInfo = models.TextField(max_length=1000,verbose_name="公告内容")
    annLink = models.CharField(blank=True,max_length=200,verbose_name="详情链接(若无请不填)")
    orderID = models.IntegerField(verbose_name="顺序ID")
    isPublish = models.BooleanField(default=False,verbose_name="发布")

    def __str__(self):
        return self.annTitle

from django.contrib import admin
from .models import *

# Register your models here

class JobsAdmin(admin.ModelAdmin):
    list_display = ('companyName','jobName','pubTime','deadline','contactEmail','isPublish')
    list_filter = ['companyName','jobName','isFullTime','isPractice','isPublish','deadline']
    list_per_page = 20
    search_fields = ['companyName','jobName','jobInfo','jobNeed']
    ordering = ['-pubTime']
    actions = ['make_published']

    def make_published(self,request,queryset):
        rows_updated = queryset.update(isPublish=True)
        if rows_updated == 1:
            message_bit = "1个job"
        else:
            message_bit = "%s个jobs" % rows_updated
        self.message_user(request, "成功发布了%s" % message_bit) 
    make_published.short_description = "发布所选的jobs"
    
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('meetingName','pubTime','isPublish')
    list_filter = ['meetingName','pubTime','isPublish']
    list_per_page = 20
    search_fields = ['meetingName','pubTime','isPublish']
    ordering = ['-pubTime']
    actions = ['make_published']

    def make_published(self,request,queryset):
        rows_updated = queryset.update(isPublish=True)
        if rows_updated == 1:
            message_bit = "1个meeting"
        else:
            message_bit = "%s个meetings" % rows_updated
        self.message_user(request, "成功发布了%s" % message_bit) 
    make_published.short_description = "发布所选的meetings"

class ContestAdmin(admin.ModelAdmin):
    list_display = ('contestName','pubTime','isPublish')
    list_filter = ['contestName','pubTime','isPublish']
    list_per_page = 20
    search_fields = ['contestName','pubTime','isPublish']
    ordering = ['-pubTime']
    actions = ['make_published']

    def make_published(self,request,queryset):
        rows_updated = queryset.update(isPublish=True)
        if rows_updated == 1:
            message_bit = "1个contest"
        else:
            message_bit = "%s个contests" % rows_updated
        self.message_user(request, "成功发布了%s" % message_bit)
    make_published.short_description = "发布所选的contests"

class LinkAdmin(admin.ModelAdmin):
    list_display = ('linkName','orderID','website','isPublish')
    list_per_page = 20
    actions = ['make_published']

    def make_published(self,request,queryset):
        rows_updated = queryset.update(isPublish=True)
        if rows_updated == 1:
            message_bit = "1个link"
        else:
            message_bit = "%s个links" % rows_updated
        self.message_user(request, "成功发布了%s" % message_bit) 
    make_published.short_description = "发布所选的meetings"

class AnnounceAdmin(admin.ModelAdmin):
    list_display = ('annTitle','annInfo','annLink','orderID','isPublish')
    list_per_page = 20
    actions = ['make_published']

    def make_published(self,request,queryset):
        rows_updated = queryset.update(isPublish=True)
        if rows_updated == 1:
            message_bit = "1个announcement"
        else:
            message_bit = "%s个announcements" % rows_updated
        self.message_user(request, "成功发布了%s" % message_bit) 
    make_published.short_description = "发布所选的announcements"



admin.site.register(Job,JobsAdmin)
admin.site.register(Meeting,MeetingAdmin)
admin.site.register(Link,LinkAdmin)
admin.site.register(Announcement,AnnounceAdmin)
admin.site.register(Contest,ContestAdmin)

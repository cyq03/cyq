# -*- coding:utf-8 -*-
import urllib
import urllib2
import re


for page in range(1,109):

    url = 'http://www.duwenzhang.com/wenzhang/aiqingwenzhang/list_1_'+str(page)+'.html'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

    content_pattern = re.compile('<table width="100%" border="0" cellspacing="0" cellpadding="0" class="tbspan" style="margin-top:6px">.*?<a href=".*?" class="ulink">(.*?)</a>', re.S)
    content_pattern2 = re.compile('<table width="100%" border="0" cellspacing="0" cellpadding="0" class="tbspan" style="margin-top:6px">.*?<td colspan="2" style="padding-left:3px">(.*?)</td>', re.S)


    content_list = re.findall(content_pattern, html)
    content_list2 = re.findall(content_pattern2, html)
    for item2 in content_list2:
        for item in content_list:
            print item
            del content_list[0]
            break
 
        print item2
        print '\n'
    input = raw_input()
    if input == "q":
        break

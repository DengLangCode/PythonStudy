# encoding:utf-8
import urllib2
import re

def DownloadFromUrl(searchname):
    url = "https://search.51job.com/list/090200,000000,0000,00,9,99,"+searchname+",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    response = urllib2.urlopen(url)
    html = response.read()
#    print(html)
    restr = """<div class="rt">([\s\S]*?)</div>"""
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(html)
    mystr = mylist[0].strip()
    restr = "(\\d+)"
    regex = re.compile(restr, re.IGNORECASE)
    mylist1 = regex.findall(mystr)
    if len(mylist1):
        return mylist1[0]
    else:
        return "失败"
    pass
print(DownloadFromUrl("python"))


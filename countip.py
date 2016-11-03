# -*- coding: utf-8 -*-
import re
import sys, os, urllib2, json
import argparse

def get_ip_area(ip):  
    try:  
        apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" %ip  
        request = urllib2.urlopen(apiurl)
        content = request.read()  
        data = json.loads(content)['data']  
        code = json.loads(content)['code']  
        if code == 0:   # success  
            #print(data['country_id']+' '+data['area']+' '+data['city']+' '+data['region'])
            #rt = data['country']+' '+data['area']+' '+data['city']+' '+data['region']+' '+data['isp']
            rt =' '.join((data['country'],data['area'],data['city'],data['region'],data['isp']))
            if rt.strip() == '':
                rt = '解析地理位置失败'
        else:  
            rt = '未知'
        request.close()
        return rt
    except Exception as ex:
        if request:
            request.close()
        print(ex)

def main(argv):
    parser = argparse.ArgumentParser(description='统计ip访问次数及解析地理位置')
    parser.add_argument('-d','--day',dest='day',action='store',help='eg: 2016-10-13',default='')
    parser.add_argument('-f','--file',dest='file',action='store',help='被统计文件',default='C:\\Users\\ZYR\\Desktop\\bbs_ws.txt')
    global args
    args = parser.parse_args(argv[1:])
    f=open(args.file,"r")
    arr={}
    ipaddress=re.compile(r'^\[INFO\]\s{1}\S+\s{1}\S+\s{1}(.*)={3}$')
    if args.day!='':
        ipaddress=re.compile(r'^\[INFO\]\s{1}\['+args.day+'\s{1}\S+\s{1}(.*)={3}$')
        
    lines = f.readlines()
    for line in lines:
        line = line.decode('utf-8','ignore')
        #print line
        #ipaddress=re.compile(r'^\[INFO\]\s{1}\S+\s{1}\S+\s{1}(.*)={3}$')
        #ipaddress=re.compile(r'^\[INFO\]\s{1}\['+args.day+'\s{1}\S+\s{1}(.*)={3}$')
        match=ipaddress.match(line)
        if match:
            print line
            ip = match.group(1) 
            if(arr.has_key(ip)): 
                arr[ip]+=1
            else: 
                arr.setdefault(ip,1)
    f.close()
    total=0
    print '====独立ip->访问次数===='
    for key,value in arr.items():
        print ''.join((key,'-->',get_ip_area(key),'-->',str(value)))
        total=total+arr[key]

    print '\n====总访问次数===='
    print total

if __name__ == '__main__':
    argv = sys.argv
    main(argv)

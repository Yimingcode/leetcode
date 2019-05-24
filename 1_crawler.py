import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
print(response.getcode())

cont = response.read()
print(len(cont))

# methond 2

url = 'http://www.baidu.com'
request = urllib.request.Request(url)

request.add_header('User-Agent','Mozilla/5.0')

response2 = urllib.request.urlopen(request)
print(response2.getcode())

print(len(response2.read()))

# method 3
import urllib
import http.cookiejar
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())

# print ("Content-type:text/html")
# print ()                             # 空行，告诉服务器结束头部
# print ('<html>')
# print ('<head>')
# print ('<meta charset="utf-8">')
# print ('<title>Hello Word - 我的第一个 CGI 程序！</title>')
# print ('</head>')
# print ('<body>')
# print ('<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>')
# print ('</body>')
# print ('</html>')
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='123123'
# )
# print(mydb)
# # mycursor = mydb.cursor()
# #
# # mycursor.execute('CREATE DATABASE runoob_db')


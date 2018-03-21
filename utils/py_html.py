# encoding: utf-8

#import os

titles = '接口测试'


def title(titles):
    title = '''
    <!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>%s</title>
		<style type="text/css">
			td{ width:40px; height:50px;}
		</style>
	</head>
	<body>
	''' % (titles)
    return title


content = '''
<div style='width: 1170px;margin-left: 15%'>
<h1>接口测试的结果</h1>'''


def time(starttime, endtime, passge, fail):
    test_time = '''
		<p><strong>开始时间:</strong> %s</p>
		<p><strong>结束时间:</strong> %s</p>
		<p><strong>耗时:</strong> %s</p>
		<p><strong>结果:</strong>
			<span >Pass: <strong >%s</strong>
			Fail: <strong >%s</strong>
			        </span></p>                  
			    <p ><strong>测试详情如下</strong></p>  </div> ''' % (starttime, endtime, (endtime - starttime), passge, fail)
    return shanghai


shanghai = '''


        <p>&nbsp;</p>
        <table border='2'cellspacing='1' cellpadding='1' width='1100'align="center" >
		<tr >
            <td ><strong>用例ID&nbsp;</strong></td>
            <td><strong>用例名字</strong></td>
            <td><strong>key</strong></td>
            <td><strong>请求内容</strong></td>
            <td><strong>url</strong></td>
            <td><strong>请求方式</strong></td>
            <td><strong>预期</strong></td>
            <td><strong>实际返回</strong></td>  
            <td><strong>结果</strong></td>
        </tr>
    '''


def passfail(tend):
    if tend == 'pass':
        htl = ' <td bgcolor="green">pass</td>'
    elif tend == 'fail':
        htl = ' <td bgcolor="gray">fail</td>'
    else:
        htl = '<td bgcolor="red">error</td>'
    return htl


def test_detail(id, name, key, contents, url, meth, exception, json, results):
    xiangqing = '''
        <tr>
            <td>%s</td>
            <td>%s</td>
       
            <td>%s</td>
            <td>%s
           </td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            %s
        </tr>
        
    ''' % (id, name, key, contents, url, meth, exception, json, passfail(results))
    return xiangqing


end = '''
	</table>
    </body>
    </html>
    '''


def result(t_title, starttime, endtime, passge, fail, id, name, key, contents, url, meth, exception, json, result):
    if type(name) == list:
        relus = ' '
        for i in range(len(name)):
            relus += (
                test_detail(id[i], name[i], key[i], contents[i], url[i], meth[i], exception[i], json[i], result[i]))
        text = title(t_title) + contents + time(starttime, endtime, passge, fail) + shanghai + relus + end
    else:
        text = title(t_title) + contents + time(starttime, endtime, passge, fail) + shanghai + test_detail(id, name, key,
                                                                                                         content, url,
                                                                                                         meth,
                                                                                                         exception,
                                                                                                         json,
                                                                                                         result) + end
    return text


def createHtml(filepath, test_title, starttime, endtime, passge, fail, id, name, key, content, url, meth, exception, json,
               results):
    texts = result(test_title, starttime, endtime, passge, fail, id, name, key, content, url, meth, exception, json,
                   results)
    with open(filepath, 'wb') as f:
        f.write(texts.encode())

# encoding: utf-8

from log import logger


@logger('保存测试结果')
def save_result(test_time, total, pass_num, fail):
    try:
        f = open('result.txt', 'a')
        f.write("%s=%s=%s=%s \n" % (test_time, total, pass_num, fail))
        f.close()
    except:
        logger.info('保存测试结果出错，原因：%s' % Exception)
        print('记录测试结果失败')

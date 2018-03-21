# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import cx_Oracle


class cxOracle:
    def __init__(self):
        self._conn = None
        self.conn = self.Connect()

    def Connect(self):
        if not self._conn:
            # 用户名/密码@数据库地址:数据库端口/SID
            self._conn = cx_Oracle.connect("c##src_qa/sr2018qa@//192.168.110.165:1521/orcl")
            return self._conn

    def _NewCursor(self):
        """操作游标"""
        cur = self._conn.cursor()
        if cur:
            return cur
        else:
            print "#Error# Get New Cursor Failed."
            return None

    def _DelCursor(self, cur):
        if cur:
            cur.close()

    def Query(self, sql, nStart=0, nNum=-1):
        """查询"""
        rt = []
        # 获取cursor
        cur = self._NewCursor()
        if not cur:
            return rt
        # 查询到列表
        cur.execute(sql)
        if (nStart == 0) and (nNum == 1):
            rt.append(cur.fetchone())
        else:
            rs = cur.fetchall()
            if nNum == - 1:
                rt.extend(rs[nStart:])
            else:
                rt.extend(rs[nStart:nStart + nNum])
        # 释放cursor
        self._DelCursor(cur)
        print rt
        # self._printResult(rt)
        return rt

    def Exec(self, sql):
        """执行"""
        # 获取cursor
        rt = None
        cur = self._NewCursor()
        if not cur:
            return rt
        # 执行语句
        rt = cur.execute(sql)
        self.conn.commit()
        # 释放cursor
        self._DelCursor(cur)
        return rt


class PayOrder:
    def __init__(self, mainId):
        self.mainId = mainId
        self.cxora = cxOracle()
        self.business_id = self._getBizId

    @property
    def _getBizId(self):
        """获取业务ID"""
        sql = "select t.business_id from tbl_src_biz_main_order t where t.main_order_id = %s" % self.mainId
        result = self.cxora.Query(sql)
        return result[0][0]

    def _queryValues(self):
        """查询表字段值"""
        sql = "select t.status from tbl_main_order_info t where t.main_orderid = %s" % self.mainId
        self.cxora.Query(sql)

        sql = "select t.status from tbl_src_biz t where t.id = %s" % self.business_id
        self.cxora.Query(sql)

        sql = "select t.status from tbl_order_info t where (t.order_type = 1 or t.order_type = 2) and t.main_orderid = %s" % self.mainId
        self.cxora.Query(sql)

        sql = "select t.status from tbl_pay_order_info t where t.main_orderid = %s" % self.mainId
        self.cxora.Query(sql)

    def payorder(self):
        self._queryValues()
        print '\\===============================================================================\\'
        sql = "update tbl_main_order_info t set t.status = 2 where t.main_orderid = %s" % self.mainId
        self.cxora.Exec(sql)
        sql = "update tbl_src_biz t set t.status = 5 where t.id = %s" % self.business_id
        self.cxora.Exec(sql)
        # sql = "update tbl_order_info t set t.status = 2 where (t.order_type = 1 or t.order_type = 2) and " \
        #       "t.main_orderid = %s" %self.mainId
        # self.cxora.Exec(sql)
        sql = "update tbl_pay_order_info t set t.status = 2 where t.main_orderid = %s" % self.mainId
        self.cxora.Exec(sql)
        self._queryValues()
        print '\\===============================================================================\\'


if __name__ == '__main__':
    pay_order = PayOrder('201705040000020093')
    pay_order.payorder()

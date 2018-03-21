#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
'''
There are some interface request data.
'''

import time
import pickle



class RequestData:

    def __init__(self):
        pass

    # 异步数据准备
    @staticmethod
    def asyncPrepareDataScheme(**updateScheme):
        #每次测试只需要更改serviceCode的值就能保证不会与上一次的测试数据重复
        reqDict = {'serviceCode': updateScheme.get('serviceCode', '01'), 'sn': updateScheme.get('sn', '0001'),
                   'moc': updateScheme.get('moc', '90800960A7F716C6B4'), 'amount': updateScheme.get('amount', 50),
                   'token': updateScheme.get('token',
                                             '1612120A00002E090102075A90800960A7F716C6B4905AD5C4D50F2C82170FFC5B7713B2C7D23E9AB1A3F06DD3AC7654112D93EBA7DE4B54AF309BF3F62C75DBBEC6DA4FFD2637D8E36AF1CC60E967CE400BE7CC9D7D91331C'),
                   'personalData': updateScheme.get('personalData',
                                                    '8407A8E87FBDD6F37F37CDE4B595D8A0205AB2A36E38685BEC23AB24C9C0258A1AE4095BA60EA1E96206697F2186059AFA1415C6CD3C6B32A8511E4CEF5444A7D66F7A703B86FEA49DC83966713AC51AD88E0A64C28536190AB1ACA8D71B98CF944C0D87164E027551AF79B16202CFA5F670C8942E6F33203AAA2F2F3CDBFD7C046F790F1F1989CF1646ABB1DA1C5F2C86C7478F6FD186B47B92ACBAF5DB69F55CBEF47B1395AC6A73A27C053D9D42DA4DC4176523A66923998893A7B2E4DD81243C1F2DD6E40CDD808FB09356360CBD36E31AD93DE840304BDB02DD7DBB05861136B4F47AB49067F9F62E5DFFF519DCDA8A20DFB97A17D045240916ABD634C757E8318F64989E623A5D181C907E8D5FD852F94DA97C315047316509A12D30306963E1D09A606C40C3601856D028F76FC695A42C216FCEFD2869315AD9897E6BCE89E0CB70027D9ABDC2F07C2890167537F99D62E91988A2738F0A117825285F87995AC8B77CF14CF29C4FEA697112E004582A6144E8DB8C3700B1E09F4CC343EBFA529B91C30314740AEDB274AC65C2A6A328DE0EEE94F2176703C6ACD4DA6371815A68F318E74E1116CF0AB46FB0CB98B3945C0D527E8DD39E3AFC84DC76DF66DBB0EC4ACB6B65A6077B060FEABCB9AEA75A38A3E14BE4AEC32FC6BF107ED7445DD8D3FE72D9922D97227BDBA8BC220D0E44BF9572FC31C79D9B7AA97AF2AEEA52BD2E72C4C8FE5AAEA0310A0013F6449D1EBDC7D491AEC7CE258874419BF28BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD09418A66BAAB38FBF7599AE70AC32BA00888BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0941CC9DB7BBAAF66468BAF473F2F8FD094612525A2DC565F2518980B538864589B8BAF473F2F8FD0948BAF473F2F8FD094F898739EAF54E89193069DD0FC2B2B678BAF473F2F8FD0944BA61EDE6DE871558BAF473F2F8FD0945577B18E69FCF4638BAF473F2F8FD0948BAF473F2F8FD094BD1B525A6D350C9B8BAF473F2F8FD094DA7DDA98F80F0EE58BAF473F2F8FD0944E72EF898BFAD019B195D80FB3026674FA9526824FC6A6114EDADCAAD60E8BE522B018021ABE7FAA5EF296A2B1D1115E23ADA5FB74D3BBD4CDE51C38870CF3605558D91AD5A40CE74C038D271FE8481394714285AED7F152C3667F86749B3982DED96EF50706B65E'),
                   'issueFee': updateScheme.get('issueFee', 30)}
        request_no = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

        f = open('pickle_tmp.dat','wb')

        pickle.dump(request_no,f)
        f.close()

        #reqDict['valiDate'] = updateScheme.get('valiDate','')#交通卡有效期，格式YYYYMMDD
        #reqDict['notifyTarget'] = updateScheme.get('notifyTarget','')#制卡数据完成通知

        return reqDict


    #查询数据准备结果

    def queryPrepareDataResultScheme(**self):
        reqDict = {'serviceCode': self.get('serviceCode', '012'), 'sn': self.get('sn', '0011')}

        #reqDict['taskId'] = updateScheme.get('taskId','')
        return reqDict

    # 查询产品信息列表

    @staticmethod
    def GetProductInformationListScheme(**update):
        reqDict = {'xmTransTime': update.get('xmTransTime', '14630445646485'),
                   'xmTransNum': update.get('xmTransNum', '123456789123'),
                   'extra': update.get('extra', '')
                   }

        return reqDict

    # 查询资金账户

    @staticmethod
    def GetPrepaymentListScheme(**update):
        reqDict = {'xmTransTime': update.get('xmTransTime', '14630445646485'),
                   'xmTransNum': update.get('xmTransNum', '123456789123'),
                   'extra': update.get('extra', '')
                   }

        return reqDict

    # 查询租赁业务列表
    @staticmethod
    def GetBusinessInformationListScheme(**update):
        reqDict = {
            'deviceInfo': update.get('deviceInfo', {'seId':'23050102030409','deviceType':'4D492035','deviceId':'987654321','accountId':'112233445566','cplc':'1234567899'}),
            'xmTransTime': update.get('xmTransTime', '14630445646485'),
            'xmTransNum': update.get('xmTransNum', '123456789123'),
            'extra': update.get('extra', '')
        }

        return reqDict

    # 查询租赁业务详细信息
    @staticmethod
    def GetBusinessDetailedInformationScheme(**update):
        reqDict = {'deviceInfo': update.get('deviceInfo', {'seId':'23050102030409','deviceType':'4D492035','deviceId':'987654321','accountId':'112233445566','cplc':'1234567899'}),
                   'SRCBusinessCode': update.get('SRCBusinessCode', '3031323332'),
                   'xmTransTime': update.get('xmTransTime', '14630445646485'),
                   'xmTransNum': update.get('xmTransNum', '123456789123'),
                   'extra': update.get('extra', '')
                   }

        return reqDict


    # 业务申请
    @staticmethod
    def ApplyPendingBusinessScheme(**update):
        reqDict = {'deviceInfo': update.get('deviceInfo',{'seId':'23050102030409','deviceType':'4D692D35','deviceId':'987654321','accountId':'112233445566','cplc':'1234567899'}),
                   'ssdInfo': update.get('ssdInfo',{'instanceAid':'A000000003869807012000','cityId':'2000','sdAid':'A000000003464D53485453FF','casdCertificate':'7f2181f17f2181ed931004401d1b6638800160210578979374714207637093010000175f2001009501825f24042115063045010053087ecc3e470923d52a5f378190690eb88b25fae69f2e3735a3c6349517f318a274213ee9a2998a7ad621aeefa80f1cf9288d40c3b41fdfa9f4a2f5046244c0d616ca67def04577ecaaf8798c85d0ed12f5470e8590cd8810d6bc1fc3e3f2138bf01cb2cab61eb37daf5f2d00cf699ab2bbe649357c83317851d2193648459cf0f34c353829ca4d7f2dfdca551775cab9ada193dc5077d33ce3d90d8c2c5f38208f56ba8efc8fb45ad8f8468e5fad1498ccf2b2fcd9f423eb413a774d608a4f85','cipheredRgk':'907C14A1CDA61EA6CED411DFA90686B355C2FF665195742C6CFE8EB48883E6D35558EA71BFB43E3E089F959316B0F316AF91BD08C91E19E89A5CCA1A6E723BC168B7BC10A7160BFF3C519B8973F11E1415E9949CEF07E041F85A69FFDF59B0D4FE9426FE58E21F8E7A90BA3B83D73FB761AC57F48507390C5B5408BA3688B163AB11D95C8471E91A7F181F45858DADD39638914DF3009AD22F9ABD1F01B2B395AB8D4D39A8C400E65D1B2DCF93421132759F42B92CC7197ABF966E6A21E76A62374C92234C1A95FE87C9','counter':'0000'}),
                   'authenticationCode': update.get('authenticationCode','03000001007001292000552305010203040927044D492035850CA000000003464D534854534D2409A0000000038698070191040100057A510E5352435F534354435F303030303155011089030020001101810905000000000199051605251375002588e4f74eb82ab1e7b411b3492024c435a4262d31c86154d45392211053add9cdceb85ed3f47dc881abee018e77b1a73b455da84c3369d6771cb8689882df0e100b6e0ac5ff19973591c82cb631b27bca4d7c75f7bfb40aab60edbb9c2bcdc2425c695b55088b9452567f6a1970c08a49223a4220c7517da3e3d0126394b27fe339dd1ac24218a52bc1335cf47cb979b7984bc3a6cea8c21b0eec654219936e916e4255a366f34fc8ff2d2b67dd23087b6cc4e91690bf14d8f8d3fdc6f9c3f6f3725b1780ed0e299e1162050d4ab69f62d85b474759d7fbbf951d3691781ebeaab57599354f03c312b7988975782e4241d0f66fb51c883457d4482a112de3cf'),
                   'xmTransTime': update.get('xmTransTime','1463044564648'),
                   'xmTransNum': update.get('xmTransNum','123456789123'),
                   'extra': update.get('extra','')
                   }

        return reqDict
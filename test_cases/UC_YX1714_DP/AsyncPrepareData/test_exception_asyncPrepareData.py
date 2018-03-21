#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import logging,json

from public.dp_http_handle import IRequest
from other_ways.data import RequestData


class AsyncPrepareDataExceptionsTestCase(IRequest,RequestData):

    def test_exception_asyncPrepareData_null_01(self):
        requestJsonDict = self.asyncPrepareDataScheme()

        requestJsonDict.pop('serviceCode')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_null_02(self):
        requestJsonDict = self.asyncPrepareDataScheme()

        requestJsonDict.pop('sn')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_null_03(self):
        requestJsonDict = self.asyncPrepareDataScheme()

        requestJsonDict.pop('moc')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s', response)

        r = response.content

        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_null_04(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0016')

        requestJsonDict.pop('amount')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_null_05(self):
        requestJsonDict = self.asyncPrepareDataScheme()

        requestJsonDict.pop('token')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_null_06(self):
        requestJsonDict = self.asyncPrepareDataScheme()

        requestJsonDict.pop('personalData')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_null_07(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0017')

        requestJsonDict.pop('issueFee')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_type_change_01(self):
        requestJsonDict = self.asyncPrepareDataScheme(serviceCode=-1)

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_type_change_02(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn=-1)

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_type_change_03(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0006',moc=-1)

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_type_change_04(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0007',personalData=123456789123456789123456789123456789123456789)

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_type_change_05(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='000',token=123456489)

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_type_change_06(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0010',amount='500')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_type_change_07(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0012',issueFee='300')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_length_illegal_01(self):
        requestJsonDict = self.asyncPrepareDataScheme(serviceCode='1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_length_illegal_02(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_length_illegal_03(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0013',moc='90800960A7F716C6B4ASDFGHJKLZXCVBN123456789')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_length_illegal_04(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0014',personaData='8407A8E87FBDD6F37F37CDE4B595D8A0205AB2A36E38685BEC23AB24C9C0258A1AE4095BA60EA1E96206697F2186059AFA1415C6CD3C6B32A8511E4CEF5444A7D66F7A703B86FEA49DC83966713AC51AD88E0A64C28536190AB1ACA8D71B98CF944C0D87164E027551AF79B16202CFA5F670C8942E6F33203AAA2F2F3CDBFD7C046F790F1F1989CF1646ABB1DA1C5F2C86C7478F6FD186B47B92ACBAF5DB69F55CBEF47B1395AC6A73A27C053D9D42DA4DC4176523A66923998893A7B2E4DD81243C1F2DD6E40CDD808FB09356360CBD36E31AD93DE840304BDB02DD7DBB05861136B4F47AB49067F9F62E5DFFF519DCDA8A20DFB97A17D045240916ABD634C757E8318F64989E623A5D181C907E8D5FD852F94DA97C315047316509A12D30306963E1D09A606C40C3601856D028F76FC695A42C216FCEFD2869315AD9897E6BCE89E0CB70027D9ABDC2F07C2890167537F99D62E91988A2738F0A117825285F87995AC8B77CF14CF29C4FEA697112E004582A6144E8DB8C3700B1E09F4CC343EBFA529B91C30314740AEDB274AC65C2A6A328DE0EEE94F2176703C6ACD4DA6371815A68F318E74E1116CF0AB46FB0CB98B3945C0D527E8DD39E3AFC84DC76DF66DBB0EC4ACB6B6jhjhjhjhjhjhjhjhjhjhjhgjkfyfyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyccc'
                                                                            'jkjkjkjkjkjkjkjkjkjkjkjkjjjjkkkkkkkkkkkkj5A6077B060FEABCB9AEA75A38A3E14BE4AEC32FC6BF107ED7445DD8D3FE72D9922D97227BDBA8BC220D0E44BF9572FC31C79D9B7AA97AF2AEEA52BD2E72C4C8FE5AAEA0310A0013F6449D1EBDC7D491AEC7CE258874419BF28BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD09418A66BAAB38FBF7599AE70AC32BA00888BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0941CC9DB7BBAAF66468BAF473F2F8FD094612525A2DC565F2518980B538864589B8BAF473F2F8FD0948BAF473F2F8FD094F898739EAF54E89193069DD0FC2B2B678BAF473F2F8FD0944BA61EDE6DE871558BAF473F2F8FD0945577B18E69FCF4638BAF473F2F8FD0948BAF473F2F8FD094BD1B525A6D350C9B8BAF473F2F8FD094DA7DDA98F80F0EE58BAF473F2F8FD0944E72EF898BFAD019B195D80FB3026674FA9526824FC6A6114EDADCAAD60E8BE522B018021ABE7FAA5EF296A2B1D1115E23ADA5FB74D3BBD4CDE51C38870CF3605558D91AD5A40CE74C038D271FE8481394714285AED7F152C3667F86749B3982DED96EF50706B65ESSSSSSSSSSSSSSSFDFFFFFFFFFFFFFFFFFFFSSDFDDDDDDDDDDD'
                                                                            '8407A8E87FBDD6F37F37CDE4B595D8A0205AB2A36E38685BEC23AB24C9C0258A1AE4095BA60EA1E96206697F2186059AFA1415C6CD3C6B32A8511E4CEF5444A7D66F7A703B86FEA49DC83966713AC51AD88E0A64C28536190AB1ACA8D71B98CF944C0D87164E027551AF79B16202CFA5F670C8942E6F33203AAA2F2F3CDBFD7C046F790F1F1989CF1646ABB1DA1C5F2C86C7478F6FD186B47B92ACBAF5DB69F55CBEF47B1395AC6A73A27C053D9D42DA4DC4176523A66923998893A7B2E4DD81243C1F2DD6E40CDD808FB09356360CBD36E31AD93DE840304BDB02DD7DBB05861136B4F47AB49067F9F62E5DFFF519DCDA8A20DFB97A17D045240916ABD634C757E8318F64989E623A5D181C907E8D5FD852F94DA97C315047316509A12D30306963E1D09A606C40C3601856D028F76FC695A42C216FCEFD2869315AD9897E6BCE89E0CB70027D9ABDC2F07C2890167537F99D62E91988A2738F0A117825285F87995AC8B77CF14CF29C4FEA697112E004582A6144E8DB8C3700B1E09F4CC343EBFA529B91C30314740AEDB274AC65C2A6A328DE0EEE94F2176703C6ACD4DA6371815A68F318E74E1116CF0AB46FB0CB98B3945C0D527E8DD39E3AFC84DC76DF66DBB0EC4ACB6B6jhjhjhjhjhjhjhjhjhjhjhgjkfyfyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyccc'
                                                                            'jkjkjkjkjkjkjkjkjkjkjkjkjjjjkkkkkkkkkkkkj5A6077B060FEABCB9AEA75A38A3E14BE4AEC32FC6BF107ED7445DD8D3FE72D9922D97227BDBA8BC220D0E44BF9572FC31C79D9B7AA97AF2AEEA52BD2E72C4C8FE5AAEA0310A0013F6449D1EBDC7D491AEC7CE258874419BF28BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD09418A66BAAB38FBF7599AE70AC32BA00888BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0941CC9DB7BBAAF66468BAF473F2F8FD094612525A2DC565F2518980B538864589B8BAF473F2F8FD0948BAF473F2F8FD094F898739EAF54E89193069DD0FC2B2B678BAF473F2F8FD0944BA61EDE6DE871558BAF473F2F8FD0945577B18E69FCF4638BAF473F2F8FD0948BAF473F2F8FD094BD1B525A6D350C9B8BAF473F2F8FD094DA7DDA98F80F0EE58BAF473F2F8FD0944E72EF898BFAD019B195D80FB3026674FA9526824FC6A6114EDADCAAD60E8BE522B018021ABE7FAA5EF296A2B1D1115E23ADA5FB74D3BBD4CDE51C38870CF3605558D91AD5A40CE74C038D271FE8481394714285AED7F152C3667F86749B3982DED96EF50706B65ESSSSSSSSSSSSSSSFDFFFFFFFFFFFFFFFFFFFSSDFDDDDDDDDDDD'
                                                                            'DFGFDGDRRRRRRRRRFDDDDFGGGGGGGGGGGGGGGGGGGGGDFGFDGDRRRRRRRRRFDDDDFGGGGGGGGGGGGGGGGGGGGGGGGGGGGDDDDDDDDDDDDGGGGGGRDFGGGGFTFJHDGJHSGFSDJFJSDFJBESBJDFSYDFSEJHGBSJBDGJBSDBSBDJSBGJDBGJBSJHBFGGSBDGJSDBJHSDBHDHSDBFSHBFERWSBJDJBFJEBJSBDFBSDBGMDSGDSDBSDBGSGBSBDVSDBVBSDJBVJKBJFBSBGSDSBDVSDBVSBVJBSDJVBJKDSBJKBDSKVBJKSBDVJKSBDVSBDVJKBJKSBJKBGJBEJKBSJKDBJKSBDVKBSDVBKSJDVBSJKDBVSDBVJKSDBJKVBDSJVBJSBDVJKSDBVJBSDVBDSBVJDSBVJDBSJVBKSBDVBSJKDVBJKSDBVJHSBJVBJHSDJDBVJSBVJBSJVBJSBDVJDBJVBSBVJBSDJVBSJVBJDBVJBSDJVBSJDBJSBDVJBJSDBVJBSDJBJBSJDBVJSDBVJS')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_length_illegal_05(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0015',token='1612120A00002E090102075A90800960A7F716C6B4905AD5C4D50F2C82170FFC5B7713B2C7D23E9AB1A3F06DD3AC7654112D93EBA7DE4B54AF309BF3F62C75DBBEC6DA4FFD2637D8E36AF1CC60E967CE400BE7CC9D7D91331CJFGSDFJSDBSDJBFUYBYBSDFUEYBJSBJHBSJDFBUYAGUYVBDVJHBEJHVUSVGSUYBVJHSBVUYBSJHBDUGVBJBUJZXVBSDJVBUYBEJBJSDBVUJSDBJVBSJDVBSUYBVUYSBJBEYSDUBFSDBJSBUVBSHSSDJBVDUVBSUYVBUYSBVUYSBSUYUYSUDVBBJSDBSBDVBJBSDJVBSJBYBFJSBDFUSYYSVY')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_length_illegal_06(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0016',amount=10000000000000000000000)

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_length_illegal_07(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0017',issueFee='100000000000000000000000000000000000000000000000000000000')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_illegal_chars_01(self):
        requestJsonDict = self.asyncPrepareDataScheme(serviceCode='3+-\*/7')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_illegal_chars_02(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='3+-\*/7')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_illegal_chars_03(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0001',moc='e+-\*/7')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_illegal_chars_04(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0002',personalData='e-+\*/8407A8E87FBDD6F37F37CDE4B595D8A0205AB2A36E38685BEC23AB24C9C0258A1AE4095BA60EA1E96206697F2186059AFA1415C6CD3C6B32A8511E4CEF5444A7D66F7A703B86FEA49DC83966713AC51AD88E0A64C28536190AB1ACA8D71B98CF944C0D87164E027551AF79B16202CFA5F670C8942E6F33203AAA2F2F3CDBFD7C046F790F1F1989CF1646ABB1DA1C5F2C86C7478F6FD186B47B92ACBAF5DB69F55CBEF47B1395AC6A73A27C053D9D42DA4DC4176523A66923998893A7B2E4DD81243C1F2DD6E40CDD808FB09356360CBD36E31AD93DE840304BDB02DD7DBB05861136B4F47AB49067F9F62E5DFFF519DCDA8A20DFB97A17D045240916ABD634C757E8318F64989E623A5D181C907E8D5FD852F94DA97C315047316509A12D30306963E1D09A606C40C3601856D028F76FC695A42C216FCEFD2869315AD9897E6BCE89E0CB70027D9ABDC2F07C2890167537F99D62E91988A2738F0A117825285F87995AC8B77CF14CF29C4FEA697112E004582A6144E8DB8C3700B1E09F4CC343EBFA529B91C30314740AEDB274AC65C2A6A328DE0EEE94F2176703C6ACD4DA6371815A68F318E74E1116CF0AB46FB0CB98B3945C0D527E8DD39E3AFC84DC76DF66DBB0EC4ACB6B65A6077B060FEABCB9AEA75A38A3E14BE4AEC32FC6BF107ED7445DD8D3FE72D9922D97227BDBA8BC220D0E44BF9572FC31C79D9B7AA97AF2AEEA52BD2E72C4C8FE5AAEA0310A0013F6449D1EBDC7D491AEC7CE258874419BF28BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD09418A66BAAB38FBF7599AE70AC32BA00888BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0948BAF473F2F8FD0941CC9DB7BBAAF66468BAF473F2F8FD094612525A2DC565F2518980B538864589B8BAF473F2F8FD0948BAF473F2F8FD094F898739EAF54E89193069DD0FC2B2B678BAF473F2F8FD0944BA61EDE6DE871558BAF473F2F8FD0945577B18E69FCF4638BAF473F2F8FD0948BAF473F2F8FD094BD1B525A6D350C9B8BAF473F2F8FD094DA7DDA98F80F0EE58BAF473F2F8FD0944E72EF898BFAD019B195D80FB3026674FA9526824FC6A6114EDADCAAD60E8BE522B018021ABE7FAA5EF296A2B1D1115E23ADA5FB74D3BBD4CDE51C38870CF3605558D91AD5A40CE74C038D271FE8481394714285AED7F152C3667F86749B3982DED96EF50706B65E')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_illegal_chars_05(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0003',token='1612120A00002E090102075A90800960A7F716C6B4905AD5C4D50F2C82170FFC5B7713B2C7D23E9AB1A3F06DD3AC7654112D93EBA7DE4B54AF309BF3F62C75DBBEC6DA4FFD2637D8E36AF1CC60E967CE400BE7CC9D7D91331C-\*/E+')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_illegal_chars_06(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0004', amount='45&*^&1')

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_illegal_chars_07(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0004', amount=4 + -7)

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_exception_asyncPrepareData_illegal_chars_08(self):
        requestJsonDict = self.asyncPrepareDataScheme(sn='0005',issueFee=4+-7)

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'
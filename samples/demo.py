# a = {'one':1,'two':2,'three':3}
# #设置默认值，该key在dict中不存在，新增键值对
# a.setdefault('four',4)
# print(a)
# #a['one'] = 1.5  #普通方法，会修改键的值
# #设置默认值，该key在dict中存在，不会修改dict内容
# # print(a.setdefault('one',3.4))
# print(a)


lista = [
{'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token', '测试执行': '是', '测试用例步骤': 'step_01'},
{'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '测试执行': '否', '测试用例步骤': 'step_01'},
{'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '测试执行': '否', '测试用例步骤': 'step_02'},
{'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '测试执行': '是', '测试用例步骤': 'step_01'},
{'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '测试执行': '是', '测试用例步骤': 'step_02'}
]

# case_list = {}
# for i in lista:
#     case_list.setdefault( 'case_info', []).append(i)
# print(case_list)

case_dict = {}
for i in lista:
    case_dict.setdefault( i['测试用例编号'], []).append(i)
# print(case_dict)

case_list = []
for k, v in case_list.items():
    case_dict = {}
    case_dict['case_name'] = k
    case_dict['case_info'] = v
    case_list.append( case_dict)

for c in case_list:
    print(c)






# all_case_list = []
# for i in lista:
#     all_case = {}
    # case_list.setdefault( i['测试用例编号'],[] ).append(i)  #核心，[]表示输出结果是一个列表
    # all_case['case_name'] = i['测试用例编号']
    # all_case['case_info'] = case_list[i['测试用例编号']]
    # all_case_list.append(all_case)
# print(all_case_list)


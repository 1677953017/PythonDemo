# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:26:33 2020

@author: Lenovo
"""


import json

from jsonpath import jsonpath

if __name__ == '__main__':
    dict = {"class": {"students": [{"student_id": "1", "name": "bob", "sex": "male", "age": 6},
                                   {"student_id": "2", "name": "amy", "sex": "female", "age": 6},
                                   {"student_id": "3", "name": "pery", "sex": "male", "age": 5}],
                                   "teachers": {"teacher_id": "1", "name": "anne", "sex": "female", "age": 32}}}

    # 获取根节点下的任意name属性的值
    print(jsonpath(dict, '$..name'))  # 输出 ['bob', 'amy', 'pery', 'anne']

    # 获取teachers节点
    print(jsonpath(dict, '$.class.teachers'))  # 输出 [{'teacher_id': '1', 'name': 'anne', 'sex': 'female', 'age': 32}]

    # 获取第一个students数据
    print(jsonpath(dict, '$..students[0]'))  # 输出  [{'student_id': '1', 'name': 'bob', 'sex': 'male', 'age': 6}]

    # 获取students的第一条数据的name属性
    print(jsonpath(dict, '$..students[0].name'))  # 输出 ['bob']

    # 获取students的0,1条数据
    print(jsonpath(dict, '$..students[0,1,3]'))   # 输出 [{'student_id': '1', 'name': 'bob', 'sex': 'male', 'age': 6}, {'student_id': '2', 'name': 'amy', 'sex': 'female', 'age': 6}]
    print(jsonpath(dict, '$..students[:2]'))    # 输出 [{'student_id': '1', 'name': 'bob', 'sex': 'male', 'age': 6}, {'student_id': '2', 'name': 'amy', 'sex': 'female', 'age': 6}]

    # 获取students的最后一条数据
    print(jsonpath(dict, '$..students[-1:]'))  # 输出 [{'student_id': '3', 'name': 'pery', 'sex': 'male', 'age': 5}]










road_name=jsonpath.jsonpath(content2,'$..name')
    #print(road_name)
road_location=jsonpath.jsonpath(content2,'$..dir')
road_index=jsonpath.jsonpath(content2,'$..index')
road_speed=jsonpath.jsonpath(content2,'$..speed')
road_traveltime=jsonpath.jsonpath(content2,'$..travelTime')
road_date=jsonpath.jsonpath(content2,'$..delayTime')
#print(road_name+"w2,"+road_location)
#      print(road_name+","+road_location+","+road_index+","+road_speed+","+road_traveltime+","+road_date))




















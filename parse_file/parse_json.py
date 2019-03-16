#!/usr/bin/env python3
# _*_ coding=utf-8 _*_

import json
from collections import OrderedDict

data = {
    'name' : 'ALIBABA',
    'num'  : 200,
    'price': 167.34
}

# python struct -> json
json_str = json.dumps(data)
print(json_str)

# json str -> python struct
data_tmp = json.loads(json_str)
print(data_tmp)

# writing json data
with open('data.json', 'w') as f:
    json.dump(data, f)

# reading data back
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)

# 字典中任何非字符串类型的key在编码时会先转换为字符串类型
print(json.dumps({1:2})) # {"1": 2}

print('******************************')

d = json.loads(json_str, object_pairs_hook=OrderedDict) # object_hook=
print(d)

print(json.dumps(data, indent=4))
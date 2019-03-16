#!/usr/bin/env python3
# _*_ coding=utf-8 _*_

import pickle
import time
import threading

data = {'Liu XiaoYu': 'Jiang Xi', 'Zhu GaoPeng': 'He Nan'}

# python object to file
with open('somefile', 'wb') as f:
    pickle.dump(data, f)

# python object to string
s = pickle.dumps(data)
print(s)

# restore from a file
with open('somefile', 'rb') as f:
    data = pickle.load(f)
    print(data)

# restore from a string
data = pickle.loads(s)
print(data)

# __getstate__()和__setstate__() 可以绕过一些不能序列化的限制
class User:
    def __init__(self, n):
        self._n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self._n > 0:
            print('T minus', self._n)
            self._n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self._n

    def __setstate__(self, n):
        self.__init__(n)

user = User(10)
s = pickle.dumps(user)
print(s)
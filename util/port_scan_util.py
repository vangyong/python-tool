#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc : 端口扫描工具

import telnetlib
import threading

import Queue


def get_ip_status(ip):
    server = telnetlib.Telnet()
    for port in range(20, 100):
        try:
            server.open(ip, port)
            print('{0} port {1} is open'.format(ip, port))
        except Exception as err:
            print('{0} port {1} is not open'.format(ip, port))
        finally:
            server.close()


def check_open(q):
    try:
        while True:
            ip = q.get_nowait()
            get_ip_status(ip)
    except Queue.Empty as e:
        pass


if __name__ == '__main__':
    host = ['192.168.100.207']  # 这里模拟多IP地址的情况，也可以从文件中读取IP——list
    q = Queue.Queue()
    for ip in host:
        q.put(ip)
    threads = []
    for i in range(10):
        t = threading.Thread(target=check_open, args=(q,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

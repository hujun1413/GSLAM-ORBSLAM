#!/usr/bin/python
# coding:utf-8


import os
import io
import traceback

#过滤掉文件中无用的位姿
pose_graph_path = '/home/cutcat/hujun_file/GSLAM-SVO/evaluations/eva_traj_tumrgbd_withloop.txt'
pose_traj_path = "/home/cutcat/hujun_file/GSLAM-SVO/evaluations/eva_traj_tumrgbd_withloop_filter.txt"
 
class PoseExtractor():
 
    def __init__(self):
        print "extracting..."
        traj_file = os.open(pose_traj_path, os.O_RDWR|os.O_CREAT|os.O_TRUNC)#读写+创建+清空打开

        pose_file = io.open(pose_graph_path, 'r', encoding= 'utf-8')
        poses_lines = pose_file.readlines()
        count = 0
        for line in poses_lines:
            #print line
            line_strip = line.strip(' ') #去除首尾空格
            list = line_strip.split(' ') #空格分割得到各数据
            if list[1] == "0.000000" and list[2] == "0.000000" and list[3] == "0.000000" and list[7].rstrip() == "1":
            	continue
            os.write(traj_file,  line) #写入文件
            count += 1
        
        print "#total poses: " + str(count) + ", output to " + pose_traj_path
        pose_file.close()
        os.close(traj_file) # 关闭文件
        
if __name__ == '__main__':
 
    try:
        pose_extractor = PoseExtractor()
    except Exception, e:
        print 'traceback.format_exc():\n%s' % traceback.format_exc()

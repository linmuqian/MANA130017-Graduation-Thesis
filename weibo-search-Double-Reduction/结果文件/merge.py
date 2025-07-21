import os
from pprint import pprint

import pandas as pd

def merge_csv_files(directory):
    # 初始化一个空的DataFrame来存储合并后的数据
    merged_data = pd.DataFrame()

    # 递归遍历目录及其子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件是否为CSV文件
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                # 读取CSV文件并将其追加到合并后的数据中
                merged_data = pd.concat([merged_data, pd.read_csv(file_path)], ignore_index=True)

    return merged_data

# 指定要读取的目录
directory = './'

# 调用函数并获取合并后的数据
merged_df = merge_csv_files(directory)

"""
微博id：微博的id，为一串数字形式
微博bid：微博的bid
微博内容：微博正文
头条文章url：微博中头条文章的url，若某微博中不存在头条文章，则该值为''
原始图片url：原创微博图片和转发微博转发理由中图片的url，若某条微博存在多张图片，则每个url以英文逗号分隔，若没有图片则值为''
视频url: 微博中的视频url和Live Photo中的视频url，若某条微博存在多个视频，则每个url以英文分号分隔，若没有视频则值为''
微博发布位置：位置微博中的发布位置
微博发布时间：微博发布时的时间，精确到天
点赞数：微博被赞的数量
转发数：微博被转发的数量
评论数：微博被评论的数量
微博发布工具：微博的发布工具，如iPhone客户端、HUAWEI Mate 20 Pro等，若没有则值为''
话题：微博话题，即两个#中的内容，若存在多个话题，每个url以英文逗号分隔，若没有则值为''
@用户：微博@的用户，若存在多个@用户，每个url以英文逗号分隔，若没有则值为''
原始微博id：为转发微博所特有，是转发微博中那条被转发微博的id，那条被转发的微博也会存储，字段和原创微博一样，只是它的本字段为空
结果文件：保存在当前目录“结果文件”文件夹下以关键词为名的文件夹里
微博图片：微博中的图片，保存在以关键词为名的文件夹下的images文件夹里
微博视频：微博中的视频，保存在以关键词为名的文件夹下的videos文件夹里
user_authentication：微博用户类型，值分别是蓝v，黄v，红v，金v和普通用户
"""

# 打印合并后的数据
pprint(merged_df.describe())
merged_df = merged_df.drop_duplicates(subset=['bid'])
pprint(merged_df.nunique())
merged_df.to_csv('merged_data.csv', index=False)

def f(text):
    try:
        return int(str(text))
    except:
        return 0

merged_df['评论数'] = merged_df['评论数'].apply(f)
influence_df = merged_df[merged_df['评论数'] > 50]
influence_df.to_csv('influence_tweet.csv', index=False)
pprint(influence_df)

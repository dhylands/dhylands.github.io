#!/usr/bin/env python3

'''
tag_generator.py

Copyright 2017 Long Qian
Contact: lqian8@jhu.edu

This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os

post_dir = '_posts/'
tag_dir = '_tag/'

filenames = glob.glob(post_dir + '*md')

total_tags = []
for filename in filenames:
    f = open(filename, 'r')
    inHeader = False
    inTag = False
    for line in f:
        if inHeader:
            current_tags = line.strip().split()
            if current_tags[0] == 'tags:':
                if len(current_tags) == 1:
                    inTag = True
                else:
                    total_tags.extend(current_tags[1:])
                    break
            elif inTag:
                if current_tags[0] == '-':
                    total_tags.extend(current_tags[1:])
                else:
                    inTag = False
                    break
        if line.strip() == '---':
            if inHeader:
                break
            inHeader = True
    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = \
        '---\n' \
        'layout: tag\n' \
        'title: ' + tag + '\n' \
        'tag: ' + tag + '\n' \
        'permalink: "/tag/' + tag + '"\n' \
        'robots: noindex\n' \
        '---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())

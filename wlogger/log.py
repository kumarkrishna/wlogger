# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse, argcomplete
import datetime
import os
import sys
import time
import pickle
import markdown
import datetime

import wlogger.engine

home = os.path.expanduser("~")

def main() :
    """ Parse the arguments using argparse package"""
    

    argparser = argparse.ArgumentParser(description='wlogger')

    argparser.add_argument("-a","--add", help=" Add to-do list", metavar="add", action="store", nargs="*")
    argparser.add_argument("-r","--remove", help=" Strike off from list ", metavar="remove", action="store", nargs="*")
    argparser.add_argument("-p","--progress", help="Add to progress", metavar="PROGRESS", action="store", nargs="*")
    argparser.add_argument("-s", "--section", metavar="section", default=None, action="store", nargs="*")
    argparser.add_argument("--config", action="store_true", default=False)
    argparser.add_argument("--md", action="store_true", default=False)
    argparser.add_argument("-e", action="store_true", default=False)
    argparser.add_argument("-V", "--version", action="store_true",default=False)

    argcomplete.autocomplete(argparser)
    args = argparser.parse_args()
    
    process(args)


def process(args) :
    """ Process the arguments. Add NLP layer later """

    if args.e : 
        detailed_usage()
        sys.exit(2)

    if args.version : 
        import release
        print(release.__version___)
        sys.exit(2)
    if args.config is True :
        wlogger.engine.reconfig()
    elif args.add is not None :
        add_util(args)
    elif args.remove is not None :
        remove_util(args)
    elif args.progress is not None :
        progress_util(args)
    elif args.md is True :
        to_md()

    else :
        display_logs()
    update_log()

def add_util(args) :

    location = wlogger.engine.engine()
    message = ' '.join(args.add)
    todo = pickle.load(open(location + '/wlogger/data/todo.p', 'r'))
    
    if args.section is not None :
        to_section = ' '.join(args.section)
    else :
        to_section = 'General'

    if to_section in todo.keys() :
        todo[to_section].append(' '.join(args.add))
    else :
        todo[to_section] = [' '.join(args.add)]
    pickle.dump(todo, open(location + '/wlogger/data/todo.p','w'))


def remove_util(args) :

    location = wlogger.engine.engine()
    message = ' '.join(args.remove)
    todo = pickle.load(open(location + '/wlogger/data/todo.p', 'r'))
    done = pickle.load(open(location + '/wlogger/data/done.p', 'r'))

    if args.section is not None :
        from_section = ' '.join(args.section)
    else :
        from_section = [key for key in todo.keys() if ' '.join(args.remove) in todo[key]]

    if from_section in todo.keys() :
        index = todo[from_section].index(' '.join(args.remove))
        todo[from_section] = todo[from_section][:index] + todo[from_section][index+1:]
        if from_section in done.keys() :
            done[from_section].append((' '.join(args.remove), datetime.datetime.now()))
        else :
            done[from_section] = [(' '.join(args.remove), datetime.datetime.now())]            
    else :        
        print("Remove from a valid section\n")
        print("Use wlogger -h for help")
        sys.exit(2)

    pickle.dump(todo, open(location + '/wlogger/data/todo.p','w'))
    pickle.dump(done, open(location + '/wlogger/data/done.p','w'))

def progress_util(args) :
    location = wlogger.engine.engine()
    message = ' '.join(args.progress)
    done = pickle.load(open(location + '/wlogger/data/done.p', 'r'))
    
    if args.section is not None :
        to_section = ' '.join(args.section)
    else :
        to_section = 'General'

    if to_section in done.keys() :
        done[to_section].append((' '.join(args.progress), datetime.datetime.now()))
    else :
        done[to_section] = [(' '.join(args.progress), datetime.datetime.now())]
    pickle.dump(done, open(location + '/wlogger/data/done.p','w'))

def update_log() :
    location = wlogger.engine.engine()
    todo = pickle.load(open(location + '/wlogger/data/todo.p', 'r'))
    done = pickle.load(open(location + '/wlogger/data/done.p', 'r'))

    filename = open(location + '/wlogger/data/wlog.txt', 'w')
    filename.writelines('ToDo List : \n\n')
    # filename.writelines('\n')

    for key in todo.keys() :
        filename.writelines(' * ' + key+'\n')
        for item in todo[key] :
            filename.writelines('\t - ' + item +'\n')
    filename.writelines('\n')
    filename.writelines('\n')

    filename.writelines('Progress List : \n')
    filename.writelines('\n')
    for key in done.keys() :
        filename.writelines(' * ' + key + '\n')
        for item in done[key] :
            filename.writelines('\t - ' + '{:60} {}'.format(item[0], (item[1]).strftime("%Y-%m-%d %H:%M:%S") )+'\n')

    filename.close()

def to_md() :
    location = wlogger.engine.engine()
    todo = pickle.load(open(location + '/wlogger/data/todo.p', 'r'))
    done = pickle.load(open(location + '/wlogger/data/done.p', 'r'))

    filename = open(location + '/wlogger/data/wlog.md', 'w')
    filename.writelines('## ToDo List : \n\n')

    for key in todo.keys() :
        filename.writelines('** ' + key+' **\n')
        for item in todo[key] :
            filename.writelines('- [ ] ' + item +'\n')
    filename.writelines('\n')
    filename.writelines('\n')

    filename.writelines('## Progress List : \n')
    filename.writelines('\n')

    for key in done.keys() :
        filename.writelines('** ' + key + '**\n')
        for item in done[key] :
            filename.writelines('- [X]' + '{:50} {}'.format(item[0], (item[1]).strftime("%Y-%m-%d %H:%M:%S") ) +'\n')

    filename.close()
    with open(location + '/wlogger/data/wlog.md', 'r') as filename :
        logs = filename.readlines()
    html = markdown.markdown('\n'.join(logs))
    with open(location + '/wlogger/data/wlog.html', 'w') as filename :
        filename.writelines(html)

def display_logs() :
    location = wlogger.engine.engine()
    with open(location + '/wlogger/data/wlog.txt') as filename :
        log = filename.readlines()

    print(''.join(log))

def detailed_usage() :
    print("Detailed")

if __name__ == "__main__":
    main()
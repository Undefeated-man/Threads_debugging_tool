"""
	###########################################################################
	#		                                                                  #
	#		Project: Threads_debugging_tool                                   #
	#		                                                                  #
	#		Filename: debugging.py                                            #
	#		                                                                  #
	#		Programmer: Vincent Holmes 1135235700@qq.com                      #
	#		                                                                  #
	#		Description: This is a debugging tool for program with multi-th   #
	#                     reads that allow you to set break points in every   #
	#                      threads, and skip some specific functions' break   #
	#                      point without quiting the processing. In additio   #
	#                     n, you can simply set "DEBUG = False" to disable    #
	#                     all the debugging print and log without comment t   #
	#                     hem.                                                #
	#		                                                                  #
	#		Start_date: 2021-07-18                                            #
	#		                                                                  #
	#		Last_update: 2021-07-19                                           #
	#		                                                                  #
	###########################################################################
"""


"""
    Introduction:
        This is a debugging tool for threading. Each time using 
        the function, you should use it like this:
            
            import debugging as dbg
            
            dbg.DEBUG = True
            dbg.DBG = True
            dbg.dbg(<the content you wanna show>)
    
    
        You can also use it to log and save in a file by setting
            "dbg.LOG = True" 
        before you using "dbg.dbg(<content>)"
        
        
        You can change the separate notation between each content
        by setting 
            "sbg.SEP = '<new notation>'"
        before using "dbg.dbg(<content>)"
        
        
        When you don't want to debug, just set 
            "dbg.DEBUG = False"
        everything won't show anymore (you don't need to delete all
        of these things writen during debugging)


        You can seperatly choose to debug different parts of code by
        setting "dbg.PART", like:
            
            dbg.PART.append(<part_num>)     # the part you wanna add
                                            # to debug
            dbg.dbg(<content>, <part_num>)
"""

import os
import time
import logging


DEBUG = True
DBG = True
LOG = False
SEP = " "
PART = []

def dbg(*content, **dic_text):
    global DEBUG
    if not DEBUG:
        return
    global DBG
    to_show = ""
    
    if len(PART) != 0:
        type_ = content[-1]
        content = content[:-1]
        if not type_ in PART:
            return

    def print_dic(dic_content, to_show=""):
        if len(dic_content.keys()) > 0:
            if to_show != "":
                to_show += "\n\n"
            for k, v in dic_content.items():
                to_show += "\t"+str(k)+": "+str(v)+"\n"
        return to_show
    
    if len(content) > 0:
        for s in content:
            if type(s) == dict:
                to_show = print_dic(s, to_show)
                continue
            to_show += str(s) + SEP
    
    if len(dic_text.keys()) > 0:
        print_dic(dic_text)
    
    if DBG:
        if LOG:
            if not os.path.exists("./log"):
                os.mkdir("./log")
                
            format = "\n\n%(asctime)s  %(thread)d(线程)  %(process)d(进程)  \
                %(filename)s  %(funcName)s\n\t line: %(lineno)d \n\t %(message)s\n\n"
            logging.basicConfig(filename='./log/debugging_%s.log'%(time.strftime("%Y%m%d", time.localtime())), \
                                level=logging.DEBUG, format=format)
            
            logging.debug(to_show)
        
        print(to_show)
        to_continue = input("Press Enter to continue(or input 'skip' to skip this break-point in the loop.)")
        if PART != []:
            to_continue = to_continue.split(" ")
            if to_continue[0] == 'skip':
                PART.remove(to_continue[1])
        else:
            if to_continue == 'skip':
                DEBUG = False
            
            
# test
if __name__ == "__main__":
    dbg("hello", "good", "yeah", {"a": 1, "b":True, "c": "fool", "d":time.time(), "e":time.time})
    for i in range(10):
        dbg(i)
    DEBUG = True
    for i in range(10):
        dbg(i*10)

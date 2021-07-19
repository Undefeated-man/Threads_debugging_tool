# Threads_debugging_tool
 This is a debugging tool for program with multi-threads that allow you to set break points in every threads, and skip some specific functions' break point without quiting the processing.  In addition, you can simply set "DEBUG = False" to disable all the debugging print and log without comment them. Each time using the function, you should use it like this:
            ```
            import debugging as dbg
            
            dbg.DEBUG = True
            dbg.DBG = True
            dbg.dbg(<the content you wanna show>)
            ```
 
 
You can also use it to log and save in a file by setting
            ```dbg.LOG = True```
before you using "dbg.dbg(<content>)"
        
 
 
You can change the separate notation between each content by setting 
            ```sbg.SEP = "<new notation>"```
before using "dbg.dbg(<content>)"
        
    
 
When you don't want to debug, just set 
            ```dbg.DEBUG = False```
everything won't show anymore (you don't need to delete all of these things writen during debugging)


 
You can seperatly choose to debug different parts of your code by setting "dbg.PART", like:
            ```
            dbg.PART.append(<part_num>)     # the part you wanna add
                                            # to debug
            dbg.dbg(<content>, <part_num>)
            ```
 and when this part you no longer want to debug it, just enter
 ```
             skip <part_num>
 ```
 then it won't debug this part any more.
 
 
 
 
 Hope that you have fun will this tool. Welcome commit!

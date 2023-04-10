import datetime

now = datetime.datetime.now()
def formattime(ft):
    return now.strftime(ft)


#time = formattime("%Y%m%d-%H%M")
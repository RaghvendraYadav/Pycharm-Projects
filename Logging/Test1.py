import logging
logging.basicConfig(filename='test1.log',level=logging.INFO)
logging.info('This is my first log File Code')
logging.warning('This is warning only proceed if it is a list')
logging.error('This is a error message from a system')
l=[1,2,3,4,5,6,7]
for i in l:
    if i ==2:
        logging.info(l)
        logging.warning('We have find out 2 in the above list')
logging.shutdown()
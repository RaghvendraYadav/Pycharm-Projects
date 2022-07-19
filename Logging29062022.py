import logging
logging.basicConfig(filename='test.log',level=logging.INFO)
logging.info('This is my first logfile ')
logging.warning('This is warnig we have used')
l=[1,2,3,4,5,6]
logging.error('This is error msg from sysytem')
for i in l:
    if i ==2:
        logging.info(i)
        logging.warning('This is warning for user tht thye have found out 2 in list')
logging.shutdown()
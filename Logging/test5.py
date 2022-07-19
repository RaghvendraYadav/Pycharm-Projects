import logging
# here check by changing the level
# DEBUG -10 INFO -20 Warning - 30 ERROR - 40 CRITICAL - 50
logging.basicConfig(filename='test5.log',level=logging.WARNING,format='%(levelname)s %(asctime)s %(name)s %(message)s')
def divide(a,b):
    logging.info('We have entered into the div function')
    try:
        logging.info('We have entered into try block ')
        divs = a/b
        logging.info('We have completed the divison')
        return  divs
    except Exception as e:
        logging.exception(e)


divide(2,0)
import logging
# here check by changing the level
# DEBUG -10 INFO -20 Warning - 30 ERROR - 40 CRITICAL - 50
logging.basicConfig(filename='test6.log',level=logging.ERROR,format='%(levelname)s %(asctime)s %(name)s %(message)s')
try:
    logging.info('I m trying to read the file ')
    with open('Ragh.txt','r'):
        logging.info('Succressfully it hs read the file')
except Exception as e:
    logging.critical('This situation is Critical')
    logging.error(e)
    logging.exception(e)
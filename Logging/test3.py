import logging
logging.basicConfig(filename='test3.log',level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')

def divide(a,b):
    logging.info('The number entered by user is %s ans %s',a,b)
    try:
        logging.info('Inside Function')
        div =a/b
        logging.info('we have completed the division operation')
        logging.info('The result of the code is {}'.format(div))
    except Exception as e:
        logging.exception(e)


#print(divide(2,2))
divide(2,4)
import logging
logging.basicConfig(filename='testCode.log',level=logging.INFO,format='%(levelname)s  %(message)s %(asctime)s %(name)s')

def divide(a,b):
    logging.info("The number enterd by user is %s and %s" ,a, b)
    try:
        logging.info('We are into the function')
        div=a/b
        logging.info('We have completed division')
        return div
    except Exception as e:
        logging.exception(e)
divide(3,0)

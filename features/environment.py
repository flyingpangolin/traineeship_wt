import logging

logformat="%(levelname)s:%(filename)s:%(lineno)d:%(asctime)s:%(message)s"
logging.basicConfig(filename='./example2.log',level=logging.INFO,format=logformat) 

def before_all(context):
   logging.info("Automated testing has started")


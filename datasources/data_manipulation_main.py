#basic data manipulation with pandas
import logging
import sys
import time


if __name__ == '__main__':
    #define data sources path
    input_white = '../datasources/winequalitydataset/winequality-white.csv'
    input_red = '../datasources/winequalitydataset/winequality-red.csv'
    
    #log to console only
    log = logging.getLogger(__name__)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    #get start time to print execution stats
    start_time = time.time()
    
    #TODO: open csv files with pandas
    log.info('Open data sources with pandas in two different dataframes')
    
    #TODO: print basic stats
    log.info('run \'describe()\' dataframe function...')

    log.info('print first 10 and last 10 records in the dataframe')

    log.info('print number of columns and rows in the dataframe')

    #TODO: perform basic data manipulation
    log.info('add one column (called \'type\' and equal to 0) to white wines dataframe and one column (called \'type\' and equal to 1) to the red wines dataframe')

    log.info('create a new dataframe containing all white and red wines with quality equal to 5, and print length of newly created dataframe')

    log.info('create a new dataframe (\'low_quality\')containing all white and red wines with quality between 1 to 4 included, and print length of newly created dataframe')
    
    log.info('cycle every row of \'low_quality\' dataframe, and for each row print density, ph, sulphates, alcohol and quality')
    
    #printing out execution stats
    elapsed_time = str(time.time() - start_time)
    log.info('Execution completed in {0} [s]'.format(elapsed_time))
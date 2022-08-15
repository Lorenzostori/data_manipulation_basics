#basic data manipulation with pandas
import logging
import sys
import time
import pandas as pd


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
    
    df_white = pd.read_csv(input_white, sep = ';') #read csv defining separator
    df_red = pd.read_csv(input_red, sep = ';') # read csv defining separator
      
    #TODO: print basic stats
    log.info('run \'describe()\' dataframe function...')
    
    # using describe() to extract dataframe statistics
    log.info(df_white.describe()) 
    log.info(df_red.describe())
    
    log.info('print first 10 and last 10 records in the dataframe')
    # using head(n) to print fist n rows of dataframe
    log.info("First 10 values in White are: ")
    log.info(df_white.head(10))
    
    #using tail(n) to print fist n rows of dataframe
    log.info("Last 10 values in White are: ")
    log.info(df_white.tail(10))
    
    log.info("First 10 values in Red are: ")
    log.info(df_red.head(10))
    
    log.info("Last 10 values in Red are: ")
    log.info(df_red.tail(10))

    log.info('print number of columns and rows in the dataframe')
    # see tuple to retrieve columns x rows with .shape
    shape_w = df_white.shape 
    column_w = shape_w[1] 
    rows_w = shape_w[0] 
    log.info('Number of columns in White is: ' + str(column_w))
    log.info('Number of rows in White is: ' + str(rows_w))
    
    shape_r = df_red.shape 
    column_r = shape_r[1]
    rows_r = shape_r[0]
    log.info('Number of columns in Red is: ' + str(column_r))
    log.info('Number of rows in Red is: ' + str(rows_r))
    
    #...or more compact:
    log.info('Number of rows and columns in White is %d and %d', len(df_white), len(df_white.columns))
    log.info('Number of rows and columns in Red is %d and %d', len(df_red), len(df_red.columns))
    
    #TODO: perform basic data manipulation
    log.info('add one column (called \'type\' and equal to 0) to white wines dataframe and one column (called \'type\' and equal to 1) to the red wines dataframe')
    
    # using .assign() to add Type = 0 column
    df_white = df_white.assign(type = 0) 
    # using .assign() to add Type = 1 column
    df_red = df_red.assign(type = 1) 
    
    #...or
    #df_white['type'] = 0
    #df_red['type'] = 1
    
    log.info(df_white)
    log.info(df_red)

    log.info('create a new dataframe containing all white and red wines with quality equal to 5, and print length of newly created dataframe')

    # filtering quality parameter = 5 with .loc()
    filtered_w = df_white.loc[df_white.quality == 5] 
    filtered_r = df_red.loc[df_red.quality == 5]
    
    wr_merge = [filtered_w, filtered_r]
    # using pd.concat() to merge two dataframes
    wr_5 = pd.concat(wr_merge) 
    log.info(wr_5)
    # see tuple to retrieve columns x rows
    # shape_wr_5 = wr_5.shape 
    # rows_wr_5 = shape_wr_5[0]
    # log.info('Number of rows in joined dataframe is: ' + str(rows_wr_5))
    log.info('Number of rows in joined dataframe is: %d',  len(wr_5))

    log.info('create a new dataframe (\'low_quality\')containing all white and red wines with quality between 1 to 4 included, and print length of newly created dataframe')
    
    # filter quality parameter <5 with .loc()
    filtered_w_low = df_white.loc[df_white.quality < 5] 
    filtered_r_low = df_red.loc[df_red.quality < 5]
    
    low_quality_merge = [filtered_w_low, filtered_r_low]
    low_quality = pd.concat(low_quality_merge) # using pd.concat() to merge two dataframes
    log.info(low_quality)
      
    #see tuple to retrieve columns x rows with .shape
    # shape_low_quality = low_quality.shape 
    # rows_low_quality = shape_low_quality[0]
    # log.info('Number of rows in joined dataframe is: ' + str(rows_low_quality))
    log.info('Number of rows in joined dataframe is: %d', len(low_quality))
    
    log.info('cycle every row of \'low_quality\' dataframe, and for each row print density, ph, sulphates, alcohol and quality')
    
    low_quality.reset_index(drop=True, inplace=True)
    for i in low_quality.index:
        log.info('Density: %d, pH: %d, sulphates: %d, alcohol: %d, quality: %d', low_quality.density[i], low_quality.pH[i], low_quality.sulphates[i], low_quality.alcohol[i], low_quality.quality[i])
        
    #printing out execution stats
    elapsed_time = str(time.time() - start_time)
    log.info('Execution completed in {0} [s]'.format(elapsed_time))
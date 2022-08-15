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
    desc_white = df_white.describe() 
    print(desc_white) 
    desc_red = df_red.describe() 
    print(desc_red)
    
    log.info('print first 10 and last 10 records in the dataframe')
    
    # using head(n) to print fist n rows of dataframe
    white_f10 = df_white.head(10) 
    print("First 10 values in White are: ")
    print(white_f10)
    
    #using tail(n) to print fist n rows of dataframe
    white_l10 = df_white.tail(10) 
    print("Last 10 values in White are: ")
    print(white_l10)
    
    red_f10 = df_red.head(10)
    print("First 10 values in Red are: ")
    print(red_f10)
    
    red_l10 = df_red.tail(10)
    print("Last 10 values in Red are: ")
    print(red_l10)

    log.info('print number of columns and rows in the dataframe')
    
    # see tuple to retrieve columns x rows with .shape
    shape_w = df_white.shape 
    column_w = shape_w[1] 
    rows_w = shape_w[0] 
    print('Number of columns in White is: ' + str(column_w))
    print('Number of rows in White is: ' + str(rows_w))
    
    shape_r = df_red.shape 
    column_r = shape_r[1]
    rows_r = shape_r[0]
    print('Number of columns in Red is: ' + str(column_r))
    print('Number of rows in Red is: ' + str(rows_r))
    
   
    #TODO: perform basic data manipulation
    log.info('add one column (called \'type\' and equal to 0) to white wines dataframe and one column (called \'type\' and equal to 1) to the red wines dataframe')
    
    # using .assign() to add Type = 0 column
    df_white_1 = df_white.assign(Type = 0) 
    # using .assign() to add Type = 1 column
    df_red_1 = df_red.assign(Type = 1) 
    
    print(df_white_1)
    print(df_red_1)

    log.info('create a new dataframe containing all white and red wines with quality equal to 5, and print length of newly created dataframe')

    # filtering quality parameter = 5 with .loc()
    filtered_w = df_white_1.loc[df_white_1.quality==5] 
    filtered_r = df_red_1.loc[df_red_1.quality==5]
    
    wr_merge = [filtered_w, filtered_r]
    # using pd.concat() to merge two dataframes
    wr_5 = pd.concat(wr_merge) 
    print(wr_5)
    
    # see tuple to retrieve columns x rows
    shape_wr_5 = wr_5.shape 
    rows_wr_5 = shape_wr_5[0]
    
    print('Number of rows in joined dataframe is: ' + str(rows_wr_5))

    log.info('create a new dataframe (\'low_quality\')containing all white and red wines with quality between 1 to 4 included, and print length of newly created dataframe')
    
    # filter quality parameter <5 with .loc()
    filtered_w_low = df_white_1.loc[df_white_1.quality<5] 
    filtered_r_low = df_red_1.loc[df_red_1.quality<5]
    
    low_quality_merge = [filtered_w_low, filtered_r_low]
    low_quality = pd.concat(low_quality_merge) # using pd.concat() to merge two dataframes
    print(low_quality)
      
    #see tuple to retrieve columns x rows with .shape
    shape_low_quality = low_quality.shape 
    rows_low_quality = shape_low_quality[0]
    
    print('Number of rows in joined dataframe is: ' + str(rows_low_quality))
    
    log.info('cycle every row of \'low_quality\' dataframe, and for each row print density, ph, sulphates, alcohol and quality')
    
    print(low_quality[['density', 'pH', 'sulphates', 'alcohol', 'quality']])
        
    #printing out execution stats
    elapsed_time = str(time.time() - start_time)
    log.info('Execution completed in {0} [s]'.format(elapsed_time))
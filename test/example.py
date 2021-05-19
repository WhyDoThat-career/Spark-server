APP_NAME = "pyspark_task_one.py"
# try:
#     sc and spark
# except NameError as e:
#     import findspark
#     findspark.init()
#     import pyspark
#     import pyspark.sql

import pyspark
import time

st = time.time()
    
sc = pyspark.SparkContext()
spark = pyspark.sql.SparkSession(sc).builder.appName(APP_NAME).getOrCreate()

df_bakery = spark.read \
    .format('csv') \
    .option('header', 'true') \
    .option('delimiter', ',') \
    .option('inferSchema', 'true') \
    .load('BreadBasket_DMS.csv')

df_sorted = df_bakery.cube('item').count() \
    .filter('item NOT LIKE \'NONE\'') \
    .filter('item NOT LIKE \'Adjustment\'') \
    .orderBy(['count', 'item'], ascending=[False, True])

df_sorted.show(10, False)

fn = time.time() - st

print('-'*20)
print('finsh time : {} sec'.format(fn))
print('-'*20)

df_sorted.coalesce(1) \
    .write.format('csv') \
    .option('header', 'true') \
    .save('output/items-sold.csv', mode='overwrite')
# import time
# def run() :
#     while True :
#         time.sleep(1)
# if __name__=="__main__" :
#     run()
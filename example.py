from pyspark.sql import SparkSession
import time

st = time.time()
spark = SparkSession.\
        builder.\
        appName("pyspark-notebook").\
        master("spark://spark-master:7077").\
        config("spark.executor.memory", "512m").\
        getOrCreate()

df_bakery = spark.read \
    .format('csv') \
    .option('header', 'true') \
    .option('delimiter', ',') \
    .option('inferSchema', 'true') \
    .load('workspace/BreadBasket_DMS.csv')

print('read csv time : {} sec'.format(time.time()-st))

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
import pyspark
import example

sc = pyspark.SparkContext('local[*]')

txt = sc.textFile('file:////usr//share//X11//Xcms.txt')

python_lines = txt.filter(lambda line: 'the' in line.lower())

print('-'*30)
print("The number of lines containing 'the' in your file is: ", python_lines.count())
print('example.Test.test :',example.Test.test)
print('-'*30)
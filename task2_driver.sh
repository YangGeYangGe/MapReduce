#!/bin/bash

# if [ $# -ne 2 ]; then
#     echo "Invalid number of parameters!"
#     echo "Usage: ./tag_driver.sh [input_location] [output_location]"
#     exit 1
# fi
hdfs dfs -rm -r temp
hdfs dfs -rm -r $2
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar \
-D stream.num.map.output.key.fields=2 \
-D mapreduce.job.reduces=3 \
-D mapreduce.job.name='Task2_Driver' \
-file task2_mapper.py \
-mapper "python task2_mapper.py" \
-file task2_reducer.py \
-reducer "python task2_reducer.py" \
-input $1 \
-output temp

hdfs dfs -cat temp/p* > testing.txt
hdfs dfs -rm -r testing.txt
hdfs dfs -put testing.txt testing.txt

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar \
-D mapreduce.job.reduces=3 \
-D mapreduce.job.name='second_Driver' \
-file second_mapper.py \
-mapper "python second_mapper.py" \
-file second_reducer.py \
-reducer "python second_reducer.py" \
-input testing.txt \
-output $2

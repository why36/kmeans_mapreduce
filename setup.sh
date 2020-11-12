#!/bin/bash
for var in $@
do
    rm -rf output
    hdfs dfs -rm -r output
    hadoop jar target/sample-1.0-SNAPSHOT.jar ${var} 10 input output
    hadoop fs -get output output
    python src/main/java/nju/plot.py ${var}
done
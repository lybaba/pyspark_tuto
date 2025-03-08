# pyspark_tuto


# Installing PySpark Using Conda
conda create -n pyspark_env

conda activate pyspark_env

conda install -c conda-forge pyspark

# Setting Env Variables

HADOOP_HOME: C:\Users\ly_ba\bigdata\hadoop-3.3.6

JAVA_HOME : C:\Users\ly_ba\tools\openjdk-11.0.26

PYSPARK_PYTHON: C:\Users\ly_ba\anaconda3\envs\pyspark_env\python.exe

Path: %JAVA_HOME%\bin;.....

SPARK_LOCAL_HOSTNAME: localhost

# install jupyter
conda install jupyter                # install jupyter + notebook
jupyter notebook  


# Using pyspark on Ubuntu WSL
export SPARK_LOCAL_HOSTNAME=localhost
export PYSPARK_PYTHON=/home/lyb/pyspark_env/bin/python3


export HADOOP_HOME=/home/lyb/bigdata/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"

export LD_LIBRARY_PATH=/home/lyb/bigdata/hadoop/lib/native:$LD_LIBRARY_PATH

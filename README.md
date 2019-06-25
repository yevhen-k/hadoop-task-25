# hadoop-task-25
Hadoop mapper and reducer to count word co-occurrence in sentences

## Task

Count word co-occurrence in sentences in any text available online.
Display top 20 most frequent pairs of words in sentences.
Any PL is sutable for mapper and reducer.
Use 3 reducers.
Split initial text file to 3 files.

## Steps

### Local (Standalone) Mode

* use `downloader.py` to download, clean-up and split *ALICE'S ADVENTURES IN WONDERLAND* text
* if you coding locally you should transfer via ssh files to server which running hadoop:

    `$ scp *.py username@ip-address:~/`

    `$ scp alice_* username@ip-address:~/`

* log in to your server
* create folder for storing input data:

    `$ hadoop fs -mkdir ~/input`

    `$ hadoop fs -cp alice_* ~/input`

* run hadoop query:

    `$ mapred streaming -input input/ -output output/ -mapper ./mapper.py -reducer ./reducer.py -file mapper.py -file reducer.py -numReduceTasks 3`

* read results:

    `$ hadoop fs -cat ~/output/* | sort -n -k3 -r | head -n20 > result.txt`
    
    `$ cat result.txt`

### Pseudo-Distributed Mode

* follow configuration listet [here](https://hadoop.apache.org/docs/r3.1.2/hadoop-project-dist/hadoop-common/SingleCluster.html#Pseudo-Distributed_Operation)
* fix `Hadoop: start-dfs.sh permission denied` as described [here](https://stackoverflow.com/questions/15211848)
* fix `start-dfs.sh Error: JAVA_HOME is not set and could not be found` as described [here](https://stackoverflow.com/questions/21533725)
* run `start-dfs.sh` and check browser at `localhost:9870`
* run mapreduce and check results:

    `$ mapred streaming -input input/ -output output/ -mapper ./mapper.py -reducer ./reducer.py -file mapper.py -file reducer.py -numReduceTasks 3`
    
    `$ hdfs dfs -cat output/* | sort -n -k3 -r | head -n20 > result.txt`
    
    `$ cat result.txt`

### Pseudo-Distributed Mode. YARN on a Single Node
* follow configuration listed [here](https://hadoop.apache.org/docs/r3.1.2/hadoop-project-dist/hadoop-common/SingleCluster.html#YARN_on_a_Single_Node)


## Links
[1] [Hadoop Single Cluster](https://hadoop.apache.org/docs/r3.1.2/hadoop-project-dist/hadoop-common/SingleCluster.html#Standalone_Operation)

[2] [Hadoop Streaming](https://hadoop.apache.org/docs/r3.1.2/hadoop-streaming/HadoopStreaming.html)

[3] [Hadoop File System Shell](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html)

[4] [IBM YARN Intro (rus)](https://www.ibm.com/developerworks/ru/library/bd-yarn-intro/index.html)
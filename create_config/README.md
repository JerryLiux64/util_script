Script simply create "num" of "config" files with the value of "keyword" from 0 to "num-1".

Ex: 

    Input:
    sample.txt:
        A=1

    Run:
    ./create_config.py sample.txt "A" 2

    Output:
    sample0.txt
        A=0

    sample1.txt
        A=1


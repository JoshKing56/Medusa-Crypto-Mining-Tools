#!/bin/bash
# for testing the functionality of reading to a file that's being streamed to

cat /dev/null > stream_test.txt
for ((i=0; i<300; i++)); do
    sleep 1;
    echo $i;
done >> stream_test.txt
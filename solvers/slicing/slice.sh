#!/bin/sh
#
cd "$(dirname "$0")"
set -e
sliced=../../output/slice/"$1".nnf
mkdir -p $(dirname "$sliced")
java -Xss512m -jar my_slice.jar ../../$1 ${sliced}
./d4 -m counting -i ${sliced}


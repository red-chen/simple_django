#!/bin/bash
DIR_NAME=$(cd `dirname $0`;pwd)
cd $DIR_NAME
cd ..
DIR_NAME=$(pwd)

python_path=$DIR_NAME/src/
python_path=$python_path:$DIR_NAME/src/deps/

echo $python_path

export PYTHONPATH=$python_path

PY=python2.7

$PY src/debug runserver 0.0.0.0:$1

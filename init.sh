#!/bin/bash

# Check current year + day to make sure we don't prematurely fetch data
YEAR=`date -d "5 hours ago" +"%Y"`
DAY=`date -d "5 hours ago" +"%d"`

echo "Currently year $YEAR day $DAY"

if (($1<=$YEAR )) && (($2<=$DAY)); then
    echo "Initializing year $1 day $2"
    folder="./$1/Day$2"

    # Check if year folder needs to be created
    if test -d "./$1"; then
     echo "year folder already exists"
    else
     echo "year folder does not exist, creating "./$1""
     mkdir "./$1"
    fi

    # Check if day folder needs to be created
    if test -d $folder; then
     echo "day folder already exists"
    else
     echo "day folder does not exist, creating $folder"
     mkdir $folder
    fi

    # Create source file from template
    if test -f "$folder/day$2.py"; then
     echo "source file exists, delete to restart from template"
    else
        echo "Creating source file $folder/day$2.py"
        cp template.py $folder/day$2.py
        sed -i "s/<YEAR>/$1/g" $folder/day$2.py
        sed -i "s/<DAY>/$2/g" $folder/day$2.py
    fi

    # Download input file
    if test -f "$folder/input.txt"; then
     echo "input file exists, delete to re-download"
    else
     echo "input file does not exist, fetching to $folder/input.txt"
     curl https://adventofcode.com/$1/day/$2/input --cookie "session=$AOC_COOKIE" -A 'psundstrom from github' --output $folder/input.txt
    fi
else
    echo "Input not available yet, hold your horses"
fi

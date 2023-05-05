#!/bin/bash

echo "----------Completion Checks----------" > ./leaderboard.txt
echo "Name     |     Status      |     Time" >> ./leaderboard.txt
echo "-------------------------------------" >> ./leaderboard.txt

for solution in solutions/*/*.py; do
	filename=$(basename -- "$solution")
	extension="${filename##*.}"
	filename="${filename%.*}"
	
	START=$(../../../tools/start.sh)
	python3 $solution > $solution.output
	TOTAL=$(../../../tools/stop.sh $START)

	if [[ -n $(diff $solution.output ./answer.txt) ]]; then
		echo "$filename          ❌               $TOTAL">> ./leaderboard.txt
	else
		echo "$filename          ✅               $TOTAL" >> ./leaderboard.txt
	fi
done

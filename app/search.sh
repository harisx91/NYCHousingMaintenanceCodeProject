touch results
> results
while [ 1=1 ]
do
Echo 'Enter a search term or enter quit to see results and leave'
read searchTerm
if [ $searchTerm = 'quit' ]; then
  break
fi
echo $searchTerm >> results
egrep -c -w -i *$searchTerm* novdescriptions.csv >> results
echo "results recorded"
done

py CreateGraph.py

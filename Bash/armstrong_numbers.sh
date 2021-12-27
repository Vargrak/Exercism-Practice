base=$1
leng=${#base}
i=0
until ((i==leng))
do 
    ((result+=${base:i:1}**leng))
    ((i+=1))
done
if ((base==result)); then echo "true"
else echo "false"
fi
exit 0

echo "Enter a number: "
read num
echo "Enter another number: "
read num2

add=$((num + num2))
sub=$((num - num2))
muli=$((num * num2))
div=$((num / num2))

echo $num " + " $num2 " = " $add
echo $num " - " $num2 " = " $sub
echo $num " * " $num2 " = " $muli
echo $num " / " $num2 " = " $div


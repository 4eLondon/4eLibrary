num = "Please enter a number: " |> IO.gets() |> String.trim() |> String.to_integer()
num2 = "Please enter a number: " |> IO.gets() |> String.trim() |> String.to_integer()

"#{num} + #{num2} = #{num+num2}" |> IO.puts()
"#{num} - #{num2} = #{num-num2}" |> IO.puts()
"#{num} * #{num2} = #{num*num2}" |> IO.puts()
"#{num} / #{num2} = #{num/num2}" |> IO.puts()


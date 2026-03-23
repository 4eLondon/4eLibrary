name = "Please enter your name: " |> IO.gets()

clean_name = String.trim(name)

"Your name is #{clean_name}" |> IO.puts()

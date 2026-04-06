# -o-o-o-o-o- [ Ruby file initialization ] -o-o-o-o-o-

=begin
In ruby, we aren't required to start our program with anything but there
are a few things things of note we can keep in mind when working with ruby files.

Firstly, running ruby files can be done in one of two ways:
1. Using the ruby interpreter directly: `ruby filename.rb`
2. Making the file executable and running it directly: `./filename.rb`

Method 1 - Using the ruby interpreter directly
To run a ruby file using the interpreter, simply type `ruby filename.rb` in your terminal.
we can also pass the -e flag to execute a single line of code: `ruby -e 'puts "Hello, World!"'`

Method 2 - Making the file executable
Given that ruby is a scripting language we can turn our programmings into
executable files if we are using unix systems such as Linux or MacOs. Shebangs (#!)
allow us to create our ruby exectuable that we can then run with ./*filename.rb* after
giving the script executable permissions

Step 1: being the file with the shebang -> #!/usr/bin/env ruby
Step 2: make the ruby file executable -> chmod +x *filename.rb*
Step 3: run the executable -> ./*filename*
=end

#!/usr/bin/env ruby
puts "Hello user"
puts "This is a unix script written in ruby"

# -o-o-o-o-o- [ Ruby variables simplified ] -o-o-o-o-o-

=begin
  In ruby there is no need to assign a datatype as the language will
  automatically assign a datatype based on whats stored in a variable.
  This means if we wish to create variables we only have to assign a name
  and value.

  eg.
  name = "Tom" -> will auto assign datatype string
  age = "45" -> will auto assign datatype int

=end

name = "Ryan"
age = 19
gender = 'm'
bank_balance = 0.22
is_broke = true

put "Username = #{name}"
put "age = #{age} yrs old"
put "gender = #{gender}"
put "Balance = #{bank_balance}"
put "is user broke = #{is_broke}"

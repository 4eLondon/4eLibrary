main :: IO ()
main = do
  putStrLn "Enter a number: "
  input <- getLine
  putStrLn "Enter another number: "
  input2 <- getLine
  
  let num = read input::Double
      num2 = read input2::Double

  putStrLn (input++" + "++input2++" = "++show(num+num2))
  putStrLn (input++" - "++input2++" = "++show(num-num2))
  putStrLn (input++" * "++input2++" = "++show(num*num2))
  putStrLn (input++" / "++input2++" = "++show(num/num2))

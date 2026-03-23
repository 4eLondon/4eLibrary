main :: IO ()
main = do
  putStrLn "what is your name: "
  name <- getLine
  putStrLn ("Your name is "++name)

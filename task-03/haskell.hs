isPrime :: Int -> Bool
isPrime n
  | n <= 1    = False
  | otherwise = all (\x -> n `mod` x /= 0) [2..intSqrt n]
  where
    intSqrt = floor . sqrt . fromIntegral

printPrimesUpTo :: Int -> IO ()
printPrimesUpTo n = do
  putStrLn $ "Prime numbers up to " ++ show n ++ ":"
  mapM_ (\x -> if isPrime x then print x else return ()) [2..n]

main :: IO ()
main = do
  let n = 10
  printPrimesUpTo n
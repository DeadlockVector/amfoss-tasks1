defmodule PrimeNumbers do
  def is_prime(2), do: true
  def is_prime(n) when n <= 1, do: false
  def is_prime(n) when rem(n, 2) == 0, do: false
  def is_prime(n) do
    is_prime(n, 3)
  end

  defp is_prime(n, divisor) when divisor * divisor > n, do: true
  defp is_prime(n, divisor) when rem(n, divisor) == 0, do: false
  defp is_prime(n, divisor) do
    is_prime(n, divisor + 2)
  end

  def print_primes(n) when n < 2, do: IO.puts("No prime numbers.")
  def print_primes(n) do
    Enum.each(2..n, fn num ->
      if is_prime(num) do
        IO.puts(num)
      end
    end)
  end
end

PrimeNumbers.print_primes(10) 
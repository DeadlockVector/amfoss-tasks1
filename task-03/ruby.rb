print "Enter the number: "
n = gets.to_i

for i in 1..n-1
    factors = 1

    for j in 2..i
        if i % j == 0
            factors += 1
        end
    end

    if factors == 2
        puts "#{i} is a prime number"
    end
end

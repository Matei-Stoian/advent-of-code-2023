input = File.readlines('input.txt',chomp:true)

def extrapolate(series)
    ans = series[-1]
    while series.any? {|diff| diff != 0}
        series = series.each_cons(2).map{|a,b| b-a}
        ans += series[-1]
    end
    return ans
end


ans1 = input.map{|line| extrapolate(line.split.map(&:to_i))}.sum
ans2 = input.map{|line| extrapolate(line.split.map(&:to_i).reverse)}.sum
p "Part 1: #{ans1}"
p "Part 2: #{ans2}"

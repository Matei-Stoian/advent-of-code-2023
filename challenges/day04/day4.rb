require 'benchmark'
class Card
    attr_reader :winners, :nums, :matches
    attr_accessor :copies
    
    def initialize(winners,nums)
        @winners,@nums = winners,nums
        @matches = get_matches
        @copies = 1
    end
    
    def get_value
        matches = @nums.size - (@nums - @winners).size
        return 0 if matches == 0
        return 2**(matches - 1)
    end

    private
        def get_matches
            @matches = @nums.size - (@nums - @winners).size
        end
end

class Solution
    attr_reader :input
    def initialize(file_path)
        @input = File.readlines(file_path,chomp:true)
    end
    def part1
        cards = []
        @input.each do |line|
            lists = line.split(": ")[1].split(" | ")
            cards.push(Card.new(lists[0].split(" "),lists[1].split(" ")))
        end
        res = cards.sum{|c| c.get_value}
        res
    end
    
    def part2
        cards = {}
        @input.each_with_index do |line,i|
            lists = line.split(": ")[1].split(" | ")
            cards[i] = Card.new(lists[0].split(" "),lists[1].split(" "))
        end
        cards.each do |i,card|
            card.copies.times do
                card.matches.times do |n|
                    cards[i+n+1].copies +=1
                end
            end
        end
        res = cards.sum{|i, c| c.copies}
    end
    def solve()
        puts "Result for the part 1 is: #{part1()}\nResult for part 2 is: #{part2()}"
    end
end

time = Benchmark.realtime do
    s = Solution.new("input.txt")
    s.solve()
end

puts "Execution Time: #{time} seconds"


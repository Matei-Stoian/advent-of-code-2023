class Solution
    attr_accessor :input 
    @@number_words =  {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
      }
    def initialize(file_path)
        @input = File.readlines(file_path,chomp:true)
    end
    def part1
        ans = 0
        @input.each do |line|
            res_string = line.gsub(/\D/,'')
            number = (res_string[0]+res_string[-1]).to_i
            ans += number 
        end
        p "Part 1: #{ans}"
    end
    
    def part2
        ans = 0
        @input.each do |line|
            ans += (first_appearance(line) + last_appearance(line)).to_i
        end
        p "Part 2: #{ans}"
    end
    def first_appearance(line)
        res = nil
        i = line.length

        @@number_words.each do |key,value|
            key = key.to_s
            if (line.include?(key) && line.index(key) < i)
                i = line.index(key)
                res = @@number_words[key.to_sym]
            end
        end
        only_digits = line[0..i].gsub(/\D/,'')
        if not only_digits[0].nil?
            res = only_digits[0]
        end
        res.to_s
    end
    def last_appearance(line)
        res = nil
        i = 0

        @@number_words.each do |key, value|
            key = key.to_s
            if (line.include?(key) && line.rindex(key) >= i)
                i = line.rindex(key)
                res = @@number_words[key.to_sym]
            end
        end
        
        only_digits = line[i..-1].gsub(/\D/,'')
        if not only_digits[0].nil?
            res = only_digits[-1]
        end
        res.to_s
    end
    def solve
        part1()
        part2()
    end
    private :first_appearance, :last_appearance
end 

s = Solution.new("input.txt")
s.solve()
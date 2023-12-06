class Solution
    attr_accessor :input
    def initialize(file_path)
        @input = File.readlines(file_path,chomp:true)
    end
    def solve
        part1()
        part2()
    end
    def part1         
        times = @input[0].scan(/\d+/).map(&:to_i)
        dists = @input[1].scan(/\d+/).map(&:to_i)
        ans = 1
        for i in 0..(times.size()-1) do
            time = times[i]
            cnt = 0
            for d in 1..time-1 do
                dist = d*(time-d)
                if dist > dists[i] 
                    cnt+=1  
                end
            end
            ans *= cnt
        end
        p "Part 1: #{ans}"
    end
    def part2 
        times = @input[0].scan(/\d+/).map(&:to_i).map(&:to_s)
        dists = @input[1].scan(/\d+/).map(&:to_i).map(&:to_s)
        realTime = ""
        realDist = ""
        for time in times do
            realTime << time
        end
        for dist in dists do
            realDist << dist
        end
        realTime = realTime.to_i
        realDist = realDist.to_i
        st = 1
        dr = realTime-1
        poz = realTime
        while st<=dr do
            mid = (st + (dr-st))//2
            dist = mid*(realTime-mid)
            if realDist <= dist 
                poz = mid
                dr = mid-1
            else
                st = mid+1
            end
        end
        leftSide,rigtSide = poz,realTime-poz
        p "Part 2: #{rigtSide-leftSide+1}"
    end
end

s = Solution.new('sample.txt')
s.solve()
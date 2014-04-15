=begin
 d20 System Stat Roller (Ruby)
 Details: Rolls 4 dice dropping the lowest and adding them, 6 times.  Stores in an array, and prints at the end.
 Program by Andrew Delso 
=end

    @statroll = []
    
    for i in 0..5
      @r1 = 1+rand(6)
      @r2 = 1+rand(6)
      @r3 = 1+rand(6)
      @r4 = 1+rand(6)
      
      if @r1<@r2 && @r1<@r3 && @r1<@r4
        @statroll[i] = @r2+@r3+@r4
      elsif @r2<@r1 && @r2<@r3 && @r2<@r4
        @statroll[i] = @r1+@r3+@r4
      elsif @r3<@r1 && @r3<@r2 && @r3<@r4
        @statroll[i] = @r1+@r2+@r4
      else
        @statroll[i] = @r1+@r2+@r3
      end
    end
    puts "The end result of your stat roll was: #{@statroll[0]}, #{@statroll[1]}, #{@statroll[2]}, #{@statroll[3]}, #{@statroll[4]}, #{@statroll[5]}."
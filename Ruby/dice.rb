#!/usr/bin/ruby

numRolls = Integer(ARGV[0])
sides = Integer(ARGV[1])
allRolls = []

#### returns array of dice rolls ####
def RollDice(numberOfRolls, numberOfSides)
  arr = []
  puts "\nRolling Dice..."
  for i in 0..(numberOfRolls - 1)
    #print "#{i} "
    arr[i] = rand(numberOfSides) + 1
  end
  return arr
end

allRolls = RollDice(numRolls, sides)

sleep 5

puts "\nInitial roll:\n"
for i in allRolls
  print "#{i} "
end

#### reroll a single value of 1, if found ####
foundOne = false
if allRolls.min == 1 # there's at least one item in the array with a value of 1
  puts "\n\nRolled at least one 1, rerolling that value... "
  #for i in allRolls
  i = 0
  while !foundOne # have we found our first value of 1 yet?
    while allRolls[i] == 1 # keep rerolling until we get a value that isn't 1
  	  allRolls[i] = rand(sides) + 1
  	  foundOne = true # we found our first value of 1, that should break us out of the outside while
  	end
  	i += 1
  end
  
  sleep 3
    
  puts "\nNew roll:\n"
  for i in allRolls
    print "#{i} "
  end
else
    puts "\n\nYour roll containted no 1's to re-roll"
end

puts "\n\n"
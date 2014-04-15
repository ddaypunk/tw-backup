STATS = ['stat1','stat2','stat3','stat4','stat5','stat6']
def stat_roller
  stats_rolled = Hash.new
  STATS.each do |stat|
    puts "Rolling for #{stat}..."
    rolls = Array.new
    4.times do
      i = 1 + rand(7)
      rolls << i
    end
    rolls.sort!.pop
    rolled_stat = 0
    rolls.each do |roll|
      rolled_stat += roll.to_i
    end
    stats_rolled[stat] = [rolled_stat]
  end
  puts "Results:"
  stats_rolled.each do |stat,roll|
    puts "#{stat} -> #{roll}"
  end
end
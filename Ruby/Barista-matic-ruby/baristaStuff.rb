class Drink
  attr_accessor :dname, :ing1, :ing2, :ing3, :ing4
  
  def initialize(dname, ing1, ing2, ing3, ing4)
    @dname = dname
    @ing1 = ing1
    @ing2 = ing2
    @ing3 = ing3
    @ing4 = ing4
  end
  
  def self.find_by_name(dname)
    found = nil
    ObjectSpace.each_object(Drink) { |o|
      found = o if o.dname == dname
      }
      found
  end
end
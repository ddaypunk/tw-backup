def Drink
  @name = nil
  @ingredients = Array.new[]
  @price = nil
  attr_accessor :name, :ingredients, :price  
end

def Ingredient
  @name = nil
  @price = nil
  attr_accessor :name, :price
end

def Inventory
  @item = Ingredient.new
  @amount = nil
  attr_accessor :item, :amount
end


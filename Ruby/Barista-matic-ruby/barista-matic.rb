#!/usr/bin/ruby

=begin
Barista-matic (Ruby)
By: Andrew Delso
April 2012
=end

#define Drink class and methods
class Drink
  Cprice = 0.75
  Dprice = 0.75
  Sprice = 0.25
  CRprice = 0.25
  SMprice = 0.35
  FMprice = 0.35
  Eprice = 1.10
  COprice = 0.90
  Wprice = 1.00
  
  def price(drink)
    if drink == 1 #should probably be the name of the drink if you can pass a string properly
      3*Eprice
    end
    if drink == 2 #should probably be the name of the drink if you can pass a string properly
      (2*Eprice)+SMprice
    end
  end
end

#declare global variables
#P_HASH = Hash["CPRICE" =>0.75, "DPRICE" =>0.75, "SPRICE" =>0.25, "CPRICE" =>0.25, "SMPRICE" =>0.35, "FMPRICE" =>0.35, "EPRICE"  =>1.10, "COPRICE"  =>0.90, "WPRICE"  =>1.00]


#declare local variables
choice = '0'
#declare ingredients and inventory using arrays
ingredients = ["Cocoa", "Coffee", "Cream", "Decaf", "Espresso", "Foam", "Steam", "Sugar", "Whipped"]
inventory = [10, 10, 10, 10, 10, 10, 10, 10, 10]

#outer control loop for main application
until choice == 'q' || choice == 'Q'
#display program title
puts "*==============================*\n"
puts "|Welcome to Barista-Matic:     |\n"
puts "|Your daily dose of caffeine!!!|\n"
puts "*==============================*\n\n"

#loop version of display inventory using array
puts "Current Inventory: (using array)\n"
puts "------------------\n\n"
for i in 0..8
    puts "#{ingredients[i]}, #{inventory[i]}\n\n"
end 
#end of ingredient inventory print loop

#begin simple version of printing the menu
#display menu
  puts "Current Menu:\n"
  puts "-------------\n\n"
  puts "1,Caffe Americano,$#{Drink.price(1)}\n\n"
  puts "2,Caffe Latte,$#{Drink.price(2)}\n\n"
  #puts "3,Caffe Mocha,$" << (ESPRESSO_PRICE+COCOA_PRICE+SMILK_PRICE+WHIPPED_PRICE) << "," << mocha_status << "\n\n"
  #puts "4,Cappuccino,$" << (2*ESPRESSO_PRICE+SMILK_PRICE+FMILK_PRICE) << "," << cappucinno_status << "\n\n"
  #puts "5,Coffee,$" << (3*COFFEE_PRICE+SUGAR_PRICE+CREAM_PRICE) << "," << coffee_status << "\n\n"
  #puts "6,Decaf Coffee,$" << (3*DECAF_PRICE+SUGAR_PRICE+CREAM_PRICE) << "," << decaf_status << "\n\n"
  puts "\n\n"

#print the input request message and take the selection
puts "Please select a drink # and hit the return key.  To exit, type \"q\" or \"Q\", and then hit the return key..."
choice = gets.chomp #take user input for the until loop

#determine what to do with the choice

end #end of until loop
#end ruby script
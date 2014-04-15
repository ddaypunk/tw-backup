require 'bigdecimal'
#require 'baristafuncs.rb'
#require 'baristadecs.rb'

  #declare price constants
  Cprice = BigDecimal.new("0.75")
  Dprice = BigDecimal.new("0.75")
  Sprice = BigDecimal.new("0.25")
  CRprice = BigDecimal.new("0.25")
  SMprice = BigDecimal.new("0.35")
  FMprice = BigDecimal.new("0.35")
  Eprice = BigDecimal.new("1.10")
  COprice = BigDecimal.new("0.90")
  Wprice = BigDecimal.new("1.00")
  
  #declare drink constants
  CAtotal = 3*Eprice
  CLtotal = 2*Eprice+SMprice
  CMtotal = Eprice+COprice+SMprice
  Captotal = 2*Eprice+SMprice+FMprice
  Cofftotal = 3*Cprice+Sprice+CRprice
  Decaftotal = 3*Dprice+Sprice+CRprice
  
  #declare ingredients and inventory using arrays
  ingredients = ["Cocoa", "Coffee", "Cream", "Decaf", "Espresso", "Foam", "Steam", "Sugar", "Whipped"]
  inventory = [10, 10, 10, 10, 10, 10, 10, 10, 10]
  drinks = ["Caffe Americano", "Caffe Latte", "Caffe Mocha", "Capuccino", "Coffee", "Decaf Coffee"]
  prices = [CAtotal.to_s("F"), CLtotal.to_s("F"), CMtotal.to_s("F"), Captotal.to_s("F"), Cofftotal.to_s("F"), Decaftotal.to_s("F")]
  menu_choice = 'r'

#begin shoes application window
Shoes.app :title => "Barista-Matic",
          :width => 450,
          :height => 525 do
  background green..black
    
    #full stack for the header
    stack :width => "100%" do
      @header = tagline "*==============================*\n            Welcome to Barista-Matic:        \n            Your daily dose of caffeine        \n*==============================*\n\n"
      @header.style :stroke => silver
    end
    
  #while (menu_choice != 'q') || (menu_choice != 'Q') do
  
    #stack and flow for the left hand inventory
    stack :width => "50%" do
      flow :width => "100%" do
      
    #loop version of display inventory using array
        @inventorytitle = para "Current Inventory: \n------------------------\n"
        @inventorytitle.style :stroke => silver
      
        for i in 0..8
            @inventoryline = para "#{ingredients[i]}: #{inventory[i]}\n"
            @inventoryline.style :stroke => silver
        end
      end
    end
  
    #stack and flow for the right hand menu
    stack :width => "50%" do
      flow :width => "100%" do
      
        #loop version of display menu with prices using array
        @menutitle = para "Current Menu:\n-------------------\n"
        @menutitle.style :stroke => silver
      
        for j in 0..5
          @menuline = para "#{drinks[j]}: #{prices[j]}\n" #add Price here after figuring out how to best accomplish it
          @menuline.style :stroke => silver
        end
      end  
    end
  
    #stack for the input
    flow :width => "100%" do
      @inputarea = para "Enter the drink you would like:"
      @inputarea.style :stroke => silver
      @choice = edit_line :width => 100
      button "Dispense" do
        if @choice.text == "1"
          alert "Dispensing Caffe Americano...\n\nCAUTION: Dispensed drinks are VERY HOT!!!"
          inventory[5] = inventory[5] - 3
        end
        #end of dispense button
        
        stack :width => "100%" do
          @espressostatus = para "Current Espresso is #{inventory[5]}"
          @espressostatus.style :stroke => silver
          @footermenuoptions = para "\nIf you would like to Quit, please enter Q or q.\n\nIf you would like to reset the menu, please enter R or r."
          @footermenuoptions.style :stroke => silver
        end
        #end of footer and status  
      end
      #end of button actions
      
   #end of input flow
   end
#end of Shoes.app
end
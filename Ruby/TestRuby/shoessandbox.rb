  Shoes.app(:title => "Dice Roller") {
     background green
     
     stack do
       para "Choose the amount of sides into the box and then click the button"
       
       list_box :items => ["coin", "d4", "d6", "d8", "d10", "d12"],
         :width => 100, :choose => "d6"
       @choice.text = list.text
       @rollpress = button "Push to Roll"
       @rolltext = para "The button has not been pressed yet..."
     end    
          
     @rollpress.click {
       @roll1 = 1+rand(6)
       @rolltext.replace "You rolled a #{@roll1} on a #{@choice} die"
     }
 }
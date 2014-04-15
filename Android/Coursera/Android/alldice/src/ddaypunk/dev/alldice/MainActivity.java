package ddaypunk.dev.alldice;

import java.util.Random;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.widget.TextView;
import android.widget.Spinner;
//import android.content.Context;
//import android.widget.Toast;

public class MainActivity extends Activity {
	//Create all variables globally for use in methods
	TextView rollResultView;
	Spinner numSidesSpinner;
	String numSidesStr;
    Random roll;
    int current_roll;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        //initialize global variables on app creation (find views, create kicker message, etc)
        rollResultView = (TextView)findViewById(R.id.textView1);
        numSidesSpinner = (Spinner)findViewById(R.id.spinner1);
        roll = new Random();   
        rollResultView.append("Please select a die type from the drop down and click ROLL!!!");

    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
    
    public void RollDice(View arg0){
    	//Each time the button to roll is pressed
    	//Grab the current spinner selection
    	//Set the textView back to blank
    	//Roll and print the results
        numSidesStr = numSidesSpinner.getSelectedItem().toString();
    	rollResultView.setText("");
    	current_roll = (roll.nextInt(numOfSides(numSidesStr))) +1;
    	
    	//display coin based messages if coin type chosen
    	if (numSidesStr.equals("d2 (coin flip)")){
    		if (current_roll == 1){
    			rollResultView.append("The coin flip shows HEADS!");
    		}
    		else{
    			rollResultView.append("The coin flip shows TAILS!");
    		}
    	}
    	//otherwise display formatted roll result
    	else{
    		rollResultView.append("You rolled a " + current_roll + " on a " + numSidesStr);
    		rollResultView.append("\n\nPlease feel free to select a new die, and ROLL AGAIN!");
    	}
    }
    
	//No longer used, but this was a tip shown when button is clicked
    //This was the first way I found out to display information to the screen
    //Then I found out a way to append it to the text view
    // so this code is not needed
    /*public void tToast(String s){
    	Context context = getApplicationContext();
    	int duration = Toast.LENGTH_LONG;
    	Toast toast = Toast.makeText(context, s, duration);
    	toast.show();
    }*/
    
	//method to convert string menu choice of sides to int
    public int numOfSides(String s){
    	if (s.equals("d2 (coin flip)")){
    		return 2;
    	}
    	
    	else if (s.equals("d4")){
    		return 4;
    	}
    	
    	else if (s.equals("d6")){
    		return 6;
    	}
    	
    	else if (s.equals("d8")){
    		return 8;
    	}
    	else if (s.equals("d10")){
    		return 10;
    	}

    	else if (s.equals("d20")){
    		return 20;
    	}
    	else if (s.equals("d100 (%)")){
        	return 100;
    	}
    	else{
    		return 0;
    	}
    }
}

package ddaypunk.dev.simplerpggen;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.app.Activity;
import android.content.Intent;

public class ResultsActivity extends Activity {

	private TextView mTextView1;
	private TextView mTextView2;
	private TextView mTextView3;
	private TextView mTextView4;
	private TextView mTextView5;
	private TextView mTextView6;
	private TextView mTextView7;
	private TextView mTextView8;
	private TextView mTextView9;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_results);
		
		//extract bundle of extras from last two activities
		Intent intent = getIntent();
		Bundle extras = intent.getExtras();
		
		//unpack the bundle into singular strings
		String playername_string = extras.getString("EXTRA_PLAYERNAME");
		String charactername_string = extras.getString("EXTRA_CHARACTERNAME");
		String definingchars_string = extras.getString("EXTRA_DEFININGCHARACTERISTICS");
		String gender_string = extras.getString("EXTRA_GENDERSELECTION");
		String height_string = extras.getString("EXTRA_CHARACTERHEIGHT");
		String weight_string = extras.getString("EXTRA_CHARACTERWEIGHT");
		String race_string = extras.getString("EXTRA_RACESELECTION");
		String archetype_string = extras.getString("EXTRA_ARCHETYPE");
		String career1_string = extras.getString("EXTRA_CAREER1");
		String career2_string = extras.getString("EXTRA_CAREER2");
		
		
		//identify all text views for the character sheet
		mTextView1 = (TextView) findViewById(R.id.resultView1);
		mTextView2 = (TextView) findViewById(R.id.resultView2);
		mTextView3 = (TextView) findViewById(R.id.resultView3);
		mTextView4 = (TextView) findViewById(R.id.resultView4);
		mTextView5 = (TextView) findViewById(R.id.resultView5);
		mTextView6 = (TextView) findViewById(R.id.resultView6);
		mTextView7 = (TextView) findViewById(R.id.resultView7);
		mTextView8 = (TextView) findViewById(R.id.resultView8);
		mTextView9 = (TextView) findViewById(R.id.resultView9);
		
		mTextView1.append("\t\t" + playername_string);
		mTextView2.append("\t\t" + charactername_string);
		mTextView3.append("\t\t" + gender_string);
		mTextView4.append("\n" + definingchars_string);
		mTextView5.append("\t\t" + height_string);
		mTextView6.append("\t\t" + weight_string);
		mTextView7.append("\t\t" + race_string);
		mTextView8.append("\t\t" + archetype_string);
		mTextView9.append("\t\t" + career1_string + " & " + career2_string);

	}

}

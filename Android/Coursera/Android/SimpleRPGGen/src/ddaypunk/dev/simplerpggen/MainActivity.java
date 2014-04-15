package ddaypunk.dev.simplerpggen;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.View;
import android.widget.EditText;
import android.widget.Spinner;

public class MainActivity extends Activity {

	// request all members for this activity
	private EditText mPlayerName;
	private EditText mCharacterName;
	private EditText mDefiningCharacteristics;
	private Spinner mGenderSelection;
	private EditText mCharacterHeight;
	private EditText mCharacterWeight;
	private Spinner mRaceSelection;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);

		// initialize all members to UI component ids
		mPlayerName = (EditText) findViewById(R.id.editText1);
		mPlayerName.requestFocus();
		mCharacterName = (EditText) findViewById(R.id.editText2);
		mDefiningCharacteristics = (EditText) findViewById(R.id.editText3);
		mGenderSelection = (Spinner) findViewById(R.id.spinner1);
		mCharacterHeight = (EditText) findViewById(R.id.editText4);
		mCharacterWeight = (EditText) findViewById(R.id.editText5);
		mRaceSelection = (Spinner) findViewById(R.id.spinner2);
		
		
		
	}
	
	public void onSaveButtonClick(View view) {
		Intent intent = new Intent(this, SecondaryActivity.class);
		Bundle extras = new Bundle();
		extras.putString("EXTRA_PLAYERNAME", mPlayerName.getText().toString());
		extras.putString("EXTRA_CHARACTERNAME", mCharacterName.getText().toString());
		extras.putString("EXTRA_DEFININGCHARACTERISTICS",mDefiningCharacteristics.getText().toString());
		extras.putString("EXTRA_GENDERSELECTION", mGenderSelection.getSelectedItem().toString());
		extras.putString("EXTRA_CHARACTERHEIGHT", mCharacterHeight.getText().toString());
		extras.putString("EXTRA_CHARACTERWEIGHT", mCharacterWeight.getText().toString());
		extras.putString("EXTRA_RACESELECTION", mRaceSelection.getSelectedItem().toString());
		intent.putExtras(extras);
		MainActivity.this.startActivity(intent);

	}
}

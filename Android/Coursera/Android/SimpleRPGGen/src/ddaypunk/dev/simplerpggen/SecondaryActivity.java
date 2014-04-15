package ddaypunk.dev.simplerpggen;

//import java.util.ArrayList;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.View;
import android.widget.Spinner;

public class SecondaryActivity extends Activity {

	private Spinner mArchetypeSelection;
	private Spinner mCareer1Selection;
	private Spinner mCareer2Selection;
	Bundle extras;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_secondary);
		
		//grab the extras from the first activity
		extras = getIntent().getExtras();
		
		mArchetypeSelection = (Spinner) findViewById(R.id.spinner1);
		mCareer1Selection = (Spinner) findViewById(R.id.spinner2);
		mCareer2Selection = (Spinner) findViewById(R.id.spinner3);

		
		//Build array for career selections from file in the future
		//this should allow me to remove selection from the first box before 
		//displaying to the second
		//ArrayList<String> spinnerArray = new ArrayList<String>();
		
	}

	
	public void onSaveButtonClick(View view) {
		Intent intent = new Intent(this, ResultsActivity.class);
		extras.putString("EXTRA_ARCHETYPE", mArchetypeSelection.getSelectedItem().toString());
		extras.putString("EXTRA_CAREER1", mCareer1Selection.getSelectedItem().toString());
		extras.putString("EXTRA_CAREER2",mCareer2Selection.getSelectedItem().toString());
		intent.putExtras(extras);
		SecondaryActivity.this.startActivity(intent);

	}

}

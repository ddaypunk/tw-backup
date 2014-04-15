package ddaypunk.dev.androidreference;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.View;

public class MainActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
	}

	//@Override
	//public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		//getMenuInflater().inflate(R.menu.main, menu);
		//return true;
	//}

	public void onDroidRefButton(View view){
		//when button is pressed, create activity intent and send extra info
		Intent intent = new Intent(MainActivity.this, RefWEbActivity.class);
		intent.putExtra("page", "http://developer.android.com/index.html");
		MainActivity.this.startActivity(intent);
		
	}
	
	public void onStackOverflowButton(View view){
		//when button is pressed, create activity intent and send extra info
		Intent intent = new Intent(MainActivity.this, RefWEbActivity.class);
		intent.putExtra("page", "http://stackoverflow.com/questions/tagged/android");
		MainActivity.this.startActivity(intent);
	}
	
	public void onDeviceRefButton(View view){
		//when button is pressed, create activity intent and send extra info
		Intent intent = new Intent(MainActivity.this, RefWEbActivity.class);
		intent.putExtra("page", "http://blog.blundell-apps.com/list-of-android-devices-with-pixel-density-buckets/");
		MainActivity.this.startActivity(intent);	
	}
	
	public void onAssetStudioButton(View view){
		//when button is pressed, create activity intent and send extra info
		Intent intent = new Intent(MainActivity.this, RefWEbActivity.class);
		intent.putExtra("page", "http://android-ui-utils.googlecode.com/hg/asset-studio/dist/index.html?utm_content=bufferbcc6a&utm_source=buffer&utm_medium=twitter&utm_campaign=Buffer");
		MainActivity.this.startActivity(intent);	
	}
	
	public void onDroidDevGroupButton(View view){
		//when button is pressed, create activity intent and send extra info
		Intent intent = new Intent(MainActivity.this, RefWEbActivity.class);
		intent.putExtra("page", "https://groups.google.com/forum/#!forum/android-developers");
		MainActivity.this.startActivity(intent);	
	}
	
}

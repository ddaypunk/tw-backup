package ddaypunk.dev.emilyssong;

import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.util.Log;
import android.view.Menu;
import android.view.View;

public class MainActivity extends Activity {

	// Create global attributes
	// Initialize if timing not needed
	MediaPlayer mysong;
	String url1 = "http://www.facebook.com/TheDelso";
	String url2 = "http://www.bandcamp.com";

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		Log.e("STATUS", "EmilySong Created");
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
	}

	@Override
	protected void onResume() {
		Log.e("STATUS", "EmilySong Resumed");
		mysong = MediaPlayer.create(this, R.raw.norasong);
		mysong.start();
		super.onResume();
	}

	@Override
	protected void onPause() {
		Log.e("STATUS", "EmilySong Paused!");
		mysong.stop();
		mysong.release();
		super.onPause();
	}

	// @Override
	// protected void onStop() {
	// Log.e("STATUS", "EmilySong Stopped");
	// mysong.stop();
	// mysong.release();
	// super.onStop();
	// }

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	public void openFacebook(View v) {
		Intent i = new Intent(Intent.ACTION_VIEW);
		i.setData(Uri.parse(url1));
		startActivity(i);
	}

	public void openBandcamp(View v) {
		Intent i = new Intent(Intent.ACTION_VIEW);
		i.setData(Uri.parse(url2));
		startActivity(i);
	}

}

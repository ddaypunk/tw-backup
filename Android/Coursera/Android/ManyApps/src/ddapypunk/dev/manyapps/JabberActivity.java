package ddapypunk.dev.manyapps;

import android.app.Activity;
import android.content.Intent;
import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Bundle;
//import android.util.Log;
import android.view.KeyEvent;
import android.view.View;
import android.webkit.WebView;

public class JabberActivity extends Activity {
	
	//Create global variables
	WebView ptrWebview;
	MediaPlayer music;
	
	//Create and initialize strings for later uses
	String wiki_url = "http://en.wikipedia.org/wiki/Jabberwocky";
	String pic_url = "http://cache.desktopnexus.com/thumbnails/784669-bigthumbnail.jpg";
	String jabber_asset = "file:///android_asset/jabberwocky.html";
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_jabber);
		
		//Find webView1 when created and store address in pointer
		ptrWebview = (WebView) findViewById(R.id.webView1);
		ptrWebview.getSettings().setBuiltInZoomControls(true);
		ptrWebview.loadUrl(jabber_asset);
		
		//start playing music after page loads
	    
	}
	
	// DEFINE MUSIC RELATED METHODS
	@Override
	protected void onResume() {
		//create the media player and start playing
		music = MediaPlayer.create(this, R.raw.battle);
		music.setLooping(true); //allow it to loop
		music.start();
		super.onResume();
	}

	@Override
	protected void onPause() {
		//stop and release the song when paused
		music.stop();
		music.release();
		super.onPause();
	}
	
	//DEFINE CONTROL OF BACK BUTTON
	public boolean onKeyDown(int keyCode, KeyEvent event) {
	    // Check if the key event was the Back button and if there's history
	    if ((keyCode == KeyEvent.KEYCODE_BACK) && ptrWebview.canGoBack()) {
	    	ptrWebview.goBack();
	        return true;
	    }
	    // If it wasn't the Back key or there's no web page history, bubble up to the default
	    // system behavior (probably exit the activity)
	    return super.onKeyDown(keyCode, event);
	}
	
	//DEFINE HANDLING OF SCREEN BUTTONS
	public void onWikiButton(View view){
		//create and initiate intent for new activity
		Intent i = new Intent(Intent.ACTION_VIEW);
		i.setData(Uri.parse(wiki_url));
		startActivity(i);
	}
	
	public void onPicButton(View view){
		//Check the current page displayed when the button is pressed
		//NOTE: If the user presses the button multiple times
		//This will cycle back through the presses
		if (ptrWebview.getOriginalUrl().equals(pic_url)){
			ptrWebview.loadUrl(jabber_asset);

		}
		else { ptrWebview.loadUrl(pic_url);}
	}

}

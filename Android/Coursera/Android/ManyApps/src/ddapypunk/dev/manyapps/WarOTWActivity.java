package ddapypunk.dev.manyapps;

import android.app.Activity;
import android.os.Bundle;
import android.view.KeyEvent;
import android.webkit.WebView;

public class WarOTWActivity extends Activity {
    
	//Create global pointer for webView1
	WebView ptrWebview;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_war_otw);
		
		//Find webView1 when created and store address in pointer
		ptrWebview = (WebView) findViewById(R.id.webView1);
		ptrWebview.getSettings().setBuiltInZoomControls(true);
		ptrWebview.loadUrl("file:///android_asset/waroftheworlds.html");

	}
	
	@Override
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

}

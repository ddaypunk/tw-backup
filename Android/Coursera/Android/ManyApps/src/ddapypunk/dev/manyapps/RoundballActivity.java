package ddapypunk.dev.manyapps;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;

public class RoundballActivity extends Activity {
    
	//Create global pointer for webView1
	WebView ptrWebview;
	
	//it was not in the instructions, but you can suppress the lint warning here
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_war_otw);
		
		
		//Find webView1 when created and store address in pointer
		ptrWebview = (WebView) findViewById(R.id.webView1);
		
		//enable needed settings to run the javascript	
		ptrWebview.getSettings().setJavaScriptEnabled(true);
		ptrWebview.getSettings().setDomStorageEnabled(true);
		
		//load the html into the webview, and it will do the rest
		ptrWebview.loadUrl("file:///android_asset/roundball/roundball.html");
	}


}

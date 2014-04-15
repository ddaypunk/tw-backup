package ddapypunk.dev.manyapps;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;

public class UofI_NasaActivity extends Activity {
	
	//Create global pointer for webView1
	WebView ptrWebview;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_war_otw);
		
		//Find webView1 when created and store address in pointer
		ptrWebview = (WebView) findViewById(R.id.webView1);
		ptrWebview.getSettings().setBuiltInZoomControls(true);
		ptrWebview.loadUrl("file:///android_asset/uofi-at-nasa.html");
	}


}

package ddaypunk.dev.javabook;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.webkit.WebView;

public class NasaActivity extends Activity {
	
	WebView ptr_webView;


	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		ptr_webView = (WebView) findViewById(R.id.webView1);
		
		ptr_webView.getSettings().setBuiltInZoomControls(true);
		//ptr_webView.getSettings().setJavaScriptEnabled(true);
		
		ptr_webView.loadUrl("file:///android_asset/nasa.html");
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.nasa, menu);
		return true;
	}

}

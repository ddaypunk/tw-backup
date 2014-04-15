package ddaypunk.dev.androidreference;

import android.os.Bundle;
import android.app.Activity;
import android.webkit.WebView;
import android.annotation.SuppressLint;

public class RefWEbActivity extends Activity {
	
	WebView webview;
	//we know javascript allows XSS, so suppress the warning
	@SuppressLint("SetJavaScriptEnabled")
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_ref_web);
		// Show the Up button in the action bar.
		
		//Using the extra from main activity, display the page
		WebView webview = (WebView) findViewById(R.id.webView1);
		Bundle extras = getIntent().getExtras();
		webview.loadUrl(extras.getString("page"));
		webview.getSettings().setBuiltInZoomControls(true);
		webview.getSettings().setJavaScriptEnabled(true);
		webview.getSettings().setDomStorageEnabled(true);
	}

}

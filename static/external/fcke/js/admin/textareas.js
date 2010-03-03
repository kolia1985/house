var fcks = new Array;

window.onload = function()
{
	// Deduce admin_media_prefix by looking at the <script>s in the
	// current document and finding the URL of *this* module.
        var scripts = document.getElementsByTagName('script');
        for (var i=0; i<scripts.length; i++) {
           if (scripts[i].src.match(/textareas/)) {
              var idx = scripts[i].src.indexOf('js/admin/textareas');
              admin_media_prefix = scripts[i].src.substring(0, idx);
	      break;
           }
	}

    // create the FCK Editor and replace the specific text area with it
    var nodeList=document.getElementsByTagName("textarea");
    for(var i=0;i<nodeList.length;i++)
    {
    	var elm=nodeList.item(i);
    	fcks[i] = new FCKeditor(elm.id);
    	fcks[i].BasePath = admin_media_prefix + "fckeditor/";	
    	fcks[i].Width = "800";
    	fcks[i].Height = "350";
    	
    	fcks[i].ReplaceTextarea();
    }                        
}

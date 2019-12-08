var doc = app.activeDocument;

var title = doc.name;
var title = title.substring(0, title.length - 3);
 
var hide = function (){ // hide all layers (based on http://forums.adobe.com/thread/644267)
     var L=doc.layers.length;
     for (j=0;j<L;j++){  doc.layers[j].visible=false; }
}
hide();
 
 
// loop through all layers
for (var i = 0; i < doc.layers.length; i++) {
 
 
 
 
 
              // Create the illusrtratorSaveOptions object to set the AI options
    var saveOpts = new IllustratorSaveOptions();
 
    // Setting IllustratorSaveOptions properties.
    saveOpts.embedLinkedFiles = true;
    saveOpts.fontSubsetThreshold = 0.0
    saveOpts.pdfCompatible = true
 
 
 
 
 
 
//Set up Variable to access layer name
          var currentLayer = app.activeDocument.layers[i];
 
// Loop through the layers and make the back ground layer visible
          if (currentLayer.name == "Background") {
                    docName = name + currentLayer.name+".eps";
                    currentLayer.visible = true;
                    }
 
 
}
 
 
// Delete Invisible Layers (based on http://www.cartotalk.com/index.php?showtopic=7491)
var myDoc=app.activeDocument;
var layerCount=myDoc.layers.length;
for (var ii = layerCount - 1; ii >= 0; ii--) {
    var currentLayer = myDoc.layers[ii];
    currentLayer.locked = false;
    var subCount = currentLayer.layers.length;
    for (var ss =subCount -1; ss >= 0; ss--){
        var subLayer = currentLayer.layers[ss];
        subLayer.locked = false;
        if (subLayer.visible == false){
            subLayer.visible = true;
            subLayer.remove();
            }
        }
    if (currentLayer.visible == false){
        currentLayer.visible = true;
        currentLayer.remove();
        }
    }
 
// Save Out Document with New Name
 
var saveName = new File ( doc.path + "/" + docName );
doc.saveAs( saveName, saveOpts );
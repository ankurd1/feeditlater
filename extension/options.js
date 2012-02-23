var defaultKey = "blue";	 
	function loadOptions() {
	    var currentKey = localStorage["Key"];
	 
	    // valid colors are red, blue, green and yellow
	    if (currentKey=="")) {
	        currentKey = defaultKey;
	    }
	 
	    var select = document.getElementById("color");
	    for (var i = 0; i < select.children.length; i++) {
	        var child = select.children[i];
	            if (child.value == currentKey) {
	            child.selected = "true";
	            break;
	        }
	    }
	}
	 
	function saveOptions() {
	    var select = document.getElementById("color");
	    var color = select.children[select.selectedIndex].value;
	    localStorage["Key"] = color;
	}
	 
	function eraseOptions() {
	    localStorage.removeItem("Key");
	    location.reload();
	}

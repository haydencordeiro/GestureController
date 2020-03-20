   
    function SaveGestures(){//save users choice of gestures
	var opt = G0.options[G0.selectedIndex];
	console.log( opt.value );
	eel.Index0(opt.value);
	var opt = G1.options[G1.selectedIndex];
	console.log( opt.value );
	eel.Index1(opt.value);
	alert("Gestures Have Been Set");
    }



	function getApps(){
		var names=document.getElementById("open_apps").value
		eel.multi_apps(names)

	}



function getInputValue()//store moodle id and password
{
var id = document.getElementById("id").value;
var pass = document.getElementById("pass").value;
eel.moodleLogin(id,pass)
alert("Moodle Id and Password successfully saved")
}
function end()//calls the main.py script 
{
	eel.end()
}


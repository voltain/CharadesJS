function generateWords(difficultylevel,wordtype,data){
		
		
	$('#diff1').removeClass('button');
	$('#diff2').removeClass('button');
	$('#diff3').removeClass('button');
	$('#diff1').removeClass('buttonselected');
	$('#diff2').removeClass('buttonselected');
	$('#diff3').removeClass('buttonselected');
	
	
	if (difficultylevel==1){
	$('#diff1').removeClass('button');
	$('#diff1').addClass('buttonselected');
	$('#diff2').addClass('button');
	$('#diff3').addClass('button');
	}
	
	if (difficultylevel==2){
	$('#diff2').removeClass('button');
	$('#diff2').addClass('buttonselected');
	$('#diff1').addClass('button');
	$('#diff3').addClass('button');
	}
	
	if (difficultylevel==3){
	$('#diff3').removeClass('button');
	$('#diff3').addClass('buttonselected');
	$('#diff1').addClass('button');
	$('#diff2').addClass('button');
	}
	
	
	var wordlist=[]
	var jsonData;
	
	    
	jsonData = JSON.parse(data);

	for (var i = 0; i < jsonData.activity.length; i++) {
		
		var counter = jsonData.activity[i];
	
		if ( counter.difficulty == difficultylevel && counter.type==wordtype ) { wordlist.push(counter.word);}
	
	}

	var chosenword = wordlist[Math.floor(Math.random()*wordlist.length)];
	return(chosenword);

		
};

function endCountdown() {
  $('#count_num').html("TIMEOUT!!!");
}

function handleTimer() {
  	if (count<=0){
  		$('#count_num').html("TIMEOUT!!!");
  	}
  	else {
  		$('#count_num').html("Countdown:  "+count);}

    count--;

}


	
function chooseDifficulty(level){

	jQuery.get('dictionary.json', function(data) {
		$('#count_num').html("START!!!");
		count=90;
		document.getElementById("word1").innerHTML = generateWords(level,"D",data);
		document.getElementById("word2").innerHTML = generateWords(level,"S",data);
		document.getElementById("word3").innerHTML = generateWords(level,"A",data);
		
	});

}

function playSound( url ){   
  document.getElementById("sound").innerHTML="<embed src='"+url+"' hidden=true autostart=true loop=false>";
}
var count=90;
var timer = setInterval(function() { handleTimer(count); }, 1000);




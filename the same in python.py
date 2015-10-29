import json
import random



jdata = json.loads(open ('convertcsv.json').read())

def gen(difficulty,type):
    chosenwords=[]
    for c in jdata:
        if c['difficulty']==1 and c["type"]=="P":
            chosenwords.append(c['word'])
        
    return(random.choice(chosenwords))

difficultyvar=1
print '''
<!doctype html>
<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->




<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>Activity 3</title>
  <meta name="description" content="">

  <meta name="viewport" content="width=device-width">
  
  <link rel="SHORTCUT ICON" href="favicon.ico"/>
  
  <script type="text/javascript">
    if (window.innerHeight <= 600) {
        loadcss('css/iphone.css');
    } else {
        loadcss('css/main.css');
    }

    function loadcss(file) {
        var el = document.createElement('link');
        el.setAttribute('rel', 'stylesheet');
        el.setAttribute('type', 'text/css');
        el.setAttribute('href', file);
        document.getElementsByTagName('head')[0].appendChild(el);
    }
</script>

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.js" type="text/javascript"></script>
<script type="text/javascript">
 
$(document).ready(function(){
 
        $(".slidingDiv").hide();
        $(".show_hide").show();
 
    $('.show_hide').click(function(){
    $(".slidingDiv").fadeIn('slow');
    });
    
    $('.hide').click(function(){
    $(".slidingDiv").fadeOut('slow');
    });
     

});
 
</script>









</head>
<body>
  <!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->
  <header>

  </header>
  <div role="main">
  
  <a href="#" class="show_hide">
    <div id="card" >
  
                  <div id="bar" class="one"><p >''' +gen(difficultyvar,"D")+'''<br /></p></div><div id="bar" class="two"><p >''' +gen(difficultyvar,"S")+'''<br /></p></div><div id="bar" class="three"><p >''' +gen(difficultyvar,"P")+'''<br /></p></div><div id="bar"  class="four"><p style="color:red;">''' +gen(difficultyvar,"D")+'''<br /></p></div><div id="bar"  class="five"><p style="color:red;">''' +gen(difficultyvar,"S")+'''<br /></p></div><div id="bar"  class="six"><p >''' +gen(difficultyvar,"P")+'''<br /></p></div>    
  
        
        
            
           
        </div>
        </a>
        <div id="menu">
        <p class="button"><a href="?level=1">3</p>
        
        <p class="button"><a href="?level=2">4</p>
        
        <p class="button"><a href="?level=3">5</p>
        </div>
        
        
<a href="#" class="hide"><div class="slidingDiv">
</div></a>

  </div>
  
  
  <footer>

  </footer>



</body>
</html>

'''

#Html_file= open("filename.html","w")
#Html_file.write(data)
#Html_file.close()

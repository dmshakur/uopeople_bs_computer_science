$("document").ready(function() {
    
    //toggle the toggle
	$(".dropdown-toggle").on("click", function(e) {
        //find the next ul (this will break if the submenu contains no ul) and turn it on or off
        //there is only one ul per .dropdown-toggle
		$(this).next('ul').toggle();
		e.stopPropagation();//dont trigger elements behind this one from being clicked (thus closing the parent menu)
		e.preventDefault();//dont do anything else
		//alert( $(this).attr("class") );
	});
	
	// this is an anchor with a .caret as a span inside it
	$(".dropdown-toggle").on("click", function(e) {
	
		//basically just a way to make the caret point back and forth every time its clicked
		//also add/remove a class to the currently opened directory
		if( $(this).find(".caret").hasClass("pointDown") ){
			$(this).find(".caret").removeClass("pointDown");
			$(this).removeClass("menu-item-opened");
		}
		else{
			$(this).find(".caret").addClass("pointDown");
			$(this).addClass("menu-item-opened");
		}
	});
	
	//this function matches a link in the side nav to the current window
	//it wont work in Cascade, only on a live site. this is because the full URL and href attributes used are different, due to GET variables; the links on the page are different from the window URL
	// ^^ fixed this
	function matchSideNavWindowURL() {
		
		//find every page link in the side navigation
		//this may be too slow when we have every page built
		// ^^ doesnt seem to have an effect
		$("#sidebar-navigation-selector").find(".side-active").each(function(index, e){
			
			//alert( "hello" );
			//alert( "URL of the link in the menu: "+e.href );
			//alert( "URL of current window: "+window.location.href );
		
        /*
            this would set up variables to be used in the Cascade fix
            had to comment this out because it would break in Internet Explorer AND Edge
            
			//turn the URL strings into URL object things
			//then extract GET value id
			var eurl = new URL(e.href);
			var eurlID = eurl.searchParams.get("id");
			//alert(eurlID);
			
			//do the same for the window URL
			var wurl = new URL(window.location.href);
			var wurlID = wurl.searchParams.get("id");
			//alert(wurlID);
        */
        
            // sets up variables so that this function still works in Cascade
            // pattern below modified from: http://papermashup.com/read-url-get-variables-withjavascript/
            var regexIDPattern = /[?&]+(id)=([^&]*)/g; // essentially matches the GET variable in the URL
            
            var eurlMatch = regexIDPattern.exec( e.href ); // get the GET from this element's URL
            regexIDPattern.lastIndex = 0; // apparently regex objects are stateful and need to be reset or whatever
            var wurlMatch = regexIDPattern.exec( window.location.href ); // get the GET from the window URL
            regexIDPattern.lastIndex = 0; // reset the thingy... ugh
            
            if (eurlMatch !== null){ //if something was found
                //console.log( "eurlID: " + eurlMatch[2] );
                var eurlID = eurlMatch[2]; //extract just the ID (the ID was the 2nd grouping in the regex)
            }
            if (wurlMatch !== null){
                //console.log( "wurlID: " + wurlMatch[2] );
                var wurlID = wurlMatch[2]; //extract just the ID
            }
            
            
            
			//if the current element's full href is equal to the window URL
            //no need to rely on the variables set up above
			if( e.href == window.location.href ){
				//a matching link was found in the side nav, and we can open the sidenav to that link
				openTreeView( $(this) );
			}
			//if no matching whole URL is found, we next see if theres a matching GET variable called ID
			//this is the fix for Cascade
            //neither of the ID values should be 'falsey' in any way
            //if for some reason EVERY sidenav link is being auto-opened, look here first, it may be thinking "undefined" = "undefined" or some such BS
			else if( eurlID !== null &&
                     eurlID !== undefined && 
                     wurlID !== null && 
                     wurlID !== undefined ){
                         
				if ( eurlID == wurlID ){
					//alert("they match! " + eurlID + "=" + wurlID);
					openTreeView( $(this) );
				}
			}
            
		});
	}
	
	//this next part automatically opens the side menu to the current page
	function openTreeView(sideNavLink){
		
		$(sideNavLink).addClass("sidenav-current-page");
		
		//'grab every parent with the class .dropdown-submenu, up to but not including #sidebar-navigation-selector'
		$(sideNavLink).parentsUntil("#sidebar-navigation-selector", ".dropdown-submenu").each(function(){
		
			//$(this).find(".dropdown-toggle").css("fontStyle","italic"); //visibility
			//$(this).css("borderLeft","1px solid #ccc");
			
			//'for each of the selected (sub)menu items, find the first immediate child .dropdown-toggle and click it to open the menu'
			//'since children() only goes a single level down and stops, it will never travel somewhere where it will open a different menu;'
			//'the way the menu structure is, there is only one .dropdown-toggle per layer'
			$(this).children(".dropdown-toggle").trigger("click");
		});
	}
	
	//auto-open the tree view
	matchSideNavWindowURL();
	
});
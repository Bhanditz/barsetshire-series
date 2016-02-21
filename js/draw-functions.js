function draw(){
	var vis =	d3.select("#body");
	var canvas=	vis.select("#vis");
	
	d3.json("data/test.json", function(error,data){
		
		var bins = canvas.selectAll(".topicbins")
					.data(data)
					.enter()
					.append("div")
					.attr("class","topicbin")
					;	
		
		var catscale=d3.scale.category10();
					
		var topicgrp = bins.append("g")
						.style("fill",function(d,i){
							return catscale(i);
						})
						;
						
					
		var binwidth=$(".topicbin").width();
		var binheight=$(".topicbin").height();
		var squarelength= Math.sqrt((binwidth*.45)*binheight/16.0);
		
		var books = topicgrp.selectAll(".books")
					.data(function(d){return d.books;})
					.enter()
					.append("div")
					.attr("class","bookbin")
					.style("width",function(d){ 
						return squarelength*d.b[0].nochap +"px";})
					;
					
		var booksvg=books.append("svg")
					.attr("class","booksvg")
					;
		var bookwidth=$('.booksvg').width();
		
		var chapters = booksvg.selectAll(".chapter")
						.data(function(d){return d.b;})
						.enter().append("g")
						.attr("class",function(d){return d.chap;})
						.attr("transform",function(d,i){
							var xcoor = squarelength*i
								ycoor =	binheight/4.0;
							return "translate(" + xcoor +"," + ycoor + ")";
						})
						;		
		
		chapters.append("rect").attr("class","chaprect")
			.attr("x",function(d,i){return i;})
			.attr("y",0)
			.attr("width",squarelength)
			.attr("height",squarelength)
			.style("opacity",function(d){return d.val;})
			;
						
		
		
		var b1scale= d3.scale.linear()
						.domain([1,3])
						.range([0,bookwidth/3.0])
						
		/*bins.append("text")
			.text(function(d){return d.topic;})
			.attr("class","topiclabel")
			;
		*/
		
	});
}

function makeBookScale(nochap){
	var binwidth1=$(".topicbin").width();
	
	bookScale=d3.scale.linear()
				.domain([0,nochap])
				.range([0,binwidth1*(2.0/3)])
				;
	return bookScale(nochap);
	
}


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
		
		var names=	bins.append("div").attr("class","namebin");
					
		var series=	bins.append("div").attr("class","seriesbin");
		
		var catscale=d3.scale.category10();
					
		var topicgrp = series.append("g")
						.style("fill",function(d,i){
							return catscale(i);
						})
						;
						
					
		var binwidth=$(".topicbin").width()
			binheight=$(".topicbin").height()
			namewidth=.05
			seriesright=.05
			allchapters=319.0
			;
			
		$(".seriesbin").width(binwidth*(1-namewidth));
		
		var cellwidth= ($(".seriesbin").width()/allchapters)*.97;
		
		
		var books = topicgrp.selectAll(".books")
					.data(function(d){return d.books;})
					.enter()
					.append("div")
					.attr("class","bookbin")
					.style("width",function(d){ 
						return cellwidth*d.totalchap +"px";})
					;
					
		var booksvg=books.append("svg")
					.attr("class","booksvg")
					;
		var bookwidth=$('.booksvg').width();
		
		var chapters = booksvg.selectAll(".chapter")
						.data(function(d){return d.b;})
						.enter().append("g")
						.attr("class",function(d){return d.chap+" name";})
						.attr("transform",function(d,i){
							var xcoor = cellwidth*i
								ycoor =	binheight/4.0;
							return "translate(" + xcoor +"," + ycoor + ")";
						})
						;		
		
		chapters.append("rect").attr("class","chaprect")
			//.attr("x",function(d,i){return i;})
			.attr("y",0)
			.attr("width",cellwidth)
			.attr("height",binheight/2)
			.style("opacity",function(d){return d.val;})
			.on("mouseover",function(d){ 
				d3.select("p")
					.append("text")
					.text("chapter" + d.chap)
					;
			})
			.on("mouseout", function(d){
				d3.select("p text").remove()
				;
			})
			;
						
		
		
		var b1scale= d3.scale.linear()
						.domain([1,6])
						.range([0,bookwidth/6.0])
						
		/*bins.append("text")
			.text(function(d){return d.topic;})
			.attr("class","topiclabel")
			;
		*/
		
	});
}


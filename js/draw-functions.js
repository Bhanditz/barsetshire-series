var barsetshireVis={

	draw: 	function (){
			var vis =	d3.select("#body");
			var canvas=	vis.select("#vis");
			
			d3.json("data/test.json", function(error,data){
				
				var binder = canvas.selectAll(".topicbins")
							.data(data)
							.enter()
							;
				
				var names = binder.append("text")
						.text(function(d){return d.topic;})
						;
				
				
				var bins = names.append("div")
							.attr("class","topicbin")
							;	
							
				var series=	bins.append("div").attr("class","seriesbin");
				
				var catscale=d3.scale.category20b();
							
				var topicgrp = series.append("g")
								.style("fill",function(d,i){
									return catscale(i);
								})
								;						
							
				var binwidth=$(".topicbin").width()
					binheight=$(".topicbin").height()
					namewidth=.02
					seriesright=.05
					allchapters=313.0
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
							
				
				booksvg.append("text")
						.text(function(d){return d.title;})
						.attr("text-anchor","middle")
						.attr("y","20")
						.attr("x", function(d){return d.totalchap*cellwidth/2.0;})
						.attr("class","titletext")
						;
				
				var chapters = booksvg.selectAll(".chapter")
								.data(function(d){return d.b;})
								.enter().append("g")
								.attr("class",function(d){return d.chap+" name";})
								.attr("transform",function(d,i){
									var xcoor = cellwidth*i
										ycoor =	binheight/6.0 + 10;
									return "translate(" + xcoor +"," + ycoor + ")";
								})
								;
				

				var opacityScale = d3.scale.linear()
								.domain([0,.04])
								.range([0,1])
								;
				
				chapters.append("rect").attr("class","chaprect")
					//.attr("x",function(d,i){return i;})
					.attr("y",0)
					.attr("width",cellwidth)
					.attr("height",binheight/1.5)
					.style("opacity",function(d){return opacityScale(d.val);})
					.on("mouseover",function(d){ 
						d3.select(".chapterbox")
							.append("text")
							.text(d.chap)
							;
						d3.select(".valuebox")
							.append("text")
							.text(d.val)
							;
					})
					.on("mouseout", function(d){
						d3.select(".chapterbox text").remove()
						;
						d3.select(".valuebox text").remove()
						;
					})
					;
				/*	
				d3.selectAll("rect")
					.style("opacity",function(d){
						if (d.val<.01){
							return 0;
						}
						else {
							return 1;
						}
					})
				*/				
				
			});
		}

};
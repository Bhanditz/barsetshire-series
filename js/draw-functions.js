var barsetshireVis = {

    draw: function(filename, minval, maxval, allchapters) {
        var vis = d3.select("#body");
        var canvas = vis.select("#vis");
		


        d3.json(filename, function(error, data) {

            var binder = canvas.selectAll(".topicbins")
                .data(data)
                .enter();

            var names = binder.append("div")
                .attr("class", "topicholder");


            names.append("div")
                .attr("class", "topictext")
                .append("text")
                .text(function(d) {
                    return d.topic;
                });


            var bins = names.append("div")
                .attr("class", "topicbin");


            var series = bins.append("div").attr("class", "seriesbin");

            var catscale = d3.scale.category20b();

            var topicgrp = series.append("g")
                /*	.style("fill","purple"),function(d,i){
                		return catscale(i);
                	}) */
            ;

            var binwidth = $(".topicbin").width(),
                binheight = $(".topicbin").height(),
                namewidth = .02,
                seriesright = .05
				;

            $(".seriesbin").width(binwidth * (1 - namewidth));

            var cellwidth = ($(".seriesbin").width() / allchapters) * .97;


            var books = topicgrp.selectAll(".books")
                .data(function(d) {
                    return d.books;
                })
                .enter()
                .append("div")
                .attr("class", "bookbin")
                .style("width", function(d) {
                    return cellwidth * d.totalchap + "px";
                });

            var booksvg = books.append("svg")
                .attr("class", "booksvg");


            /*	booksvg.append("text")
            			.text(function(d){return d.title;})
            			.attr("text-anchor","middle")
            			.attr("y","20")
            			.attr("x", function(d){return d.totalchap*cellwidth/2.0;})
            			.attr("class","titletext")
            			;
            */
            var chapters = booksvg.selectAll(".chapter")
                .data(function(d) {
                    return d.b;
                })
                .enter().append("g")
                .attr("class", "chapbin")
                .attr("transform", function(d, i) {
                    var xcoor = cellwidth * i,
                        //ycoor =	binheight/6.0 + 10;
                        ycoor = 0;
                    return "translate(" + xcoor + "," + ycoor + ")";
                });


            var opacityScale = d3.scale.linear()
                .domain([minval, maxval])
                .range([0, 1]);

            chapters.append("rect")
                .attr("class", function(d) {
                    var badchars = [",", ".", "!", "?", "-"]
                    var temp = d.chap;
                    var lst = temp.split(" ");
                    var name = "";
                    for (x in lst) {
                        name += lst[x];
                    }
                    return name;
                })
                //.attr("x",function(d,i){return i;})
                .attr("y", function(d) {
                    return binheight / 6.0;
                })
                .attr("width", cellwidth)
                .attr("height", binheight * (2 / 3.0))
                .style("opacity", function(d) {
                    return opacityScale(d.val);
                })
                .on("mouseover", function(d) {
                    d3.select("#chapterbox")
                        .append("text")
                        .text(d.chap);
                    d3.select("#valuebox")
                        .append("text")
                        .text(d.val);

                })
                .on("mouseout", function(d) {
                    d3.select("#chapterbox text").remove();
                    d3.select("#valuebox text").remove();
                })
                /*		.on("click", function(d){

                			var boxhght = d3.select(this).attr("height")
                			var chapname = d3.select(this).attr("class");
                			var classchap = "." + chapname;

                			if (boxhght == binheight){
                				barsetshireVis.rectShrink(classchap, binheight/1.5, binheight);
                			}
                			else {
                				barsetshireVis.rectGrow(classchap, binheight);
                			}

                		}) */
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
    },

    rectGrow: function(chap, hght) {

        d3.selectAll(chap)
            .transition()
            .duration(800)
            .attr("y", 0)
            .attr("height", hght);

    },

    rectShrink: function(chap, hght, binheight) {

        d3.selectAll(chap)
            .transition()
            .duration(800)
            .attr("y", function() {
                return binheight / 6.0 + 10;
            })
            .attr("height", hght);
    },

    toggleVis: function() {
        var fixheight = $(".topicbin").height();

        var binpos = fixheight / 6.0,
            oldheight = fixheight * (2 / 3.0);

        if ($('button').hasClass("button-off") == true) {
            barsetshireVis.toggleCompress();
            $('button').attr("class", "btn button-on");
        } else {
            barsetshireVis.toggleExtend(binpos, oldheight);
            $('button').attr("class", "btn button-off");
        }



    },

    toggleCompress: function() {

        d3.selectAll(".topicholder")
            .transition()
            .style("margin-bottom", "0px");

        d3.selectAll(".topicbin")
            .transition()
            .delay(750)
            .duration(900)
            .style("border", "none");

        var topheight = $('.topicbin').height();

        d3.selectAll("rect")
            .transition()
            .delay(1400)
            //.duration(700)
            .attr("y", 0);

        d3.selectAll("rect")
            .transition()
            .delay(2000)
            .duration(1000)
            .attr("height", topheight);


    },

    toggleExtend: function(binpos, binht) {

        d3.selectAll("rect")
            .transition()
            .attr("y", binpos)
            .attr("height", binht);

        d3.selectAll(".topicbin")
            .transition()
            .style("border", "1px solid black");

        d3.selectAll(".topicholder")
            .transition()
            .style("margin-bottom", "20px");
    },

    titleDraw: function(titleList) {


        var titlebin = d3.select("#titles")
            .append("svg")
            .attr({
                "width": "100%",
                "height": "30px"
            });

        titlebin.selectAll("titlenames")
            .data(titleList)
            .enter()
            .append("text")
            .text(function(d) {
                return d.name;
            })
            .attr({
                "y": 20,
                "x": function(d) {
                    return d.xval;
                },
                "text-anchor": "center",
                "class": "titletext"
            });

    }

};

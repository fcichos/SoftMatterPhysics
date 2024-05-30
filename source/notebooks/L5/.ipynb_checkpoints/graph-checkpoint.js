var svg = d3.select(element)
    .append("svg")
    .attr("width", 300)
    .attr("height", 300);    

svg.append("circle")
    .style("stroke", "gray")
    .style("fill", "cyan")
    .attr("r", 130)
    .attr("cx", 150)
    .attr("cy", 150)
    .transition()
        .delay(100)
        .duration(10000)  
        .attr("r", 10)
        .attr("cx", 150)
        .style("fill", "blue"); 
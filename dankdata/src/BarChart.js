import React, {Component} from 'react';
import * as d3 from "d3";

// Same as data.tsv
import dataTsv from './data.tsv';


class BarChart extends Component {
    componentDidMount() {
        this.drawChart();
    }

    drawChart() {
        const data = [12, 5, 6, 6, 9, 10];

        const svg = d3.select("root")
            .append("svg")
            .attr("width", 200)
            .attr("height", 150)
            .style("margin-left", 100);

        svg.selectAll("rect")
            .data(data)
            .enter()
            .append("rect")
            .attr("x", (d, i) => i * 70)
            .attr("y", (d, i) => 150 - 10 * d)
            .attr("width", 65)
            .attr("height", (d, i) => d * 10)
            .attr("fill", "green");
    }

    render(){
        return <div id={"#chart"}></div>
    }
}

export default BarChart;
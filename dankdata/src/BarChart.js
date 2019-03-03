import React, {Component} from 'react';
import * as d3 from "d3";

// Same as data.tsv
import dataTsv from './data.tsv';



class BarChart extends Component {
    render() {
        return (
            <div className="BarChart">
                    <script>
                    var barPadding = 5;
                    var barWidth = (svgWidth / dataset.length);

                    var barChart = svg.selectAll("rect")
                    .data(dataTsv)
                    .enter()
                    .append("rect")
                    .attr("y", (svgHeight - d)
                    })
                    .attr("height", d
                    })
                    .attr("width", barWidth - barPadding)
                    .attr("transform", "translate("+ [barWidth * i, 0] +")";
                    });
                    </script>
            </div>
        );
    }
}

export default BarChart;
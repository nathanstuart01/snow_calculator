import React from 'react';
import { VictoryChart, VictoryLine } from 'victory';

const BaseData = props => {

    // need to find a way to make the graph wait to display data once it is available 
    // want a graph that displays each areas base data, adds the new data each day when it comes in
    //to do this loop through all areas and after each day of data, create a new graph point 
    // for each area create a new line as well
    //displays data as a line graph, with a tag for each area or a legend 
    // displays date on the x axis, base total in inches on the y axis 
    console.log(props.data[0]['base_total']);

		return (
			<div>
                <VictoryChart domainPadding={20} >
                    <VictoryLine 
                        style={{
                            data: { stroke: "5510F6"}
                        }}
                        data={[
                            {x: new Date(2018,11,24), y: 30 },
                            {x: new Date(2018,11,25), y: 35 },
                            {x: new Date(2018,11,26), y: 45 },
                            ]}
                    />
                    <VictoryLine 
                        style={{
                            data: { stroke: "E92027"}
                        }}
                        data={[
                            {x: new Date(2018,11,24), y: 27 },
                            {x: new Date(2018,11,25), y: 33 },
                            {x: new Date(2018,11,26), y: 42 },
                            ]}
                    />
                </VictoryChart>
            </div>
        );
}

export default BaseData;
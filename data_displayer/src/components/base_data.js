import React from 'react';
import { VictoryChart, VictoryLine, VictoryAxis } from 'victory';

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
                <VictoryChart domainPadding={20}>
                    <VictoryAxis dependentAxis
                     />
                    <VictoryAxis  
                        scale= {[new Date('December 01, 2018'), new Date('April 28, 2019')]}
                        label='Date'
                    />
                    <VictoryLine 
                        style={{
                            data: { stroke: "5510F6"}
                        }}
                        data={[
                            {x: 1, y: 30 },
                            {x: 2, y: 35 },
                            {x: 3, y: 45 },
                            ]}
                    />
                    <VictoryLine 
                        style={{
                            data: { stroke: "E92027"}
                        }}
                        data={[
                            {x: 1, y: 27 },
                            {x: 2, y: 33 },
                            {x: 3, y: 42 },
                            ]}
                    />
                </VictoryChart>
            </div>
        );
}

export default BaseData;
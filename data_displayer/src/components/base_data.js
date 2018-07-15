import React from 'react';
import { VictoryChart, VictoryLine } from 'victory';

const BaseData = (props) => {

    const baseData = props.baseData;

    if (baseData[0]) {
        console.log(baseData[0]['base_total']);
    } else {
        console.log('no base data for alta yet');
    }

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
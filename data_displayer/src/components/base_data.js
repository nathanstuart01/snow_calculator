import React from 'react';
import {VictoryLine, VictoryChart} from 'victory';

const BaseData = props => {

    const date1 = new Date('2018-11-01');
    const date2 = new Date('2019-05-01');
    const date3 = new Date('2018-11-25');
    const date4 = new Date('2018-11-26');
    const date5 = new Date('2018-11-27');
    const date6 = new Date('2018-11-28');
    const date7 = new Date('2018-11-29');
    const date8 = new Date('2018-12-15');


    return (
        <div>
        <VictoryChart
            scale={{x: "time", y: "linear"}}
            domain={{x:[date1, date2], y:[0,150]}}
        >        
            <VictoryLine 
                style={{
                    data: { stroke: "#0000FF" }
                    }}
                data={[
                    {x:date3, y:30},
                    {x:date4, y:40},
                    {x:date5, y:45},
                    {x:date6, y:50},
                    {x:date7, y:60},
                    {x:date8, y:75}
                ]}
            />
        </VictoryChart>
        </div>
        );
}

export default BaseData;
import React from 'react';
import {VictoryBar, VictoryChart} from 'victory';


const TwentyFourHourData = (props) => {
	 


  return(
		<div>
		  <h2>24 Hr Data</h2>
        <VictoryChart domainPadding={50}>
          <VictoryBar
            categories={{
                x: ["alta", "snowbird"]
              }}
              data={[
                  {x: 'alta', y:5},
                  {x: 'snowbird', y:4}
                ]}
          />
        </VictoryChart>
    </div>
      );
}

export default TwentyFourHourData;
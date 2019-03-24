import React from 'react';

const TwentyFourDataNotReady = props => {

    let currentDate = new Date().toLocaleString();

    return (

        <div>
        	<p id='twentyFourDataNotReadyParagraph'>
        		Twenty four hour snowfall data for Utah ski areas as of: {currentDate} is 
        		currently not available. Please check back after 7 AM, when areas usually post their snowfall data. Thanks!
        	</p>
        </div>

        );
}


export default TwentyFourDataNotReady;
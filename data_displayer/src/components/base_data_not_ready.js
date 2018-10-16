import React from 'react';

const BaseDataNotReady = props => {

    let currentDate = new Date().toLocaleString();

    return (

        <div>
        	<p id='baseDataNotReadyParagraph'>
        		Base depth snowfall data for Utah ski areas as of: {currentDate} is 
        		currently not available. Please check back after 7 AM, when areas usually post their snowfall data. Thanks!
        	</p>
        </div>

        );
}


export default BaseDataNotReady;
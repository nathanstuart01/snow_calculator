import React from 'react';

const DataNotReady = props => {

    let currentDate = new Date().toLocaleString();

    let Message = "Base and twenty four hour snowfall data for Utah ski areas as of: " + currentDate + " is not available yet"


    return (

        <div>
        {Message}
        </div>

        );
}


export default DataNotReady;
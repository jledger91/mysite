import React from 'react';

import './404.scss';

const NotFound = () => {
  
  return (
    <div className='not-found'>
      <div className='heading'>
        <h1>404</h1>
      </div>
      
      <div className='whoops'>
        <strong>Whoops!</strong> The page you are looking for does not exist.
      </div>
    </div>
  );
}

export default NotFound;

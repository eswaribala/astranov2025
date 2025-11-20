import React from 'react';
import { useState,useEffect } from 'react';

function Timer() {
  const[currentTime, setCurrentTime] = useState(new Date());
  // Update time every second
  useEffect(() => {
    const timerId = setInterval(()=>{
      setCurrentTime(new Date());
    },1000)
    return () => clearInterval(timerId);
  }, []);

  //render the time
  return(
    <h4>{currentTime.toLocaleTimeString()}</h4>
  )
}
export default Timer;


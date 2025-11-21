import React from 'react';

import Login from '../../molecules/Login/Login';
import  './AstraHome.css';
import { Routes, Route } from 'react-router-dom';
import Dashboard from '../Dashboard/Dashboard';
import { useState } from 'react';
import ContentAdv from '../../atoms/ContentAdv/ContentAdv';
const AstraHome = () => {

  const[isLoggedIn, setIsLoggedIn] = useState(false);
   function handleLoginStatus(status) {
        setIsLoggedIn(status);
    }
 return(
   <div class='formLayout'> 
        {(!isLoggedIn)&& (
    <div class='formLayout'>
        <ContentAdv/>
        {<Login  loginStatus={handleLoginStatus} /> }
    </div>
    ) }

        {isLoggedIn && (
            <Routes>
               
                <Route path="/login" element={<Login />} />
               
                <Route path="/dashboard" element={<Dashboard />} />
                
               </Routes>
        )}

   </div>
    )
  
};



export default AstraHome;

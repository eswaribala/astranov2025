import React from 'react';
import AstraBanner from '../../atoms/Banner/Banner';
import  './Header.css';
import Logo from '../../atoms/Logo/Logo';
import Timer from '../../atoms/Timer/Timer';
import Title from '../../atoms/Title/Title';


const Header = () => (
  <div>
   <div>
     <Title/>
    </div> 
  <div class="Header" data-testid="Header">
    <Logo/>
    <AstraBanner/>
    <Timer/>
  </div>
  </div>
);



export default Header;

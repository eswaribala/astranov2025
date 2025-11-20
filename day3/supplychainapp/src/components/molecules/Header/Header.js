import React from 'react';
import AstraBanner from '../../atoms/Banner/Banner';
import  './Header.css';
import Logo from '../../atoms/Logo/Logo';
import Timer from '../../atoms/Timer/Timer';


const Header = () => (
  <div class="Header" data-testid="Header">
    <Logo/>
    <AstraBanner/>
    <Timer/>
  </div>
);



export default Header;

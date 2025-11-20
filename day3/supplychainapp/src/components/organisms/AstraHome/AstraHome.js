import React from 'react';
import AstraHeader from '../../molecules/Header/Header';
import  './AstraHome.css';
import HomeContent from '../../molecules/HomeContent/HomeContent';

const AstraHome = () => (
  <div  data-testid="AstraHome">
    <AstraHeader/>
    <div class="content">
      <HomeContent />
    </div>
  </div>
);



export default AstraHome;

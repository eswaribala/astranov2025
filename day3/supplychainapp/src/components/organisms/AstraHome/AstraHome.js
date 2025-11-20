import React from 'react';
import AstraHeader from '../../molecules/Header/Header';
import styles from './AstraHome.module.css';
import HomeContent from '../../molecules/HomeContent/HomeContent';

const AstraHome = () => (
  <div className={styles.AstraHome} data-testid="AstraHome">
    <AstraHeader/>
    <HomeContent/>
  </div>
);



export default AstraHome;

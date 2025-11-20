import React from 'react';
import AstraHeader from '../../molecules/Header/Header';
import styles from './AstraHome.module.css';

const AstraHome = () => (
  <div className={styles.AstraHome} data-testid="AstraHome">
    <AstraHeader/>
  </div>
);



export default AstraHome;

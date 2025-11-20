import React from 'react';
import logo from '../../../assets/astralogo.jpg';

import styles from './Logo.module.css';

const Logo = () => (
  <img src={logo} alt="Company Logo" className={styles.logo} />  
);



export default Logo;

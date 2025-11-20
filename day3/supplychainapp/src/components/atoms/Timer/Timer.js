import React from 'react';
import PropTypes from 'prop-types';
import styles from './Timer.module.css';

const Timer = () => (
  <div className={styles.Timer} data-testid="Timer">
    Timer Component
  </div>
);

Timer.propTypes = {};

Timer.defaultProps = {};

export default Timer;

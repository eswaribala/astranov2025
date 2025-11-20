import React from 'react';
import PropTypes from 'prop-types';
import styles from './Banner.module.css';

const Banner = () => (
  <div className={styles.Banner} data-testid="Banner">
    Banner Component
  </div>
);

Banner.propTypes = {};

Banner.defaultProps = {};

export default Banner;

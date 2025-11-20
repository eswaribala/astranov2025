import React from 'react';
import ad1 from '../../../assets/images/ad1.png';
import { Image } from 'primereact/image';
import './ContentAdv.css';

const ContentAdv = () => (
  <Image data-testid="ContentAdv"  src={ad1}  alt="Image"  class="ContentAdv" />
);


export default ContentAdv;

import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import ContentAdv from './ContentAdv';

describe('<ContentAdv />', () => {
  test('it should mount', () => {
    render(<ContentAdv />);

    const contentAdv = screen.getByTestId('ContentAdv');

    expect(contentAdv).toBeInTheDocument();
  });
});
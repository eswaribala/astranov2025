import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import HomeContent from './HomeContent';

describe('<HomeContent />', () => {
  test('it should mount', () => {
    render(<HomeContent />);

    const homeContent = screen.getByTestId('HomeContent');

    expect(homeContent).toBeInTheDocument();
  });
});
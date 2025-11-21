import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import LocationsList from './LocationsList';

describe('<LocationsList />', () => {
  test('it should mount', () => {
    render(<LocationsList />);

    const locationsList = screen.getByTestId('LocationsList');

    expect(locationsList).toBeInTheDocument();
  });
});
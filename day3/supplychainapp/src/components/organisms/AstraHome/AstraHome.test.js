import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import AstraHome from './AstraHome';

describe('<AstraHome />', () => {
  test('it should mount', () => {
    render(<AstraHome />);

    const astraHome = screen.getByTestId('AstraHome');

    expect(astraHome).toBeInTheDocument();
  });
});
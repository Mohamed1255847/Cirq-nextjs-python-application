'use client';

import React, { useState } from 'react';
import styled from 'styled-components';
import { BlochSphere } from '@/components/blochSphere/page';

// Styled button component
const StyledButton = styled.button`
  padding: 12px 20px;
  margin: 10px;
  font-size: 16px;
  color: #fff;
  background: linear-gradient(135deg, #6c757d, #495057);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    background: linear-gradient(135deg, #5a6268, #343a40);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }

  &:active {
    transform: translateY(0);
    box-shadow: none;
  }
`;

// Styled input component
const StyledInput = styled.input`
  padding: 10px;
  margin: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
`;

export default function BlochSpherePage() {
  const [state, setState] = useState<[number, number, number]>([0, 0, 1]); // Initial state |0⟩
  const [input, setInput] = useState<[string, string, string]>(['0', '0', '1']); // Input state

  // Update state from input
  const updateStateFromInput = () => {
    const [x, y, z] = input.map(Number);
    const norm = Math.sqrt(x**2 + y**2 + z**2);
    if (norm !== 0) {
      setState([x / norm, y / norm, z / norm]);
    } else {
      alert('The input cannot be a zero vector.');
    }
  };

  // Handle input change
  const handleInputChange = (index: number, value: string) => {
    const newInput = [...input];
    newInput[index] = value;
    setInput([newInput[0], newInput[1], newInput[2]]);
  };

  // Hadamard Transformation
  const applyHadamard = () => {
    const [x, y, z] = state;
    const newState: [number, number, number] = [
      (x + z) / Math.sqrt(2),
      y / Math.sqrt(2),
      (z - x) / Math.sqrt(2),
    ];
    setState(newState);
  };

  // Pauli-X Transformation
  const applyPauliX = () => {
    const [x, y, z] = state;
    setState([-x, -y, z]);
  };

  // Pauli-Y Transformation
  const applyPauliY = () => {
    const [x, y, z] = state;
    setState([-y, x, -z]);
  };

  // Pauli-Z Transformation
  const applyPauliZ = () => {
    const [x, y, z] = state;
    setState([-x, y, -z]);
  };

  return (
    <>
      <div>
        <StyledInput
          type="text"
          value={input[0]}
          onChange={(e) => handleInputChange(0, e.target.value)}
          placeholder="Enter value for x"
        />
        <StyledInput
          type="text"
          value={input[1]}
          onChange={(e) => handleInputChange(1, e.target.value)}
          placeholder="Enter value for y"
        />
        <StyledInput
          type="text"
          value={input[2]}
          onChange={(e) => handleInputChange(2, e.target.value)}
          placeholder="Enter value for z"
        />
        <StyledButton onClick={updateStateFromInput}>Update State</StyledButton>
        <StyledButton onClick={() => setState([0, 0, 1])}>Change to |0⟩</StyledButton>
        <StyledButton onClick={() => setState([0, 0, -1])}>Change to |1⟩</StyledButton>
        <StyledButton onClick={() => setState([1 / Math.sqrt(2), 0, 1 / Math.sqrt(2)])}>
          Change to |+⟩
        </StyledButton>
        <StyledButton onClick={applyHadamard}>Hadamard</StyledButton>
        <StyledButton onClick={applyPauliX}>Pauli-X</StyledButton>
        <StyledButton onClick={applyPauliY}>Pauli-Y</StyledButton>
        <StyledButton onClick={applyPauliZ}>Pauli-Z</StyledButton>
      </div>
      <div>
        Current State: x: {state[0]}, y: {state[1]}, z: {state[2]}
      </div>
      <BlochSphere qubitState={state} />
    </>
  );
}

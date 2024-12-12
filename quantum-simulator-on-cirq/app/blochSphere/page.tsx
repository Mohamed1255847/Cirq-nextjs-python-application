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

export default function BlochSpherePage() {
    const [state, setState] = useState<[number, number]>([1, 0]); // Initial state |0⟩

    // Hadamard Transformation
    const applyHadamard = () => {
        const [a, b] = state;
        const newState: [number, number] = [
            (a + b) / Math.sqrt(2),
            (a - b) / Math.sqrt(2),
        ];
        setState(newState);
    };

    // Pauli-X Transformation
    const applyPauliX = () => {
        const [a, b] = state;
        setState([b, a]);
    };

    // Pauli-Z Transformation
    const applyPauliZ = () => {
        const [a, b] = state;
        setState([a, -b]);
    };

    // Phase Gate Transformation
    const applyPhaseGate = () => {
        const [a, b] = state;
        setState([a, b * Math.sqrt(-1)]); // Introduces a phase factor
    };

    return (
        <>
            <div>
                <StyledButton onClick={() => setState([1, 0])}>Change to |0⟩</StyledButton>
                <StyledButton onClick={() => setState([0, 1])}>Change to |1⟩</StyledButton>
                <StyledButton onClick={() => setState([1 / Math.sqrt(2), 1 / Math.sqrt(2)])}>
                    Change to |+⟩
                </StyledButton>
                <StyledButton onClick={applyHadamard}>Hadamard</StyledButton>
                <StyledButton onClick={applyPauliX}>Pauli-X</StyledButton>
                <StyledButton onClick={applyPauliZ}>Pauli-Z</StyledButton>
                <StyledButton onClick={applyPhaseGate}>Phase Gate</StyledButton>
            </div>
            <BlochSphere qubitState={state} />
        </>
    );
}

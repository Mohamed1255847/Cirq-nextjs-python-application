'use client';

import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import { useSetupCircuitMutation, useRunCircuitMutation } from '@/feature/api';

// Types
interface Circuit {
  id: number;
  name: string;
  message: string;
  circuit: string;
}

// Example data (You can replace this with your actual circuits data)
const circuitOptions: Circuit[] = [
  { id: 1, name: 'Circuit 1', message: '', circuit: '' },
  { id: 2, name: 'Circuit 2', message: '', circuit: '' },
  // Add more circuits as needed
];

// Styled components
const Container = styled.div`
  display: flex;
  height: 100vh;
  background-color: #f8f9fa;
`;

const CircuitList = styled.div`
  flex: 1;
  background-color: rgba(255, 255, 255, 0.7);
  color: #343a40;
  padding: 20px;
  overflow-y: auto;
  border-right: 2px solid #dee2e6;
  backdrop-filter: blur(10px);
`;

const CircuitButton = styled.button`
  display: block;
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  background-color: rgba(52, 58, 64, 0.8);
  border: none;
  cursor: pointer;
  color: white;
  text-align: left;
  font-size: 16px;
  border-radius: 5px;
  transition: background-color 0.3s;

  &:hover {
    background-color: rgba(52, 58, 64, 0.9);
  }
`;

const CircuitDetails = styled.div`
  flex: 3;
  padding: 40px;
  overflow-y: auto;
  background-color: #ffffff;
  border-left: 2px solid #dee2e6;
`;

const Title = styled.h2`
  margin-top: 0;
  color: #343a40;
`;

const Info = styled.div`
  margin-bottom: 20px;
  font-size: 18px;
  color: #495057;
  line-height: 1.5;

  code {
    background: #f1f1f1;
    padding: 2px 4px;
    border-radius: 4px;
    font-family: 'Courier New', Courier, monospace;
  }
`;

const Error = styled.h1`
  color: red;
`;

export default function CircuitsPage() {
  const [selectedCircuit, setSelectedCircuit] = useState<Circuit | null>(null);

  const [setupCircuit, { data: setupData, isError: setupError }] = useSetupCircuitMutation();
  const [runCircuit, { data: runData, isError: runError }] = useRunCircuitMutation();

  useEffect(() => {
    if (selectedCircuit) {
      const runSelectedCircuit = async () => {
        try {
          const setupResult = await setupCircuit(selectedCircuit).unwrap();
          if (setupResult) {
            await runCircuit(setupResult).unwrap();
          }
        } catch (error) {
          console.error("An error occurred during the run process:", error);
        }
      };

      runSelectedCircuit();
    }
  }, [selectedCircuit, runCircuit, setupCircuit]);

  const handleCircuitClick = (circuit: Circuit) => {
    setSelectedCircuit(circuit);
  };

  return (
    <Container>
      <CircuitList>
        {circuitOptions.map((circuit) => (
          <CircuitButton key={circuit.id} onClick={() => handleCircuitClick(circuit)}>
            {circuit.name}
          </CircuitButton>
        ))}
      </CircuitList>
      <CircuitDetails>
        {selectedCircuit ? (
          <>
            {setupData && (
              <>
                <Title>Setup Result:</Title>
                <Info>{setupData.message}</Info>
                <Info>{setupData.circuit}</Info>
              </>
            )}
            {runData && (
              <>
                <Title>Run Result:</Title>
                <Info>{runData.message}</Info>
                <Info>{runData.circuit}</Info>
              </>
            )}
          </>
        ) : (
          <Title>Select a circuit to see its details.</Title>
        )}
        {setupError && <Error>Error in setup the circuit</Error>}
        {runError && <Error>Error in running the circuit</Error>}
      </CircuitDetails>
    </Container>
  );
}

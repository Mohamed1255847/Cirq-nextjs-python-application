import React, { useState } from 'react';
import styled from 'styled-components';
import { QuantumCircuitContainer, QubitLine, Qubit, Operation, Info, Title } from './parts';
import { Circuit } from './types';
import { CodeBlock, CodeContainerStyle } from '@/components/code-block-component';

const StyledButton = styled.button`
  background-color: #6200ea;
  color: white;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #3700b3;
  }
`;

const QuantumCircuit: React.FC<{ circuit: string }> = ({ circuit }) => {
  const operations = circuit.match(/X\^0\.5|M\('m'\)|H|X|Y|Z|S|T/g) || [];

  return (
    <QuantumCircuitContainer>
      <QubitLine>
        <Qubit>Q0</Qubit>
        {operations.map((op, idx) => (
          <Operation key={idx} type={op.startsWith('M') ? 'measurement' : 'gate'}>
            {op}
          </Operation>
        ))}
      </QubitLine>
    </QuantumCircuitContainer>
  );
};

export const CircuitBlockComponent: React.FC<{ circuitData: Circuit; circuitId: number; indexNumber: number }> = ({ circuitData, circuitId, indexNumber }) => {
  const [showName, setShowName] = useState(false);
  const [showDescription, setShowDescription] = useState(false);
  const [showResults, setShowResults] = useState(false);
  const [showCode, setShowCode] = useState(false);

  if (!circuitData) {
    return null;
  }

  return circuitData && circuitId === indexNumber && (
    <>
      {showName && <Title>{circuitData?.name}:</Title>}
      <StyledButton onClick={() => setShowName(!showName)}>
        {showName ? 'Hide Name' : 'Show Name'}
      </StyledButton>
      <StyledButton onClick={() => setShowDescription(!showDescription)}>
        {showDescription ? 'Hide Description' : 'Show Description'}
      </StyledButton>
      <StyledButton onClick={() => setShowResults(!showResults)}>
        {showResults ? 'Hide Results' : 'Show Results'}
      </StyledButton>
      <StyledButton onClick={() => setShowCode(!showCode)}>
        {showCode ? 'Hide Code' : 'Show Code'}
      </StyledButton>

      <Info>Circuit: {circuitData?.circuit}</Info>
      <QuantumCircuit circuit={circuitData?.circuit} />

      {showDescription && <Info>{circuitData?.description}</Info>}
      {showResults && <Info>Results: {JSON.stringify(circuitData?.results)}</Info>}
      {showCode && (
        <CodeContainerStyle>
          {circuitData?.code && <CodeBlock code={circuitData?.code} />}
        </CodeContainerStyle>
      )}
    </>
  );
};



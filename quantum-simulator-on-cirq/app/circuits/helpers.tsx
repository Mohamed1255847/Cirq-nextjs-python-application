import React, { useState } from 'react';
import styled from 'styled-components';
import { Info, Title } from './parts';
import { Circuit } from './types';
import { CodeBlock, CodeContainerStyle } from '@/components/code-block-component';
import ReactMarkdown from 'react-markdown';

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

const ImageContainer = styled.img``;

const CircuitContainer = styled.div`
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 10px;
  margin: 10px 0;
  font-family: 'Courier New', Courier, monospace; 
  font-size: 30px; /* Increase the font size */ 
  line-height: 1.6; /* Increase line height for clarity */
`;

interface QuantumCircuitDisplayProps {
  circuit: string;
}

const QuantumCircuitDisplay: React.FC<QuantumCircuitDisplayProps> = ({ circuit }) => (
  <CircuitContainer>
    <ReactMarkdown>{`\`\`\`\n${circuit}\n\`\`\``}</ReactMarkdown>
  </CircuitContainer>
);

// interface QuantumCircuitProps {
//   circuit: string;
// }

// const QuantumCircuit: React.FC<QuantumCircuitProps> = ({ circuit }) => {
//   const operations = circuit.match(/X\^0\.5|M\('m'\)|H|X|Y|Z|S|T/g) || [];

//   return (
//     <QuantumCircuitContainer>
//       <QubitLine>
//         <Qubit>Q0</Qubit>
//         {operations.map((op, idx) => (
//           <Operation key={idx} type={op.startsWith('M') ? 'measurement' : 'gate'}>
//             {op}
//           </Operation>
//         ))}
//       </QubitLine>
//     </QuantumCircuitContainer>
//   );
// };

interface CircuitBlockComponentProps {
  circuitData: Circuit;
  circuitId: number;
  indexNumber: number;
}

export const CircuitBlockComponent: React.FC<CircuitBlockComponentProps> = ({ circuitData, circuitId, indexNumber }) => {
  const [showDescription, setShowDescription] = useState(false);
  const [showResults, setShowResults] = useState(false);
  const [showCode, setShowCode] = useState(false);

  if (!circuitData) {
    return null;
  }

  return circuitData && circuitId === indexNumber && (
    <>
      <Title>{circuitData?.name}:</Title>
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
      <QuantumCircuitDisplay circuit={circuitData?.circuit} />
      {/* <QuantumCircuit circuit={circuitData?.circuit} /> */}

      <ImageContainer src={`data:image/png;base64,${circuitData?.image}`} alt="Quantum Circuit Diagram" />

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

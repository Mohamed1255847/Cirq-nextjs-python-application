'use client';

import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import {
  useSetupCircuitMutation,
  useRunCircuitMutation,
  useBellStateCircuitQuery,
  useBasicGatesCircuitQuery,
  useQftCircuitQuery,
  useTeleportationCircuitQuery,
  useVqeCircuitQuery,
  usePhaseEstimationCircuitQuery,
  useDeutschJozsaCircuitQuery,
  useEntanglementSwappingCircuitQuery,
} from '@/feature/api';

// Types
interface Circuit {
  id: number;
  name: string;
  message: string;
  circuit: string;
}

const circuitOptions: Circuit[] = [
  { id: 1, name: 'Circuit 1', message: '', circuit: '(0, 0): ───X^0.5───M(\'m\')───' },
  { id: 3, name: 'Bell State Circuit', message: '', circuit: '(0, 0): ───H───@───M(\'m\')───' },
  { id: 4, name: 'Basic Gates Circuit', message: '', circuit: '(1, 0): ───X───Y───Z───M(\'m\')───' },
  { id: 5, name: 'QFT Circuit', message: '', circuit: '(0, 0): ───H───S───T───M(\'m\')───' },
  { id: 6, name: 'Teleportation Circuit', message: '', circuit: '(0, 0): ───H───@───M(\'m\')───' },
  { id: 7, name: 'VQE Circuit', message: '', circuit: '(0, 0): ───H───X───Y───Z───M(\'m\')───' },
  { id: 8, name: 'Phase Estimation Circuit', message: '', circuit: '(0, 0): ───H───S───T───M(\'m\')───' },
  { id: 9, name: 'Deutsch-Jozsa Circuit', message: '', circuit: '(0, 0): ───H───@───M(\'m\')───' },
  { id: 10, name: 'Entanglement Swapping Circuit', message: '', circuit: '(0, 0): ───H───@───M(\'m\')───' },
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

// Styled components for the quantum circuit visualization
const QuantumCircuitContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 20px;
  background-color: #fff;
  border: 2px solid #343a40;
  border-radius: 10px;
  width: fit-content;
`;

const QubitLine = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 20px;
`;

const Qubit = styled.div`
  width: 20px;
  height: 20px;
  border: 1px solid #343a40;
  border-radius: 50%;
  margin-right: 10px;
  background-color: #343a40;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
`;

const Operation = styled.div`
  padding: 5px 10px;
  background-color: ${({ type }) => (type === 'measurement' ? '#28a745' : '#007bff')};
  color: white;
  margin-right: 10px;
  border-radius: 5px;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
`;

// QuantumCircuit Component
const QuantumCircuit = ({ circuit }) => {
  // Parse the circuit string to extract gates and measurements
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

export default function CircuitsPage() {
  const [selectedCircuit, setSelectedCircuit] = useState<Circuit | null>(null);

  const [setupCircuit, { data: setupData, isError: setupError }] = useSetupCircuitMutation();
  const [runCircuit, { data: runData, isError: runError }] = useRunCircuitMutation();
  const { data: bellStateData } = useBellStateCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 3,
  });
  const { data: basicGatesData } = useBasicGatesCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 4,
  });
  const { data: qftData } = useQftCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 5,
  });
  const { data: teleportationData } = useTeleportationCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 6,
  });
  const { data: vqeData } = useVqeCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 7,
  });
  const { data: phaseEstimationData } = usePhaseEstimationCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 8,
  });
  const { data: deutschJozsaData } = useDeutschJozsaCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 9,
  });
  const { data: entanglementSwappingData } = useEntanglementSwappingCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 10,
  });

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
            {bellStateData && selectedCircuit.id === 3 && (
              <>
                <Title>Bell State Circuit Result:</Title>
                <Info>{bellStateData.circuit}</Info>
                <Info>{bellStateData.results}</Info>
              </>
            )}
            {basicGatesData && selectedCircuit.id === 4 && (
              <>
                <Title>Basic Gates Circuit Result:</Title>
                <Info>{basicGatesData.circuit}</Info>
                <Info>{basicGatesData.results}</Info>
              </>
            )}
            {qftData && selectedCircuit.id === 5 && (
              <>
                <Title>QFT Circuit Result:</Title>
                <Info>{qftData.circuit}</Info>
                <Info>{qftData.results}</Info>
              </>
            )}
            {teleportationData && selectedCircuit.id === 6 && (
              <>
                <Title>Teleportation Circuit Result:</Title>
                <Info>{teleportationData.circuit}</Info>
                <Info>{teleportationData.results}</Info>
              </>
            )}
            {vqeData && selectedCircuit.id === 7 && (
              <>
                <Title>VQE Circuit Result:</Title>
                <Info>{vqeData.circuit}</Info>
                <Info>{vqeData.results}</Info>
              </>
            )}
            {phaseEstimationData && selectedCircuit.id === 8 && (
              <>
                <Title>Phase Estimation Circuit Result:</Title>
                <Info>{phaseEstimationData.circuit}</Info>
                <Info>{phaseEstimationData.results}</Info>
              </>
            )}
            {deutschJozsaData && selectedCircuit.id === 9 && (
              <>
                <Title>Deutsch-Jozsa Circuit Result:</Title>
                <Info>{deutschJozsaData.circuit}</Info>
                <Info>{deutschJozsaData.results}</Info>
              </>
            )}
            {entanglementSwappingData && selectedCircuit.id === 10 && (
              <>
                <Title>Entanglement Swapping Circuit Result:</Title>
                <Info>{entanglementSwappingData.circuit}</Info>
                <Info>{entanglementSwappingData.results}</Info>
              </>
            )}
            <QuantumCircuit circuit={selectedCircuit.circuit} />
          </>
        ) : (
          <Title>Select a circuit to see its details.</Title>
        )}
        {setupError && <Error>Error in setting up the circuit</Error>}
        {runError && <Error>Error in running the circuit</Error>}
      </CircuitDetails>
    </Container>
  );
}

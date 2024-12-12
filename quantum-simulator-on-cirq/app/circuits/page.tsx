'use client';
import { useState } from 'react';
import {
  useBellStateCircuitQuery,
  useBasicGatesCircuitQuery,
  useQftCircuitQuery,
  useTeleportationCircuitQuery,
  useVqeCircuitQuery,
  usePhaseEstimationCircuitQuery,
  useDeutschJozsaCircuitQuery,
  useEntanglementSwappingCircuitQuery,
  useSimpleQuantumCircuitQuery,
} from '@/feature/api';
import {Circuit} from './types';
import {CircuitButton , CircuitDetails,CircuitList,Container,Info,Title} from './parts';
import {QuantumCircuit} from './helpers';
import {circuitOptions} from './constants';


export default function CircuitsPage() {
  const [selectedCircuit, setSelectedCircuit] = useState<Circuit | null>(null);

const { data: simplestQuantamCircuteData,error } = useSimpleQuantumCircuitQuery(undefined, {
  skip: selectedCircuit?.id !== 2,
});
console.log({simplestQuantamCircuteData,error})
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
              {simplestQuantamCircuteData && selectedCircuit.id === 2 && (
              <>
                <Title>Simplest Quantam Circuit Result:</Title>
                <Info>{simplestQuantamCircuteData.name}</Info>
                <Info>{simplestQuantamCircuteData.description}</Info>
                <Info>Circuit: {simplestQuantamCircuteData.circuit}</Info>
                <Info>Results: {JSON.stringify(simplestQuantamCircuteData.results)}</Info>
              </>
            )}
            {bellStateData && selectedCircuit.id === 3 && (
              <>
                <Title>Bell State Circuit Result:</Title>
                <Info>{bellStateData.name}</Info>
                <Info>{bellStateData.description}</Info>
                <Info>Circuit: {bellStateData.circuit}</Info>
                <Info>Results: {JSON.stringify(bellStateData.results)}</Info>
              </>
            )}
            {basicGatesData && selectedCircuit.id === 4 && (
              <>
                <Title>Basic Gates Circuit Result:</Title>
                <Info>{basicGatesData.name}</Info>
                <Info>{basicGatesData.description}</Info>
                <Info>Circuit: {basicGatesData.circuit}</Info>
                <Info>Results: {JSON.stringify(basicGatesData.results)}</Info>
              </>
            )}
            {qftData && selectedCircuit.id === 5 && (
              <>
                <Title>QFT Circuit Result:</Title>
                <Info>{qftData.name}</Info>
                <Info>{qftData.description}</Info>
                <Info>Circuit: {qftData.circuit}</Info>
                <Info>Results: {JSON.stringify(qftData.results)}</Info>
              </>
            )}
            {teleportationData && selectedCircuit.id === 6 && (
              <>
                <Title>Teleportation Circuit Result:</Title>
                <Info>{teleportationData.name}</Info>
                <Info>{teleportationData.description}</Info>
                <Info>Circuit: {teleportationData.circuit}</Info>
                <Info>Results: {JSON.stringify(teleportationData.results)}</Info>
              </>
            )}
            {vqeData && selectedCircuit.id === 7 && (
              <>
                <Title>VQE Circuit Result:</Title>
                <Info>{vqeData.name}</Info>
                <Info>{vqeData.description}</Info>
                <Info>Circuit: {vqeData.circuit}</Info>
                <Info>Results: {JSON.stringify(vqeData.results)}</Info>
              </>
            )}
            {phaseEstimationData && selectedCircuit.id === 8 && (
              <>
                <Title>Phase Estimation Circuit Result:</Title>
                <Info>{phaseEstimationData.name}</Info>
                <Info>{phaseEstimationData.description}</Info>
                <Info>Circuit: {phaseEstimationData.circuit}</Info>
                <Info>Results: {JSON.stringify(phaseEstimationData.results)}</Info>
              </>
            )}
            {deutschJozsaData && selectedCircuit.id === 9 && (
              <>
                <Title>Deutsch-Jozsa Circuit Result:</Title>
                <Info>{deutschJozsaData.name}</Info>
                <Info>{deutschJozsaData.description}</Info>
                <Info>Circuit: {deutschJozsaData.circuit}</Info>
                <Info>Results: {JSON.stringify(deutschJozsaData.results)}</Info>
              </>
            )}
            {entanglementSwappingData && selectedCircuit.id === 10 && (
              <>
                <Title>Entanglement Swapping Circuit Result:</Title>
                <Info>{entanglementSwappingData.name}</Info>
                <Info>{entanglementSwappingData.description}</Info>
                <Info>Circuit: {entanglementSwappingData.circuit}</Info>
                <Info>Results: {JSON.stringify(entanglementSwappingData.results)}</Info>
              </>
            )}
            <QuantumCircuit circuit={selectedCircuit.circuit} />
          </>
        ) : (
          <Title>Select a circuit to see its details.</Title>
        )}
      </CircuitDetails>
    </Container>
  );
}

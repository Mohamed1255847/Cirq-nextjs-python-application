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
import { CircuitInfoType } from './types';
import { CircuitButton, CircuitDetails, CircuitList, Container } from './parts';
import { CircuitBlockComponent } from './helpers';
import { circuitOptions } from './constants';

export default function CircuitsPage() {
  const [selectedCircuit, setSelectedCircuit] = useState<CircuitInfoType>({
    id:0,
    name: "Simplest Quantum Circuit Result",
    message: "",
    circuit: "(0, 0): ───X^0.5───M('m')───",
  });

  const { data: simplestQuantumCircuitData } = useSimpleQuantumCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 0,
  });
  const { data: bellStateData } = useBellStateCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 1,
  });
  const { data: basicGatesData } = useBasicGatesCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 2,
  });
  const { data: qftData } = useQftCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 3,
  });
  const { data: teleportationData } = useTeleportationCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 4,
  });
  const { data: vqeData } = useVqeCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 5,
  });
  const { data: phaseEstimationData } = usePhaseEstimationCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 6,
  });
  const { data: deutschJozsaData } = useDeutschJozsaCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 7,
  });
  const { data: entanglementSwappingData } = useEntanglementSwappingCircuitQuery(undefined, {
    skip: selectedCircuit?.id !== 8,
  });

  const handleCircuitClick = (circuit: CircuitInfoType) => {
    setSelectedCircuit(circuit);
  };

  const circuitsDataResult = [
    { circuitData: simplestQuantumCircuitData, circuitId: 0 },
    { circuitData: bellStateData, circuitId: 1 },
    { circuitData: basicGatesData, circuitId: 2 },
    { circuitData: qftData, circuitId: 3 },
    { circuitData: teleportationData, circuitId: 4 },
    { circuitData: vqeData, circuitId: 5 },
    { circuitData: phaseEstimationData, circuitId: 6 },
    { circuitData: deutschJozsaData, circuitId: 7 },
    { circuitData: entanglementSwappingData, circuitId: 8 },
  ];
  
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
        {circuitsDataResult.map(({ circuitData }, index) => (
          <CircuitBlockComponent key={index} circuitData={circuitData} circuitId={selectedCircuit.id} indexNumber={index} />
        ))}
      </CircuitDetails>
    </Container>
  );
}

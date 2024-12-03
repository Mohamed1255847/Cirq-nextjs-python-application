'use client';
import React, { useEffect, useState } from 'react';
import styled from 'styled-components';

import { 
  useLazyHadamardGateQuery, 
  useLazyPauliYGateQuery, 
  useLazyPhaseGateQuery, 
  useLazyPauliZGateQuery, 
  useLazyTGateQuery, 
  useLazyXGateQuery 
} from '@/feature/api';

// Types
interface Gate {
  description: string;
  example: string;
  gate: (number | string)[][];
  name: string;
  usage: string;
}

interface Result<T> {
  data: T | undefined;
  status: string;
}

// Styled components
const Container = styled.div`
  display: flex;
  height: 100vh;
  background-color: #f8f9fa;
`;

const GateList = styled.div`
  flex: 1;
  background-color: rgba(255, 255, 255, 0.7);
  color: #343a40;
  padding: 20px;
  overflow-y: auto;
  border-right: 2px solid #dee2e6;
  backdrop-filter: blur(10px);
`;

const GateButton = styled.button`
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

const GateDetails = styled.div`
  flex: 3;
  padding: 40px;
  overflow-y: auto;
  background-color: #ffffff;
  border-left: 2px solid #dee2e6;
`;

const GateHeader = styled.h2`
  margin-top: 0;
  color: #343a40;
`;

const GateInfo = styled.div`
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

const GateMatrix = styled.pre`
  padding: 20px;
  background: #e9ecef;
  border-radius: 5px;
  white-space: pre-wrap;
  font-family: 'Courier New', Courier, monospace;
  font-size: 16px;
`;

export default function GatesPage() {
  const [gates, setGates] = useState<Gate[]>([]);
  const [selectedGate, setSelectedGate] = useState<Gate | null>(null);

  const [fetchHadamardGate] = useLazyHadamardGateQuery();
  const [fetchPauliYGate] = useLazyPauliYGateQuery();
  const [fetchPhaseGate] = useLazyPhaseGateQuery();
  const [fetchPauliZGate] = useLazyPauliZGateQuery();
  const [fetchTGate] = useLazyTGateQuery();
  const [fetchXGate] = useLazyXGateQuery();

  useEffect(() => {
    const fetchAllGates = async () => {
      const results: Array<Result<Gate>> = await Promise.all([
        fetchHadamardGate(''),
        fetchPauliYGate(''),
        fetchPhaseGate(''),
        fetchPauliZGate(''),
        fetchTGate(''),
        fetchXGate('')
      ]);

      const allGates = results.map(result => result.data as Gate);
      setGates(allGates);
    };

    fetchAllGates();
  }, [fetchHadamardGate, fetchPauliYGate, fetchPhaseGate, fetchPauliZGate, fetchTGate, fetchXGate]);

  const handleGateClick = (gate: Gate) => {
    setSelectedGate(gate);
  };

  return (
    <Container>
      <GateList>
        {gates.map((gate, index) => (
          <GateButton key={index} onClick={() => handleGateClick(gate)}>
            {gate.name}
          </GateButton>
        ))}
      </GateList>
      <GateDetails>
        {selectedGate ? (
          <>
            <GateHeader>{selectedGate.name}</GateHeader>
            <GateInfo><strong>Description:</strong> {selectedGate.description}</GateInfo>
            <GateInfo><strong>Usage:</strong> {selectedGate.usage}</GateInfo>
            <GateInfo><strong>Example:</strong> <code>{selectedGate.example}</code></GateInfo>
            <GateMatrix>
              {selectedGate.gate.map(row => row.join(', ')).join('\n')}
            </GateMatrix>
          </>
        ) : (
          <GateHeader>Select a gate to see its details.</GateHeader>
        )}
      </GateDetails>
    </Container>
  );
}

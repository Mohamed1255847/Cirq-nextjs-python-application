'use client';

import React from 'react';
import styled from 'styled-components';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import { useSetupCircuitMutation, useRunCircuitMutation, useLazyHadamardGateQuery } from '@/feature/api';
import Matrix from '@/components/matrixComponent/matrixComponent';

const Page = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
`;

const Title = styled.h1`
  font-size: 24px;
  margin: 20px 0;
`;

const Error = styled.h1`
  color: red;
`;

export default function Home() {
  const [setupCircuit, { data: setupData, isError: setupError }] = useSetupCircuitMutation();
  const [runCircuit, { data: runData, isError: runError }] = useRunCircuitMutation();
  const [getHadamardGate, { data: hadamardGate, error }] = useLazyHadamardGateQuery();

  const handelSetupAndRunCircuitNumber1 = async (arg: unknown) => {
    try {
      const setupResult = await setupCircuit(arg).unwrap();
      if (setupResult) {
        await runCircuit(arg).unwrap();
      }
    } catch (error) {
      console.error("An error occurred during the setup or run process:", error);
    }
  };

  return (
    <Page>
      <Stack spacing={2} direction="row">
        <Button onClick={() => handelSetupAndRunCircuitNumber1(null)} variant="contained">
          Build a Simple Circuit
        </Button>
      </Stack>
      <Stack>
        <Button onClick={() => getHadamardGate('')} variant="contained">
          Hadamard Gate
        </Button>
      </Stack>

      {setupData && (
        <>
          <Title>{setupData?.message}</Title>
          <Title>{setupData?.circuit}</Title>
        </>
      )}
      {runData && (
        <>
          <Title>{runData?.message}</Title>
          <Title>{runData?.circuit}</Title>
        </>
      )}
      {setupError && <Error>Error in setup the circuit</Error>}
      {runError && <Error>Error in running the circuit</Error>}
      {error && <Error>Hadamard Gate error: {error.toString()}</Error>}

      {hadamardGate && (
        <Matrix data={hadamardGate?.gate} />
      )}
    </Page>
  );
}

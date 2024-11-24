'use client';
import styles from "./page.module.css";
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import { useSetupCircuitMutation, useRunCircuitMutation } from '@/feature/api';

export default function Home() {
  const [setupCircuit, { data: setupData, isSuccess: isSetupSuccess, isError: setupError }] = useSetupCircuitMutation();
  const [runCircuit, { data: runData, isError: runError }] = useRunCircuitMutation();

  console.log({ setupData, runData, setupError, runError });

  return (
    <div className={styles.page}>
      <Stack spacing={2} direction="row">
        <Button key="setup" onClick={setupCircuit} variant="contained">
          Build a Simple Circuit
        </Button>
        <h1>{setupData?.message}</h1>
        <h1>{setupData?.circuit}</h1>
        {isSetupSuccess && !setupError && (
          <Button key="run" onClick={runCircuit} variant="contained">
            Run the Circuit
          </Button>
        )}
      </Stack>
    </div>
  );
}

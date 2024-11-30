'use client';
import styles from "./page.module.css";
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import { useSetupCircuitMutation, useRunCircuitMutation } from '@/feature/api';

export default function Home() {
  const [setupCircuit, { data: setupData, isError: setupError }] = useSetupCircuitMutation();
  const [runCircuit, { data: runData, isError: runError }] = useRunCircuitMutation();

  const handelSetupAndRunCircuitNumber1 = async (arg: unknown) => {
    try {
      const setupResult = await setupCircuit(arg).unwrap();
      if (setupResult) {
        console.log("happen2");
        await runCircuit(arg).unwrap();
      }
    } catch (error) {
      console.error("An error occurred during the setup or run process:", error);
    }
  }

  const setupDataComponent = setupData && (
    <>
      <h1>{setupData?.message}</h1>
      <h1>{setupData?.circuit}</h1>
    </>
  )

  const runDataComponent = runData && (
    <>
      <h1>{runData?.message}</h1>
      <h1>{runData?.circuit}</h1>
    </>
  )

  return (
    <div className={styles.page}>
      <Stack spacing={2} direction="row">
        <Button key="setup and run circuit" onClick={handelSetupAndRunCircuitNumber1} variant="contained">
          Build a Simple Circuit
        </Button>
        {setupDataComponent}
        {runDataComponent}
        {setupError && <h1> Error in setup the circuit </h1>}
        {runError && <h1> Error in running the circuit </h1>}
      </Stack>
    </div>
  );
}


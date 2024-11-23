"use client"
import styles from "./page.module.css";
import {
  useQuery,
} from '@tanstack/react-query';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

export default function Home() {
  const url = process.env.PYURl;
  const { data: dataRunCircuit, refetch: runCircuit, } = useQuery({
    queryKey: ['repoData'],
    queryFn: () =>
      fetch('http://127.0.0.1:5000/run-cirq', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      }).then(res => res.json()),
    enabled: false,

  });
  
  const { isPending, error, data, isSuccess, refetch: setupCircuit, } = useQuery({
    queryKey: ['repoData'],
    queryFn: () =>
      fetch('http://127.0.0.1:5000/setup-circuit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      }).then(res => res.json()),
    enabled: false,

  });

  
  console.log({ isPending, error, data, url, dataRunCircuit })
  return (
    <div className={styles.page}>
      <Stack spacing={2} direction="row">
        <Button key="run" onClick={setupCircuit} variant="contained">Build a simple Circuit</Button>
        <h1>{data?.message}</h1>
        <h1>{data?.circuit}</h1>
        {isSuccess && data && !error && <Button key="run2" onClick={runCircuit} variant="contained">Run the Circuit</Button>}
      </Stack>
    </div>
  );
}

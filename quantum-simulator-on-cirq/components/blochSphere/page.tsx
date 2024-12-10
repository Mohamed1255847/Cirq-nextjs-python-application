import React, { useEffect, useState } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Sphere, Line } from '@react-three/drei';
import { multiply, abs, arg } from 'mathjs';

interface Axis {
  from: [number, number, number];
  to: [number, number, number];
  color: string;
}

const hadamard = [
  [1 / Math.sqrt(2), 1 / Math.sqrt(2)],
  [1 / Math.sqrt(2), -1 / Math.sqrt(2)],
];

const applyUnitary = (unitary: number[][], state: number[]) => {
  return multiply(unitary, state);
};

const getBlochCoordinates = (state: number[]) => {
  const theta = 2 * Math.acos(abs(state[0]));
  const phi = arg(state[1]);
  return {
    x: Math.sin(theta) * Math.cos(phi),
    y: Math.sin(theta) * Math.sin(phi),
    z: Math.cos(theta),
  };
};

const BlochSphere: React.FC = () => {
  const [qubitState, setQubitState] = useState([1, 0]); // Initial state |0⟩

  useEffect(() => {
    const newState = applyUnitary(hadamard, qubitState);
    setQubitState(newState);
  }, []);

  const qubitCoordinates = getBlochCoordinates(qubitState);

  const radius = 1;
  const axes: Axis[] = [
    { from: [0, 0, 0], to: [radius, 0, 0], color: 'red' }, // X-axis
    { from: [0, 0, 0], to: [0, radius, 0], color: 'green' }, // Y-axis
    { from: [0, 0, 0], to: [0, 0, radius], color: 'blue' }, // Z-axis
  ];

  return (
    <Canvas>
      <ambientLight />
      <pointLight position={[10, 10, 10]} />
      <Sphere args={[radius, 32, 32]} position={[0, 0, 0]}>
        <meshStandardMaterial color={'lightblue'} wireframe />
      </Sphere>
      {axes.map((axis, index) => (
        <Line key={index} points={[axis.from, axis.to]} color={axis.color} lineWidth={2} />
      ))}
      <mesh position={[qubitCoordinates.x, qubitCoordinates.y, qubitCoordinates.z]}>
        <sphereGeometry args={[0.05, 32, 32]} />
        <meshStandardMaterial color={'yellow'} />
      </mesh>
      <OrbitControls enableZoom enablePan />
    </Canvas>
  );
};

const App: React.FC = () => {
  return (
    <div style={{ height: '100vh' }}>
      <BlochSphere />
    </div>
  );
};

export default App;

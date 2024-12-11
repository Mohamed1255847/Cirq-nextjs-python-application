import React, { useEffect, useState } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Sphere, Line, Html } from '@react-three/drei';
import { multiply, abs, arg, atan2 } from 'mathjs';

interface Axis {
  from: [number, number, number];
  to: [number, number, number];
  color: string;
  label: string;
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
  const phi = arg(state[1]) || 0;
  return {
    x: Math.sin(theta) * Math.cos(phi),
    y: Math.sin(theta) * Math.sin(phi),
    z: Math.cos(theta),
    theta,
    phi,
  };
};

export const BlochSphere: React.FC = () => {
  const [qubitState, setQubitState] = useState([1, 0]); // Initial state |0⟩

  useEffect(() => {
    const newState = applyUnitary(hadamard, qubitState);
    setQubitState(newState);
  }, []);

  const { x, y, z, theta, phi } = getBlochCoordinates(qubitState);

  const radius = 1;
  const axes: Axis[] = [
    { from: [0, 0, 0], to: [radius, 0, 0], color: 'red', label: 'X' }, // X-axis
    { from: [0, 0, 0], to: [0, radius, 0], color: 'green', label: 'Y' }, // Y-axis
    { from: [0, 0, 0], to: [0, 0, radius], color: 'blue', label: 'Z' }, // Z-axis
  ];

  return (
    <Canvas style={{ height: '100vh' }}>
      <ambientLight />
      <pointLight position={[10, 10, 10]} />
      {/* Sphere with |0⟩ and |1⟩ labels */}
      <Sphere args={[radius, 32, 32]} position={[0, 0, 0]}>
        <meshStandardMaterial color={'lightblue'} wireframe />
      </Sphere>
      <Html position={[0, 0, radius + 0.2]} center>
        |0⟩
      </Html>
      <Html position={[0, 0, -radius - 0.2]} center>
        |1⟩
      </Html>
      {/* Axes */}
      {axes.map((axis, index) => (
        <Line key={index} points={[axis.from, axis.to]} color={axis.color} lineWidth={2}>
          <Html position={axis.to.map((v) => v + 0.2) as [number, number, number]} center>
            {axis.label}
          </Html>
        </Line>
      ))}
      {/* Qubit Position */}
      <mesh position={[x, y, z]}>
        <sphereGeometry args={[0.05, 32, 32]} />
        <meshStandardMaterial color={'yellow'} />
      </mesh>
      {/* Theta and Phi Information */}
      <Html position={[x, y, z]} center>
        <div style={{ color: 'white', backgroundColor: 'black', padding: '4px', borderRadius: '4px' }}>
          θ: {(theta * (180 / Math.PI)).toFixed(2)}°<br />
          φ: {(phi * (180 / Math.PI)).toFixed(2)}°
        </div>
      </Html>
      <OrbitControls enableZoom enablePan />
    </Canvas>
  );
};

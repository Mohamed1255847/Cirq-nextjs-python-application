'use client'; 
import React, { useRef } from 'react';
import { Canvas } from '@react-three/fiber';
import { Sphere, Line } from '@react-three/drei';
import { Line2 } from 'three-stdlib';


export const BlochSphere = ({ x, y, z }: { x: number, y: number, z: number }) => {
  const vectorRef = useRef<Line2 | null>(null);
  return (
    <Canvas>
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} />

      <Sphere args={[1, 32, 32]} visible>
        <meshStandardMaterial color="lightblue" wireframe />
      </Sphere>

      <Line
        points={[
          [0, 0, 0], // Start of X-axis
          [1.5, 0, 0], // End of X-axis
        ]}
        color="red"
        lineWidth={2}
      />
      <Line
        points={[
          [0, 0, 0], // Start of Y-axis
          [0, 1.5, 0], // End of Y-axis
        ]}
        color="green"
        lineWidth={2}
      />
      <Line
        points={[
          [0, 0, 0], // Start of Z-axis
          [0, 0, 1.5], // End of Z-axis
        ]}
        color="blue"
        lineWidth={2}
      />

      <Line
        ref={vectorRef}
        points={[
          [0, 0, 0], // Start of Bloch vector
          [x, y, z], // End of Bloch vector
        ]}
        color="yellow"
        lineWidth={4}
      />
    </Canvas>
  );
}


'use client'
import React, { useEffect, useRef } from 'react';
import { Circuit, Renderer, RxGate, MeasurementGate, XGate, HGate } from 'quantum-circuit-drawer';

interface QuantumCircuitProps {
    circuitString: string;
}

const QuantumCircuit: React.FC<QuantumCircuitProps> = ({ circuitString }) => {
    const containerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (containerRef.current && circuitString) {
            containerRef.current.innerHTML = '';

            const circuit = new Circuit(1); 
            const gates = circuitString.match(/([a-zA-Z]+(?:\([^)]*\))?)/g);
            gates?.forEach((gate, index) => {
                if (gate === 'Rx(π/2)') {
                    circuit.addGate(new RxGate(Math.PI / 2), index);
                } else if (gate === 'X') {
                    circuit.addGate(new XGate(), index);
                } else if (gate === 'H') {
                    circuit.addGate(new HGate(), index);
                } else if (gate === 'M(\'m\')') {
                    circuit.addGate(new MeasurementGate('m'), index);
                }
            });

            const renderer = new Renderer(circuit, containerRef?.current);
            renderer.draw();
        }
    }, [circuitString]);

    return <div ref={containerRef} style={{ width: '800px', height: '200px', border: '1px solid #ccc' }}></div>;
};

export default QuantumCircuit;


'use client';
import React, { useState } from 'react';
import ReactFlow, { Controls, Background } from 'reactflow';
import 'reactflow/dist/style.css';

export default function QFM() {
    const [inputString, setInputString] = useState('');
    const [result, setResult] = useState<{
        result: string;
        acceptance_probability: number;
        automata: {
            states: { id: string; label: string; type: string }[];
            transitions: { id: string; source: string; target: string; label: string }[];
        };
    } | null>(null);
    const [error, setError] = useState<string | null>(null);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        // Validate input
        if (!inputString || !/^[01]+$/.test(inputString)) {
            setError('Input string must contain only 0s and 1s.');
            return;
        }

        try {
            const response = await fetch('http://localhost:5000/qfa', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ input_string: inputString }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            setResult(data);
            setError(null); // Clear any previous errors
        } catch (err) {
            setError('An error occurred while simulating the QFA. Please try again.');
            console.error(err);
        }
    };

    // Convert automata structure to React Flow nodes and edges
    const nodes = result?.automata.states.map((state) => ({
        id: state.id,
        position: { x: Math.random() * 400, y: Math.random() * 400 }, // Random positions for simplicity
        data: { label: state.label },
        type: state.type,
    })) || [];

    const edges = result?.automata.transitions.map((transition) => ({
        id: transition.id,
        source: transition.source,
        target: transition.target,
        label: transition.label,
        animated: true, // Animate transitions
    })) || [];

    return (
        <div className="App" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '20px' }}>
            <h1>Quantum Finite Automata Simulator</h1>
            <form onSubmit={handleSubmit} style={{ marginBottom: '20px' }}>
                    <input
                        type="text"
                        value={inputString}
                        onChange={(e) => setInputString(e.target.value)}
                        placeholder="Enter a string of 0s and 1s"
                        style={{ marginLeft: '10px', padding: '5px' }}
                    />
                <button type="submit" style={{ marginLeft: '10px', padding: '5px 10px' }}>
                    Simulate
                </button>
            </form>

            {error && (
                <div style={{ color: 'red', marginBottom: '20px' }}>
                    <h2>Error:</h2>
                    <p>{error}</p>
                </div>
            )}

            {result && (
                <div style={{ marginBottom: '20px' }}>
                    <h2>Result:</h2>
                    <pre>{JSON.stringify(result, null, 2)}</pre>
                </div>
            )}

            <div style={{ width: '100%', height: '400px', border: '1px solid #ddd', borderRadius: '5px' }}>
                <ReactFlow nodes={nodes} edges={edges}>
                    <Background />
                    <Controls />
                </ReactFlow>
            </div>
        </div>
    );
}
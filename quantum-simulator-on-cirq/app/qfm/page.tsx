'use client';
import React, { useState } from 'react';

export default function QFM() {
    const [inputString, setInputString] = useState('');
    const [result, setResult] = useState<{ result: string; acceptance_probability: number } | null>(null);
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

    return (
        <div className="App">
            <h1>Quantum Finite Automata Simulator</h1>
            <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        value={inputString}
                        onChange={(e) => setInputString(e.target.value)}
                        placeholder="Enter a string of 0s and 1s"
                    />
                <button type="submit">Simulate</button>
            </form>

            {error && (
                <div style={{ color: 'red' }}>
                    <h2>Error:</h2>
                    <p>{error}</p>
                </div>
            )}

            {result && (
                <div>
                    <h2>Result:</h2>
                    <pre>{JSON.stringify(result, null, 2)}</pre>
                </div>
            )}
        </div>
    );
}
'use client'
import { useState } from 'react';
import { Input, Button, message } from 'antd';
import axios from 'axios';
import AutomataVisualization from '@/components/AutomataVisualization/page';

const MOQFA = () => {
    const [inputString, setInputString] = useState('');
    const [result, setResult] = useState<{
        result: string;
        acceptance_probability: number;
        automata: {
            states: { id: string; label: string; type: string }[];
            transitions: { id: string; source: string; target: string; label: string }[];
        };
    } | null>(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async () => {
        if (!inputString || !/^[01]+$/.test(inputString)) {
            message.error('Input string must contain only 0s and 1s.');
            return;
        }

        setLoading(true);
        try {
            const response = await axios.post('http://localhost:5000/mo-qfa', {
                input_string: inputString,
            });
            setResult(response.data);
        } catch (err) {
            message.error('An error occurred while simulating the QFA.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>Measure-Once Quantum Finite Automata (MO-QFA)</h1>
            <p>
                <strong>Description:</strong> MO-QFA performs a single measurement at the end of the computation.
                It is defined by a set of states, transition matrices, and an accepting state.
            </p>
            <p>
                <strong>Use Cases:</strong> MO-QFA is useful for problems where a single decision is made after processing the entire input.
                Examples include language recognition and decision problems.
            </p>
            <p>
                <strong>Problem and Solution:</strong> Consider the problem of recognizing the language of strings with an even number of 1s.
                MO-QFA can solve this by transitioning between states based on the input symbols and accepting if the final state corresponds to an even count.
            </p>
            <p>
                <strong>Why `0` and `1`:</strong> In quantum computing, `0` and `1` represent the basis states of a qubit.
                Quantum automata use these symbols to define transitions and measurements.
            </p>
            <p>
                <strong>Quantum vs. Classical:</strong> Unlike classical automata, quantum automata can exist in superpositions of states, allowing them to process multiple paths simultaneously.
                This gives quantum automata an advantage in certain computational tasks.
            </p>
            <Input
                placeholder="Enter a string of 0s and 1s"
                value={inputString}
                onChange={(e) => setInputString(e.target.value)}
                style={{ width: '300px', marginRight: '10px' }}
            />
            <Button type="primary" onClick={handleSubmit} loading={loading}>
                Simulate
            </Button>

            {result && (
                <div style={{ marginTop: '20px' }}>
                    <h2>Result:</h2>
                    <pre>{JSON.stringify(result, null, 2)}</pre>
                    <h2>Automata Visualization:</h2>
                    <AutomataVisualization
                        states={result.automata.states}
                        transitions={result.automata.transitions}
                    />
                </div>
            )}
        </div>
    );
};

export default MOQFA;
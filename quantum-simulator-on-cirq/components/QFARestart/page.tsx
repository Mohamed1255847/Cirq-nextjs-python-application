'use client'

import { useState } from 'react';
import { Input, Button, message } from 'antd';
import axios from 'axios';

const QFARestart = () => {
    const [inputString, setInputString] = useState('');
    const [result, setResult] = useState<{
        result: string;
        acceptance_probability: number;
    } | null>(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async () => {
        if (!inputString || !/^[01]+$/.test(inputString)) {
            message.error('Input string must contain only 0s and 1s.');
            return;
        }

        setLoading(true);
        try {
            const response = await axios.post('http://localhost:5000/qfa-restart', {
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
            <h1>Quantum Automata with Restart (QFA-R)</h1>
            <p>
                QFA-R can &quot;restart&quot; the computation if it reaches a non-halting state.
                It is defined by the following transition matrices:
                <pre>
                    T(0) = [[1, 0, 0], [0, 0, 1], [0, 1, 0]] (Swap q1 and q2)
                    T(1) = [[0, 1, 0], [1, 0, 0], [0, 0, 1]] (Swap q0 and q1)
                </pre>
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
                </div>
            )}
        </div>
    );
};

export default QFARestart;
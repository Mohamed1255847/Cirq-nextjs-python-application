'use client'
import React, { useState } from 'react';
import { BlochSphere } from '@/components/blochSphere/page';


export default function BlochSpherePage() {

    const [state, setState] = useState([1, 0]); // Initial state |0⟩


    return (
        <>
            <BlochSphere qubitState={state} />
            <button onClick={() => setState([0, 1])}>Change to |1⟩</button>
            <button onClick={() => setState([1 / Math.sqrt(2), 1 / Math.sqrt(2)])}>
                Change to |+⟩
            </button>
        </>
    )
} 
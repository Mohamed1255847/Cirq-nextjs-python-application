'use client'
import React from 'react';
import ReactFlow, { Controls, Background } from 'reactflow';
import 'reactflow/dist/style.css';

interface State {
    id: string;
    label: string;
    type: string;
}

interface Transition {
    id: string;
    source: string;
    target: string;
    label: string;
}

interface AutomataVisualizationProps {
    states: State[];
    transitions: Transition[];
}

const AutomataVisualization: React.FC<AutomataVisualizationProps> = ({ states, transitions }) => {
    // Convert states to React Flow nodes
    const nodes = states.map((state, index) => ({
        id: state.id,
        data: { label: state.label },
        position: { x: index * 200, y: 100 }, // Arrange states horizontally
        type: state.type === 'input' ? 'input' : state.type === 'output' ? 'output' : 'default',
    }));

    // Convert transitions to React Flow edges
    const edges = transitions.map((transition) => ({
        id: transition.id,
        source: transition.source,
        target: transition.target,
        label: transition.label,
        animated: true, // Animate transitions
    }));

    return (
        <div style={{ width: '100%', height: '400px', border: '1px solid #ddd', borderRadius: '5px' }}>
            <ReactFlow nodes={nodes} edges={edges}>
                <Background />
                <Controls />
            </ReactFlow>
        </div>
    );
};

export default AutomataVisualization;
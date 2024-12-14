"use client"

import styled from 'styled-components';


interface SymbolType { symbol: string; name: string; description: string; }
const symbols: SymbolType[] = [{ symbol: '───', name: 'Wire', description: 'Connects components' },
{ symbol: 'H', name: 'Hadamard Gate', description: 'Applies a Hadamard operation to create superposition' },
{ symbol: 'X', name: 'Pauli-X Gate', description: 'Flips the state of the qubit (quantum NOT gate)' },
{ symbol: 'M', name: 'Measurement', description: 'Measures the qubit state' },
{ symbol: '@', name: 'Control Line', description: 'Indicates control for conditional operations' },
{ symbol: '║', name: 'Vertical Line', description: 'Connects elements in vertical direction' },
{ symbol: '─', name: 'Horizontal Line', description: 'Connects elements in horizontal direction' },
{ symbol: '┼', name: 'Cross Point', description: 'Indicates intersection of connections' },
{ symbol: '^', name: 'Power Line', description: 'Indicates power connection' },
{ symbol: '┌──┐', name: 'Circuit Boundary', description: 'Encloses the circuit layout' },
{ symbol: '└──┘', name: 'Circuit Boundary End', description: 'Marks the end of a circuit layout' },
{ symbol: '╬', name: 'Joint', description: 'Connects multiple lines' },
{ symbol: 'm1, m2', name: 'Measurement Markers', description: 'Specific measurement points in the circuit' },];




const Container = styled.div`
  margin: 20px;
  font-family: Arial, sans-serif;
`;

const SymbolRow = styled.div`
  display: flex;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #ddd;
`;

const Symbol = styled.div`
  width: 60px;
  font-weight: bold;
`;

const Name = styled.div`
  width: 150px;
`;

const Description = styled.div`
  flex-grow: 1;
`;

export default function SymbolListPage() {
    return (<Container>
        {symbols.map((item, index) => (
            <SymbolRow key={index}>
                <Symbol>{item.symbol}</Symbol>
                <Name>{item.name}</Name>
                <Description>{item.description}</Description>
            </SymbolRow>
        ))}
    </Container>)
}


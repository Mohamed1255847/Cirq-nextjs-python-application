import styled from 'styled-components';




export const Container = styled.div`
  display: flex;
  height: 100vh;
  background-color: #f8f9fa;
`;

export const CircuitList = styled.div`
  flex: 1;
  background-color: rgba(255, 255, 255, 0.7);
  color: #343a40;
  padding: 20px;
  overflow-y: auto;
  border-right: 2px solid #dee2e6;
  backdrop-filter: blur(10px);
`;

export const CircuitButton = styled.button`
  display: block;
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  background-color: rgba(52, 58, 64, 0.8);
  border: none;
  cursor: pointer;
  color: white;
  text-align: left;
  font-size: 16px;
  border-radius: 5px;
  transition: background-color 0.3s;

  &:hover {
    background-color: rgba(52, 58, 64, 0.9);
  }
`;

export const CircuitDetails = styled.div`
  flex: 3;
  padding: 40px;
  overflow-y: auto;
  background-color: #ffffff;
  border-left: 2px solid #dee2e6;
`;

export const Title = styled.h2`
  margin-top: 0;
  color: #343a40;
`;

export const Info = styled.div`
  margin-bottom: 20px;
  font-size: 18px;
  color: #495057;
  line-height: 1.5;

  code {
    background: #f1f1f1;
    padding: 2px 4px;
    border-radius: 4px;
    font-family: 'Courier New', Courier, monospace;
  }
`;

export const Error = styled.h1`
  color: red;
`;

export const QuantumCircuitContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 20px;
  background-color: #fff;
  border: 2px solid #343a40;
  border-radius: 10px;
  width: fit-content;
`;

export const QubitLine = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 20px;
`;

export const Qubit = styled.div`
  width: 20px;
  height: 20px;
  border: 1px solid #343a40;
  border-radius: 50%;
  margin-right: 10px;
  background-color: #343a40;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
`;

export const Operation = styled.div`
  padding: 5px 10px;
  background-color: ${({ type }) => (type === 'measurement' ? '#28a745' : '#007bff')};
  color: white;
  margin-right: 10px;
  border-radius: 5px;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
`;

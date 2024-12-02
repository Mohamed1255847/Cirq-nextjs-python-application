'use client';

import React from 'react';
import styled from 'styled-components';

const MatrixContainer = styled.div`
  display: inline-block;
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px;
`;

const MatrixRow = styled.div`
  display: flex;
`;

const MatrixCell = styled.div`
  max-width: 250px ; 
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #ccc;
  margin: -1px 0 0 -1px; 
  overflow: hidden; 
  text-overflow: ellipsis;  
  white-space: nowrap;  
  padding:20px
`;

type MatrixProps = {
  data: (number | string)[][];
};

const Matrix: React.FC<MatrixProps> = ({ data }) => {
  return (
    <MatrixContainer>
      {data?.map((row, rowIndex) => (
        <MatrixRow key={rowIndex}>
          {row.map((value, colIndex) => (
            <MatrixCell key={colIndex}>
              {value}
            </MatrixCell>
          ))}
        </MatrixRow>
      ))}
    </MatrixContainer>
  );
};

export default Matrix;

import React from 'react';
import styled from 'styled-components';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { oneLight } from 'react-syntax-highlighter/dist/esm/styles/prism';

interface CodeBlockProps {
  code: string;
}

export const CodeContainerStyle = styled.div`
  background: #282c34;
  color: white;
  padding: 20px;
  border-radius: 10px;
  width: 80%;
  margin: 20px auto;
  text-align: center;
`;

export const CodeBlock: React.FC<CodeBlockProps> = ({ code }) => (
  <SyntaxHighlighter language="python" style={oneLight}>
    {code}
  </SyntaxHighlighter>
);



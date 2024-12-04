import Typist from 'react-typist';
import styled from 'styled-components';

const TypingContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f0f0;
  font-size: 2.5em;
  font-weight: bold;
  color: #000;
`;

const TypingEffect: React.FC = () => {
    return (
        <TypingContainer>
            <Typist>
                <Typist.Delay ms={500} />
                Marvelous Quantum
                <Typist.Backspace count={17} delay={1000} />
                Quantum Circuits Stand on Cirq from Google
                <Typist.Backspace count={43} delay={1000} />
                Quantum Gates Stand on Cirq from Google
                <Typist.Backspace count={43} delay={1000} />
                introduced by
                <Typist.Backspace count={20} delay={1000} />
                Mohamed Afify
                <Typist.Backspace count={20} delay={1000} />
                Andreea Florentina
                <Typist.Backspace count={20} delay={1000} />
                Mihai Neagu
                <Typist.Backspace count={20} delay={1000} />
                Marvelous Quantum
            </Typist>
        </TypingContainer>
    );
};

export default TypingEffect;

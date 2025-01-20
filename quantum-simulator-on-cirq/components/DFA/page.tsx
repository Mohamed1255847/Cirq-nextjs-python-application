'use client'
import "katex/dist/katex.min.css";
import { InlineMath, BlockMath } from "react-katex";
import Image from 'next/image'
import Figure1 from './32.png';

const DFAExplanation = () => {
    return (
        <div style={{ maxWidth: "800px", margin: "0 auto", padding: "20px" }}>
            <div
                style={{
                    textAlign: "center",
                    margin: "20px 0",
                    border: "1px solid #ccc",
                    padding: "10px",
                    borderRadius: "8px",
                }}
            >
                <Image
                    src={Figure1}
                    width={800}
                    height={400}
                    alt="Picture of the author"
                />

                <p style={{ marginTop: "10px", fontStyle: "italic" }}>
                    <strong>Fig. 1a:</strong> State diagram of a DFA.
                </p>
            </div>
            <h1>Deterministic Finite Automaton (DFA)</h1>

            <p>
                A <strong>Deterministic Finite Automaton (DFA)</strong> is a finite-state
                machine that accepts or rejects input strings of symbols. Here,{" "}
                <strong>deterministic</strong> refers to the fact that a DFA only
                produces a unique computation for each input string. We only consider the
                case of DFAs as it has been proven that DFAs have equivalent computing
                power to non-deterministic finite automata.
            </p>

            <h2>State Diagram of a DFA</h2>
            <p>
                As shown in <strong>Fig. 1a</strong>, a typical DFA is illustrated with a
                state diagram. In this example automaton, there are two states{" "}
                <InlineMath math="S_0" /> and <InlineMath math="S_1" />, which are
                denoted graphically by circles. The automaton takes a finite sequence of{" "}
                <InlineMath math="0" />s and <InlineMath math="1" />s as input.
            </p>

            <h3>Transitions</h3>
            <p>
                For each state, there is a transition arrow leading out to a next state
                for both <InlineMath math="0" /> and <InlineMath math="1" />. Upon
                reading a symbol, a DFA jumps deterministically from one state to another
                by following the transition arrow. For example, if the automaton is
                currently in state <InlineMath math="S_0" /> and the current input symbol
                is <InlineMath math="1" />, then it deterministically jumps to state{" "}
                <InlineMath math="S_1" />.
            </p>

            <h3>Start and Accepted States</h3>
            <p>
                A DFA has a <strong>start state</strong> (denoted graphically by an arrow
                coming in from nowhere) where computations begin, and a set of{" "}
                <strong>accepted states</strong> (denoted graphically by a double
                circle). If the automaton ends at an accepted state after reading the
                last symbol of the input string, this string of symbols is regarded as
                being accepted by the DFA; otherwise, it is regarded as being rejected by
                the DFA.
            </p>

            <h2>Example: Even Binary Number</h2>
            <p>
                DFAs are often used to solve (recognize) decision problems, which are
                defined as computational problems where the answer for every instance is
                either <strong>Yes</strong> or <strong>No</strong>. For example,
                determining whether a binary number is even or not is a typical decision
                problem, which can be solved by the DFA shown in <strong>Fig. 1a</strong>
                .
            </p>

            <h3>Mathematical Representation</h3>
            <p>
                The DFA for recognizing even binary numbers can be represented as:
            </p>
            <BlockMath
                math={`
          \\text{DFA} = (Q, \\Sigma, \\delta, q_0, F)
        `}
            />
            <ul>
                <li>
                    <InlineMath math="Q" />: Set of states, e.g.,{" "}
                    <InlineMath math="Q = \\{S_0, S_1\\}" />
                </li>
                <li>
                    <InlineMath math="\\Sigma" />: Input alphabet, e.g.,{" "}
                    <InlineMath math="\\Sigma = \\{0, 1\\}" />
                </li>
                <li>
                    <InlineMath math="\\delta" />: Transition function, e.g.,{" "}
                    <InlineMath math="\\delta(S_0, 0) = S_0" />,{" "}
                    <InlineMath math="\\delta(S_0, 1) = S_1" />
                </li>
                <li>
                    <InlineMath math="q_0" />: Start state, e.g.,{" "}
                    <InlineMath math="q_0 = S_0" />
                </li>
                <li>
                    <InlineMath math="F" />: Set of accepted states, e.g.,{" "}
                    <InlineMath math="F = \\{S_0\\}" />
                </li>
            </ul>

            <h3>State Diagram</h3>
            <p>
                The state diagram for this DFA can be visualized as:
            </p>
            <pre>
                {`
        +-------+      0      +-------+
        |       | ----------> |       |
        |  S0   |             |  S1   |
        |       | <---------- |       |
        +-------+      1      +-------+
        `}
            </pre>
            <p>
                Here, <InlineMath math="S_0" /> is both the start state and the accepted
                state. The DFA accepts strings that end with <InlineMath math="0" />,
                which correspond to even binary numbers.
            </p>
        </div>
    );
};

export default DFAExplanation;
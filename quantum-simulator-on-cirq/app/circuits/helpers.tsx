import {QuantumCircuitContainer , QubitLine ,Qubit ,Operation} from './parts'




export const QuantumCircuit = ({ circuit }: React.FC) => {
    const operations = circuit.match(/X\^0\.5|M\('m'\)|H|X|Y|Z|S|T/g) || [];
 
   return (
     <QuantumCircuitContainer>
       <QubitLine>
         <Qubit>Q0</Qubit>
         {operations.map((op, idx) => (
           <Operation key={idx} type={op.startsWith('M') ? 'measurement' : 'gate'}>
             {op}
           </Operation>
         ))}
       </QubitLine>
     </QuantumCircuitContainer>
   );
 };
 
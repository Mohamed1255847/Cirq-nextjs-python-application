import { CircuitInfoType } from "./types";

 export const circuitOptions: CircuitInfoType[] = [
   {
     id: 0,
     name: "Simplest Quantum Circuit Result",
     message: "",
     circuit: "(0, 0): ───X^0.5───M('m')───",
   },
   {
     id: 1,
     name: "Bell State Circuit",
     message: "",
     circuit: "(0, 0): ───H───@───M('m')───",
   },
   {
     id: 2,
     name: "Basic Gates Circuit",
     message: "",
     circuit: "(1, 0): ───X───Y───Z───M('m')───",
   },
   {
     id: 3,
     name: "Quantum Fourier Transform",
     message: "",
     circuit: "(0, 0): ───H───S───T───M('m')───",
   },
   {
     id: 4,
     name: "Teleportation Circuit",
     message: "",
     circuit: "(0, 0): ───H───@───M('m')───",
   },
   {
     id: 5,
     name: "Variational Quantum Eigensolver",
     message: "",
     circuit: "(0, 0): ───H───X───Y───Z───M('m')───",
   },
   {
     id: 6,
     name: "Phase Estimation Circuit",
     message: "",
     circuit: "(0, 0): ───H───S───T───M('m')───",
   },
   {
     id: 7,
     name: "Deutsch-Jozsa Circuit",
     message: "",
     circuit: "(0, 0): ───H───@───M('m')───",
   },
   {
     id: 8,
     name: "Entanglement Swapping Circuit",
     message: "",
     circuit: "(0, 0): ───H───@───M('m')───",
   },
 ];


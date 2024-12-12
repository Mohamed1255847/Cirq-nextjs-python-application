import {Circuit} from './types';



export const circuitOptions: Circuit[] = [
    { id: 2, name: 'Simplest Quantum Circuit Result', message: '', circuit: '(0, 0): ───X^0.5───M(\'m\')───' },
    { id: 3, name: 'Bell State Circuit', message: '', circuit: '(0, 0): ───H───@───M(\'m\')───' },
    { id: 4, name: 'Basic Gates Circuit', message: '', circuit: '(1, 0): ───X───Y───Z───M(\'m\')───' },
    { id: 5, name: 'QFT Circuit', message: '', circuit: '(0, 0): ───H───S───T───M(\'m\')───' },
    { id: 6, name: 'Teleportation Circuit', message: '', circuit: '(0, 0): ───H───@───M(\'m\')───' },
    { id: 7, name: 'VQE Circuit', message: '', circuit: '(0, 0): ───H───X───Y───Z───M(\'m\')───' },
    { id: 8, name: 'Phase Estimation Circuit', message: '', circuit: '(0, 0): ───H───S───T───M(\'m\')───' },
    { id: 9, name: 'Deutsch-Jozsa Circuit', message: '', circuit: '(0, 0): ───H───@───M(\'m\')───' },
    { id: 10, name: 'Entanglement Swapping Circuit', message: '', circuit: '(0, 0): ───H───@───M(\'m\')───' },
  ];
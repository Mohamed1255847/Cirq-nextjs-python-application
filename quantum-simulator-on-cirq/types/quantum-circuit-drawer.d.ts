declare module 'quantum-circuit-drawer' {
    export class Circuit {
        constructor(numQubits: number);
        addGate(gate: any, index: number): void;
    }

    export class Renderer {
        constructor(circuit: Circuit, elementId: string);
        draw(): void;
    }

    export class RxGate {
        constructor(angle: number);
    }

    export class MeasurementGate {
        constructor(name: string);
    }

    export class XGate {}
    export class HGate {}
}

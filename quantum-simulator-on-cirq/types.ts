declare module 'three/examples/jsm/lines/Line2' {
    import { Line } from 'three';
    export class Line2 extends Line {
      // Additional properties and methods for Line2
    }
  }
  
  declare module 'three/examples/jsm/lines/LineMaterial' {
    import { ShaderMaterial } from 'three';
    export class LineMaterial extends ShaderMaterial {
      linewidth: number;
      // Additional properties and methods for LineMaterial
    }
  }
  
  declare module 'three/examples/jsm/lines/LineGeometry' {
    import { BufferGeometry } from 'three';
    export class LineGeometry extends BufferGeometry {
      setPositions(array: number[]): void;
      // Additional properties and methods for LineGeometry
    }
  }
  
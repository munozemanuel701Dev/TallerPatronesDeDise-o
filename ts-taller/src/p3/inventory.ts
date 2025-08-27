/**
 * Punto 3: Control/Optimización de inventario con Strategy.
 *
 * El dominio se modela con `InventoryStructure`. Los algoritmos de análisis
 * se encapsulan detrás de la interfaz `OptimizationAlgorithm` y se pueden
 * conmutar en tiempo de ejecución desde `InventoryContext`.
 */
export interface InventoryStructure {
  products: number;
  warehouses: number;
  shelves: number;
  distributionCenters: number;
  factories: number;
}

export interface OptimizationAlgorithm {
  name: string;
  analyze(structure: InventoryStructure): string;
}

export class SimpleReorder implements OptimizationAlgorithm {
  name = "SimpleReorder";
  analyze(s: InventoryStructure): string {
    const safetyStock = Math.ceil(s.products * 0.1);
    return `Mantener stock de seguridad: ${safetyStock}`;
  }
}

export class BalanceWarehouses implements OptimizationAlgorithm {
  name = "BalanceWarehouses";
  analyze(s: InventoryStructure): string {
    const ratio = s.warehouses > 0 ? s.products / s.warehouses : s.products;
    return `Balancear a ~${Math.ceil(ratio)} productos por almacén`;
  }
}

export class InventoryContext {
  constructor(private algorithm: OptimizationAlgorithm) {}
  setAlgorithm(algorithm: OptimizationAlgorithm) {
    this.algorithm = algorithm;
  }
  run(structure: InventoryStructure) {
    return this.algorithm.analyze(structure);
  }
}



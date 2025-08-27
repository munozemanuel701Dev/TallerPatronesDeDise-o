/**
 * Punto 5: Tres patrones de distintos grupos en un ejemplo mínimo.
 * - Creacional: Singleton (`AppConfig`).
 * - Estructural: Facade (`ShopFacade`).
 * - Comportamiento: Observer (`PriceSubject`).
 */
// Singleton
export class AppConfig {
  private static instance: AppConfig | null = null;
  private constructor(public readonly version: string) {}
  static getInstance() {
    if (!this.instance) this.instance = new AppConfig("1.0.0");
    return this.instance;
  }
}

// Facade
class PaymentGateway { charge(amount: number) { return `Cobrado ${amount}`; } }
class InventoryService { reserve(sku: string) { return `Reservado ${sku}`; } }
export class ShopFacade {
  private pay = new PaymentGateway();
  private inv = new InventoryService();
  checkout(sku: string, amount: number) {
    const r1 = this.inv.reserve(sku);
    const r2 = this.pay.charge(amount);
    return `${r1} | ${r2}`;
  }
}

// Observer
export interface Observer { update(price: number): void; }
export class PriceSubject {
  private observers: Observer[] = [];
  attach(o: Observer) { this.observers.push(o); }
  detach(o: Observer) { this.observers = this.observers.filter(x => x !== o); }
  setPrice(p: number) { for (const o of this.observers) o.update(p); }
}
export class EmailNotifier implements Observer {
  update(price: number): void { console.log(`P5 - email precio: ${price}`); }
}

export function runP5Demo() {
  console.log("P5 - Singleton version:", AppConfig.getInstance().version);
  const shop = new ShopFacade();
  console.log("P5 - Facade:", shop.checkout("SKU-1", 99));
  const subject = new PriceSubject();
  subject.attach(new EmailNotifier());
  subject.setPrice(123);
}



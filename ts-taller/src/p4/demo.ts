/**
 * Demostración del Punto 4.
 * Apilamos decoradores sobre `SavingsAccount` y probamos casos límite.
 */
import { AMLDepositNotifier, LargeWithdrawAuthorization, SavingsAccount, WeeklyWithdrawLimit } from "./account.js";

export function runP4Demo() {
  const base = new SavingsAccount();
  const withLimit = new WeeklyWithdrawLimit(base, 2);
  const withAuth = new LargeWithdrawAuthorization(withLimit, 100, (amount) => {
    return amount <= 500; // simular aprobación simple
  });
  const withAML = new AMLDepositNotifier(withAuth, 50, (amount) => {
    console.log("P4 - AML: depósito alto notificado:", amount);
  });

  withAML.deposit(200);
  withAML.deposit(60);
  console.log("P4 - balance tras depósitos:", withAML.balance());
  withAML.withdraw(50);
  withAML.withdraw(30);
  try { withAML.withdraw(20); } catch (e) { console.log("P4 - tercer retiro bloqueado"); }
  try { withAML.withdraw(200); } catch (e) { console.log("P4 - retiro grande sin autorización bloqueado"); }
}



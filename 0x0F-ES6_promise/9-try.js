export default function guardrail(mathFunction) {
  const queue = [];
  let x = 0;
  try {
    x = mathFunction();
  } catch (e) {
    x = `Error: ${e.message}`;
  }
  queue.push(x);
  queue.push('Guardrail was processed');
  return queue;
}

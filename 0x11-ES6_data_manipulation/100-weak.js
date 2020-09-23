export const weakMap = new WeakMap();
export function queryAPI(endpoint) {
  let calls = 0;
  if (weakMap.has(endpoint)) {
    calls = weakMap.get(endpoint);
  }
  weakMap.set(endpoint, calls + 1);
  if (calls + 1 >= 5) {
    throw Error('Endpoint load is high');
  }
}

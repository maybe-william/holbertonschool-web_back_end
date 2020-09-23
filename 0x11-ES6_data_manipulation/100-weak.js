export const weakMap = new WeakMap();
export default function queryAPI(endpoint) {
  let calls = weakMap.get(endpoint);
  if (calls === undefined) {
    calls = 0;
  }
  weakMap.set(endpoint, calls + 1);
  if (calls + 1 >= 5) {
    throw Error('Endpoint load is high');
  }
}

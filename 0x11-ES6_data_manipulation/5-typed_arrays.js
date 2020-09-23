export default function createInt8TypedArray(length, position, value) {
  const x = new Int8Array(length);
  x.set(value, position);
  return x;
}

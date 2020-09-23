export default function createInt8TypedArray(length, position, value) {
  const x = new UInt8Array(length);
  x.set(value, position);
  return x;
}

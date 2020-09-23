export default function setFromArray(arr) {
  if (!Array.isArray(arr)) {
    return new Set();
  }
  return new Set(arr);
}

export default function updateUniqueItems(map) {
  if (map instanceof Map) {
    for (const x of map) {
      if (x[1] === 1) {
        map.set(x[0], 100);
      }
    }
    return map;
  }
  throw Error('Cannot process');
}

export default function createIteratorObject(report) {
  const employees = [];
  for (const x in report.allEmployees) {
    if (report.allEmployees.hasOwnPropery(x)) {
      for (const y of report.allEmployees[x]) {
        employees.push(y);
      }
    }
  }
  const obj = {
    [Symbol.iterator]() {
      const next = () => {
        if (employees.length === 0) {
          return {
            value: undefined,
            done: true,
          };
        }
        return {
          value: employees.pop(),
          done: false,
        };
      };
      return next;
    },
  };
  return obj;
}

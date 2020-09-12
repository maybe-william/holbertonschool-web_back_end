export default function createReportObject(employeesList) {
  const ret = {
    allEmployees: { ...employeesList },
    getNumberOfDepartments(employeesList) {
      return [...employeesList].length / 2;
    },

  };
  return ret;
}

export default function createReportObject(employeesList) {
  const ret = {
    allEmployees: { ...employeesList },
    getNumberOfDepartments(employeesList) {
      return Object.keys({ ...employeesList }).length;
    },

  };
  return ret;
}

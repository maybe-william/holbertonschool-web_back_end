export default function createReportObject(employeesList) {
  const ret = {
    allEmployees: { ...employeesList },
    getNumberOfDepartments(EmployeesList) {
        return [...employeesList].length / 2;
    },

  };
  return ret;
}

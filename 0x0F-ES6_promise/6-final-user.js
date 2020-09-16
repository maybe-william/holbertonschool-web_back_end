import createUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const x = uploadPhoto(fileName);
  const y = createUser(firstName, lastName);
  return Promise.allSettled([y, x]).then((res) => {
    for (const x of res) {
      if (x.status === 'rejected') {
        x.value = `Error: ${x.reason.message}`;
        delete x.reason;
      }
    }
    return res;
  });
}

import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const x = uploadPhoto();
  const y = createUser();
  return Promise.all(x, y)
    .then((values) => console.log(`${values[0].body} ${values[1].firstName} ${values[1].lastName}`),
      () => console.log('Signup system offline'));
}

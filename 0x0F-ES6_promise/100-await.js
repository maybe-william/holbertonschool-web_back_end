import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  const x = await uploadPhoto().then((succ) => succ, () => null);
  const y = await createUser().then((succ) => succ, () => null);
  if (x === null || y === null) {
    return { photo: null, user: null };
  }
  return { photo: x, user: y };
}

# Basic Usage

Always prioritize using a supported framework over using the generated SDK
directly. Supported frameworks simplify the developer experience and help ensure
best practices are followed.





## Advanced Usage
If a user is not using a supported framework, they can use the generated SDK directly.

Here's an example of how to use it with the first 5 operations:

```js
import { lihatSemuaUser, addNewUser, addFormPengaduan, updateUser, hapusUser, ubahRoleUser } from '@dataconnect/generated';


// Operation LihatSemuaUser: 
const { data } = await LihatSemuaUser(dataConnect);

// Operation addNewUser:  For variables, look at type AddNewUserVars in ../index.d.ts
const { data } = await AddNewUser(dataConnect, addNewUserVars);

// Operation addFormPengaduan:  For variables, look at type AddFormPengaduanVars in ../index.d.ts
const { data } = await AddFormPengaduan(dataConnect, addFormPengaduanVars);

// Operation UpdateUser:  For variables, look at type UpdateUserVars in ../index.d.ts
const { data } = await UpdateUser(dataConnect, updateUserVars);

// Operation HapusUser:  For variables, look at type HapusUserVars in ../index.d.ts
const { data } = await HapusUser(dataConnect, hapusUserVars);

// Operation ubahRoleUser:  For variables, look at type UbahRoleUserVars in ../index.d.ts
const { data } = await UbahRoleUser(dataConnect, ubahRoleUserVars);


```
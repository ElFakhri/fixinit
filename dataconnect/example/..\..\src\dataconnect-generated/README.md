# Generated TypeScript README
This README will guide you through the process of using the generated JavaScript SDK package for the connector `example`. It will also provide examples on how to use your generated SDK to call your Data Connect queries and mutations.

***NOTE:** This README is generated alongside the generated SDK. If you make changes to this file, they will be overwritten when the SDK is regenerated.*

# Table of Contents
- [**Overview**](#generated-javascript-readme)
- [**Accessing the connector**](#accessing-the-connector)
  - [*Connecting to the local Emulator*](#connecting-to-the-local-emulator)
- [**Queries**](#queries)
  - [*LihatSemuaUser*](#lihatsemuauser)
- [**Mutations**](#mutations)
  - [*addNewUser*](#addnewuser)
  - [*addFormPengaduan*](#addformpengaduan)

# Accessing the connector
A connector is a collection of Queries and Mutations. One SDK is generated for each connector - this SDK is generated for the connector `example`. You can find more information about connectors in the [Data Connect documentation](https://firebase.google.com/docs/data-connect#how-does).

You can use this generated SDK by importing from the package `@dataconnect/generated` as shown below. Both CommonJS and ESM imports are supported.

You can also follow the instructions from the [Data Connect documentation](https://firebase.google.com/docs/data-connect/web-sdk#set-client).

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig } from '@dataconnect/generated';

const dataConnect = getDataConnect(connectorConfig);
```

## Connecting to the local Emulator
By default, the connector will connect to the production service.

To connect to the emulator, you can use the following code.
You can also follow the emulator instructions from the [Data Connect documentation](https://firebase.google.com/docs/data-connect/web-sdk#instrument-clients).

```typescript
import { connectDataConnectEmulator, getDataConnect } from 'firebase/data-connect';
import { connectorConfig } from '@dataconnect/generated';

const dataConnect = getDataConnect(connectorConfig);
connectDataConnectEmulator(dataConnect, 'localhost', 9399);
```

After it's initialized, you can call your Data Connect [queries](#queries) and [mutations](#mutations) from your generated SDK.

# Queries

There are two ways to execute a Data Connect Query using the generated Web SDK:
- Using a Query Reference function, which returns a `QueryRef`
  - The `QueryRef` can be used as an argument to `executeQuery()`, which will execute the Query and return a `QueryPromise`
- Using an action shortcut function, which returns a `QueryPromise`
  - Calling the action shortcut function will execute the Query and return a `QueryPromise`

The following is true for both the action shortcut function and the `QueryRef` function:
- The `QueryPromise` returned will resolve to the result of the Query once it has finished executing
- If the Query accepts arguments, both the action shortcut function and the `QueryRef` function accept a single argument: an object that contains all the required variables (and the optional variables) for the Query
- Both functions can be called with or without passing in a `DataConnect` instance as an argument. If no `DataConnect` argument is passed in, then the generated SDK will call `getDataConnect(connectorConfig)` behind the scenes for you.

Below are examples of how to use the `example` connector's generated functions to execute each query. You can also follow the examples from the [Data Connect documentation](https://firebase.google.com/docs/data-connect/web-sdk#using-queries).

## LihatSemuaUser
You can execute the `LihatSemuaUser` query using the following action shortcut function, or by calling `executeQuery()` after calling the following `QueryRef` function, both of which are defined in [..\..\src\dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
lihatSemuaUser(options?: ExecuteQueryOptions): QueryPromise<LihatSemuaUserData, undefined>;

interface LihatSemuaUserRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<LihatSemuaUserData, undefined>;
}
export const lihatSemuaUserRef: LihatSemuaUserRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `QueryRef` function.
```typescript
lihatSemuaUser(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<LihatSemuaUserData, undefined>;

interface LihatSemuaUserRef {
  ...
  (dc: DataConnect): QueryRef<LihatSemuaUserData, undefined>;
}
export const lihatSemuaUserRef: LihatSemuaUserRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the lihatSemuaUserRef:
```typescript
const name = lihatSemuaUserRef.operationName;
console.log(name);
```

### Variables
The `LihatSemuaUser` query has no variables.
### Return Type
Recall that executing the `LihatSemuaUser` query returns a `QueryPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `LihatSemuaUserData`, which is defined in [..\..\src\dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface LihatSemuaUserData {
  profiles: ({
    id: string;
    email: string;
    namaLengkap: string;
    role: string;
  } & Profile_Key)[];
}
```
### Using `LihatSemuaUser`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, lihatSemuaUser } from '@dataconnect/generated';


// Call the `lihatSemuaUser()` function to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await lihatSemuaUser();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await lihatSemuaUser(dataConnect);

console.log(data.profiles);

// Or, you can use the `Promise` API.
lihatSemuaUser().then((response) => {
  const data = response.data;
  console.log(data.profiles);
});
```

### Using `LihatSemuaUser`'s `QueryRef` function

```typescript
import { getDataConnect, executeQuery } from 'firebase/data-connect';
import { connectorConfig, lihatSemuaUserRef } from '@dataconnect/generated';


// Call the `lihatSemuaUserRef()` function to get a reference to the query.
const ref = lihatSemuaUserRef();

// You can also pass in a `DataConnect` instance to the `QueryRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = lihatSemuaUserRef(dataConnect);

// Call `executeQuery()` on the reference to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeQuery(ref);

console.log(data.profiles);

// Or, you can use the `Promise` API.
executeQuery(ref).then((response) => {
  const data = response.data;
  console.log(data.profiles);
});
```

# Mutations

There are two ways to execute a Data Connect Mutation using the generated Web SDK:
- Using a Mutation Reference function, which returns a `MutationRef`
  - The `MutationRef` can be used as an argument to `executeMutation()`, which will execute the Mutation and return a `MutationPromise`
- Using an action shortcut function, which returns a `MutationPromise`
  - Calling the action shortcut function will execute the Mutation and return a `MutationPromise`

The following is true for both the action shortcut function and the `MutationRef` function:
- The `MutationPromise` returned will resolve to the result of the Mutation once it has finished executing
- If the Mutation accepts arguments, both the action shortcut function and the `MutationRef` function accept a single argument: an object that contains all the required variables (and the optional variables) for the Mutation
- Both functions can be called with or without passing in a `DataConnect` instance as an argument. If no `DataConnect` argument is passed in, then the generated SDK will call `getDataConnect(connectorConfig)` behind the scenes for you.

Below are examples of how to use the `example` connector's generated functions to execute each mutation. You can also follow the examples from the [Data Connect documentation](https://firebase.google.com/docs/data-connect/web-sdk#using-mutations).

## addNewUser
You can execute the `addNewUser` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [..\..\src\dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
addNewUser(vars: AddNewUserVariables): MutationPromise<AddNewUserData, AddNewUserVariables>;

interface AddNewUserRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (vars: AddNewUserVariables): MutationRef<AddNewUserData, AddNewUserVariables>;
}
export const addNewUserRef: AddNewUserRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
addNewUser(dc: DataConnect, vars: AddNewUserVariables): MutationPromise<AddNewUserData, AddNewUserVariables>;

interface AddNewUserRef {
  ...
  (dc: DataConnect, vars: AddNewUserVariables): MutationRef<AddNewUserData, AddNewUserVariables>;
}
export const addNewUserRef: AddNewUserRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the addNewUserRef:
```typescript
const name = addNewUserRef.operationName;
console.log(name);
```

### Variables
The `addNewUser` mutation requires an argument of type `AddNewUserVariables`, which is defined in [..\..\src\dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:

```typescript
export interface AddNewUserVariables {
  id: string;
  email: string;
  namaLengkap: string;
}
```
### Return Type
Recall that executing the `addNewUser` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `AddNewUserData`, which is defined in [..\..\src\dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface AddNewUserData {
  profile_insert: Profile_Key;
}
```
### Using `addNewUser`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, addNewUser, AddNewUserVariables } from '@dataconnect/generated';

// The `addNewUser` mutation requires an argument of type `AddNewUserVariables`:
const addNewUserVars: AddNewUserVariables = {
  id: ..., 
  email: ..., 
  namaLengkap: ..., 
};

// Call the `addNewUser()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await addNewUser(addNewUserVars);
// Variables can be defined inline as well.
const { data } = await addNewUser({ id: ..., email: ..., namaLengkap: ..., });

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await addNewUser(dataConnect, addNewUserVars);

console.log(data.profile_insert);

// Or, you can use the `Promise` API.
addNewUser(addNewUserVars).then((response) => {
  const data = response.data;
  console.log(data.profile_insert);
});
```

### Using `addNewUser`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, addNewUserRef, AddNewUserVariables } from '@dataconnect/generated';

// The `addNewUser` mutation requires an argument of type `AddNewUserVariables`:
const addNewUserVars: AddNewUserVariables = {
  id: ..., 
  email: ..., 
  namaLengkap: ..., 
};

// Call the `addNewUserRef()` function to get a reference to the mutation.
const ref = addNewUserRef(addNewUserVars);
// Variables can be defined inline as well.
const ref = addNewUserRef({ id: ..., email: ..., namaLengkap: ..., });

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = addNewUserRef(dataConnect, addNewUserVars);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.profile_insert);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.profile_insert);
});
```

## addFormPengaduan
You can execute the `addFormPengaduan` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [..\..\src\dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
addFormPengaduan(vars: AddFormPengaduanVariables): MutationPromise<AddFormPengaduanData, AddFormPengaduanVariables>;

interface AddFormPengaduanRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (vars: AddFormPengaduanVariables): MutationRef<AddFormPengaduanData, AddFormPengaduanVariables>;
}
export const addFormPengaduanRef: AddFormPengaduanRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
addFormPengaduan(dc: DataConnect, vars: AddFormPengaduanVariables): MutationPromise<AddFormPengaduanData, AddFormPengaduanVariables>;

interface AddFormPengaduanRef {
  ...
  (dc: DataConnect, vars: AddFormPengaduanVariables): MutationRef<AddFormPengaduanData, AddFormPengaduanVariables>;
}
export const addFormPengaduanRef: AddFormPengaduanRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the addFormPengaduanRef:
```typescript
const name = addFormPengaduanRef.operationName;
console.log(name);
```

### Variables
The `addFormPengaduan` mutation requires an argument of type `AddFormPengaduanVariables`, which is defined in [..\..\src\dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:

```typescript
export interface AddFormPengaduanVariables {
  id: string;
  namaLengkap: string;
  email: string;
  description: string;
  lokasi: string;
  pictureUrl?: string | null;
}
```
### Return Type
Recall that executing the `addFormPengaduan` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `AddFormPengaduanData`, which is defined in [..\..\src\dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface AddFormPengaduanData {
  pengaduan_insert: Pengaduan_Key;
}
```
### Using `addFormPengaduan`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, addFormPengaduan, AddFormPengaduanVariables } from '@dataconnect/generated';

// The `addFormPengaduan` mutation requires an argument of type `AddFormPengaduanVariables`:
const addFormPengaduanVars: AddFormPengaduanVariables = {
  id: ..., 
  namaLengkap: ..., 
  email: ..., 
  description: ..., 
  lokasi: ..., 
  pictureUrl: ..., // optional
};

// Call the `addFormPengaduan()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await addFormPengaduan(addFormPengaduanVars);
// Variables can be defined inline as well.
const { data } = await addFormPengaduan({ id: ..., namaLengkap: ..., email: ..., description: ..., lokasi: ..., pictureUrl: ..., });

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await addFormPengaduan(dataConnect, addFormPengaduanVars);

console.log(data.pengaduan_insert);

// Or, you can use the `Promise` API.
addFormPengaduan(addFormPengaduanVars).then((response) => {
  const data = response.data;
  console.log(data.pengaduan_insert);
});
```

### Using `addFormPengaduan`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, addFormPengaduanRef, AddFormPengaduanVariables } from '@dataconnect/generated';

// The `addFormPengaduan` mutation requires an argument of type `AddFormPengaduanVariables`:
const addFormPengaduanVars: AddFormPengaduanVariables = {
  id: ..., 
  namaLengkap: ..., 
  email: ..., 
  description: ..., 
  lokasi: ..., 
  pictureUrl: ..., // optional
};

// Call the `addFormPengaduanRef()` function to get a reference to the mutation.
const ref = addFormPengaduanRef(addFormPengaduanVars);
// Variables can be defined inline as well.
const ref = addFormPengaduanRef({ id: ..., namaLengkap: ..., email: ..., description: ..., lokasi: ..., pictureUrl: ..., });

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = addFormPengaduanRef(dataConnect, addFormPengaduanVars);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.pengaduan_insert);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.pengaduan_insert);
});
```


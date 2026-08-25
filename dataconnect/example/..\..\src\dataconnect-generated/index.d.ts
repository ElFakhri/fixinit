import { ConnectorConfig, DataConnect, QueryRef, QueryPromise, ExecuteQueryOptions, MutationRef, MutationPromise, DataConnectSettings } from 'firebase/data-connect';

export const connectorConfig: ConnectorConfig;
export const dataConnectSettings: DataConnectSettings;

export type TimestampString = string;
export type UUIDString = string;
export type Int64String = string;
export type DateString = string;




export interface AddFormPengaduanData {
  pengaduan_insert: Pengaduan_Key;
}

export interface AddFormPengaduanVariables {
  id: string;
  namaLengkap: string;
  email: string;
  description: string;
  lokasi: string;
  pictureUrl?: string | null;
}

export interface AddNewUserData {
  profile_insert: Profile_Key;
}

export interface AddNewUserVariables {
  id: string;
  email: string;
  namaLengkap: string;
}

export interface LihatSemuaUserData {
  profiles: ({
    id: string;
    email: string;
    namaLengkap: string;
    role: string;
  } & Profile_Key)[];
}

export interface Pengaduan_Key {
  id: string;
  __typename?: 'Pengaduan_Key';
}

export interface Profile_Key {
  id: string;
  __typename?: 'Profile_Key';
}

interface LihatSemuaUserRef {
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<LihatSemuaUserData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): QueryRef<LihatSemuaUserData, undefined>;
  operationName: string;
}
export const lihatSemuaUserRef: LihatSemuaUserRef;

export function lihatSemuaUser(options?: ExecuteQueryOptions): QueryPromise<LihatSemuaUserData, undefined>;
export function lihatSemuaUser(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<LihatSemuaUserData, undefined>;

interface AddNewUserRef {
  /* Allow users to create refs without passing in DataConnect */
  (vars: AddNewUserVariables): MutationRef<AddNewUserData, AddNewUserVariables>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect, vars: AddNewUserVariables): MutationRef<AddNewUserData, AddNewUserVariables>;
  operationName: string;
}
export const addNewUserRef: AddNewUserRef;

export function addNewUser(vars: AddNewUserVariables): MutationPromise<AddNewUserData, AddNewUserVariables>;
export function addNewUser(dc: DataConnect, vars: AddNewUserVariables): MutationPromise<AddNewUserData, AddNewUserVariables>;

interface AddFormPengaduanRef {
  /* Allow users to create refs without passing in DataConnect */
  (vars: AddFormPengaduanVariables): MutationRef<AddFormPengaduanData, AddFormPengaduanVariables>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect, vars: AddFormPengaduanVariables): MutationRef<AddFormPengaduanData, AddFormPengaduanVariables>;
  operationName: string;
}
export const addFormPengaduanRef: AddFormPengaduanRef;

export function addFormPengaduan(vars: AddFormPengaduanVariables): MutationPromise<AddFormPengaduanData, AddFormPengaduanVariables>;
export function addFormPengaduan(dc: DataConnect, vars: AddFormPengaduanVariables): MutationPromise<AddFormPengaduanData, AddFormPengaduanVariables>;


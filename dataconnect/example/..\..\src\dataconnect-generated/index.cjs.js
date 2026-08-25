const { queryRef, executeQuery, validateArgsWithOptions, mutationRef, executeMutation, validateArgs, makeMemoryCacheProvider } = require('firebase/data-connect');

const connectorConfig = {
  connector: 'example',
  service: 'itechno-3c5fd-service',
  location: 'asia-southeast2'
};
exports.connectorConfig = connectorConfig;
const dataConnectSettings = {
  cacheSettings: {
    cacheProvider: makeMemoryCacheProvider()
  }
};
exports.dataConnectSettings = dataConnectSettings;

const lihatSemuaUserRef = (dc) => {
  const { dc: dcInstance} = validateArgs(connectorConfig, dc, undefined);
  dcInstance._useGeneratedSdk();
  return queryRef(dcInstance, 'LihatSemuaUser');
}
lihatSemuaUserRef.operationName = 'LihatSemuaUser';
exports.lihatSemuaUserRef = lihatSemuaUserRef;

exports.lihatSemuaUser = function lihatSemuaUser(dcOrOptions, options) {
  
  const { dc: dcInstance, vars: inputVars, options: inputOpts } = validateArgsWithOptions(connectorConfig, dcOrOptions, options, undefined,false, false);
  return executeQuery(lihatSemuaUserRef(dcInstance, inputVars), inputOpts && { fetchPolicy: inputOpts.fetchPolicy });
}
;

const addNewUserRef = (dcOrVars, vars) => {
  const { dc: dcInstance, vars: inputVars} = validateArgs(connectorConfig, dcOrVars, vars, true);
  dcInstance._useGeneratedSdk();
  return mutationRef(dcInstance, 'addNewUser', inputVars);
}
addNewUserRef.operationName = 'addNewUser';
exports.addNewUserRef = addNewUserRef;

exports.addNewUser = function addNewUser(dcOrVars, vars) {
  const { dc: dcInstance, vars: inputVars } = validateArgs(connectorConfig, dcOrVars, vars, true);
  return executeMutation(addNewUserRef(dcInstance, inputVars));
}
;

const addFormPengaduanRef = (dcOrVars, vars) => {
  const { dc: dcInstance, vars: inputVars} = validateArgs(connectorConfig, dcOrVars, vars, true);
  dcInstance._useGeneratedSdk();
  return mutationRef(dcInstance, 'addFormPengaduan', inputVars);
}
addFormPengaduanRef.operationName = 'addFormPengaduan';
exports.addFormPengaduanRef = addFormPengaduanRef;

exports.addFormPengaduan = function addFormPengaduan(dcOrVars, vars) {
  const { dc: dcInstance, vars: inputVars } = validateArgs(connectorConfig, dcOrVars, vars, true);
  return executeMutation(addFormPengaduanRef(dcInstance, inputVars));
}
;

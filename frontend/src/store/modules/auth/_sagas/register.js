import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { LOGIN, REGISTER } from '../actions';

function* register(action) {
  const { data } = action.payload;
  
  const result = yield http.post('/api/users/', data);
  
  if (result.status === 201) {
    const { username, password } = data;
    yield put({ type: LOGIN, payload: { username, password }});
  }
}

export function* registerSaga() {
  yield takeLatest(REGISTER, register);
}

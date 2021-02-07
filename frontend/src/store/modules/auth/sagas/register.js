import { put, takeLatest } from 'redux-saga/effects';

import { LOGGED_IN, REGISTER } from '../actions';
import * as http from '../../../../utils/http';

function* register(action) {
  const { data } = action.payload;
  const result = yield http.post('/api/users/', data);
  
  if (result.status === 201) {
    yield put({ type: LOGGED_IN, payload: result.json })
  }
}

export function* registerSaga() {
  yield takeLatest(REGISTER, register);
}

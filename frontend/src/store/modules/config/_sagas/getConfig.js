import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { GET_CONFIG, SET_CONFIG } from '../actions';

function* getConfig() {
  const result = yield http.get('/api/config/');
  
  if (result.status === 200) {
    yield put({ type: SET_CONFIG, payload: result.json });
  }
}

export function* getConfigSaga() {
  yield takeLatest(GET_CONFIG, getConfig);
}

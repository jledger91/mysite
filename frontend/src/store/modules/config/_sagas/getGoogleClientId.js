import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { GET_GOOGLE_CLIENT_ID, SET_GOOGLE_CLIENT_ID } from '../actions';

function* getGoogleClientId() {
  const result = yield http.get('/api/google_client_id');
  
  const { google_client_id } = result.json;
  
  if (result.status === 200 && google_client_id) {
    yield put({ type: SET_GOOGLE_CLIENT_ID, payload: google_client_id });
  }
}

export function* getGoogleClientIdSaga() {
  yield takeLatest(GET_GOOGLE_CLIENT_ID, getGoogleClientId);
}

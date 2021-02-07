import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { GET_USERS, SET_USERS } from '../actions';

function* getUsers(action) {
  const { params } = action.payload | {};
  
  const result = yield http.get('/api/users/', params);
  
  if (result.status === 200) {
    yield put({ type: SET_USERS, payload: {
        list: result.json,
      }})
  }
}

export function* getUsersSaga() {
  yield takeLatest(GET_USERS, getUsers)
}

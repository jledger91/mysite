import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { GET_FILMS, SET_FILMS } from '../actions';

function* getFilms(action) {
  const { params } = action.payload | {};
  
  const result = yield http.get('/api/films/', params);
  
  if (result.status === 200) {
    yield put({ type: SET_FILMS, payload: {
        list: result.json,
      }})
  }
}

export function* getFilmsSaga() {
  yield takeLatest(GET_FILMS, getFilms)
}

import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { GET_FILM, SET_FILM } from '../actions';

function* getFilm(action) {
  const { id } = action.payload;
  
  const result = yield http.get(`/api/films/${id}`);
  
  if (result.status === 200) {
    yield put({ type: SET_FILM, payload: {
        detail: result.json,
      }});
  }
}

export function* getFilmSaga() {
  yield takeLatest(GET_FILM, getFilm);
}

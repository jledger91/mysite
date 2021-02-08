import { put, takeEvery } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { GET_FILMS, SET_FILMS } from '../actions';

function* getFilms(action) {
  const { key, params } = action.payload;
  
  const result = yield http.get('/api/films/', params);
  if (result.status === 200) {
    yield put({ type: SET_FILMS, payload: {
        key: key,
        list: {
          results: result.json.results,
          pagination: {
            limit: params.limit,
            offset: params.offset,
            next: result.json.next,
            previous: result.json.previous,
          }
        },
      }})
  }
}

export function* getFilmsSaga() {
  yield takeEvery(GET_FILMS, getFilms)
}
